---
layout: page
date: 2024-01-01 00:00:00 +0200
categories: [research,development]
tags: [simulation,research,specification,verification,model checking,quint,apalache,tla]
---

# Quint: Another look at the logic of TLA<sup>+</sup>

**Roles in the project**:
  - Product Owner (2023)
  - Project Lead and Principal Research Scientist (2020-2022)

> I stopped to actively work on Quint in the end of 2023,
  when I became independent.
{: .prompt-tip }

[Quint][] is an alternative syntax for the logic TLA<sup>+</sup>. When we
started the project at [Informal Systems][] in 2021, we wanted to test the
following hypothesis:

*Would engineers onboard to TLA<sup>+</sup> faster, when they are offered a
syntax that looks more like a programming language?*

In short, we believe that the answer is positive. For instance, see the recent
blogposts on specification and model checking of [ChonkyBFT][chonky-paper]
and [ZKsync Governance][zksync-gov].

In addition to the alternative syntax, Quint offers several features that
are expected by software engineers:

 - a type checker and an effects checker,
 - a VSCode plugin,
 - a testing framework and a randomized simulator.

Quint was developed by [Shon Feder][], [Gabriela Moreira][], [Thomas Pani][],
[Jure Kukovec][], and myself. It is maintained and further extended at
Informal Systems.

{% include embed/youtube.html id='OZIX8rs-kOA' %}

[Thomas Pani]: https://thpani.net/ 
[Jure Kukovec]: https://forsyte.at/people/kukovec/
[Shon Feder]: https://shonfeder.net/
[Gabriela Moreira]: https://github.com/bugarela
[Informal Systems]: https://informal.systems
[Quint]: https://github.com/informalsystems/quint
[chonky-paper]: {{ 'posts/chonkybft-paper/' | relative_url }}
[zksync-gov]: {{ 'posts/zksync-governance/' | relative_url }}