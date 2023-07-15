#!/usr/bin/env python3.10
from __future__ import annotations

from typing import Any

from langchain import LLMChain, BasePromptTemplate
from langchain.base_language import BaseLanguageModel

from typing import Any

from vlsi_flow.steps.programming.prompts import DEFAULT_RTL_PROMPT


class PairProgram(LLMChain):
    """
    Chain to development a module in the VLSI design flow with a pair.
    """
    llm: BaseLanguageModel
    prompt: BasePromptTemplate = DEFAULT_RTL_PROMPT
    verbose: bool = True

    @classmethod
    def from_llm(
            cls,
            llm: BaseLanguageModel,
            prompt: BasePromptTemplate = DEFAULT_RTL_PROMPT,
            verbose: bool = True,
            **kwargs: Any) -> PairProgram:
        return cls(llm=llm, prompt=prompt, verbose=verbose, **kwargs)
