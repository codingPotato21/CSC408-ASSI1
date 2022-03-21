# Example AD-Police Service Guide Bot.

This Bot provides an example Bot that introduces users to the services offered by the AD-Police.

## To try the Bot

### Creating and activating the virtual environment

- [On Linux/macOS]
- Create a venv `python3 -m venv venv`
- Activate the venv `source venv/bin/activate`

- [On Windows]
- Create a venv `python -m venv venv`
- Activate the venv `cvenv\Scripts\activate.bat`

Keep in mind that the virtual environment needs to be activated every time when the Bot code
needs to be worked on using the second command. The first command for creating the virtual
environment needs to be run only once when creating the project.

### Installing Required Libraries

- `pip install -r requirements.txt`

### Running the Bot

- [On Linux/macOS]
- `python3 app.py`

- [On Windows]
- `python app.py`

### Testing the Bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/Botframework-emulator) is a desktop application that allows Bot developers to test and debug their Bots on localhost or running remotely through a tunnel.

- Install the latest Bot Framework Emulator from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the Bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- File -> Open Bot
- Enter a Bot URL of `http://localhost:3978/api/messages`

### Deploy the Bot to Azure

To learn more about deploying a Bot to Azure, see [Deploy your Bot to Azure](https://aka.ms/azuredeployment) for a complete list of deployment instructions.

## MIT License

- This example as well as the original examples provided by the Microsoft Azure team are licensed under the MIT license.

MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Important disclaimer

- This Bot was made as an example for a university assignement we are not responsible for any of the following:

If someone will want to use or try this example I or any of the contributors don't take responsibility for ruined software/hardware both local or remote be it privately owned or public, broken computers, broken servers, dead drives, any sort of legal issues or any issue in general, thermonuclear war or you loosing your sleep because it didn't work and you had to fix it.

Please do some research, if you have any concerns about features included in this example before using it!
YOU are choosing to make these modifications to your software/hardware or onto a cloud service, and if you point the finger at us for messing up your equipment or getting into trouble, we will laugh at you.

Thank you.
