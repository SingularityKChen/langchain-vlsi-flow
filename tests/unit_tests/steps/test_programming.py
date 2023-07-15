#!/usr/bin/env python3.10
from vlsi_flow.steps.programming.prompts import DEFAULT_RTL_PROMPT


def test_programming_prompts() -> None:
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
    test_cases = "Basic Instruction Decoding"
    input_variables = DEFAULT_RTL_PROMPT.input_variables
    print("input_variables:", input_variables)
    rtl_prompts = DEFAULT_RTL_PROMPT.format(
        spec=spec,
        module_description=module_description,
        hdl=hdl,
        test_cases=test_cases
    )
    print(rtl_prompts)
