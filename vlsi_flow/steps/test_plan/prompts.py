#!/usr/bin/env python3.10
from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate

_FINAL_TEST_PLAN_TEMPLATE = """{introduction_prompt}
{spec_prompt}
{module_description_prompt}
{test_methods_prompt}
{test_framework_prompt}
{write_test_plan_prompt}
"""

introduction_template = """
You are a senior Digital Design Verification Engineer. \
And you are writing a test plan. Please specify the test method, test framework, \
and test cases based on the given specification."""

spec_template = """
The specification is: {spec}"""

module_description_template = """
The description of the module is: {module_description}."""

test_methods_template = """
Please choose at least one verification method from the following options: {test_method_list}."""

test_framework_template = """
Please choose at least one test framework from the following options: {test_framework_list}."""

write_test_plan_template = """
Please write the test plan in a markdown code block format. \
Heads of the test plan should be the name of test cases, \
and the content of each test case should contains the following information:
- objective;
- test method;
- test framework;
- test environment setup;
- test steps;
- expected results;
- test coverage;
- test deliverables
- test schedule;
- risks and mitigation;
- dependencies;
"""

_FINAL_TEST_PLAN_PROMPT = PromptTemplate.from_template(_FINAL_TEST_PLAN_TEMPLATE)
introduction_prompt = PromptTemplate.from_template(introduction_template)
spec_prompt = PromptTemplate.from_template(spec_template)
module_description_prompt = PromptTemplate.from_template(module_description_template)
test_methods_prompt = PromptTemplate.from_template(test_methods_template)
test_framework_prompt = PromptTemplate.from_template(test_framework_template)
write_test_plan_prompt = PromptTemplate.from_template(write_test_plan_template)

test_plan_prompts = [
    ("introduction_prompt", introduction_prompt),
    ("spec_prompt", spec_prompt),
    ("module_description_prompt", module_description_prompt),
    ("test_methods_prompt", test_methods_prompt),
    ("test_framework_prompt", test_framework_prompt),
    ("write_test_plan_prompt", write_test_plan_prompt)
]
DEFAULT_TEST_PLAN_PROMPT = PipelinePromptTemplate(
    final_prompt=_FINAL_TEST_PLAN_PROMPT,
    pipeline_prompts=test_plan_prompts
)
