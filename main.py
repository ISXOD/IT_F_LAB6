from matplotlib.pyplot import* #эту библиотеку необходимо предварительно установить, написав в командной строке pip install matplotlib

INF = 10000
E = 1000 # ЭДС [B]
R = 6 # сопротивление [Ом]
r = 4 # внутренне сопротивление [Ом]
Imax = E / r

arr_I, arr_U, arr_Efficiency, arr_PUseful, arr_PFull = [], [], [], [], []

for R in range(0, INF):

    I = E / (R + r)
    arr_I.append(I)

    U = E * (1 - I / Imax)
    arr_U.append(U)

    Efficiency = 1 - I / Imax
    arr_Efficiency.append(Efficiency)

    PUseful = E * I * (1 - I/Imax)
    arr_PUseful.append(PUseful)

    PFull = E * I
    arr_PFull.append(PFull)

figure()
title("зависимость напряжения")
xlabel("I")
ylabel("U")
plot(arr_I, arr_U)
savefig("U")

figure()
title("зависимость полной мощности")
xlabel("I")
ylabel("PFull")
plot(arr_I, arr_PFull)
savefig("PFull")

figure()
title("зависимость полезной мощности")
xlabel("I")
ylabel("PUseful")
plot(arr_I, arr_PUseful)
savefig("PUseful")

figure()
title("зависимость КПД")
xlabel("I")
ylabel("efficiency")
plot(arr_I, arr_Efficiency)
savefig("efficiency")
show()
