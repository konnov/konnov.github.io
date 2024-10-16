---
title: "Quint"
excerpt: "Alternative syntax for the logic of TLA+"
header:
  teaser: /assets/images/quint.png
sidebar:
  - image: /assets/images/quint.png
    image_alt: "quint"
  - title: Website
    nav: quint
  - title: "Roles"
    text: "Project lead"
  - text: "Product owner"
  - title: "Language"
    text: "TypeScript"
  - title: "License"
    text: "Apache 2.0"
---

Quint is an alternative syntax for the logic TLA<sup>+</sup>. When we
started the project at [Informal Systems][] in 2021, we wanted to test the
following hypothesis:

*Would engineers onboard to TLA<sup>+</sup> faster, when they are offered a
syntax that looks more like a programming language?*

In short, we believe that the answer is positive. For instance, see the recent
blogpost on specification and model checking of [ChonkyBFT][chonky-blogpost]
and [ZKsync Governance][zksync-gov].

In addition to the alternative syntax, Quint offers several features that
are expected by software engineers:

 - a type checker and an effects checker,
 - a VSCode plugin,
 - a testing framework and a randomized simulator.

Quint was developed by [Shon Feder][], [Gabriela Moreira][], [Thomas Pani][],
[Jure Kukovec][], and myself. It is maintained and further extended at
Informal Systems.

<!-- [![My talk on Quint at Gateway to Cosmos](https://img.youtube.com/vi/OZIX8rs-kOA/maxresdefault.jpg)](https://www.youtube.com/watch?v=OZIX8rs-kOA) -->

{% include youtube.html id="OZIX8rs-kOA" %}


[Thomas Pani]: https://thpani.net/ 
[Jure Kukovec]: https://forsyte.at/people/kukovec/
[Shon Feder]: http://shonfeder.net/
[Gabriela Moreira]: https://github.com/bugarela
[Informal Systems]: https://informal.systems
[chonky-blogpost]: https://protocols-made-fun.com/consensus/matterlabs/quint/specification/modelchecking/2024/07/29/chonkybft.html
[zksync-gov]: https://protocols-made-fun.com/zksync/matterlabs/quint/specification/modelchecking/2024/09/12/zksync-governance.html
