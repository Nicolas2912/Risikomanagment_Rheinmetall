import random
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import skew


realX = []
realY = [189.1127166748047, 190.29312133789062, 191.2276153564453, 188.17822265625, 192.801513671875, 189.26025390625, 191.4243621826172, 189.35862731933594, 193.88357543945312, 193.34254455566406, 195.65419006347656, 193.58847045898438, 194.42459106445312, 196.24440002441406, 198.11338806152344, 182.71878051757812, 177.65283203125, 183.75164794921875, 188.07984924316406, 183.7024688720703, 187.09616088867188, 190.0963897705078, 190.34231567382812, 183.01388549804688, 193.7360076904297, 197.22808837890625, 195.7525634765625, 198.80197143554688, 205.9828338623047, 209.5240936279297, 208.14694213867188, 204.80242919921875, 209.5240936279297, 206.6714324951172, 212.37677001953125, 217.68865966796875, 217.295166015625, 219.55764770507812, 220.34458923339844, 218.77069091796875, 219.45928955078125, 217.295166015625, 223.7874755859375, 223.7874755859375, 223.49237060546875, 210.50778198242188, 215.8196563720703, 222.31195068359375, 223.7874755859375, 222.8037872314453, 222.016845703125, 221.91848754882812, 222.11521911621094, 227.91893005371094, 230.77162170410156, 232.83734130859375, 236.77206420898438, 244.0513153076172, 245.52684020996094, 244.93661499023438, 253.00282287597656, 242.6741485595703, 241.39535522460938, 240.9035186767578, 239.9198455810547, 236.6737060546875, 242.18231201171875, 242.4774169921875, 244.54315185546875, 253.00282287597656, 251.42892456054688, 253.7897491455078, 252.8060760498047, 249.1664581298828, 242.2806854248047, 253.49465942382812, 240.706787109375, 242.96925354003906, 233.23081970214844, 245.82192993164062, 252.90444946289062, 251.72401428222656, 256.83917236328125, 258.7081604003906, 267.1678161621094, 268.9384460449219, 267.9547424316406, 267.2662048339844, 269.13519287109375, 271.200927734375, 273.46337890625, 253.9864959716797, 255.0685272216797, 258.8065185546875, 261.0690002441406, 262.8396301269531, 262.64288330078125, 265.49554443359375, 265.7906799316406, 265.9873962402344, 266.2825012207031, 269.4302673339844, 272.57806396484375, 258.51141357421875, 263.0363464355469, 261.1673583984375, 261.2657470703125, 264.02001953125, 257.42938232421875, 262.05267333984375, 260.6755065917969, 259.1999816894531, 263.3999938964844, 259.29998779296875, 266.79998779296875, 267.1000061035156, 264.8999938964844, 261.70001220703125, 263.20001220703125, 261.6000061035156, 263.20001220703125, 248.8000030517578, 247.6999969482422, 247.5, 247.60000610351562, 245.1999969482422, 236.39999389648438, 240.10000610351562, 236.39999389648438, 235.1999969482422, 236.5, 236.39999389648438, 240.5, 247.89999389648438, 245.3000030517578, 247.6999969482422, 259.8999938964844, 260.1000061035156, 258.20001220703125, 258.70001220703125, 256.5, 255.89999389648438, 245.1999969482422, 242.8000030517578, 249.10000610351562, 249.89999389648438, 250.8000030517578, 251.89999389648438, 252.3000030517578, 249.1999969482422, 241.39999389648438, 242.1999969482422, 249.3000030517578, 250.6999969482422, 252.3000030517578, 254.0, 252.89999389648438, 253.39999389648438, 258.79998779296875, 256.8999938964844, 257.3999938964844, 255.8000030517578, 255.10000610351562, 253.3000030517578, 252.89999389648438, 253.89999389648438, 253.10000610351562, 257.3999938964844, 262.5, 263.8999938964844, 259.0, 264.8999938964844, 268.3999938964844, 266.79998779296875, 265.5, 260.1000061035156, 264.79998779296875, 259.79998779296875, 249.89999389648438, 247.39999389648438, 249.39999389648438, 249.0, 245.6999969482422, 248.60000610351562, 245.3000030517578, 243.3000030517578, 248.8000030517578, 249.89999389648438, 248.10000610351562, 251.3000030517578, 248.1999969482422, 247.60000610351562, 248.89999389648438, 246.6999969482422, 244.6999969482422, 244.60000610351562, 251.8000030517578, 255.0, 254.10000610351562, 256.79998779296875, 260.5, 265.0, 260.70001220703125, 258.20001220703125, 250.89999389648438, 250.39999389648438, 248.8000030517578, 250.8000030517578, 248.39999389648438, 251.6999969482422, 243.89999389648438, 239.5, 237.1999969482422, 233.0, 234.39999389648438, 233.8000030517578, 250.5, 254.60000610351562, 261.5, 268.6000061035156, 269.1000061035156, 269.6000061035156, 268.0, 267.1000061035156, 258.29998779296875, 259.8999938964844, 258.8999938964844, 267.0, 266.70001220703125, 271.0, 266.1000061035156, 270.1000061035156, 270.3999938964844, 276.5, 271.5, 270.3999938964844, 272.3999938964844, 271.8999938964844, 274.5, 272.0, 273.6000061035156, 282.5, 278.70001220703125, 280.29998779296875, 276.79998779296875, 279.1000061035156, 278.79998779296875, 289.1000061035156, 289.0, 283.5, 283.3999938964844, 276.1000061035156]
print(len(realY))
for t in range(len(realY)):
    realX.append(t)

anzahlSims = 1000
x = [len(realY)]
y = []
for n in range(anzahlSims):
    y.append([276.0])

for t in range(100):
    x.append(t+1+len(realY))
    for n in range(anzahlSims):
        Zufallszahl = np.random.normal()
        r=np.exp(Zufallszahl * 30/281.5*np.sqrt(1.0/len(realY)))
        #r=np.random.normal(1,0.01)
        y[n].append(y[n][t]*r)

plt.plot(realX, realY)
for n in range(anzahlSims):
    plt.plot(x, y[n])


plt.title('Rheinmetall - Markov Chain')
plt.legend()
plt.grid()
plt.xlabel("Zeit in Tagen")
plt.ylabel("Preis in €")
# Show the plot
plt.show()

distributions = []
for i in range(anzahlSims):
    distributions.append(y[i][100])
plt.hist(distributions, bins=30, density=True, alpha=0.7, color='skyblue', edgecolor='black')

plt.title('Product Distribution', fontsize=16, fontweight='bold')
plt.xlabel('Value', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.gca().set_facecolor('#f5f5f5')
plt.gca().patch.set_alpha(0.1)
plt.show()



print(skew(distributions))