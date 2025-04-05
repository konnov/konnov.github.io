---
title: Apalache has moved
description: >-
  Apalache has moved from Informal Systems to github.com/apalache and apalache-mc.org....
date: 2024-08-13 23:59:00 +0200
categories: [tooling]
tags: [research,specification,verification,model checking,quint,apalache,TLA+,smt,tool,open source]
image:
  lqip: /assets/img/apalache-funding.webp
  path: /assets/img/apalache-funding.png
  alt: Apalache history
---

After being hosted for about 4 years on [my github][konnov-gh] and about 5 years
under [`github.com/informalsystems`][informal-gh], [Apalache][] has moved to its
own GitHub organization [`github.com/apalache-mc`][apalache-gh] and [Apalache
repository][apalache-repo].

Apalache website has also moved to [`apalache-mc.org`][apalache-site]. You can
also ask questions about the model checker on [Apalache forum][discourse].

## Apalache: Symbolic model checker for TLA<sup>+</sup> and Quint

Perhaps, the most concise summary of Apalache can be found on [Leslie
Lamport's page on TLA<sup>+</sup>][]:

> Apalache is an alternative to TLC for checking TLA+ specifications.
> While TLC is an explicit-state model checker, Apalache is a symbolic
> model checker.  It checks safety for bounded executions and inductive
> invariants for unbounded executions, assuming that all data structures
> are finite.  The tool leverages the SMT solver Z3, from Microsoft
> Research.

The canonical version of Apalache is currently hosted under the Github
organization [github.com/apalache-mc][]. To see successful applications of
Apalache, check [Apalache examples][].

Currently, Apalache is not funded by any organization. See [FUNDING.md][] for
the past funding. The project is de-facto funded by its current maintainers and
contributors, including [Jure Kukovec][], [Thomas Pani][], and myself. If you
would like to sponsor the project, please contact us, or simply sponsor us on
GitHub by clicking the "Sponsor" button on the [Github page][Apalache Github]!

I started the [research project on Apalache][] at TU Wien in 2016, after
receiving the grant of 539k EUR from [Vienna Science and Technology
Fund][]. In 2018, I continued research on Apalache at [VeriDis][], Inria
Nancy. From 2019 to 2023, I was leading industrial adoption of Apalache at
[Interchain Foundation][] and [Informal Systems][]. Many researchers and
engineers have contributed to Apalache, including: [Thanh Hai Tran][],
[Shon Feder][], [Jure Kukovec][], [Gabriela Moreira][], [Rodrigo Otoni][],
[Thomas Pani][], [Andrey Kupriyanov][], and [Philip Offtermatt][].

[Leslie Lamport's page on TLA<sup>+</sup>]: https://lamport.azurewebsites.net/tla/tools.html
[Apalache examples]: https://github.com/konnov/apalache-examples
[Apalache Github]: https://github.com/apalache-mc/apalache
[Vienna Science and Technology Fund]: https://www.wwtf.at/index.php?lang=EN
[research project on Apalache]: https://www.wwtf.at/funding/programmes/ict/ICT15-103/
[VeriDis]: https://team.inria.fr/veridis/
[Philip Offtermatt]: https://p-offtermatt.github.io/
[Thomas Pani]: https://thpani.net/ 
[Rodrigo Otoni]: https://swystems.usi.ch/author/rodrigo-otoni/
[Thanh Hai Tran]: https://scholar.google.com/citations?user=2JrhrNcAAAAJ&hl=en
[Jure Kukovec]: https://www.linkedin.com/in/jure-kukovec/
[Andrey Kupriyanov]: https://www.linkedin.com/in/andrey-kuprianov/
[Shon Feder]: https://shonfeder.net/
[Gabriela Moreira]: https://github.com/bugarela
[Informal Systems]: https://informal.systems
[Interchain Foundation]: https://interchain.io/
[github.com/apalache-mc]: https://github.com/apalache-mc/
[FUNDING.md]: https://github.com/apalache-mc/apalache/blob/main/FUNDING.md
[Apalache]: https://github.com/apalache-mc/apalache
[informal-gh]: https://github.com/informalsystems/
[apalache-gh]: https://github.com/apalache-mc/
[konnov-gh]: https://github.com/konnov
[apalache-repo]: https://github.com/apalache-mc/apalache
[apalache-site]: https://apalache-mc.org/
[discourse]: https://apalache.discourse.group/