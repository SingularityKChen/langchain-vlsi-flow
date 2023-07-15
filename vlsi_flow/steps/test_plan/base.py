#!/usr/bin/env python3.10
from __future__ import annotations

from typing import Any

from langchain import LLMChain, BasePromptTemplate
from langchain.base_language import BaseLanguageModel

from vlsi_flow.steps.test_plan.prompts import DEFAULT_TEST_PLAN_PROMPT


class TestPlan(LLMChain):
    """
    Chain that writes a test plan and test cases in the VLSI design flow.
    """
    llm: BaseLanguageModel
    prompt: BasePromptTemplate = DEFAULT_TEST_PLAN_PROMPT
    verbose: bool = True

    @classmethod
    def from_llm(
            cls,
            llm: BaseLanguageModel,
            prompt: BasePromptTemplate = DEFAULT_TEST_PLAN_PROMPT,
            verbose: bool = True,
            **kwargs: Any) -> TestPlan:
        return cls(llm=llm, prompt=prompt, verbose=verbose, **kwargs)
