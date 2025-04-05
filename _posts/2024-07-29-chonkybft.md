---
title: Specification and model checking of BFT consensus by Matter Labs
description: >-
  In 2024, I was engaged by the Security Team at MatterLabs. They
  needed help in formally specifying and checking the properties of the new
  algorithm that was being designed by the Consensus Team....
date: 2024-07-29 23:00:00 +0200
categories: [service]
tags: [matter labs,simulation,consensus,research,specification,verification,model checking,paper,quint,TLA+]
---

Earlier this year, I was engaged by the Security Team at [Matter Labs][]. They
needed help in formally specifying and checking the properties of the new
algorithm that was being designed by the Consensus Team. What intrigued me is
that the Consensus Team had the experience of implementing BFT algorithms with
their [Era Consensus][], but their new algorithm – called ChonkyBFT – existed
only in Rust-like pseudo-code. So the team wanted to start with a formal
specification before diving into a full-featured implementation. Since I had the
experience in [specification and model checking][spec] of the [Tendermint
consensus][Tendermint] at Informal Systems, this seemed like a feasible task to
me.

See all the details in the much longer [blogpost][].

> We have published the [research paper][] on ChonkyBFT.
{: .prompt-tip }

[blogpost]: https://protocols-made-fun.com/consensus/matterlabs/quint/specification/modelchecking/2024/07/29/chonkybft.html
[research paper]: {{ 'posts/chonkybft-paper/' | relative_url }}
[Matter Labs]: https://matter-labs.io/
[Era Consensus]: https://github.com/matter-labs/era-consensus
[spec]: https://github.com/cometbft/cometbft/blob/main/spec/light-client/accountability/Synopsis.md
[Tendermint]: https://arxiv.org/abs/1807.04938
[Quint]: {{ 'quint' | relative_url }}
[Apalache]: {{ 'apalache' | relative_url }}