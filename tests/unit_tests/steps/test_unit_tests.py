#!/usr/bin/env python3.10
from vlsi_flow.steps.unit_tests.prompts import DEFAULT_UNIT_TESTS_PROMPT


def test_unit_prompts() -> None:
    spec = """an out of order 32-bit RISC-V CPU that supports standard "G (IMA-FD)" extensions"""
    module_description = """{
        "module_name": "Instruction Decode Unit",
        "module_function": "Decodes instructions and extracts necessary information",
        "module_description": "This module decodes the fetched instructions and extracts necessary information such as opcode, register operands, immediate values, etc.",
        "module_interface": {
          "clk": {
            "direction": "input",
            "width": 1,
            "description": "Clock signal"
          },
          "reset": {
            "direction": "input",
            "width": 1,
            "description": "Reset signal"
          },
          "instruction_in": {
            "direction": "input",
            "width": 32,
            "description": "Input instruction"
          },
          "opcode_out": {
            "direction": "output",
            "width": 7,
            "description": "Output opcode"
          },
          "rs1_out": {
            "direction": "output",
            "width": 5,
            "description": "Output register source 1"
          },
          "rs2_out": {
            "direction": "output",
            "width": 5,
            "description": "Output register source 2"
          },
          "rd_out": {
            "direction": "output",
            "width": 5,
            "description": "Output register destination"
          },
          "imm_out": {
            "direction": "output",
            "width": 32,
            "description": "Output immediate value"
          }
        }""".replace("\n", "").replace("  ", "")
    hdl = "Chisel"
    test_framework = "chiseltest"
    test_method = "simulation"
    test_case = """## Test Case 1: Basic Instruction Decoding
### Objective:
Verify that the Instruction Decode Unit decodes basic instructions correctly and extracts the necessary information.

### Test Method:
Simulation

### Test Framework:
chiseltest

### Test Environment Setup:
- Set up the simulation environment with appropriate clock and reset signals.
- Instantiate the Instruction Decode Unit module.
- Connect the necessary input and output signals.

### Test Steps:
1. Provide a set of basic instructions as input to the Instruction Decode Unit.
2. Drive the clock signal and ensure proper synchronization.
3. Observe the output signals from the Instruction Decode Unit.
4. Compare the decoded instructions and extracted operands against the expected values.

### Expected Results:
- The Instruction Decode Unit correctly decodes the input instructions.
- The extracted information such as opcode, register operands, and immediate values are accurate.

### Test Coverage:
- Verify the decoding of a variety of basic instructions.
- Validate the extraction of different types of operands (registers and immediates).

### Test Deliverables:
- Test report summarizing the results and observations.

### Test Schedule:
- Estimated test duration: 1 day

### Risks and Mitigation:
- Risk: Incorrect decoding of instructions may lead to incorrect execution.
  - Mitigation: Thoroughly review the design and validate against the RISC-V specification.
- Risk: Incomplete test coverage of instruction types.
  - Mitigation: Add additional test cases to cover a wider range of instructions.

### Dependencies:
- Availability of the Instruction Decode Unit module.
- Correct implementation of the G (IMA-FD) extensions.""".replace("\n", "").replace("  ", "")
    input_variables = DEFAULT_UNIT_TESTS_PROMPT.input_variables
    print("input_variables:", input_variables)
    unit_test_prompts = DEFAULT_UNIT_TESTS_PROMPT.format(
        spec=spec,
        module_description=module_description,
        hdl=hdl,
        test_method=test_method,
        test_framework=test_framework,
        test_case=test_case
    )
    print(unit_test_prompts)
