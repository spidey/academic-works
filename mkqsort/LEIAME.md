mkqsort - MultiKey QuickSort
============================

**mkqsort** lê todas as linhas do arquivo de entrada e exibe-as ordenadamente. Para isso, o programa utiliza o algoritmo **MultiKey QuickSort**, também conhecido como **Three-Way Radix QuickSort**. O programa tem como limitação o limite de apenas um arquivo de entrada por vez. Se você quiser ordenar vários arquivos, você vai precisar rodar **mkqsort** em cada um deles, ou concatená-los usando cat antes de processá-los.

COMPILAÇÃO
----------
**mkqsort** utiliza a ferramenta make para compilar automaticamente o programa. Os requerimentos do processo de compilação são:
- gcc
- biblioteca C padrão
- make

Vários SO's \*nix já vêm com esses pacotes incluídos desde a instalação. Se você não possui algum desses pacotes instalados, uma simples e rápida busca na árvore de pacotes no repositório ou no sistema de gerenciamento de pacotes do seu SO será o suficiente para te auxiliar no download, descompactação e instalação dos requerimentos.

Assim que todos os requerimentos sejam atendidos, simplesmente mude a pasta de trabalho para */caminho/para/o/fonte/do/mkqsort/src* e execute o *make*:

    $ cd /caminho/para/o/fonte/do/mkqsort/src
    $ make

Se você quiser, você também pode executar `make clean` para deletar os binários temporários gerados na compilação. Apenas certifique-se de copiar o programa, em *../bin/mkqsort*, para outra pasta, como seu diretório *home (~)*, ou ele também será deletado.

INSTALAÇÃO
----------

**mkqsort** não precisa ser instalado, é um programa stand-alone, isto é, apenas o executável é necessário para o seu perfeito funcionamento. Se for sua vontade, você pode mover o programa para um das pastas configuradas na sua variável de ambiente `PATH`, como, por exemplo, */usr/bin* ou */usr/local/bin*, de forma que um simples `mkqsort` chame o aplicativo, ao invés de `/caminho/para/o/binario/mkqsort`.

COMO USAR
---------

**mkqsort** é auto-explicativo (em inglês). Se os parâmetros corretos não forem especificados, o programa identifica o problema automaticamente e exibe uma mensagem de erro, juntamente com a sintaxe correta de uso:

`$ mkqsort [-s] <arquivo_de_entrada>`

A opção `-s` se refere ao modo silencioso. Neste modo, o programa exibe apenas as linhas do arquivo de entrada ordenadamente na saída, omitindo as informações sobre o tempo gasto e o custo computacional da ordenação.

SUPORTE
-------
Se você tiver sugestões, correções, críticas, dúvidas ou precisar de ajuda para usar o **mkqsort**, mande-me e-mail em __spideybr@gmail.com__. Estarei esperando seu feedback para sempre melhorar meus programas. Por favor, não deixe de adicionar **[mkqsort]** no início do assunto do e-mail, para facilitar a sua identificação.
