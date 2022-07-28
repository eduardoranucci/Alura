from Cep import addressSearch
import requests

cep = '01001000'
cep_object = addressSearch(cep)
bairro, cidade, uf = cep_object.acess_via_cep()
print(bairro, cidade, uf)