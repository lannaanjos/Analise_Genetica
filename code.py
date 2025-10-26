from Bio import SeqIO
import pandas as pd

arquivo = "proteinas.fa"

headers = []
seqs = []
classes = []

# Extração do proteinas.fa

for registro in SeqIO.parse(arquivo, "fasta"):
    headers.append(registro.id)
    seqs.append(str(registro.seq))    
    classes.append(registro.description)
    
print(f'Total de seqs processadas: {len(seqs)}')

data_proteinas = pd.DataFrame({
    'header': headers,
    'sequencia': seqs,
    'classe_scop': classes
})

# stats
print(f'total de proteínas: {len(data_proteinas)}')
print(f'comprimento medio: {data_proteinas['sequencia'].str.len().mean():.2f} aminoacidos')
print(f'Menor comprimento: {data_proteinas['sequencia'].str.len().min()} aminoacidos')
print(f'comprimento max: {data_proteinas['sequencia'].str.len().max()} aminoacidos')

print(data_proteinas.head())
    

