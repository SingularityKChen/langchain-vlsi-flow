#!/usr/bin/env python3.10
from __future__ import annotations

from typing import Any

from langchain import LLMChain, BasePromptTemplate
from langchain.base_language import BaseLanguageModel

from vlsi_flow.steps.unit_tests.prompts import DEFAULT_UNIT_TESTS_PROMPT


class UnitTests(LLMChain):
    """
    Chain that interprets a unit test plan and test cases in the VLSI design flow and generates unit tests.
    """
    llm: BaseLanguageModel
    prompt: BasePromptTemplate = DEFAULT_UNIT_TESTS_PROMPT
    verbose: bool = True

    @classmethod
    def from_llm(
            cls,
            llm: BaseLanguageModel,
            prompt: BasePromptTemplate = DEFAULT_UNIT_TESTS_PROMPT,
            verbose: bool = True,
            **kwargs: Any) -> UnitTests:
        return cls(llm=llm, prompt=prompt, verbose=verbose, **kwargs)
