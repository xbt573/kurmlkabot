# kurmlkabot

Telegram bot which detects anime in groups.

To start it, replace placeholders in env.sh to your data, and launch this command
```bash
. ./env.sh; python3 main.py
```

And of course, before launch don't forget install all dependencies, using commands below.
```bash
  pip install pyrogram
  pip install TgCrypto
  pip install opencv-python
  pip install animeface
  pip install Pillow
```

But if you're Windows user, yours adventures are not over yet)
Animeface will not work under Windows, so you need to install wsl, and no, this is not World Surf League, that's Windows Subsystem for Linux :)

Open your PowerShell and type 
```bash
  wsl --install
```
This will install wsl, probably you need to reboot after it.

After that you need to navigate to aka.ms/wsltore and download linux distro, choose whatever you want, I will use Ubuntu 22.04 LTS.

Install Ubuntu, run it, and create your user.
Next open cmd, and type wsl, if you did everything mentioned earlier, you will see your linux user.

Now, we need to install all the dependencies, but now in linux)

But first

```bash
  sudo apt-get update
```

Now lets install dependencies
```bash
  pip install pyrogram TgCrypto opencv-python animeface Pillow
```

```bash
  sudo apt install python3-opencv
```

Now you need to navigate into your project folder, in my case is "C:\Users\User\PycharmProjects\kurmlkabot"
But in terminal it's should look like this:
```bash
  cd PycharmProjects/kurmlkabot
```

Finally, navigate into env.sh file and write your api_id and hash_is, and also dont forget to write export before each statement.
It should look like this:
```bash
  export API_ID="your_api_id"
  export API_HASH="your_api_hash"
```

And now lets run our bot

```bash
  . ./env.sh; python3 main.py 
```

If bot is successfully running, you will receive this message "Enter phone number or bot token:"
Then enter your token, and now your bot is completely working. Enjoy!