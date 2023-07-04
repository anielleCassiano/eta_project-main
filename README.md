# ETA

## Setup

```bash
pip install -r requirements.txt
```

## Unittest

```bash
python -m unittest -v
```

## Pytest

```bash
pytest .
```

## Test Coverage

- `coverage` and `pytest-cov` packages are required
- Add `pragma: no cover` to exclude code from coverage report

### With `pytest`

Terminal report:

 ```bash
pytest --cov-report term-missing --cov .
 ```

HTML report:

```bash
pytest --cov-report html --cov .
```

### With `unittest`

To generate report:

```bash
python -m coverage run -m unittest
```

To view report in terminal:

```bash
python -m coverage report
```

To view report in HTML:

```bash
python -m coverage html
```

# ETA – Testes Unitários - Projeto
## Data de Entrega
* Até 23:59 de Sábado, 14 de julho de 2023, via link do seu Git
### Preparação
Clone o código do repositório: [https://github.com/fabriciotorquato/eta_project](https://github.com/fabriciotorquato/eta_project)

## Problema Proposto
1. Criar os testes unitários necessários para validar os métodos da aplicação
2. Encontrar bugs através dos testes unitários e corrigi-los.
3. Refatorar o código seguindo as boas práticas de clean code.

## Task
1. Use o PyTest e crie testes unitários para as classes desenvolvidas. Lembre-se que cada
classe abaixo deve ter sua própria classe de testes separada com todos os testes
necessários para a validação:
   1. a. ice_cream_stand.py
   1. [x] Feito
   1. b. restaurant.py
   1. [x] Feito

2. Para cada classe de testes:
   1. a. Crie quantos testes unitários forem necessários para validar os métodos. Utilize
   técnicas baseada em estrutura, caminho ou requisitos, vistos na disciplina (a
   escolha é sua). Mas lembre- se que cada método deve ter pelo menos um teste
   unitário.
   1. [x] Feito
   2. b. Cada teste deve ter uma mensagem apropriada indicando a falha (caso
   aconteça).
   1. [x] Feito
   3. c. Use clean code para os seus testes unitários.
   1. [x] Feito

3. Use seus testes para identificar bugs presentes no código. Existem pelo menos 5 bugs
inseridos. Você deve encontrar e corrigir pelo menos 3 deles. Registre através de
comentário no método da classe o bug identificado e a correção.
   1. [x] Feito

4. Use técnicas de refatoração para melhorar pelo menos 4 pontos do código. Registre
através de comentário a refatoração realizada.
   1. [x] Feito

5. Cada pessoa deve enviar o seu próprio projeto.
   1. [x] Glecinilson
   2. [x] Anielle

## Notas
### O seguinte esquema vai ser usado para notas
|                        | Cobertura                                            | Detecção e correção de erros                      | Refatoração                                    |
|------------------------|------------------------------------------------------|---------------------------------------------------|------------------------------------------------|
| Tarefa                 | Todos os métodos estão cobertos por testes unitários | Pelo menos 3 bugs foram encontrados e corrigidos. | Pelo menos 4 pontos do código foram melhorados |
| Distribuição das notas | 50%                                                  | 25%                                               | 25%                                            |