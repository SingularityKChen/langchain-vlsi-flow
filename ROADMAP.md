# LangChain VLSI Flow Roadmap

This roadmap outlines the planned development milestones for the LangChain VLSI flow system, with the ultimate goal of achieving text-to-GDSII conversion utilizing the power of GPTs with existing tools.

## Release 0.0.1

Create an initial demo capable of generating working RTL/Testbench based on a given digital circuit specification. The focus is on implementing a matrix sum circuit in Chisel 5, specifically the lab 3 of CS250 at UCB in fall 13.

### Roles

Product Owner (PO)

- [ ] Establish a TODO list generation process for DE and DV
- [ ] Hold necessary meetings and activities

Architect

- [ ] Define building blocks and their interfaces

Digital Design Engineer (DE): Generate RTL with a given digital circuit specification.

- [ ] Implement matrix sum circuit in Chisel 5
- [ ] Write Unit Test

Digital Design Verification Engineer (DV):  Generate and validate the generated RTL/Testbench with a given digital circuit specification.

- [ ] Write functional verification test plans
- [ ] Write functional verification test cases
- [ ] Review Chisel RTL


### Development Flows

- [ ] TDD practices

### Tools and PL

- [ ] Verilator
- [ ] Chisel 5 (Scala)
- [ ] Python
- [ ] Yaml

### Knowledge Database

- [ ] Chisel 5 materials
- [ ] Chisel 5 code templates
- [ ] Scrum materials

## Release 0.0.2

Enhance the demo by generating basic in-order five-stage RISC-V cores with I ISA that can pass Difftest (TDD).

### Roles

Product Owner:

- [ ] Improve task refinement process.

Digital Design Verification Engineer:

- [ ] Perform RISC-V CPU functional verification using DiffTest.

### Development Flows

- [ ] Optimized TDD practices

### Tools and PL

- [ ] DiffTest

### Knowledge Database

- [ ] RISC-V ISA
- [ ] DiffTest Documentation

## Release 0.0.3

Further enhance the system by generating in-order five-stage RISC-V cores G (including four standard extensions: "IMAFD") that can pass Difftest (TDD).
Start backend by introducing OpenLane VLSI design flow.

### Tools and PL

- [ ] OpenLane VLSI design flow

## Release 0.0.x

...

## From release 0.1.1

### Roles

Architect:

+ Analyze and optimize the required algorithm in a hardware-friendly manner
+ Clarify the goal of the optimization
+ Desice the hardware-software boundary
+ ...

Modeling Engineer:

+ ESL
+ Performance and power model
+ Language
  + SystemC (or generated from RTL)
  + Transaction-Level Modeling (TLM) 2.0

Digital Design Engineer: 

+ write SDC
+ Clock domain and power domain
+ Low power design
+ Language
  + Verilog, SystemVerilog
  + Tcl

Digital Design Verification Engineer:

+ Establish Constrained Random Verification (CRV) testbench in SystemVerilog with UVM
+ Capable of using VIPs
+ Formal verification applications
+ Continuous Integration (CI)

Physical Design Engineer:

+ Synthesis and optimization
+ Power analysis and optimization
+ PnR flow, timing closure
+ Low power
+ Tools
  + Genus, Joules, Innovous
+ Language
  + Tcl

Design for Test Engineer:

+ ...

FPGA Engineer:

+ FPGA emulation
+ DevOps

### Flows

+ Optimize OpenLane VLSI design flow scripts
+ arch model (TLM 2.0)
+ Backend flow

### Tools and PL

+ OpenLane
+ memory compiler
+ Genus, Joules, Innovous
+ Tcl, bash
+ Verilog, SystemVerilog, SystemC
+ Makefile

### Knowledge Database

+ Optimize the list of reference websites
+ Code template for other roles

