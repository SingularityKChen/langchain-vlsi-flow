#!/usr/bin/env python3.10
from vlsi_flow.steps.arch_design.prompts import DEFAULT_ARCH_DESIGN_PROMPT


def test_programming_prompts() -> None:
    chip_description = """an out-of-order 32-bit RISC-V CPU that supports standard "G (IMA-FD)" extensions \
with branch prediction and L1 cache."""
    input_variables = DEFAULT_ARCH_DESIGN_PROMPT.input_variables
    print("input_variables:", input_variables)
    arch_design_prompts = DEFAULT_ARCH_DESIGN_PROMPT.format(
        chip_description=chip_description,
    )
    print(arch_design_prompts)
