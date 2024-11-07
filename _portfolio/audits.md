---
title: "Protocol audits and research"
excerpt: "Protocol audits and research for Web3"
header:
  teaser: /assets/images/mechanical-bug.png
sidebar:
  - image: /assets/images/mechanical-bug.png
    image_alt: "logo"
  - title: "Role"
    text: "Security researcher"
  - title: "Languages"
    text: "Solidity"
  - text: "Rust/Cosmwasm"
  - text: "Golang/Cosmos SDK"
  - text: "TLA+"
  - title: "Platforms"
    text: "Ethereum"
  - text: "Stellar"
  - text: "Cosmos"
---

**Protocol specification and verification.** For the most recent work, see:

 - [Specification and model checking of BFT consensus][MLbft] for Matter Labs.

 - [Specification and Model-checking of the ZKsync Governance Protocol][zksync]
 for Matter Labs.

For a recent example of research on reasoning about safety of consensus, see
[Model checking safety of Ben-Or's Byzantine consensus with Apalache][Ben-Or].

**Code audits.** I have a proven track record of submitting **valid** high and
medium findings at [Code4rena][], [Sherlock][], and [Hackerone][], individually, as
well as in a team. In addition to that, I was conducting several Web3 protocol
audits while working at [Informal Systems][]. Need a proof? DM.

Given my expertise, I am flexible to help you with a range of activities
along the stack/confidence axes:

**Stack:**

  - Consensus, e.g., Tendermint/CometBFT or your custom consensus
  - Interchain communication, e.g, bridges and IBC
  - Smart contracts and dApps, e.g., Soroban, Solidity, Cosmwasm

**Confidence:**

  - Manual code review
  - Fuzzing, e.g., using Medusa
  - Protocol specification and analysis, e.g., in TLA<sup>+</sup> and [Quint][]
  - Model checking, e.g., using TLC and [Apalache][]
  - Math proofs

If you think that your project is too big for one person, or you are short
on time, I am connected to a network of researchers, including my former
peers.

[Informal Systems]: https://informal.systems
[Code4rena]: https://code4rena.com/
[Sherlock]: https://www.sherlock.xyz/
[Hackerone]: https://www.hackerone.com/
[MLbft]: https://protocols-made-fun.com/consensus/matterlabs/quint/specification/modelchecking/2024/07/29/chonkybft.html
[Quint]: https://quint-lang.org/
[Apalache]: https://github.com/apalache-mc/apalache
[zksync]: https://protocols-made-fun.com/zksync/matterlabs/quint/specification/modelchecking/2024/09/12/zksync-governance.html
[Ben-Or]: https://protocols-made-fun.com/specification/modelchecking/tlaplus/apalache/2024/11/03/ben-or.html