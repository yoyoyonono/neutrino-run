import os
from datetime import datetime
os.chdir(os.getcwd())
# Project settings

fileList = os.listdir('.\\score\\musicxml\\')
print('Which one?')
print(*(f'{x}: {y}' for (x, y) in enumerate(fileList)), sep='\n')
sourceName = ''.join(fileList[int(input('?'))].split('.')[:-1])
numThreads = int(input('How many threads? (recommended 3): '))

# Project settings
extension = 'musicxml'

# NEUTRINO.exe
voiceList = os.listdir('.\\model\\')
print('Which one?')
print(*(f'{x}: {y}' for (x, y) in enumerate(voiceList)), sep='\n')
voiceDir = voiceList[int(input('?'))]
styleShift = int(input('What style shift? (recommended 0): '))

# WORLD.exe
pitchShift = float(input('What pitch shift? (recommended 1.0): '))
formantShift = float(input('What formant shift? (recommended 1.0): '))

print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} : start MusicXMLtoLabel')
os.system(f'.\\bin\\musicXMLtoLabel.exe score\\musicxml\\{sourceName}.{extension} score\\label\\full\\{sourceName}.lab score\\label\\mono\\{sourceName}.lab')

print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} : start NEUTRINO')
os.system(f'.\\bin\\NEUTRINO.exe score\\label\\full\\{sourceName}.lab score\\label\\timing\\{sourceName}.lab output\\{sourceName}.f0 output\\{sourceName}.mgc output\\{sourceName}.bap model\\{voiceDir}\\ -n {numThreads} -k {styleShift} -m -t')

print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} : start WORLD')
os.system(f'.\\bin\\WORLD.exe output\\{sourceName}.f0 output\\{sourceName}.mgc output\\{sourceName}.bap -f {pitchShift} -m {formantShift} -o output\\{sourceName}_syn.wav -n {numThreads} -t')

print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} : start NSF')
os.system(f'.\\bin\\NSF_IO.exe score\\label\\full\\{sourceName}.lab score\\label\\timing\\{sourceName}.lab output\\{sourceName}.f0 output\\{sourceName}.mgc output\\{sourceName}.bap {voiceDir} output\{sourceName}_nsf.wav -t')

print(f'{datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} : end')