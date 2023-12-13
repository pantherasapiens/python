import pandas as pd
import matplotlib.pyplot as plt

# Read the data from the CSV file
data = pd.read_csv("crimeRecord1.csv")

# Define the sections based on 'Crime Head' values
sections = [
    'Murder',
    'Culpable Homicide not amounting to Murder',
    'Causing Death by Negligence',
    'Dowry Deaths',
    'Abetment of Suicide',
    'Attempt to Commit Murder',
    'Attempt to commit Culpable Homicide',
    'Attempt to Commit Suicide',
    'Miscarriage, Infanticide, Foeticide and Abandonment',
    'Hurt',
    'Wrongful Restraint/Confinement',
    'Assault on Women with Intent to Outrage her Modesty',
    'Kidnapping and Abduction',
    'Human Trafficking',
    'Exploitation of Trafficked Person',
    'Selling of Minors for Prostitution',
    'Buying of Minors for Prostitution',
    'Rape',
    'Offences against State',
    'Unlawful Assembly',
    'Riots',
    'Offences promoting enmity between different groups',
    'Affray',
    'Theft',
    'Burglary',
    'Extortion & Blackmailing',
    'Robbery',
    'Attempt to Commit Dacoity/Robbery',
    'Dacoity',
    'Making Preparation and Assembly for committing Dacoity',
    'Criminal Misappropriation',
    'Criminal Breach of Trust',
    'Dishonestly Receiving/Dealing-in Stolen Property',
    'Offences relating to Documents & Property Marks',
    'Offences relating to Elections',
    'Disobedience to order duly promulgated by Public Servant',
    'Harbouring an Offender',
    'Offences relating to Adulteration or Sale of Food/Drugs',
    'Rash Driving on Public way',
    'Obstruction on Public way',
    'Sale of obscene Books/Objects',
    'Obscene Acts and Songs at Public Places',
    'Offences relating to Religion',
    'Cheating by Impersonation',
    'Offences related to Mischief',
    'Arson',
    'Criminal Trespass',
    'Cruelty by Husband or his Relatives',
    'Circulate False/Fake News/Rumours',
    'Criminal Intimidation',
    'Insult to the Modesty of Women',
    'Other IPC crimes'
]

# Loop through and process each section based on 'Crime Head'
for section in sections:
    section_data = data[data['Crime Head'] == section]
    
    # Plotting
    plt.figure(figsize=(10, 6))
    plt.title(f"Crime Cases for {section}")
    plt.plot(section_data['SL'], section_data['Cases (2019)'], label='2019 Cases')
    plt.plot(section_data['SL'], section_data['Cases (2020)'], label='2020 Cases')
    plt.plot(section_data['SL'], section_data['Cases (2021)'], label='2021 Cases')
    
    plt.xlabel('Serial Number')
    plt.ylabel('Number of Cases')
    plt.legend()
    plt.grid(True)
    
    # Show or save the plot for each section
    plt.show()