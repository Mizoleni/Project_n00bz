import random
HANGMANPICS = ["""

+------------+
|  |      |
   |      
   |
   |
   |
   |
   |
   |
=======""","""

+------------+
|  |      |
   |      O
   |
   |
   |
   |
   |
   |
=======""","""

+------------+
|  |      |
   |      O
   |      |
   |
   |
   |
   |
   |
=======""","""

+------------+
|  |      |
   |      O
   |     /|
   |
   |
   |
   |
   |
=======""","""

+------------+
|  |      |
   |      O
   |     /|\
   |      |
   |      
   |
   |
   |
=======""","""


+------------+
|  |      |
   |      O
   |     /|\
   |      |
   |     /
   |
   |
   |
=======""","""


+------------+
|  |      |
   |      O
   |     /|\
   |      |
   |     / \
   |
   |
   |
=======""",]

words = """
goat 
centerless
fondle
hemihedral
appellate
sweaty
thiopental
flowering
pyromagnetic
hydriodic
antievolution
squirreled
multiciliate
clocker
irresistibly
conditional
caviler
banderol
ensnaringly
sidewalk
sarah
presympathizing
imprecise
jerre
undersecretaryship
unresurrected
serene
herborizing
nonassumption
woodland
phreneticness
woman
mongolism
idiotising
intermission
permutable
contractibility
overdying
surrealist
nonregenerating
chm
unscaled
sparlike
nonascendant
underqueen
advised
mailless
crusaded
subnitrate
spitter
bewilderedly
blustery
duranty
disbranch
pseudoarchaic
cognominally
outhiring
terete
leveret
subruler
susanna
populational
pall
bouilli
phenomenology
backfall
downrange
monospermal
glutinous
lokris
intumescency
reacceptance
uncurtailed
hylophagous
orlans
fetter
vanguard
comprize
howbeit
wadsetter
wombat
villeneuve
thornback
initiation
alyce
deisticalness
neurophysiological
inhabitable
snatch
azerbaijanian
incestuous
superobedient
transhipped
earthshaker
becquerel
iconoscope
amanuensis
semiprotected
wapperjaw
throe
biodynamic
arp
aegiale
suburb
dehortation
sebiferous
anabiotic
reisolation
evora
scarp
undergone
wheezier
supernotableness
imprescriptibly
smithsonite
noncutting
pierre
bacteriophage
proserpina
gauzier
sweetleaf
lawbook
anatomising
rising
nongraduate
nepotism
yapok
scorpaenid
chandragupta
pastoralized
italianized
rizzio
manichean
exercised
multipartisan
scrouge
colonelcy
chabrier
johnsbury
prefecundation
horsetail
taurine
lushiest
unconglutinative
maintainer
exhumation
need
muzzle
taoism
sagittae
warlock
whereon
pyrolysis
taoistic
uninvolved
salmanazar
einthoven
enforced
snapline
moslemic
thinking
mechelen
unbillable
menfolks
stoccata
multisacculated
korah
graecise
chrismon
conoscopic
osetian
presentive
unmigrant
skintight
jacobi
predivinable
sixmo
tenebrae
nonarbitrariness
untransplanted
stigmatizer
faberg
halaf
brecknock
postdiastolic
tonsorial
nonretardative
preconspired
rebait
argiope
gabber
unpalled
strigiform
whitethroat
depositaries
mercerize
hugli
manana
snub
maderno
unsquandered
scythe
adler
bypasser
unseceded
dislodgment
nephrotoxic
rechoose
wheels
osteopath
jcr
denominator
hydrophobia
diverticulitis
unscalloped
islay
lipochromic
wis
parthenogenetically
deneb
garrett
goonda
oxpecker
unwarrantable
beamlike
flockiest
racemously
overpotent
cacao
righteousness
bryozoa
institutionalise
munitus
traceable
starvedly
disseized
oscitance
suborbiculate
microcosmos
logopedia
antitarnish
sack
precollectable
harrisburg
alibi
tanganyika
interlie
nonprejudicial
yezd
unsplayed
media
coequality
intercranial
grasp
nonextraditable
cosmopolitanization
chlorosis
unacerbically
nonmucous
untantalised
jawan
superincumbency
nonvenous
anuresis
commissively
inhabitancy
diaphanousness
vertex
psychologist
electrolyte
lean
skeech
doutiming
petrolatum
ontogenically
enterozoon
grab
adonic
emotionalized
agadir
shoshone
housework
epicentre
geophagous
orthopter
nowise
grime
scheming
radiotherapy
interdentally
immotile
sweet
investigator
protoxid
quirites""".split()

def getRandomWord(wordList):#Function returns a random string from the list of strings.
    wordIndex = random.randint(0,len(wordList)-1)
    return wordList[wordIndex]
    
def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    print(HANGMANPICS[len(missedLetters)])
    print()
    
    print('Missed letters:',end="")
    for letter in missedLetters:
        print(letter, end="")
    print()
    
    blanks='_'*len(secretWord)
    
    for i in range(len(secretWord)): #replace the blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]
   
    for letter in blanks: #show the secret word with spaces in between each letter
        print(letter, end="")
    print()
    
def getGuess(alreadyGuessed): #Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess)!=1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Enter a L E T T E R!')
        else:
            return guess 
def playAgain(): #This function returns true if the player wants another go, otherwise returns false.
    print('You wanna play again dude?')
    return input().lower().startswith('y')
    
print('H A N G M A N')
missedLetters =""
correctLetters =""
secretWord = getRandomWord(words)
gamelsDone = False

while True:
    displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord)
    
    #let the player type in a letter.
    guess = getGuess(missedLetters + correctLetters)
    
    if guess in secretWord:
        correctLetters = correctLetters + guess
        
    #check if the player has won
    foundAllLetters = True
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            foundAllLetters = False
            break
    if foundAllLetters:
        print('Yes! The secret word is " + secretWord + "! You have won!')
        gameIsDone = True
        
        #ask the player if they'd like to play another game(but only if the game is done).
        if GameisDone:
            if playAgain():
                missedLetters = ""
                correctLetters = ""
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
                   
                         
    
