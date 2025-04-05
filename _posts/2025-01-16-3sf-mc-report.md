---
title: Exploring Automatic Model-Checking of the Ethereum specification (tech. report)
description: >-
  We have published the report on model checking of accountability in the 3-slot finality
  protocol for Ethereum Foundation...
date: 2025-01-16 23:00:00 +0200
categories: [service]
tags: [ethereum foundation,consensus,research,specification,verification,model checking,paper,TLA+]
image:
  lqip: /assets/img/3sf-mc-report.webp
  path: /assets/img/3sf-mc-report.png
  alt: a screenshot of the paper
---

In Q3-Q4 of 2025, [Thomas Pani][], [Jure Kukovec][], [Thanh Hai Tran][],
[Roberto Saltini][], and I worked on model checking of the brand-new (back then,
under development) [3-Slot Finality protocol][] for Ethereum Foundation. Due to
a large scope of the protocol, we limited ourselves to the accountability of the
protocol.

Model checking of accountability for 3SF happened to be quite challenging and,
thus, exciting! We have thrown a lot of tools at the protocol, including
[Apalache][], [Alloy][], [CVC5][], and [Kissat][]. We could not break
accountability with all these tools. It is worth noting that this verification
problem poses a serious challenge for all these tools. See the details and our
thoughts on this in the [report][].

I am going to write my thoughts on how the model checkers could be improved to
address protocols like 3SF in a longer blog post.

[3-Slot Finality protocol]: https://arxiv.org/abs/2411.00558
[report]: https://arxiv.org/abs/2501.07958
[Thomas Pani]: https://thpani.net/
[Jure Kukovec]: https://www.linkedin.com/in/jure-kukovec/
[Thanh Hai Tran]: https://www.linkedin.com/in/thanh-hai-tran/
[Roberto Saltini]: https://x.com/robsaltini
[Apalache]: {{ 'apalache' | relative_url }}
[Alloy]: https://alloytools.org/
[CVC5]: https://cvc5.github.io/
[Kissat]: https://fmv.jku.at/kissat/