import locale
import os
import gettext

# run in console if new translations are includes:
# msgfmt -o locales/de/LC_MESSAGES/messages.mo locales/de/LC_MESSAGES/messages.po
# msgfmt -o locales/en/LC_MESSAGES/messages.mo locales/en/LC_MESSAGES/messages.po
LOCALE = os.getenv('LANG', 'de')
_ = gettext.translation('messages', localedir='locales', languages=[LOCALE]).gettext

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(_("hello_world"))
    print(_("this_is_a_test"))
