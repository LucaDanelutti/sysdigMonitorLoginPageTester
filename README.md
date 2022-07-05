# Sysdig Monitor login page tester
This is a simple end to end tester for the Sysdig Monitor login page.

It's written in `python`, it uses `selenium` to simulate the user interaction and `unittest` to handle tests setup/execution/teardown automatically.

## How to run it
The following dependencies are needed:
* python3
* selenium library for python3 (`python3 -m pip install -r requirements.txt`)
* [GeckoDriver](https://github.com/mozilla/geckodriver/releases)
* [ChromeDriver](https://chromedriver.chromium.org)
* [Google Chrome](https://www.google.com/intl/it_it/chrome/)

Note: be sure to download the corresponding version of ChromeDriver based on your version of Google Chrome installed. E.g. If you are using Chrome version 103, please download ChromeDriver 103.0.5060.53

Simply execute `python3 tester.py`.

If you want you can specify one or more test cases. E.g. `python3 tester.py ForgotPasswordLink ChangeRegion`

## Future improvements
* Introduce different browsers other than Google Chrome
* Introduce different kind of devices (e.g. mobile phones, tablets)
* Add more tests. E.g:
    - Test the "Log in with:" options
    - Test the "Not a customer?" link
    - Submit an empty username/password
    - Check the form placeholders
    - Check UI styles
    - Check image urls
* After that, review the structure of test cases (group them toghether in subclasses/different files)