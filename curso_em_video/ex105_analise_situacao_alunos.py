# Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e
# vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*notas, sit=False):
    """
    - Função para analisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando ou não se deve mostrar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    aluno = dict()
    aluno['total'] = len(notas)
    aluno['maior'] = max(notas)
    aluno['menor'] = min(notas)
    aluno['media'] = sum(notas)/len(notas)

    if sit:
        if aluno['media'] < 5.0:
            aluno['situacao'] = 'RUIM'
        elif aluno['media'] >= 7:
            aluno['situacao'] = 'BOA'
        else:
            aluno['situacao'] = 'RAZOAVEL'
    return aluno


# Programa Principal
resp = notas(5.5, 2.5, 10, 4, 10, sit= True)
print(resp)
