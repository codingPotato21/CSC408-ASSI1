## This Bot is based on the examples provided by the Microsoft Azure team.
## A version of the original code examples can be found on the Microsoft Github-repo here: https://github.com/microsoft/BotBuilder-Samples
## Licensed under the MIT License.

## - Project Info -
# Github-repo: https://github.com/codingPotato69/CSC408-ASSI1
# Contributors: 
#       1- Adnan Youssef
#       2- Naji Mohammed
#       3- Omar Ahmed
## Licensed under the MIT License.

from typing import List


class UserProfile:
    def __init__(
        self, companies_to_review: List[str] = None
    ):
        self.companies_to_review: List[str] = companies_to_review
