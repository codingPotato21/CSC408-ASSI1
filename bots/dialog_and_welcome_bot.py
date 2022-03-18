# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List
from botbuilder.core import (
    ConversationState,
    MessageFactory,
    UserState,
    TurnContext,
)
from botbuilder.dialogs import Dialog
from botbuilder.schema import ChannelAccount, CardAction, ActionTypes, SuggestedActions

from .dialog_bot import DialogBot
from helpers.dialog_helper import DialogHelper


class DialogAndWelcomeBot(DialogBot):
    def __init__(
        self,
        conversation_state: ConversationState,
        user_state: UserState,
        dialog: Dialog,
    ):
        super(DialogAndWelcomeBot, self).__init__(
            conversation_state, user_state, dialog
        )

    async def on_members_added_activity(
        self, members_added: List[ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            # Greet anyone that was not the target (recipient) of this message.
            if member.id != turn_context.activity.recipient.id:
                return await self._send_welcome_message(turn_context)

    async def _send_welcome_message(self, turn_context: TurnContext):
        for member in turn_context.activity.members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    MessageFactory.text(
<<<<<<< Updated upstream
                        f"Welcome to AD Police Service Bot. This bot helps redirect you to your selected "
                        f"service page, and informs you about the requirements for the service. "
=======
                        f"Welcome to AD-Police Bot {member.name}. "
                        f"This bot will assist you in finding services offered on the AD-Police website."
>>>>>>> Stashed changes
                    )
                )

                await DialogHelper.run_dialog(
                    self.dialog,
                    turn_context,
                    self.conversation_state.create_property("DialogState"),
        )