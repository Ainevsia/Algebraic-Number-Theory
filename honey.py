def multipleReplace(text, wordDict):
    for key in wordDict:
        text = text.replace(key, wordDict[key])
    return text


dict = {
    'âŽ¼': 'r',
    'âŽº': 'o',
    'â”œ': 't',
    'â””': 'm',
    'â‰¤': 'y',
    'âŒ': 'c',
    'âŽ»': 'p',
    'â”¤': 'u',
    'âŠ': 'e',
    'Â·': '~',
    'â‰': 'b',
    'â‹': 'i',
    'âŽ½': 's',
    'â”Œ': 'l',
    'â–’': 'a',
    'â”‚': 'x',
    'Ï€': '{',
    'â”¬': 'w',
    'â': 'd',
    'Â°': 'f',
    'Â±': 'g',
    'Â£': '}',
    'â¤': 'h',
    'â”¼':'n'
}

s = '''root@myLOVELYcomputer:~/cybrics# ls -la
total 12
drwxr-xr-x  2 root root 4096 Jul 22  2019 .
drwxr-xr-x 21 root root 4096 Jul 22  2019 ..
-rw-r--r--  1 root root   44 Jul 22  2019 flag
root@myLOVELYcomputer:~/cybrics# echo $'\e(0'

âŽ¼âŽºâŽºâ”œ@â””â‰¤LOVELYâŒâŽºâ””âŽ»â”¤â”œâŠâŽ¼:Â·/âŒâ‰¤â‰âŽ¼â‹âŒâŽ½# â”ŒâŽ½ -â”Œâ–’
â”œâŽºâ”œâ–’â”Œ 12
ââŽ¼â”¬â”‚âŽ¼-â”‚âŽ¼-â”‚  2 âŽ¼âŽºâŽºâ”œ âŽ¼âŽºâŽºâ”œ 4096 Jâ”¤â”Œ 22  2019 .
ââŽ¼â”¬â”‚âŽ¼-â”‚âŽ¼-â”‚ 21 âŽ¼âŽºâŽºâ”œ âŽ¼âŽºâŽºâ”œ 4096 Jâ”¤â”Œ 22  2019 ..
-âŽ¼â”¬-âŽ¼--âŽ¼--  1 âŽ¼âŽºâŽºâ”œ âŽ¼âŽºâŽºâ”œ   44 Jâ”¤â”Œ 22  2019 Â°â”Œâ–’Â±
âŽ¼âŽºâŽºâ”œ@â””â‰¤LOVELYâŒâŽºâ””âŽ»â”¤â”œâŠâŽ¼:Â·/âŒâ‰¤â‰âŽ¼â‹âŒâŽ½# âŒâ–’â”œ Â°â”Œâ–’Â± 
âŒâ‰¤â‰âŽ¼â‹âŒâŽ½Ï€â¤0â”Œâ‰¤_âŒâŽ¼4âŽ»_1âŽ½_â”œâ¤â‹âŽ½_â–’â”Œ13â”¼â‹$â¤_0âŽ¼_â”¬4â”œ?Â£
âŽ¼âŽºâŽºâ”œ@â””â‰¤LOVELYâŒâŽºâ””âŽ»â”¤â”œâŠâŽ¼:Â·/âŒâ‰¤â‰âŽ¼â‹âŒâŽ½# '''
print(multipleReplace(s, dict))
