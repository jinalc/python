import re

# 1. Write a regex(WAR) that matches the word ‘python’ case insensitive.
print('1. Write a regex(WAR) that matches the word ‘python’ case insensitive.')
pattern1 = '\\bpython\\b'
str1 = 'hi this is python or Python or pyTHon string'
result = re.findall(pattern1, str1, re.I)
print(result)
print()

# 2. WAR that matches any string of any length except newlines.
print('2. WAR that matches any string of any length except newlines.')
pattern2 = '\S+'
str2 = '''hi this is first line
this is second line'''
result = re.findall(pattern2, str2)
print(result)
print()

# 3. WAR that matches stings in the format ‘aaaabbbb’, where a denotes digit and b denotes nondigit symbols.
print('3. WAR that matches stings in the format ‘aaaabbbb’, where a denotes digit and b denotes nondigit symbols.')
pattern3 = '(\d{4}\D{4})'
str3 = '1234rtyu mnjkloper 0987njik 9087$%^&'
result = re.findall(pattern3, str3)
print(result)
print()

# 4. WAR to match xx_xx_XX, where x = any alphabet; _ = any white space; X = any nonwhitespace.
print('4. WAR to match xx_xx_XX, where x = any alphabet; _ = any white space; X = any nonwhitespace.')
pattern4 = '([A-Z|a-z]{2}\s{1}[A-Z|a-z]{2}\s{1}\S{2})'
str4 = '''ad rt jj 12 rt jj rty gh 23 vn
qw rt '''
result = re.findall(pattern4, str4)
print(result)
print()

# 5. WAR to match strings starting with 3 digit characters.
print('5. WAR to match strings starting with 3 digit characters.')
pattern5 = '\\b\d{3}[\D]*\\b'
str5 = 'rty678 123erty 345fghj rew321 rt567hjk $$1234 123'
result = re.findall(pattern5, str5)
print(result)
print()

# 6. WAR to match individual characters which are not vowels.
print('6. WAR to match individual characters which are not vowels.')
pattern6 = '[^aeiou]'
str6 = 'This is string. It has vowel and non-vowel characters.'
result = re.findall(pattern6, str6, re.I)
print(result)
print()

# 7. WAR that matches any 4 digit number.
print('7. WAR that matches any 4 digit number.')
pattern7 = '\d{4}'
str7 = 'werty5678 1234 fg6789 098jd45 '
result = re.findall(pattern7, str7)
print(result)
print()

# 8. WAR to match numbers with 6-10 digits.
print('8. WAR to match numbers with 6-10 digits.')
pattern8 = '\d{6,10}'
str8 = '123456tyhuiop 12fgyu rtyu1234567890bhui'
result = re.findall(pattern8, str8)
print(result)
print()

# 9. WAR to match any lower case alphabet.
print('9. WAR to match any lower case alphabet.')
pattern9 = '[a-z]'
str9 = 'TEST this StrfiG'
result = re.findall(pattern9, str9)
print(result)
print()

# 10. WAR to match all strings of the form ABBBBBB; where B can repeat 0 or more times.
print('10. WAR to match all strings of the form ABBBBBB; where B can repeat 0 or more times.')
pattern10 = '\\bA[B]*\\b'
str10 = 'A AA ABB ABBBBB AAAAB AB'
result = re.findall(pattern10, str10)
print(result)
print()

# 11. WAR to match all string ending in any of these three characters (., ?, !)
print('11. WAR to match all string ending in any of these three characters (., ?, !)')
pattern11 = '[^?.!]+[?.!]$'
str11 = 'This. that! what?'
result = re.findall(pattern11, str11)
print(result)
print()

# 12. WAR to match and extract values of all 3 digit numbers.
print('12. WAR to match and extract values of all 3 digit numbers.')
pattern12 = '\d{3}'
str12 = 'This123yju. 345That567! What?567 ?ght567y ij?JIN 456'
result = re.findall(pattern12, str12)
print(result)
print()

# 13. WAR to check if a string is a negative string i.e. If contains any of the words: not, no,
print('13. WAR to check if a string is a negative string i.e. If contains any of the words: not, no,')
pattern13 = '\\bno[?t]{0,1}\\b'
str13_1 = 'this is a positive sentence'
str13_2 = 'this is not a postive sentence'
str13_3 = 'there is no positive sentence here'
result = re.search(pattern13, str13_1)
if result:
    print('true')
else:
    print('false')
result = re.search(pattern13, str13_2)
if result:
    print('true')
else:
    print('false')
result = re.search(pattern13, str13_3)
if result:
    print('true')
else:
    print('false')
print()

# 14. WAR to extract XML tags [use backreference to validate and groups to extract content and the tag]
print('14. WAR to extract XML tags [use backreference to validate and groups to extract content and the tag]')
pattern14_1 = '<[\w|\s]*[?=][?"][\w]*[?"]>'
pattern14_2 = '<[\w|\s]*>'
pattern14_3 = '<[?/][\w|\s]*>'
str14 = '''<?xml version="1.0" ?>
<Configuration>
    <Appenders>
        <Routing name="file">
            <Routes pattern="$${main:0}">
                <!-- This route is chosen if there is no value for main argument 0 -->
                <Route key="$${main:0}">
                    <File fileName="test-output/logs/init.log" name="file-init">
                        <PatternLayout pattern="%d [%t] %-5level: %msg%n%throwable"/>
                    </File>
                </Route>
                <!-- This route is chosen if there is a value for main argument 0 -->
                <Route>
                    <File fileName="test-output/logs/${main:0}.log" name="file-${main:0}">
                        <PatternLayout pattern="%d [%t] [${main:0}] %-5level: %msg%n%throwable"/>
                    </File>
                </Route>
            </Routes>
        </Routing>
        <Console name="console" target="SYSTEM_OUT">
            <PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} - %msg%n" />
        </Console>
    </Appenders>
    <Loggers>
        <Root level="DEBUG">
            <AppenderRef ref="file"/>
            <AppenderRef ref="console"/>
        </Root>
    </Loggers>
</Configuration>'''
result = re.findall(pattern14_1, str14)
print(result)
result = re.findall(pattern14_2, str14)
print(result)
result = re.findall(pattern14_3, str14)
print(result)
print()
