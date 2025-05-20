from main import soma

def test_soma():
    """
    Testa a função soma.
    
    Verifica se a função soma retorna o resultado correto para diferentes entradas.
    """
    assert soma(1, 2) == 3
    assert soma(-1, 1) == 0
    assert soma(0, 0) == 0
    assert soma(-1, -1) == -2
    assert soma(100, 200) == 300
