s=int(input())
hora=3600

converterh= s / hora
converterm= s % hora
converterm2= converterm / 60
converterm3= converterm % 60

print("{0:.0f}:{1:.0f}:{2:.0f}".format(converterh,converterm2,converterm3))
