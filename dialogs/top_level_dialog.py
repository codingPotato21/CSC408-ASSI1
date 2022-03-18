# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

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


class TopLevelDialog(ComponentDialog):
    def __init__(self, dialog_id: str = None):
        super(TopLevelDialog, self).__init__(dialog_id or TopLevelDialog.__name__)

        # Key name to store this dialogs state info in the StepContext
        self.USER_INFO = "value-userInfo"

        self.add_dialog(TextPrompt(TextPrompt.__name__))
        self.add_dialog(NumberPrompt(NumberPrompt.__name__))

        self.add_dialog(ReviewSelectionDialog(ReviewSelectionDialog.__name__))

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
                    #image="https://via.placeholder.com/20/FF0000?text=R",
                    #image_alt_text=">> ",
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
            # start the review selection dialog.
            return await step_context.begin_dialog(ReviewSelectionDialog.__name__)
        else:
            return await step_context.end_dialog(user_profile)


    async def acknowledgement_step(
        self, step_context: WaterfallStepContext
    ) -> DialogTurnResult:
        # Set the user's company selection to what they entered in the review-selection dialog.
        user_profile: UserProfile = step_context.values[self.USER_INFO]
        user_profile.companies_to_review = step_context.result

        # Show information about the selected service
        message = (
            f"You have selected **{user_profile.companies_to_review[0]}**. Here is the available information on the service: \n\n"
            f"**Description:** {user_profile.companies_to_review[1]}\n\n"
        #    f"**Requirements:** {user_profile.companies_to_review[2]}\n\n"
        #    f"**Service-URL:** {user_profile.companies_to_review[3]}\n\n"
        )

        # Thank them for participating.
        await step_context.context.send_activity(MessageFactory.text(message))

        # Exit the dialog, returning the collected user information.
        return await step_context.end_dialog(user_profile)
