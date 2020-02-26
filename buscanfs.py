#
# Consulta site Prefeitura de SP e gera arquivo da NFS-e em PDF.
# Precisa abrir o site de consulta e pegar os dados da variavel Cookies e 
# preenche-lo abaixo antes de executá-lo, e precisa do arquivo Results.csv
# na pasta esse arquivo tem que ter o numero da NFS-e e a chave de verificacao
# sepados por ponto e virgula(;).
#
import requests, re, time
from PIL import Image
from io import BytesIO

base = 'https://nfe.prefeitura.sp.gov.br/contribuinte/notaprintimg.aspx?inscricao=27681432&nf=%s&verificacao=%s&imprimir=1'

cookies = {'PMSP_NFE_CPFCNPJ':'30989726000160',
            'ASP.NET_SessionId':'totafggzbhba2qzxu2b5m5yw',
            '_gid':'GA1.4.376376823.1582717994',
            'PMSP_NFeID':'427263CAE8069A1DB54F7FE611A2A62AF022AAD2548FEE6A7F87FF8FCA3AC1D0469F71EF66A2AC11B0A03DB439BA91A9158BC7542AEE32C97009B21B1217276FAF9B28284D0D07A4DB9CFF1DACBB8B18B7DF6099AEB44F94D07EC1A157903CA45E20B851A02B90689BAA5FAB489B1A0AFC8A9DEE9DFC858A99FEBAFFFD96ED2C9199ECBB068067ECAB85F8DE26A664C269C6BFD2C92AA2B519EDB1877B4402AA0AF944608F4D45C1633EE9FD14C05A5EFB65D6CE'
}

arquivo = open('Results.csv', 'r')

for linha in arquivo:
    linha = linha.strip()
    nronfs = linha.split(';')[0]
    codnfs = linha.split(';')[1]
    url = 'https://nfe.prefeitura.sp.gov.br/contribuinte/notaprintimg.aspx?inscricao=27681432&nf=%s&verificacao=%s&imprimir=1' % (nronfs,codnfs)
    #url = 'https://nfe.prefeitura.sp.gov.br/contribuinte/notaprint.aspx?inscricao=27681432&nf=%s&verificacao=%s' % (nronfs,codnfs)
    headers = {'Referer': 'https://nfe.prefeitura.sp.gov.br/contribuinte/notaprint.aspx?inscricao=27681432&nf=%s&verificacao=%s' % (nronfs,codnfs),
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
                }
    #out_f = 'C:\\Users\\rsilva\\hello\\NFS\\NFS_000'+nronfs+'.gif'
    out_p = 'C:\\Users\\rsilva\\hello\\NFS\\NFS_'+nronfs+'.pdf'
    #f = open(out_f, 'wb+')
    #f.write(requests.get(url=url,headers=headers,cookies=cookies).content)
    #f.close
    im = Image.open(BytesIO(requests.get(url=url,headers=headers,cookies=cookies).content)).convert("RGB")
    im.save(out_p, 'PDF', resolution=19.0,quality=60,optimize=True)
    print(linha)
    print(url)
    time.sleep(5)

arquivo.close()
