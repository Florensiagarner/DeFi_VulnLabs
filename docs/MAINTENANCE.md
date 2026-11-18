# Maintenance and validation

This repository contains **deliberately vulnerable** smart contracts for authorized local security education. Do not deploy these exercises with real funds.

## Quick start

1. Install Foundry (`forge --version`).
2. Initialize the dependency submodules: `git submodule update --init --recursive`.
3. Run `python3 scripts/audit_repository.py` to check exercise metadata.
4. Run `forge build` and `forge test -vv` to compile and execute the examples.
5. Run a single exercise with `forge test --match-path 'src/test/Reentrancy.sol' -vvvv`.

The archive includes dependency directories as originally supplied; they may be empty placeholders. If you are working from this ZIP without a Git remote/submodule metadata, install compatible `forge-std` and `openzeppelin-contracts` dependencies into `lib/` before building. Do not assume the ZIP is self-contained.

## Design principles

- Keep each vulnerable example unchanged unless a specific test is proven incorrect.
- Add patched counterparts and regression tests separately, with descriptive filenames.
- Pin dependency versions and compiler versions before claiming reproducibility.
- Avoid external RPC/fork tests in default CI; configure secrets and fork tests separately.
- Never commit API keys, mnemonic phrases, or funded private keys.

## Compatibility

Some examples intentionally target pre-0.8 Solidity semantics. Avoid forcing a single compiler version across all exercises. Foundry's auto-detection should resolve compatible compiler versions when installed/downloadable.

## Validation scope

The Python audit checks file structure and basic metadata only. It does **not** prove security, exploit correctness, compiler success, or passing Foundry tests. CI is configured to attempt those checks when dependencies and compilers are available.
