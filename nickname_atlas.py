

from pyscript import display, document


def search_nickname(event=None):
    """Display the nickname selected by the user."""
    document.getElementById("display1").innerHTML = ""

    nickname = document.getElementById("country_input").value

    if nickname:
        display(nickname, target="display1")
    else:
        display("Please choose a country.", target="display1")