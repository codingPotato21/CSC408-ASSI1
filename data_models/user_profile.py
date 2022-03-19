# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List


class UserProfile:
    def __init__(
        self, companies_to_review: List[str] = None
    ):
        self.companies_to_review: List[str] = companies_to_review
