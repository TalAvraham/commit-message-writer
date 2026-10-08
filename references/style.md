# House style

## Subject line
- Use lowercase types: `fix:`, not `Fix:`.
- Keep it to 50 characters or fewer, in the imperative mood ("add", not "added").
- No trailing period.
- The scope is optional and goes in parentheses: `feat(api): add pagination`.

## Body
- Wrap at 72 characters.
- Explain *why* the change was made. The diff already shows *what* changed.
- Use bullets only when there are three or more distinct changes.

## Footers
- Reference tickets as `Refs: ABC-123`.
- Breaking changes: `BREAKING CHANGE: <description>`, and add `!` after the type.
- Co-authors: `Co-authored-by: Name <email>`.

## Monorepos
Prefix the scope with the package name: `fix(web/auth): ...`.
