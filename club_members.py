"""Participation Activity 2: Basketball Varsity members."""

from pyscript import display
from js import document


GRADE_7 = {"Kevin Santos", "Keane Pacana"}
GRADE_8 = {"Divine Adili", "Kiefer Alas"}
GRADE_9 = {"Ethan Chase", "Thirdy Rovena"}
GRADE_10 = {"Sebastian Uclaray", "Almakram Arbison"}

MEMBERS = GRADE_7 | GRADE_8 | GRADE_9 | GRADE_10


def add_member(event=None):
    """Add a member and display the updated list."""
    first_name = document.getElementById("first-name").value.strip()
    last_name = document.getElementById("last-name").value.strip()

    if first_name and last_name:
        MEMBERS.add(f"{first_name} {last_name}")

    member_list = "<br>".join(sorted(MEMBERS))

    display(member_list, target="results")
    display(
        f"The total number of members: {len(MEMBERS)}",
        target="results"
    )