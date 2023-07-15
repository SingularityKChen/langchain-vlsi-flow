#!/usr/bin/env python3.10
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate

_FINAL_ARCH_DESIGN_TEMPLATE = """{introduction_prompt}
{chip_description_prompt}
{write_module_definition_prompt}
{write_module_description_prompt}
"""

introduction_template = """
You are a senior circuit architect, and you are designing a chip."""

chip_description_template = """
The chip description is: {chip_description}"""

write_module_definition_template = """
Please design the modules in this chip in a markdown code block format."""

write_module_description_template = """
Please describe the modules one by one in compact JSON format. \
For each module, the keys are module name, module function, module description, \
and module interface.
The keys of the module interface are the port names, port directions, \
port widths, and port descriptions."""

_FINAL_ARCH_DESIGN_PROMPT = PromptTemplate.from_template(_FINAL_ARCH_DESIGN_TEMPLATE)
introduction_prompt = PromptTemplate.from_template(introduction_template)
chip_description_prompt = PromptTemplate.from_template(chip_description_template)
write_module_definition_prompt = PromptTemplate.from_template(write_module_definition_template)
write_module_description_prompt = PromptTemplate.from_template(write_module_description_template)

arch_design_prompts = [
    ("introduction_prompt", introduction_prompt),
    ("chip_description_prompt", chip_description_prompt),
    ("write_module_definition_prompt", write_module_definition_prompt),
    ("write_module_description_prompt", write_module_description_prompt)
]
DEFAULT_ARCH_DESIGN_PROMPT = PipelinePromptTemplate(
    final_prompt=_FINAL_ARCH_DESIGN_PROMPT,
    pipeline_prompts=arch_design_prompts
)
