from pyscript import document, display

grade7 = {"Gerthy Bausa", "Jericho Magsalin"}
grade8 = {"Charles Lapid", "John Broas"}
grade9 = {"Achilles Obogne", "Euan Urbano",}
grade10 = {"Joaquin Castor", "Phoenix Hizon", "Erin Urbano"}

all_members = grade7 | grade8 | grade9 | grade10

def check_club(e):

    first_name = document.getElementById("firstName").value
    last_name = document.getElementById("lastName").value

    full_name = first_name + " " + last_name

    new_members = all_members | {full_name}

    members_list = "<br>".join(sorted(new_members))
    total_members = len(new_members)

    result = document.getElementById("result")
    result.innerHTML = f"""

    <h3>All Club Members</h3>

    {members_list}
    <br><br>
    Total Members: {total_members}
    """