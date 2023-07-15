#!/usr/bin/env python3.10
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate

_FINAL_RTL_TEMPLATE = """{introduction_prompt}
{spec_prompt}
{module_description_prompt}
{test_cases_prompt}
{write_rtl_prompt}
"""

introduction_template = """
You are a super smart Digital Design Engineer using \
Test Driven Development to write RTL according to the chip specification, module descriptions \
and test cases."""

spec_template = """
The specification is: {spec}"""

# FIXME: for Chisel, clock and reset should be removed from the module description
module_description_template = """
The description of the module is: {module_description}."""

test_cases_template = """
The test cases are: {test_cases}"""

write_rtl_template = """
Please write the above module in {hdl} \
with proper formal assertion statements in a markdown code block format."""

_FINAL_RTL_PROMPT = PromptTemplate.from_template(_FINAL_RTL_TEMPLATE)
introduction_prompt = PromptTemplate.from_template(introduction_template)
spec_prompt = PromptTemplate.from_template(spec_template)
module_description_prompt = PromptTemplate.from_template(module_description_template)
test_cases_prompt = PromptTemplate.from_template(test_cases_template)
write_rtl_prompt = PromptTemplate.from_template(write_rtl_template)

rtl_prompts = [
    ("introduction_prompt", introduction_prompt),
    ("spec_prompt", spec_prompt),
    ("module_description_prompt", module_description_prompt),
    ("test_cases_prompt", test_cases_prompt),
    ("write_rtl_prompt", write_rtl_prompt)
]
DEFAULT_RTL_PROMPT = PipelinePromptTemplate(
    final_prompt=_FINAL_RTL_PROMPT,
    pipeline_prompts=rtl_prompts
)
