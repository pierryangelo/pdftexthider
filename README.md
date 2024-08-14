# PDF Text Hider

## Descrição

O **PDF Text Hider** é uma ferramenta de desktop para ocultar textos e imagens de uma cor específica em arquivos PDF. Ideal para edição de documentos onde você deseja remover ou ocultar conteúdo sensível, mantendo o restante do documento intacto.

## Funcionalidades

- **Selecionar Arquivo PDF**: Escolha o arquivo PDF a ser processado.
- **Escolher Cor do Texto**: Selecione a cor do texto que deve ser ocultado.
- **Selecionar Arquivo de Saída**: Defina o local para salvar o arquivo PDF modificado.
- **Barra de Progresso**: Monitore o progresso do processamento.
- **Ocultar Texto e Imagens**: Substitua textos e imagens da cor especificada por um fundo branco.

## Requisitos

- Python 3.x
- Biblioteca `PyMuPDF` (fitz)
- Biblioteca `tkinter` (geralmente incluída com Python)

## Instalação

Siga estes passos para configurar o ambiente e instalar as dependências necessárias:

1. **Clone o Repositório**

   ```bash
   git clone https://github.com/seu-usuario/pdf-text-hider.git
   cd pdf-text-hider
   ```

2. **Criar e Ativar um Ambiente Virtual**

   - **No Windows**:

     ```bash
     python -m venv pymupdf-venv
     pymupdf-venv\Scripts\activate
     ```

   - **No macOS/Linux**:

     ```bash
     python3 -m venv pymupdf-venv
     source pymupdf-venv/bin/activate
     ```

3. **Criar o Arquivo `requirements.txt`**

   Crie um arquivo chamado `requirements.txt` com o seguinte conteúdo:

   ```text
   PyMuPDF==1.20.0
   ```

4. **Instalar Dependências**

   Instale as dependências usando pip:

   ```bash
   pip install -r requirements.txt
   ```

5. **Verificar Instalação do Tkinter**

   O `tkinter` geralmente vem incluído com Python, mas se não estiver instalado, você pode instalá-lo conforme seu sistema operacional:

   - **No Windows e macOS**: Normalmente já está incluído com Python.
   - **No Ubuntu/Debian**:

     ```bash
     sudo apt-get install python3-tk
     ```

   - **No Fedora**:

     ```bash
     sudo dnf install python3-tkinter
     ```

## Uso

1. **Execute o Script**

   Navegue até o diretório do projeto e execute o script:

   ```bash
   python pdf_hider_gui.py
   ```

2. **Interface Gráfica**

   - **Input PDF File**: Clique no botão "Browse" para selecionar o arquivo PDF que deseja processar.
   - **Output PDF File**: Clique no botão "Browse" para definir onde o arquivo PDF modificado será salvo.
   - **Text Color (RGB)**: Insira a cor do texto a ser ocultado no formato `(R, G, B)` ou clique em "Select Color" para escolher uma cor através de um seletor de cores.
   - **Process PDF**: Clique no botão "Process PDF" para iniciar o processamento.

3. **Resultado**

   Após o processamento, o PDF com o texto e imagens ocultados será salvo no local especificado.

## Contribuição

Se você deseja contribuir para o projeto, siga estes passos:

1. **Faça um Fork do Repositório**

   - No GitHub, vá para o repositório e clique em "Fork" no canto superior direito.

2. **Crie uma Branch para sua Feature ou Correção**

   ```bash
   git checkout -b nome-da-sua-branch
   ```

3. **Faça suas Alterações e Commit**

   ```bash
   git add .
   git commit -m "Descrição das suas alterações"
   ```

4. **Submeta um Pull Request**

   - Vá para o repositório original e clique em "New Pull Request".

## Licença

Este projeto é licenciado sob a [MIT License](LICENSE). Veja o arquivo `LICENSE` para detalhes.

## Contato

Para dúvidas, sugestões ou problemas, entre em contato com [seu-email@example.com](mailto:seu-email@example.com).

---

Agradecemos por usar o PDF Text Hider! Se encontrar algum problema ou tiver sugestões para melhorias, sinta-se à vontade para contribuir.

