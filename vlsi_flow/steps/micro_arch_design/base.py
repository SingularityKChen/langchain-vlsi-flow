#!/usr/bin/env python3.10
from __future__ import annotations

from typing import Any

from langchain import LLMChain, BasePromptTemplate
from langchain.base_language import BaseLanguageModel

from vlsi_flow.steps.micro_arch_design.prompts import DEFAULT_MICRO_ARCH_DESIGN_PROMPT


class MicroArchDesign(LLMChain):
    """
    Chain that interprets the requirements of a module and generates a micro-architecture design in the VLSI design flow.
    """
    llm: BaseLanguageModel
    prompt: BasePromptTemplate = DEFAULT_MICRO_ARCH_DESIGN_PROMPT
    verbose: bool = True

    @classmethod
    def from_llm(
            cls,
            llm: BaseLanguageModel,
            prompt: BasePromptTemplate = DEFAULT_MICRO_ARCH_DESIGN_PROMPT,
            verbose: bool = True,
            **kwargs: Any) -> MicroArchDesign:
        return cls(llm=llm, prompt=prompt, verbose=verbose, **kwargs)
