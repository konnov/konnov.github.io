---
title: Specification and Model-checking of the ZKsync Governance Protocol
description: >-
  A detailed blogpost that summarizes our work on formal specification
  of ZKsync Governance and model checking of its properties...
date: 2024-09-15 23:00:00 +0200
categories: [service]
tags: [matter labs,simulation,smart contracts,research,specification,verification,model checking,quint,solidity]
---

After our success in specification and model checking of the ChonkyBFT consensus
in Quint, Denis Kolegov at [Matter Labs][] offered me to apply [Quint][] and its
tools to a slightly different domain: ZKsync governance contracts in Solidity.
We used the Quint simulator and the model checker [Apalache][]. Check our
[technical blogpost][blogpost] that summarizes our experience and highlights the
important modeling decisions we made.

Also, check the [talk][] at DeFi Security Summit 2024 on this work, which I gave
later.

[blogpost]: https://protocols-made-fun.com/zksync/matterlabs/quint/specification/modelchecking/2024/09/12/zksync-governance.html
[talk]: {{ 'posts/dss2024/' | relative_url }}
[Matter Labs]: https://matter-labs.io/
[Quint]: {{ 'quint' | relative_url }}
[Apalache]: {{ 'apalache' | relative_url }}