# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List

from botbuilder.dialogs import (
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
    ComponentDialog,
)
from botbuilder.dialogs.prompts import ChoicePrompt, PromptOptions
from botbuilder.dialogs.choices import Choice, FoundChoice
from botbuilder.core import MessageFactory


class ReviewSelectionDialog(ComponentDialog):
    def __init__(self, dialog_id: str = None):
        super(ReviewSelectionDialog, self).__init__(
            dialog_id or ReviewSelectionDialog.__name__
        )

        self.COMPANIES_SELECTED = "value-companiesSelected"
        #self.DONE_OPTION = "cancel"

        self.available_services = [
            "Fines' Materials Inquiry",
            "Vehicle's Accidents Inquiry",
            "Payment Receipts Inquiry",
            "Vehicle's Certificate Inquiry",
            "Reserved Plates Inquiry",
            "Traffic Fines Inquiry",
            "Registered Vehicles Inquiry",
            "Other Services",
        ]

        self.add_dialog(ChoicePrompt(ChoicePrompt.__name__))
        self.add_dialog(
            WaterfallDialog(
                WaterfallDialog.__name__, [self.selection_step, self.final_step]
            )
        )

        self.initial_dialog_id = WaterfallDialog.__name__

    async def selection_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        # step_context.options will contains the value passed in begin_dialog or replace_dialog.
        # if this value wasn't provided then start with an emtpy selection list.  This list will
        # eventually be returned to the parent via end_dialog.
        selected: [str] = step_context.options if step_context.options is not None else []
        step_context.values[self.COMPANIES_SELECTED] = selected

        # create a list of options to choose, with already selected items removed.
        options = self.available_services.copy()
    #    options.append(self.DONE_OPTION)
        if len(selected) > 0:
            options.remove(selected[0])

        # prompt with the list of choices
        prompt_options = PromptOptions(
            prompt=MessageFactory.text(f"Please choose a service to review."),
            retry_prompt=MessageFactory.text("Please choose an option from the list."),
            choices=self._to_choices(options),
        )
        return await step_context.prompt(ChoicePrompt.__name__, prompt_options)

    def _to_choices(self, choices: [str]) -> List[Choice]:
        choice_list: List[Choice] = []
        for choice in choices:
            choice_list.append(Choice(value=choice))
        return choice_list

    async def final_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        selected: List[str] = step_context.values[self.COMPANIES_SELECTED]
        choice: FoundChoice = step_context.result
        selected.append(choice.value)

        if (choice.value == "Fines' Materials Inquiry"):
            selected.append("This service allows you to search for traffic fines' materials values and black points. \n\n"
            f"**Requirment:** Emirate and Material code \n\n"
            f"* URL-Service: https://es.adpolice.gov.ae/trafficservices/PublicServices/MaterialsInquiry.aspx?Culture=en")
        #    selected.append("Emirate and Material code")
        #    selected.append("https://es.adpolice.gov.ae/trafficservices/PublicServices/MaterialsInquiry.aspx?Culture=en")

        elif (choice.value == "Vehicle's Accidents Inquiry"):
            selected.append("This service allows you to retrieve all accidents happened for a specific vehicle. \n\n"
                f"**Requirment:**Chassis Number \n\n"
                f"* URL-Service:https://es.adpolice.gov.ae/trafficservices/PublicServices/AccidentsInquiry.aspx?Culture=en")
        #    selected.append("Chassis Number")
        #    selected.append("https://es.adpolice.gov.ae/trafficservices/PublicServices/AccidentsInquiry.aspx?Culture=en")

        elif (choice.value == "Payment Receipts Inquiry"):
            selected.append("This service allows you to inquire for a specific receipt using its number. \n\n"
                f"**Requirment:**Receipt Number \n\n"
                f"* URL-Service:https://es.adpolice.gov.ae/trafficservices/PublicServices/ReceiptsInquiry.aspx?Culture=en")
        #    selected.append("Receipt Number")
        #    selected.append("https://es.adpolice.gov.ae/trafficservices/PublicServices/ReceiptsInquiry.aspx?Culture=en")

        elif (choice.value == "Vehicle's Certificate Inquiry"):
            selected.append("This service allows you to inquire about about a specific vehicle's certificate using its number. \n\n"
                f"**Requirment:**Certificate Number \n\n"
                f"* URL-Service:https://es.adpolice.gov.ae/trafficservices/PublicServices/CertificateInquiry.aspx?Culture=en")
        #    selected.append("Certificate Number")
        #    selected.append("https://es.adpolice.gov.ae/trafficservices/PublicServices/CertificateInquiry.aspx?Culture=en")

        elif (choice.value == "Reserved Plates Inquiry"):
            selected.append("This service allows you to check the expiry date for a reserved plate. \n\n"
                f"**Requirment:** Traffic Number, Plate Number, Plate Source, Plate Color, Plate Kind \n\n"
                f"* URL-Service:https://es.adpolice.gov.ae/trafficservices/PublicServices/ReservedPlatesInquiry.aspx?Culture=en")
        #    selected.append("Traffic Number, Plate Number, Plate Source, Plate Color, Plate Kind")
        #    selected.append("https://es.adpolice.gov.ae/trafficservices/PublicServices/ReservedPlatesInquiry.aspx?Culture=en")

        elif (choice.value == "Traffic Fines Inquiry"):
            selected.append("This service allows you to inquire about existing traffic fines. \n\n"
                f"**Requirment:**Traffic Number, Emirates ID, Vehicle Plate, or Driving License \n\n"
                f"* URL-Service:https://es.adpolice.gov.ae/TrafficServices/FinesPublic/Inquiry.aspx?Culture=en")
        #    selected.append("Traffic Number, Emirates ID, Vehicle Plate, or Driving License")

        #    selected.append("https://es.adpolice.gov.ae/TrafficServices/FinesPublic/Inquiry.aspx?Culture=en")

        elif (choice.value == "Registered Vehicles Inquiry"):
            selected.append("This service allows you to inquire about your registered vehicles.\n\n"
                f"**Requirment:** Username and Password \n\n"
                f"* URL-Service:https://es.adpolice.gov.ae/TrafficServices/Registration/login.aspx?ReturnUrl=%2fTrafficServices%2fPublicServices%2fRegisteredVehicles.aspx%3fCulture%3den&Culture=en")
        #    selected.append("Username and Password")
        #    selected.append("https://es.adpolice.gov.ae/TrafficServices/Registration/login.aspx?ReturnUrl=%2fTrafficServices%2fPublicServices%2fRegisteredVehicles.aspx%3fCulture%3den&Culture=en")

        elif (choice.value == "Other Services"):
            selected.append("You can visit the public services section in the AD Police website here.\n\n"
            f"* Service-URL: https://es.adpolice.gov.ae/TrafficServices/PublicServices/Default.aspx?Culture=en ")
        #    selected.append("")
        #    selected.append("https://es.adpolice.gov.ae/TrafficServices/PublicServices/Default.aspx?Culture=en")

        return await step_context.end_dialog(selected)
