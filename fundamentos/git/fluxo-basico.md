# Fluxo básico do Git

## Perguntas de fixação

### 1. O que é Git?

Minha resposta: aplicação desktop para o versionamento de arquivos, resgatando estados anteriores

Versão revisada: Git é um sistema de controle de versão. Ele registra o histórico de mudanças de um projeto, permite comparar estados anteriores, voltar a versões antigas e organizar o desenvolvimento de código.

Observações: A ideia de versionamento e resgate de estados anteriores está correta. O ajuste principal é evitar chamar Git de “aplicação desktop”; ele é uma ferramenta/sistema de versionamento, geralmente usado pelo terminal.

### 2. O que é GitHub?

Minha resposta: aplicação web para o compartilhamento de arquivos em repositórios, públicos ou particulares

Versão revisada: GitHub é uma plataforma web para hospedar, compartilhar e sincronizar repositórios Git, podendo manter projetos públicos ou privados.

Observações: A resposta está correta no geral. O ajuste é deixar claro que GitHub hospeda repositórios Git, não apenas arquivos soltos.

### 3. Qual é a diferença entre Git e GitHub?

Minha resposta: git é o aplicativo local que versiona o documento, github é a plataforma que permite o compartilhamento

Versão revisada: Git é a ferramenta local que controla versões do projeto. GitHub é a plataforma online onde eu posso publicar, compartilhar e sincronizar repositórios Git.

Observações: Resposta correta. Só trocaria “documento” por “projeto” ou “repositório”, porque Git normalmente versiona um conjunto de arquivos.

### 4. O que aconteceu quando eu rodei `git init`?

Minha resposta: sinaliza para o aplicativo que aquele diretório deve ser inicializado, isto é, registrado seus estados e salvo localmente

Versão revisada: O comando `git init` transformou o diretório atual em um repositório Git local, criando a pasta oculta `.git/`, onde o Git guarda as informações internas do versionamento.

Observações: A ideia estava correta, mas faltou mencionar a pasta `.git/`, que é a parte central do que acontece no `git init`.

### 5. O que significa um arquivo estar como `untracked`?

Minha resposta: demonstra que o arquivo não está tendo seu histórico de alterações rastreado pela aplicação

Versão revisada: Um arquivo `untracked` é um arquivo que existe na pasta do projeto, mas ainda não foi adicionado ao controle de versão do Git.

Observações: Correto. O Git vê o arquivo, mas ainda não o incluiu no histórico do repositório.

### 6. Para que serve `git add .`?

Minha resposta: sinaliza para o aplicativo adicionar todos os documentos daquele diretório no pacote atual de atualização de estado

Versão revisada: O comando `git add .` adiciona todas as mudanças do diretório atual à staging area, preparando esses arquivos para o próximo commit.

Observações: A ideia de “pacote atual de atualização de estado” está próxima. O termo técnico mais preciso é staging area.

### 7. O que é a staging area?

Minha resposta: estado de preparação para um próximo commit, organizando e diferenciando arquivos

Versão revisada: A staging area é a área de preparação do Git. Ela contém as mudanças que foram selecionadas para entrar no próximo commit.

Observações: Resposta correta. A staging area permite escolher o que será incluído no próximo registro do histórico.

### 8. O que é um commit?

Minha resposta: uma "fotografia" do estado atual daquele arquivo, acompanhado de um comentário breve descritivo

Versão revisada: Um commit é um registro no histórico do repositório. Ele salva um estado do projeto em determinado momento, acompanhado de uma mensagem descritiva.

Observações: A metáfora da fotografia está boa. Só ajustei para “estado do projeto”, porque um commit pode incluir vários arquivos, não apenas um arquivo.

### 9. O commit foi criado no meu notebook ou no GitHub?

Minha resposta: apenas localmente

Versão revisada: O commit foi criado localmente, no notebook. Ele só aparece no GitHub depois de um `git push`.

Observações: Resposta correta.

### 10. Para que serve `git remote add origin`?

Minha resposta: sinaliza para o aplicativo, remotamente, adicionar o diretório apelidado de "origin" no staging area

Versão revisada: O comando `git remote add origin` adiciona um repositório remoto ao projeto local e dá a ele o apelido `origin`.

Observações: Aqui havia uma confusão. Esse comando não adiciona nada à staging area. Ele apenas registra o endereço remoto do GitHub dentro da configuração local do repositório.

### 11. O que significa `origin`?

Minha resposta: apelido para o diretório de origem do rastreamento

Versão revisada: `origin` é o nome convencional dado ao repositório remoto principal de um projeto.

Observações: Não é exatamente o “diretório de origem do rastreamento”. É um apelido para o endereço remoto, geralmente no GitHub.

### 12. O que significa `fetch`?

Minha resposta: resgatar os arquivos daquele repositório

Versão revisada: `fetch` significa buscar informações e commits do repositório remoto, sem aplicar automaticamente essas mudanças ao meu trabalho atual.

Observações: A ideia de “resgatar” está próxima, mas `fetch` não é simplesmente baixar arquivos para substituir os seus. Ele atualiza as referências remotas para que o Git saiba o que existe no servidor.

### 13. O que significa `push`?

Minha resposta: fazer o upload das modificações locais para o repositório

Versão revisada: `push` significa enviar commits locais para o repositório remoto.

Observações: Resposta quase correta. O ajuste é que o Git envia commits, não apenas “modificações” ou arquivos soltos.

### 14. Para que serve `git push -u origin main`?

Minha resposta: "git, envie para o repositório remoto as mudanças realizadas nesse diretório"

Versão revisada: O comando `git push -u origin main` envia a branch local `main` para o repositório remoto chamado `origin` e configura essa relação como padrão para pushes futuros.

Observações: Sua explicação estava correta no sentido geral. Faltava apenas mencionar que `main` é a branch enviada e que `-u` cria o vínculo padrão.

### 15. Por que depois do primeiro `push -u` geralmente basta usar `git push`?

Minha resposta: porque a ligação com o repositório remoto já está estabelecida

Versão revisada: Porque o Git já sabe que a branch local `main` deve enviar suas mudanças para a branch `main` do remoto `origin`.

Observações: Resposta correta.

### 16. Por que as pastas vazias não apareceram no `git status`?

Minha resposta: o git reconhece apenas documentos, não diretórios

Versão revisada: Porque o Git rastreia arquivos, não pastas vazias. Uma pasta só aparece no repositório quando contém pelo menos um arquivo rastreado.

Observações: Resposta correta.

### 17. Para que usamos arquivos `.gitkeep`?

Minha resposta: para forçar o git a entender um diretório vazio como importante

Versão revisada: Usamos arquivos `.gitkeep` para permitir que uma pasta vazia seja incluída no repositório Git.

Observações: Resposta correta. O `.gitkeep` não é um recurso oficial especial do Git; é uma convenção usada para manter diretórios vazios no repositório.

### 18. O que significa `working tree clean`?

Minha resposta: significa que a árvore local de arquivos está de acordo com o repositório em sua última atualização

Versão revisada: `working tree clean` significa que não há mudanças pendentes no diretório de trabalho. Tudo que existe localmente já foi registrado em commit ou não há alterações novas desde o último commit.

Observações: Sua resposta estava quase correta. Só cuidado: isso não significa necessariamente que o GitHub está atualizado. Para saber isso, também é preciso observar mensagens como `Your branch is up to date with 'origin/main'`.

### 19. Qual é o fluxo básico de trabalho com Git daqui para frente?

Minha resposta: git add, git commit, git push

Versão revisada: O fluxo básico é verificar o estado com `git status`, preparar mudanças com `git add`, registrar com `git commit` e enviar para o GitHub com `git push`.

Observações: Sua resposta estava correta, mas faltava incluir `git status`, que deve ser usado com frequência para entender o estado do repositório.

### 20. Qual é a diferença entre `git commit` e `git push`?

Minha resposta: o commit registra um estado do arquivo, o git push envia esse arquivo para o repositório

Versão revisada: `git commit` registra mudanças no histórico local do repositório. `git push` envia commits locais para o repositório remoto, como o GitHub.

Observações: A ideia estava correta. O ajuste é que `push` envia commits, não simplesmente arquivos.

## Resumo em uma frase

Minha resposta: Git é uma aplicação de versionamento que resgata o histórico de edições e permite derivar branches de mudanças prototipais que podem sempre serem recuperadas, enquanto o GitHub é um domínio para o upload e compartilhamento de repositórios

Versão revisada: Git é um sistema de controle de versão que registra o histórico de mudanças de um projeto localmente, enquanto GitHub é uma plataforma online para hospedar, compartilhar e sincronizar repositórios Git.

Observações: Seu resumo estava bom, mas ficou um pouco longo e incluiu branches antes de consolidar o básico. Para esta anotação inicial, a versão mais limpa é melhor.
