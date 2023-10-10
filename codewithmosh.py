# 12345
try:
    f = open('words.txt')
    # if f.name == 'words.txt':
    #     raise Exception

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print('Excuting Finally.....')
