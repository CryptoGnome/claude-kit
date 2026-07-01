# Vulnerability triage patterns

Grep/ripgrep patterns for the `security-audit` skill's triage step. This **over-catches on purpose** — every hit is a *candidate* to investigate (trace source→sink), never a finding on its own. Adapt patterns to the project's language.

## Injection
- **SQL:** string-built queries — `query(` / `execute(` with `+`, a template literal, or an f-string containing a variable; `.raw(`, `sequelize.query`, `db.query(` with interpolation. Flag when a request value reaches it unparameterized.
- **Command:** `exec`, `execSync`, `spawn`, `child_process`, `os.system`, `subprocess` with `shell=True`, backticks, `eval`, `new Function(`.
- **Path traversal:** `readFile` / `open` / `sendFile` / `path.join` with a request-derived path; missing `../` normalization.
- **SSRF:** `fetch` / `axios` / `requests.get` / `http.get` / `urllib` with a URL from the request; webhook / callback / proxy / image-url params.
- **SSTI / XXE:** template render with user input; XML parser with external entities enabled.

## AuthN / AuthZ / access control
- Routes / handlers / mutations missing an auth check; `isAdmin` / `role` / `ownerId` compared loosely or not at all.
- **IDOR:** an object fetched by an id straight from the request with no ownership check.
- JWT: `verify` with `algorithms: ['none']`, missing signature verification, or a secret hardcoded in source.
- Server Actions / API routes that *assume* middleware or a layout guarded them.

## Web
- **XSS:** `dangerouslySetInnerHTML`, `innerHTML`, `v-html`, `document.write`, unescaped template output.
- **CSRF:** state-changing routes with no token / `SameSite` / origin check.
- **Open redirect:** `redirect(` / `Location:` set from a request param.

## Data & memory
- **Insecure deserialization:** `pickle.loads`, `yaml.load` (not `safe_load`), `unserialize`, `Marshal.load`, JSON merged into an object without guarding `__proto__`.
- **Prototype pollution:** recursive merge / `set` / `assign` over user-supplied JSON.
- **ReDoS:** user input flowing into a regex with nested quantifiers.

## Secrets & crypto
- Hardcoded credentials — search for token/key prefixes and assignments like `password =`, `api[_-]?key =`, AWS-style `AKIA…`, and PEM `BEGIN … PRIVATE KEY` blocks. (Any real hit is a finding *and* should be rotated.)
- Weak crypto: `md5` / `sha1` for passwords; `Math.random()` / `rand()` for tokens or nonces; ciphers with no IV; `ECB` mode; a hardcoded IV or salt.

## Concurrency & logic
- **TOCTOU / race:** check-then-act on a shared resource (e.g. read balance → write) without a lock, transaction, or atomic op.
- Missing overflow guards where relevant; off-by-one on limits/bounds.

## LLM / agentic (for AI apps)
- Untrusted content (a web page, email, file, or tool output) flowing into a prompt without isolation → prompt injection.
- Tool / function definitions whose arguments come from untrusted text; an agent able to run shell or `fetch` on attacker-influenced input.
- Secrets or system prompts reachable by the model and returnable to the user.
