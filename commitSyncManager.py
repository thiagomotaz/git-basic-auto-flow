import subprocess

args = ['a.exe']
p = subprocess.Popen(args,
		stdin=subprocess.PIPE,
		stdout=subprocess.PIPE,
		stderr=subprocess.PIPE,
		text=True)

saida = p.communicate("MensagemCommit") #tentar receber por args via terminal

print("Saidas do subprocesso");
print("\n-----------------------\nSaida padrao: \n" + saida[0] + "\n------------------------\n");

print("Programa python finalizado")