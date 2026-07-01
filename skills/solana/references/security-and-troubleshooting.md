# Solana security & troubleshooting

Companion to the `solana` skill. (Source: Solana Foundation's `solana-dev-skill`, MIT.)

## Security vulnerability catalog (Anchor + Pinocchio fix)
- **Missing owner check** → `Account<'info, T>` (Anchor) / `owned_by` (Pinocchio).
- **Missing signer check** → `Signer<'info>` / `is_signer()`.
- **Arbitrary CPI** → typed `Program<'info, T>` / assert `key() == spl_token::ID`.
- **Reinit attack** → `init`, never `init_if_needed`.
- **PDA sharing** → put user-specific pubkeys in seeds (`[b"pool", vault.key(), owner.key()]`).
- **Type cosplay** → check the account discriminator.
- **Duplicate mutable accounts** → compare keys (Anchor v0.32: `#[account(mut, dup = account_a)]`).
- **Revival attack** → close accounts (`#[account(mut, close = destination)]`).
- **Data matching** → `has_one`.
- **Sysvar spoofing (Pinocchio)** → `Clock::get()` / `Rent::get()`, don't trust a passed sysvar account.
- **Bump canonicalization** → store `find_program_address` bump; verify with `create_program_address`.
- **Lamport griefing** → fund only the deficit.
- **Writable / read-only** → enforce `is_writable()`.

## Token-2022 pitfalls
- Transfer fee is deducted at the receiver end — never assume 1:1. `calculate_fee` and `calculate_inverse_fee` are NOT inverses — use `transfer_checked_with_fee`.
- Permanent-delegate authority can move ANY amount. Mint close + reinit bypasses extension rules ("no close authority" is not enough).
- Use `anchor_spl::token_interface` + `transfer_checked`; validate transfer hooks (mint, transferring state, token accounts belong to the mint).

## Pinocchio specifics
- `entrypoint!(process_instruction)` with `(&Address, &[AccountView], &[u8]) -> ProgramResult`.
- `nostd_panic_handler!()` ONLY for `no_std` — never in SBF/std builds (duplicate lang-item error).
- No implicit validation — do every signer/owner/program-ID check manually in `TryFrom<&[AccountView]>`.
- 1-byte discriminator (255 max) vs Anchor's 8-byte; layout `[discriminator:u8 | version:u8 | data]`. Order struct fields largest-to-smallest alignment + `assert_no_padding!`. Zero allocations via borrowed `&'a [AccountView]`; `account.close()` to prevent revival.

## Version compatibility (Jan 2026)
- Anchor 1.0.x → Solana CLI 3.x, Rust 1.79–1.85+, platform-tools v1.52, `solana-*` crates `^3`. TS pkg renamed `@coral-xyz/anchor` → `@anchor-lang/core`.
- Anchor 0.31+ binaries need GLIBC ≥ 2.39 (fail on Ubuntu 22.04 / Debian 12 — build from source).
- edition2024 break: platform-tools v1.48 bundles cargo 1.84.0 (no `edition=2024`); pin `blake3=1.8.2`, `constant_time_eq=0.3.1`, `base64ct=1.7.3`, `indexmap=2.11.4`.

## Common-error fixes
- `anchor build` IDL fail → add `idl-build = ["anchor-lang/idl-build"]` (required since 0.30), or `anchor build --no-idl`.
- `cargo build-sbf not found` → install Agave via `release.anza.xyz/stable/install`.
- `ECONNREFUSED ::1:8899` → Node 17+ IPv6; use `127.0.0.1` or `NODE_OPTIONS=--dns-result-order=ipv4first`.
- LiteSVM `undefined symbol __isoc23_strtol` → GLIBC < 2.38; fall back to `solana-bankrun`.
- Anchor 0.29 → 0.30 migration: `.accounts()` → `.accountsPartial()`; add `overflow-checks = true` to `[profile.release]`.
