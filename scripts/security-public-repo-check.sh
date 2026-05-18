#!/usr/bin/env bash
set -euo pipefail

# Public-repo ingress/secret guardrail for BDA AI Dev Standard.
# Scans tracked and untracked non-ignored text files for production ingress
# endpoints or credential-looking values that must not be committed publicly.

repo_root="$(git rev-parse --show-toplevel 2>/dev/null || pwd)"
cd "$repo_root"

failures=0

report_failure() {
  local file="$1"
  local message="$2"
  printf 'SECURITY CHECK FAILED: %s: %s\n' "$file" "$message" >&2
  failures=$((failures + 1))
}

# Include tracked + untracked files while respecting .gitignore. Exclude binary files
# and this script, because it necessarily documents the forbidden signatures.
while IFS= read -r file; do
  [[ -f "$file" ]] || continue
  [[ "$file" == scripts/security-public-repo-check.sh ]] && continue
  [[ "$file" == .git/* ]] && continue

  if ! LC_ALL=C grep -Iq . "$file"; then
    continue
  fi

  # Production endpoint must not be committed in public docs/config.
  if grep -EIn 'innohub\.bda\.co\.th' "$file" >/dev/null; then
    report_failure "$file" "contains production InnoHub endpoint"
  fi

  # SiamACC secret-like names/values are not allowed in this public repo.
  if grep -EIn 'siamacc[^[:alnum:]_/-]*(secret|token|key|password|passwd|pwd)|SIAMACC_(SECRET|TOKEN|KEY|PASSWORD|PASSWD|PWD)=' "$file" >/dev/null; then
    report_failure "$file" "contains SiamACC secret/token/key pattern"
  fi

  # Supabase privileged database keys must never be public.
  if grep -EIn 'supabase[^[:alnum:]_-]*service[_-]?role|service[_-]?role[^[:alnum:]_-]*supabase|SUPABASE_SERVICE_ROLE' "$file" >/dev/null; then
    report_failure "$file" "contains Supabase service-role pattern"
  fi

  # Public examples may define the variable only as an empty placeholder.
  if grep -EIn "^[[:space:]]*(export[[:space:]]+)?INNOHUB_INGEST_TOKEN=[\"']?[^[:space:]\"'#][^#]*" "$file" >/dev/null; then
    report_failure "$file" "sets INNOHUB_INGEST_TOKEN to a non-empty value"
  fi

  # Generic private key material should not be committed.
  if grep -EIn -- '-----BEGIN (RSA |DSA |EC |OPENSSH |PGP )?PRIVATE KEY-----' "$file" >/dev/null; then
    report_failure "$file" "contains private key material"
  fi

done < <(git ls-files -co --exclude-standard)

if [[ "$failures" -gt 0 ]]; then
  printf '\nPublic repo security check failed with %d issue(s). Remove production endpoints/secrets before committing.\n' "$failures" >&2
  exit 1
fi

printf 'Public repo security check passed.\n'
