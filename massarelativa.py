pesoaa={'A':89.094, #g/mol
        'R':174.204,
        'N':132.12,
        'D':133.08,
        'C':121.16,
        'E':147.130,
        'Q':146.146,
        'G':75.067,
        'H':155.157,
        'I':131.17,
        'L':131.17,
        'K':146.19,
        'M':149.21,
        'F':165.19,
        'P':115.13,
        'S':105.09,
        'T':119.12,
        'W':204.22,
        'Y':181.19,
        'V':117.15}
cadeia1="IPEYVDWRQKGAVTPVKNQGSCGSCWAFSAVVTIEGIIKIRTGNLNQYSEQELLDCDRRSYGCNGGYPWSALQLVAQYGIHYRNTYPYEGVQRYCRSREKGPYAAKTDGVRQV"
    #insert("Entre a cadeia 1:")
cadeia2="QPYNQGALLYSIANQPVSVVLQAAGKDFQLYRGGIFVGPCGNKVDHAVAAVGYGPNYILIKNSWGTGWGENGYIRIKRGTGNSYGVCGLYTSSFYPVKN"
    #insert("Entre a cadeia 2:")
cadeiateste=list("QGSCGSCWAFS")
def somadospesos(cadeia):
    somafinal=0
    for i in range(len(cadeia)):
        somafinal+=pesoaa[cadeia[i]]
    return somafinal
m1=somadospesos(cadeia1)
m2=somadospesos(cadeia2)
mu=(m1+m2)/m1*m2
print ("massa relativa:",mu)
hcortado=1.054*10**-34

E=hcortado*(3/mu)**0.5
print("Solução de Shrodinger:",E)
