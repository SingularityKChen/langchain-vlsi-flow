#!/usr/bin/env python3.10
from vlsi_flow.steps.micro_arch_design.prompts import DEFAULT_MICRO_ARCH_DESIGN_PROMPT


def test_programming_prompts() -> None:
    spec = """an out-of-order 32-bit RISC-V CPU that supports standard "G (IMA-FD)" extensions \
with branch prediction and L1 cache."""
    module_description = """{
  "module_name": "Branch_Prediction_Unit",
  "module_function": "Predict branches",
  "module_description": "Predicts branches and provides the next instruction address",
  "module_interfaces": [
    {
      "port_name": "clk",
      "port_direction": "input",
      "port_width": "1",
      "port_description": "Clock signal"
    },
    {
      "port_name": "reset",
      "port_direction": "input",
      "port_width": "1",
      "port_description": "Reset signal"
    },
    {
      "port_name": "control_signals",
      "port_direction": "input",
      "port_width": "variable",
      "port_description": "Control signals from the Instruction Decode module"
    },
    {
      "port_name": "current_pc",
      "port_direction": "input",
      "port_width": "32",
      "port_description": "Current Program Counter value"
    },
    {
      "port_name": "branch_target",
      "port_direction": "input",
      "port_width": "32",
      "port_description": "Branch target address"
    },
    {
      "port_name": "next_pc",
      "port_direction": "output",
      "port_width": "32",
      "port_description": "Next instruction address"
    }
  ]
}""".replace("\n", "").replace("  ", "")
    input_variables = DEFAULT_MICRO_ARCH_DESIGN_PROMPT.input_variables
    print("input_variables:", input_variables)
    micro_arch_design_prompt = DEFAULT_MICRO_ARCH_DESIGN_PROMPT.format(
        chip_description=spec,
        module_description=module_description
    )
    print(micro_arch_design_prompt)
