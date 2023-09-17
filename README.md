
# 🧠 cerebrum 

Cerebrum is an script for collecting Razer Silver from the app Razer Cortex Games. It currently semi-automates watching ads for silver, and collects daily quests.

The cortex is the outer layer of the cerebrum. Which plays an important role in conciousness. Fitting for an "AI".


 ## 💠 Features 

- Watches and closes ad's
- Watches ad's for bonus silver
- Collects daily quest rewards
- Closes review nag screen


## 🖥️ Usage

- Connect USB and enable USB debugging on Android device.
- Open a cmd prompt and make sure you see your device listed when entering the command 'adb devices'. You can 'adb kill-server' then 'adb start-server' if you dont see your device.
- Open the app 'Razer Cortex Games'.
- Run main.py.

## 📦 Required Packages 
- airtest - https://airtest.readthedocs.io/en/latest/index.html
- pocoui - https://poco.readthedocs.io/en/latest/index.html
