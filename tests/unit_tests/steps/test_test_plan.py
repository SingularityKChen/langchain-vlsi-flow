#!/usr/bin/env python3.10
from vlsi_flow.steps.test_plan.prompts import DEFAULT_TEST_PLAN_PROMPT


def test_test_plan_prompts() -> None:
    spec = """an out of order 32-bit RISC-V CPU that supports standard "G (IMA-FD)" extensions."""
    module_description = """{
    "module_name": "Instruction Decode Unit",
    "module_function": "Decodes instructions and extracts necessary information",
    "module_description": "This module decodes the fetched instructions and extracts necessary information such as opcode, register operands, immediate values, etc.",
    "module_interface": {
    "module_name": "Instruction Decode Unit",
    "module_function": "Decodes fetched instructions",
    "module_description": "This module decodes the fetched instructions and prepares them for execution.",
    "module_interface": {
      "clk": {"direction": "input", "width": 1, "description": "Clock signal"},
      "reset": {"direction": "input", "width": 1, "description": "Reset signal"},
      "instruction": {"direction": "input", "width": 32, "description": "Fetched instruction"},
      "decoded_instruction": {"direction": "output", "width": 32, "description": "Decoded instruction"},
      "operands": {"direction": "output", "width": 64, "description": "Operands for the instruction"}
    }
  }""".replace("\n", "").replace("  ", "")
    test_method_list = ["formal", "simulation"]
    test_framework_list = ["UVM", "chiseltest"]
    input_variables = DEFAULT_TEST_PLAN_PROMPT.input_variables
    print("input_variables:", input_variables)
    test_plan_prompts = DEFAULT_TEST_PLAN_PROMPT.format(
        spec=spec,
        module_description=module_description,
        test_method_list=test_method_list,
        test_framework_list=test_framework_list
    )
    print(test_plan_prompts)
