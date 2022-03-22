## This Bot is based on the examples provided by the Microsoft Azure team.
## A version of the original code examples can be found on the Microsoft Github-repo here: https://github.com/microsoft/BotBuilder-Samples
## Licensed under the MIT License.

## - Project Info -
# Github-repo: https://github.com/codingPotato21/CSC408-ASSI1
# Contributors: 
#       1- Adnan Youssef
#       2- Naji Mohammed
#       3- Omar Ahmed
## Licensed under the MIT License.

from difflib import SequenceMatcher

from botbuilder.core import MessageFactory
from botbuilder.dialogs import (
    WaterfallDialog,
    DialogTurnResult,
    WaterfallStepContext,
    ComponentDialog,
)
from botbuilder.dialogs.prompts import PromptOptions, TextPrompt, NumberPrompt
from botbuilder.schema import ChannelAccount, CardAction, ActionTypes, SuggestedActions

from data_models import UserProfile
from dialogs.review_selection_dialog import ReviewSelectionDialog
from dialogs.search_selection_dialog import SearchSelectionDialog

class TopLevelDialog(ComponentDialog):
    def __init__(self, dialog_id: str = None):
        super(TopLevelDialog, self).__init__(dialog_id or TopLevelDialog.__name__)

        # Key name to store this dialogs state info in the StepContext
        self.USER_INFO = "value-userInfo"

        self.add_dialog(TextPrompt(TextPrompt.__name__))
        self.add_dialog(NumberPrompt(NumberPrompt.__name__))

        self.selectionDialog = ReviewSelectionDialog(ReviewSelectionDialog.__name__)
        self.add_dialog(self.selectionDialog)

        self.searchDialog = SearchSelectionDialog(SearchSelectionDialog.__name__)
        self.add_dialog(self.searchDialog)

        self.add_dialog(
            WaterfallDialog(
                "WFDialog",
                [
                    self.initial_step,
                    self.second_step,
                    self.acknowledgement_step,
                ],
            )
        )

        self.initial_dialog_id = "WFDialog"

    async def initial_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        # Create an object in which to collect the user's information within the dialog.
        step_context.values[self.USER_INFO] = UserProfile()

        """
        Creates and sends an activity with suggested actions to the user. When the user
        clicks one of the buttons the text value from the "CardAction" will be displayed
        in the channel just as if the user entered the text. There are multiple
        "ActionTypes" that may be used for different situations.
        """

        prompt = MessageFactory.text("You can ask the bot about a service you are interested in or select to view the full list of services below:")

        prompt.suggested_actions = SuggestedActions(
            actions=[
                CardAction(
                    title="Show list of all available services",
                    type=ActionTypes.im_back,
                    value="Show list of all available services",
                )
            ]
        )

        prompt_options = PromptOptions(
            prompt
        )

        return await step_context.prompt(TextPrompt.__name__, prompt_options)

    async def second_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        user_profile: UserProfile = step_context.values[self.USER_INFO]
        text = step_context.result.lower()

        if text == "show list of all available services":
            # Start the review selection dialog.
            return await step_context.begin_dialog(ReviewSelectionDialog.__name__)
        else:
            # Try to parse the user input.
            services_list = self.selectionDialog.available_services
            match_percentage = []

            # IK, it's janky but im too lazy and sick of this.
            for item in services_list:
                s = SequenceMatcher(None, services_list[services_list.index(item)].lower(), text.lower())
                match_percentage.append(round(s.ratio(), 2))

            m = max(match_percentage)
            top_matches = [i for i, j in enumerate(match_percentage) if j == m]

            # Create a service list for the search dialog.
            service_list = []
            for service_index in top_matches:
                service_list.append(self.selectionDialog.available_services[service_index])
            self.searchDialog.available_services = service_list

            return await step_context.begin_dialog(SearchSelectionDialog.__name__)

    async def acknowledgement_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        # Set the user's company selection to what they entered in the review-selection dialog.
        user_profile: UserProfile = step_context.values[self.USER_INFO]
        user_profile.services_to_review = step_context.result

        # Show information about the selected service
        message = (
            f"You have selected **{user_profile.services_to_review[0]}**. Here is the available information on the service: \n\n"
            f"**Description:** {user_profile.services_to_review[1]}\n\n"
        )

        # Thank them for participating.
        await step_context.context.send_activity(MessageFactory.text(message))

        # Exit the dialog, returning the collected user information.
        return await step_context.end_dialog(user_profile)
