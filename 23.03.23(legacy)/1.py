'''великая китайская мудрость гласит: если то что тебе нежно есть в интернете - скопируй это'''
def reversed3(variable):
    if len(variable) == 1:
        return variable
    return variable[-1] + reversed3(variable[:-1])

n = reversed3(input())
print(n)