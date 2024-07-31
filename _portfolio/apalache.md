---
title: "Apalache"
excerpt: "Symbolic model checker for TLA+"
header:
  teaser: /assets/images/apalache.png
sidebar:
  - image: /assets/images/apalache.png
    image_alt: "logo"
  - title: Website
    nav: apalache
  - title: "Roles"
    text: "Principal investigator"
  - text: "Project lead"
  - text: "Product owner"
  - title: "Language"
    text: "Scala"
  - title: "License"
    text: "Apache 2.0"
---

Perhaps, the most concise summary of Apalache can be found on [Leslie
Lamport's page on TLA<sup>+</sup>][]:

> Apalache is an alternative to TLC for checking TLA+ specifications.
> While TLC is an explicit-state model checker, Apalache is a symbolic
> model checker.  It checks safety for bounded executions and inductive
> invariants for unbounded executions, assuming that all data structures
> are finite.  The tool leverages the SMT solver Z3, from Microsoft
> Research.

The canonical version of Apalache is currently hosted under the Github
organization [github.com/apalache-mc][]. It is managed by [Informal Systems][]
and myself.

I started the [research project on Apalache][] at TU Wien in 2016, after
receiving the grant of 539k EUR from [Vienna Science and Technology
Fund][]. In 2018, I continued research on Apalache at [VeriDis][], Inria
Nancy. From 2019 to 2023, I was leading industrial adoption of Apalache at
[Interchain Foundation][] and [Informal Systems][]. Many researchers and
engineers have contributed to Apalache, including: [Thanh Hai Tran][],
[Shon Feder][], [Jure Kukovec][], [Gabriela Mafra][], [Rodrigo Otoni][],
[Thomas Pani][], [Andrey Kupriyanov][], and [Philip Offtermatt][].

<!-- [![Apalache Tutorial](https://img.youtube.com/vi/NXLJoUKJnDQ/maxresdefault.jpg)](https://www.youtube.com/NXLJoUKJnDQ?t=5596) -->

{% include youtube.html id="NXLJoUKJnDQ" %}


[Leslie Lamport's page on TLA<sup>+</sup>]: https://lamport.azurewebsites.net/tla/tools.html
[Apalache Github]: https://github.com/apalache-mc/apalache
[Vienna Science and Technology Fund]: https://www.wwtf.at/index.php?lang=EN
[research project on Apalache]: https://www.wwtf.at/funding/programmes/ict/ICT15-103/
[VeriDis]: https://team.inria.fr/veridis/
[Philip Offtermatt]: https://p-offtermatt.github.io/
[Thomas Pani]: https://thpani.net/ 
[Rodrigo Otoni]: https://swystems.usi.ch/author/rodrigo-otoni/
[Thanh Hai Tran]: https://scholar.google.com/citations?user=2JrhrNcAAAAJ&hl=en
[Jure Kukovec]: https://forsyte.at/people/kukovec/
[Andrey Kupriyanov]: https://dblp.org/pid/05/7915.html
[Shon Feder]: http://shonfeder.net/
[Gabriela Mafra]: https://github.com/bugarela
[Informal Systems]: https://informal.systems
[Interchain Foundation]: https://interchain.io/
[github.com/apalache-mc]: https://github.com/apalache-mc/