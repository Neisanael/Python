print("=====================================================================")
freq = int(input("Insert Sound Frequency : "))
print("Deciding Which one is the sound...")
if freq <= 130 and freq > 106 :
    decide = "Jackhammer"
if freq <= 106 and freq > 70 :
    decide = "Gas Lawnmower"
if freq <= 70 and freq > 40 :
    decide = "Alarm Clock"
if freq <= 40 and freq > 0 :
    decide = "Quiet Room"
if freq <= 0 :
    decide = "what is this shit ?"
print("The sound of ", decide)
print("=====================================================================")