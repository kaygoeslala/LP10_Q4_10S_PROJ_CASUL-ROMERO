from pyscript import document

takenuser = {
    "Ancheta, Arthur Eugene Maximus Adarna": ("Sapphire", "Math"),
    "Asuncion, Miguelito Alonso Brigoli": ("Sapphire", "FARTS"),
    "Battung, John Lorenzo Quisumbing": ("Sapphire", "FOOTBALL"),
    "Bautista, John Paul De Guzman": ("Sapphire", "URU"),
    "Cade Chua": ("Sapphire", "Goku")
}

def ShowClassmates(event):
    classmates = ""

    for username, (section, fav_character) in takenuser.items():
        classmates += f"""
        <div>
            <b>Name:</b> {username}<br>
            <b>Section:</b> {section}<br>
            <b>Favorite Character:</b> {fav_character}<br>
            <hr>
        </div>
        """

    document.getElementById("classmate-list").innerHTML = classmates

def AddClassmate(event):

    username = document.getElementById("username").value.strip()
    section = document.getElementById("section").value.strip()
    fav_character = document.getElementById("fav").value.strip()

    if not username or not section or not fav_character:
        document.getElementById("signed").innerText = "Please fill in all fields!"
        return

    if username in takenuser:
        document.getElementById("signed").innerText = "You're already here!"
        return

    takenuser[username] = (section, fav_character)
    document.getElementById("signed").innerText = f"{username} added successfully!"

    # clear inputs
    document.getElementById("username").value = ""
    document.getElementById("section").value = ""
    document.getElementById("fav").value = ""

    # 🔥 AUTO REFRESH LIST
    ShowClassmates(None)