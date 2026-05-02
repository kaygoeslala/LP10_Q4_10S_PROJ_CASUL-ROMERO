from pyscript import document, display
import numpy as np
import matplotlib.pyplot as plt

days = []
absences = []

def displaying(e):

    day = document.getElementById('dayInput').value
    absence = int(document.getElementById('absenceInput').value)

    days.append(day)
    absences.append(absence)

    converted_absences = np.array(absences)

    plt.clf()

    fig, ax = plt.subplots()

    ax.plot(days, converted_absences, marker='o')
    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Absences")
    ax.grid()

    # 🔥 IMPORTANT: prevent stacking
    document.getElementById("plot").innerHTML = ""

    # 🔥 THIS replaces plt.show()
    display(fig, target="plot", append=False)