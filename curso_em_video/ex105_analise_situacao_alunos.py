from typing import Dict, Any, Union


def notas(*notas, sit=False):
    """
    - Função para analisar notas e situações de vários alunos
    :param notas: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando ou não se deve mostrar a situação
    :return: dicionário com várias informações sobre a situação da turma
    """
    aluno: Dict[str, Union[Union[int, float, str], Any]] = {}
    aluno['total'] = len(notas)
    aluno['maior'] = max(notas)
    aluno['menor'] = min(notas)
    aluno['media'] = sum(notas)/len(notas)

    if sit:
        if aluno['media'] < 5.0:
            aluno['situacao'] = 'RUIM'
        elif aluno['media'] > 7:
            aluno['situacao'] = 'BOA'
        else:
            aluno['situacao'] = 'RAZOAVEL'
    return aluno


resp = notas(9, 10, 3, 4, 10, sit=True)
print(resp)
