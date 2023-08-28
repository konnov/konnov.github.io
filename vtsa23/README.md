# Course material for VTSA23

This is the material for the lectures read by Igor Konnov at
[VTSA'23][].

To follow the lecture, visit the [Google slides][].

To experiment with the tools, please install the following:

 - [Quint][]: see the installation instructions
 - [Quint plugin][]
 - [Microsoft LiveShare Plugin][], if you want to interactively follow the code in the lecture

## Specifying blockchain protocols with TLA+ and Quint and checking them with Apalache

TLA+ is a language and logic for formal specification of all kinds of computer
systems. System designers use this language to specify concurrent, distributed,
and fault-tolerant protocols, which are traditionally presented in pseudo-code.
At Informal Systems, we have been using TLA+ to specify and reason about the
protocols and distributed applications that are running in Cosmos blockchains.
Our main tool of choice for TLA+ is the symbolic model checker called Apalache.
In 2023, we introduced a new specification language called Quint. This language
is an alternative syntax for TLA+ that should look more familiar to engineers.

In this lecture, we demonstrate the main principles of writing specifications
and checking them with Apalache. We are using examples from the blockchain
industry. We also show the practical applications of the tooling provided by
Apalache and Quint.

[VTSA'23]: https://resources.mpi-inf.mpg.de/departments/rg1/conferences/vtsa23/
[Google slides]: https://docs.google.com/presentation/d/1sEM4YM3bKmVaG-yJVqZV8z0VyhE7s7dxQe_jKDruYC0/edit?usp=sharing
[Quint]: https://github.com/informalsystems/quint/
[Quint plugin]: https://marketplace.visualstudio.com/items?itemName=informal.quint-vscode
[Microsoft LiveShare Plugin]: https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare
