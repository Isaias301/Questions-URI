while True:
    try:
        text = list(input())
        first_i = True
        first_b = True
        for i in range(len(text)):
            if text[i] == '_':
                if first_i:
                    text[i] = '<i>'
                    first_i = False
                else:
                    text[i] = '</i>'
                    first_i = True
            elif text[i] == '*':
                if first_b:
                    text[i] = '<b>'
                    first_b = False
                else:
                    text[i] = '</b>'
                    first_b = True
        print(''.join(text))
    except:
        break
