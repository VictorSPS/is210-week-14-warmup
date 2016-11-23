#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Pet module"""

import pet


class Dog(pet.Pet):
    """Pet is the parent class for Dog"""

    def __init__(self, has_shots=False, **kwargs):
        """Constructor for Dog class.
        Args:
            has_shots(boolean, optional): a boolean, defaults to False
            **kwargs: arbitrary arguments passed from parent pet.Pet class.
        """
        pet.Pet.__init__(self, **kwargs)
        self.has_shots = has_shots
