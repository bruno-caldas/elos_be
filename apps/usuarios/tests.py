from django.test import TestCase
from django.contrib.auth.models import User
from usuarios.models import Estado, DadoPessoal

class EstadoTestCase(TestCase):
    def setUp(self):

        # dados moc
        moc_estado1 = {
            "sigla":"sp",
            "estado":"São Paulo",
            "atende": False}
        
        # instância de teste
        Estado.objects.create(**moc_estado1)

    def test_doadores_str_(self):

        # pega instância de teste criada no setUp do testCase
        estado = Estado.objects.get(sigla='sp')

        # unit test
        self.assertEqual(estado.__str__(), 'sp')

class DadoPessoalTestCase(TestCase):
    def setUp(self):

        # dados moc
        moc_estado2 = {
            "sigla":"sp",
            "estado":"São Paulo",
            "atende": False}

        # instancia de Estado
        uf = Estado.objects.create(**moc_estado2)

        # instancia de User
        user = User.objects.create(username='Fulano')
    
        moc_dado_pessoal_user1 = {
            "usuario":user,
            "telefone_fixo":"551132136418",
            "telefone_celular":"5511936187752",
            "endereco":"rua a",
            "numero":"34",
            "complemento":"sdf",
            "cidade":"sao paulo",
            "uf":uf,
            "cep":"04543-433"}
        DadoPessoal.objects.create(**moc_dado_pessoal_user1)

    def test_doadores_str_(self):

        # pega instância de teste criada no setUp do testCase
        dado_pessoal = DadoPessoal.objects.get(cep='04543-433')

        # unit test
        self.assertEqual(str(dado_pessoal.__str__()), 'Fulano')