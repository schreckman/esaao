from src import application_gui as ag

# run in console if new translations are includes:
# msgfmt -o locales/de/LC_MESSAGES/messages.mo locales/de/LC_MESSAGES/messages.po
# msgfmt -o locales/en/LC_MESSAGES/messages.mo locales/en/LC_MESSAGES/messages.po

if __name__ == '__main__':
    app = ag.App()
    app.mainloop()
