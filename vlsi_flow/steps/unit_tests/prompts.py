#!/usr/bin/env python3.10
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate

_FINAL_UNIT_TESTS_TEMPLATE = """{introduction_prompt}
{spec_prompt}
{module_description_prompt}
{test_case_prompt}
{write_unit_tests_prompt}
"""

introduction_template = """
You are a super smart Digital Design Verification Engineer using \
Test Driven Development to write unit tests according to a chip specification, module descriptions \
and test cases."""

spec_template = """
The specification is: {spec}"""

module_description_template = """
The description of the module is: {module_description}."""

test_case_template = """
The test case is: {test_case}"""

write_unit_tests_template = """
Please write the above unit test cases of this module in {hdl} \
based on the test framework {test_framework} and test method {test_method}.
Each test case should be written as a separate test function in a markdown code block format."""

_FINAL_UNIT_TESTS_PROMPT = PromptTemplate.from_template(_FINAL_UNIT_TESTS_TEMPLATE)
introduction_prompt = PromptTemplate.from_template(introduction_template)
spec_prompt = PromptTemplate.from_template(spec_template)
module_description_prompt = PromptTemplate.from_template(module_description_template)
test_case_prompt = PromptTemplate.from_template(test_case_template)
write_unit_tests_prompt = PromptTemplate.from_template(write_unit_tests_template)

unit_tests_prompts = [
    ("introduction_prompt", introduction_prompt),
    ("spec_prompt", spec_prompt),
    ("module_description_prompt", module_description_prompt),
    ("test_case_prompt", test_case_prompt),
    ("write_unit_tests_prompt", write_unit_tests_prompt)
]
DEFAULT_UNIT_TESTS_PROMPT = PipelinePromptTemplate(
    final_prompt=_FINAL_UNIT_TESTS_PROMPT,
    pipeline_prompts=unit_tests_prompts
)
