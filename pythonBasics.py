# this File Is my cheatsheet for python commands and syntax
# mostly using Camel Case

#function with global var example
def function():
    global testGlobalVar        # I don't think that we should use global variables this way.
    testGlobalVar = 4
    print("function example")

#declaration
numberOne,numberTwo,numberThree = 1,2,3
tab = [numberOne,numberTwo,numberThree]
a,b,c = tab

#print can combine only the same type
print("three numbers are :" + str(a) + " "+ str(b) + " " + str(c))

textOne = "text 1"
textTwo = "text 2"
mergerText = textOne + textTwo

print(a+b)

#function with global var example continuation
function()
print(testGlobalVar)

'''
data types:
text:
    -str
Number:
    - int
    - float
    - complex (complex is for imaginary numbets example : number = 4 + 2j  !!!be careful j not i!!! )
map:
    - dict
sequence:
    - list 
    - tuple
    - range
bool:
    - bool
Binary:
    - bytes
    - bytearray
    - memoryview

checking type : type(var)
'''
stringType = "example" 
intType = 24
floatType = 24.5
complexType = 4 + 5j
listType = ["one", "two", "three"]
tupleType = ("one", "two", "three")
rangeType = range(4)
dictType = {"mother": "Dorota", "father": "Piotr"}
setType = {"one", "two", "three"}
frozensetType  = ({"one", "two", "three"}) #makes set immutable 
boolType = True
bytesType = b"FFFF"
bytearrayType = bytearray(4)
memoryviewType = memoryview(bytes(4))

# conversion between numbers for example is possible (casting for int float + str)
intVal = int(floatType)
floatVal = float(intType)
complexVal = complex(intType)

#random 
import random
rand = random.randrange(1,10)
print(rand)

#string
basicString = "hello world!"
fewSentences = """hello my name is Jacob.       
I would love to be a machine learning expert.
That is why I am learning python."""    #line end is also saved so the structure is exactly as shown
letterE = basicString[1] #every tab starts from zero :)
print(letterE)

#looping through every letter in a word
for letter in "word":
    print(letter)

#checking length
len(basicString)

#check if a word is used in text returning true or false
jacobName = "Jacob" in fewSentences
print(jacobName)
notJacobName = "Jacob" not in fewSentences
print(notJacobName)

#slicing strings
sliceBasicString = basicString[0:4] # letters 0-3 so excluding 4
print(sliceBasicString)

#slicing from start and end
sliceStart = basicString[:5]
sliceEnd = basicString[6:]

#negative indexing is also possible 
negativeIndexing = basicString[-6:-1]
print(negativeIndexing)

#converting into upperCase and loverCase
upperBasicString = basicString.upper()
lowerBasicString = basicString.lower()

#removing whitespace
noWhitespacesBasicString = basicString.strip()

#replacing letters
replacesBasicString = basicString.replace("l","k")

#spliting string deletes the splitter and separates every split
splitingBasicString =basicString.split("l")
print(splitingBasicString)

#combining strings
combinedString = basicString + "Sentence:" + fewSentences

#combining string and int using format
winningNumber = 3
notWinningNumber = 17
text = "winning number is {} not {}"		
print(text.format(winningNumber,notWinningNumber))
text = "winning number is {1} not {0}"		# can aslo add {0} to place format argument 0 in this place
print(text.format(winningNumber,notWinningNumber))

''' 
espace characters:   (used for example in text)
\' - single quote
\\ - backlash
\n - newline
\r - carriage return
\t - tab
\b - backspace
\f - form feed (not sure what this one is)
\ ooo - octal value
\ xhh -hex value
'''

'''
string methods:		(few of them)
capitalize() - first character to upperCase
center() - centering text for example text ="abcd" (10) is equal to "   abcd   "
count() - ("v") counts numbers of letter v in text
encode() - returnds encoded text
endswith() - ("v") bool if the text ends with v letter
expandtabs() - set tab size in string for example (2)
find() - ("v") searches for the v and returns position
format() - line 128 in this file
index() - exactly same as find()
islanum() - true/false if the text is all numerical
isalpha() - true/false if the text is all alphabet letters
isdecimal() -true/false if the text is all decimal
isdigit() - true/false if the text is all digits
islower() - true/false if the text is all lowerCase
isprintable() - true/false if the text is printable
isspace() - true/false if the text is all whitespaces
isupper() - true/false if the text is all upperCase
join() - joins the element to the text
lower() - converts text to lowerCase
strip() - line 112 in this file
partition() - returns tuple parted into 3 parts
replace() - line 115 in this file
rfind() - ("v") searches for the v and returns the last position
rindex() - ("v") searches for the v and returns the last position
rsplit() - line 118 in this file
rstrip() - line 112 in this file
split() - line 118 in this file
splitlines() - split string at line breaks and return list of them
startswith() - true/false if text stars with specific value
strip() - line 112 in this file
swapcase() - lowerCase becomes upperCase and the opposite
title() - converts first character of each word into upperCase
translate() - for example mydict = {h:s} translates h to s in the text
upper() -  converts to upperCase
zfill() -  fills text with 0 for example text=44 text.zfill(5) -> text = 00044
'''

#Bool is True or False
#if statement returns bool
#every number is true except 0
print(bool("1"))
print(bool(1))
print(bool(0))

#list sets and tuples are true if they are not empty
#it can be also checked with:
checkBoolValue = 10
print(isinstance(checkBoolValue, int))


'''
Operators in python
+ - add
- - subtract
* - multiply
/ - divide
% - modulo
** - x^y
// - floor division

Asignment Operators (self explainatory mostly)
=
+=
-=
*=
/=
%=
**=
//=
&= -> bit and
|= -> bit or
^= -> bit xor
>>= -> bitshift right
<<= -> bitshift left

Comparison Operators (self explainatory)
==
!=
>
<
>=
<=

Logical Operators (self explainatory)
and
or
not

Identity Operators (self explainatory)
is
is not

Membership Operators (self explainatory)
in
not in

Bitwise Operators
& - and
| - or
^ - xor
~ - not
<< - zero fill left shift (shift left - shl)
>> - signed right shift (shift arithmetic right - sar)
'''
