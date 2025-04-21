# Sistema de Gerenciamento de Carros  

Este projeto é um sistema simples de gerenciamento de estoque de carros, permitindo a adição e listagem de veículos novos e usados.  

## Funcionalidades  

- **Adicionar carro**: Permite cadastrar carros novos ou usados com informações como marca, modelo, ano, preço e quilometragem (para usados).  
- **Listar carros**: Exibe todos os veículos cadastrados no estoque.  

## Classes  

### `Carro` (Classe Base)  
- **Atributos**:  
  - `marca` (str): Marca do carro (ex: Ford, Toyota).  
  - `modelo` (str): Modelo do carro (ex: Fiesta, Corolla).  
  - `ano` (int): Ano de fabricação.  
  - `preco` (float): Preço do veículo.  

- **Métodos**:  
  - `info_carro()`: Exibe informações básicas do carro.  

### `CarroUsado` (Herda de `Carro`)  
- **Atributos adicionais**:  
  - `km` (int): Quilometragem do carro usado.  

- **Métodos**:  
  - Sobrescreve `info_carro()` para incluir a quilometragem.  

## Como Usar  

1. **Adicionar um carro**:  
   - Escolha o tipo (`1` para novo, `2` para usado).  
   - Insira os dados solicitados (marca, modelo, ano, preço e km, se for usado).  

2. **Listar carros**:  
   - Exibe todos os veículos cadastrados no estoque.  

## Exemplo de Uso  

```python
add_carro()  # Cadastra um novo carro
lista_carro()  # Lista todos os carros no estoque
```

## Melhorias Futuras  

- Validação de entrada para evitar erros (ex: ano como número).  
- Edição e remoção de carros do estoque.  
- Persistência de dados (salvar em arquivo ou banco de dados).  

## Autor  

[Seu Nome]  

---  
**Nota**: Este código ainda contém alguns bugs (como atribuição incorreta de atributos no `__init__` da classe `Carro`). Recomenda-se revisar e corrigir antes de usar em produção.
