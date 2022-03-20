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

from botbuilder.core import StatePropertyAccessor, TurnContext
from botbuilder.dialogs import Dialog, DialogSet, DialogTurnStatus


class DialogHelper:
    @staticmethod
    async def run_dialog(
        dialog: Dialog, turn_context: TurnContext, accessor: StatePropertyAccessor
    ):
        dialog_set = DialogSet(accessor)
        dialog_set.add(dialog)

        dialog_context = await dialog_set.create_context(turn_context)
        results = await dialog_context.continue_dialog()
        if results.status == DialogTurnStatus.Empty:
            await dialog_context.begin_dialog(dialog.id)
