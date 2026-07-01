# Ethereum reference

Companion to the `ethereum` skill. Two kinds of content that don't belong inline: **facts that go stale** (re-verify live) and **niche agent-era standards**. (Source: Austin Griffith's ethskills — ethskills.com.)

## Current-network reality (early 2026 — VERIFY LIVE; this goes stale)
Don't trust model training data on these — check `cast base-fee` / `cast gas-price` and forkcast.org.
- Mainnet gas is often **under 1 gwei** (60–300× cheaper than the "10–30 gwei" many models assume): ~$0.004 / transfer, ~$0.04 / swap, ~$0.24 / ERC-20 deploy.
- Upgrades shipped: **Pectra** (May 2025), **Fusaka** (Dec 2025); **EIP-7702** live.
- **Base** = cheapest major L2; **Arbitrum** = deepest DeFi liquidity. Dominant DEXes: **Aerodrome** (Base) / **Velodrome** (OP), not Uniswap everywhere.
- **Celo** is now an OP-Stack L2 (not an L1); Polygon zkEVM is winding down.
- Testnet = **Sepolia** (`11155111`). Goerli/Rinkeby are dead.
- Free RPCs: `eth.llamarpc.com`, `rpc.ankr.com/eth`, `rpc.buidlguidl.com`; prod: Alchemy / Infura / QuickNode.

## Tooling quick-reference
- `cast call "balanceOf(address)(uint256)" <addr>` · `cast send "transfer(address,uint256)"` · `cast base-fee` · `cast 4byte-decode` · `cast resolve-name`
- `anvil --fork-url $RPC` · `forge create` / `forge script` / `forge verify-contract`
- abi.ninja to poke any verified contract · Blockscout MCP (`mcp.blockscout.com/mcp`) for agent onchain lookups.
- Prefer **viem + wagmi** over ethers.js.

## Agent-era standards (production-ready, but niche)
Inherit OZ for the classics (ERC-20/721/1155/4626, `ERC20Permit`/ERC-2612, `EIP712`). Newer:
- **EIP-3009** `transferWithAuthorization` — USDC gasless transfer (what makes x402 work).
- **EIP-7702** smart EOAs — delegation persists until cleared (gotcha).
- **ERC-4337** account abstraction.
- **ERC-8004** onchain agent identity / reputation / validation registries (deployed Jan 2026, same addresses across 20+ chains). **Verify the exact address onchain before use — never hardcode one from memory.**
- **x402** HTTP-402 payment protocol (`@x402/core @x402/fetch @x402/evm`).
