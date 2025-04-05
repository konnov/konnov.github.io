---
title: ChonkyBFT&#58; Consensus Protocol of ZKsync (paper)
description: >-
  The paper on ChonkyBFT is out!
  It contains the protocol description, mathematical proofs
  of correctness, formal specification and verification in Quint,
  and experiments...
date: 2025-03-19 23:00:00 +0200
categories: [service]
tags: [matter labs,simulation,consensus,research,specification,verification,model checking,paper,quint,apalache,TLA+]
image:
  lqip: /assets/img/chonkybft-paper.webp
  path: /assets/img/chonkybft-paper.png
  alt: a screenshot of the paper
---

In July 2024, we wrote the [long blogpost][blogpost] about formal specification
of ChonkyBFT in [Quint][], as well as about testing its safety with the Quint
simulator and model checking with [Apalache][].

The results of that work were exciting and delivered the customer ([Matter
Labs][]) good assurance in protocol safety. After this success, they wanted to
push the boundaries even further. We agreed to continue this research project
along two dimensions:

 - Writing mathematical proofs, as customary in distributed computing, and
 - Developing an inductive invariant and proving safety with it.

We have finished the work along the both dimensions. You can see the results
delivered in the [paper][] that we have published on arXiv. Also, check the
detailed [Quint specification][].

As it often happens, we had to simplify the protocol, in order to check the
inductive invariant in a reasonable time frame. [Simplified specification][]
contains the details in the inductive invariant. In the last weeks of the
project, we had 299 verification tasks running in parallel. What I find exciting
is that the most of the astronomical time went into waiting for the SMT solver
to finish the proofs. I find this use of my time much more productive than
crunching tactics in an interactive theorem prover by hand.

[paper]: https://arxiv.org/abs/2503.15380
[blogpost]: https://protocols-made-fun.com/consensus/matterlabs/quint/specification/modelchecking/2024/07/29/chonkybft.html
[Matter Labs]: https://matter-labs.io/
[Quint]: {{ 'quint' | relative_url }}
[Apalache]: {{ 'apalache' | relative_url }}
[Quint specification]: https://github.com/matter-labs/era-consensus/tree/main/spec/protocol-spec
[Simplified specification]: https://github.com/matter-labs/era-consensus/tree/main/spec/protocol-spec/simplified