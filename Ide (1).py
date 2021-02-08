from itertools import product
print('LET THE EXPERIMENT IS OF TOSSING THREE COINS')
n=3
sample_space=set(product(['H','T'],repeat=n))
print('REQUIRED SAMPLE SPACE WILL BE ',sample_space,'=8')
lenght=len(sample_space)
print("LET OUS ASSUME THAT THE OUTCOMES WILL BE TAILS APPERA FIRST")
A={OT for OT in sample_space if OT[0]=='T'}
print('THEN THE DESIRED OUTCOME BE A=',A,'=4')
def prob(X):
     return len(X)/len(sample_space)
print('THEREFORE THE P(A)=',prob(A))

LET THE EXPERIMENT IS OF TOSSING THREE COINS
REQUIRED SAMPLE SPACE WILL BE  {('T', 'H', 'T'), ('H', 'T', 'H'), ('T', 'T', 'T'), ('H', 'T', 'T'), ('T', 'T', 'H'), ('H', 'H', 'T'), ('T', 'H', 'H'), ('H', 'H', 'H')} =8
LET OUS ASSUME THAT THE OUTCOMES WILL BE TAILS APPERA FIRST
THEN THE DESIRED OUTCOME BE A= {('T', 'H', 'T'), ('T', 'T', 'T'), ('T', 'T', 'H'), ('T', 'H', 'H')} =4
THEREFORE THE P(A)= 0.5
  
