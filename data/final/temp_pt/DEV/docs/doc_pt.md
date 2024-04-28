# Manual do TCA-Media Downloader 3

O TCA-Media Downloader 3 é um programa escrito em python-3 totalmente acessível com leitores de ecrã.

É baseado na biblioteca YT-DLP, que nos permite baixar conteúdo multimídia de centenas de sites. [Aqui você pode descobrir os sites oficialmente suportados](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md):



Além disso, o TCA-Media Downloader 3 utiliza FFMPEG, biblioteca que, combinada com YT-DLP, nos permite converter os nossos downloads para diversos formatos.

O TCA-Media Downloader 3 está focado principalmente no YouTube, mas como já foi dito, é compatível com muitos mais sites, adicionando compatibilidade com alguns não oficiais. Este último dependerá se YT-DLP conseguir obter as informações necessárias para fazer o download, ou seja, se detectar multimídia na página que disponibilizamos.

Este manual tem como objetivo descrever a interface do TCA-Media Downloader 3, na sua primeira versão. Os novos recursos adicionados ao longo das diferentes atualizações serão refletidos na secção [Changelog] (#changelog). Novas opções e sua descrição serão apontadas nesta secção, portanto, o manual principal detalhará apenas a primeira versão.

Da mesma forma, à medida que recebermos uma atualização, tentaremos fornecer uma descrição detalhada das novas alterações incluídas em tal atualização.

O TCA-Media Downloader 3 vem com um atualizador incorporado, que nos fornecerá atualizações do programa. Essas atualizações serão divididas em 3 secções, Biblioteca, Recursos e Completa.

1. Atualizações no ramo da biblioteca: Este ramo receberá pequenas atualizações da biblioteca e correções de bugs.
2. Atualizações no ramo de recursos: Este ramo receberá atualizações de novos recursos adicionados ao programa. Aprimoramentos e melhorias de recursos implementados anteriormente estarão no ramo de bibliotecas; este ramo refletirá apenas novos recursos.
3. Atualizações na versão completa: Esta versão receberá atualizações completas do programa. Este ramo atualizará todos os componentes do programa e será usado para atualizá-lo com novos recursos, correções de bugs importantes ou bibliotecas críticas.

Ao verificar se há atualizações, na descrição será especificado o ramo ao qual pertence a atualização e sempre poderemos saber pela nomenclatura da versão atualizada.

O TCA-Media Downloader na sua primeira versão será 3.0.0.0, o primeiro 0 pertence ao ramo completo, o segundo indica o ramo de recursos e o último pertence ao ramo da biblioteca.

Este manual descreverá a parte principal do programa, permitindo ao utilizador explorá-lo e descobrir todo o potencial com o qual tentamos fornecer o TCA-Media Downloader 3 para nossa própria diversão.

De antemão, diremos que nesta versão, TCA-Media Downloader incorpora novos formatos de download, mais opções de download, novas possibilidades de personalização de download e, algo que poucos programas possuem, para não dizer nenhum.

Poderemos pesquisar vídeos, como nas versões anteriores, mas além disso, agora poderemos pesquisar playlists e canais de forma rápida e simples, podendo interagir com tais resultados.

Da mesma forma, nesta versão é possível realizar vários downloads ao mesmo tempo, podendo reproduzir simultaneamente, enquanto continuamos usando o programa.

Esperamos adicionar novos recursos já em desenvolvimento e alguns em projeto.

Nesta primeira versão tentamos dar-lhe o que o TCA-Media Downloader 2 tinha, mas vitaminado e com novas funcionalidades para lhe dar a versão final mais estável possível.

Assim que for provado que a versão final é estável o suficiente, começaremos a adicionar novos recursos que acreditamos que todos irão gostar.

##Descrição da interface

Nesta primeira versão, podemos dizer que o programa está dividido em 3 secções:

1. Separadores.
2. Reprodutor.
3. Controlos.

###Separadores

Nesta primeira versão temos 3 separadores, URL (Alt+1), Pesquisa (Alt+2) e downloads (Alt+3).

Poderemos alternar entre eles com as teclas Alt+1, alt+2 e alt+3, bem como com Ctrl + Tab para ir para o próximo separador ou Ctrl + Shift + Tab para ir para o separador anterior.

Poderemos saber em qual separador estamos a qualquer momento pressionando a combinação Ctrl+Espaço.
####URL (Alt+1)

Este separador, quando focado, deixar-nos-á no campo para inserir uma URL.

Só funcionará se detectar que o que inserimos é um endereço válido, caso contrário não fará nada.
Como mencionei, este programa é focado principalmente no YouTube, portanto, se colocarmos uma URL do youtube, ele detectará que tipo de URL é.

#####vídeo, lista de reprodução ou canal.

Caso não seja uma URL do YouTube e seja de outro site compatível, ou se quisermos tentar baixar conteúdo multimídia de lá, isso nos dará outras possibilidades de download.

Bem, uma vez que colocamos uma URL, se pressionarmos enter, um menu de contexto com opções relacionadas a tal URL será mostrado. Estas opções mudam dependendo do tipo de URL inserido.

Na URL de um vídeo do YouTuve teremos as seguintes opções:

* Download regular: Esta opção permitirá baixar o vídeo com as opções que escolhemos (descritas mais tarde), adicionará o download com uma propriedade de vídeo e com formato (explicado mais tarde), poderemos ver o download no separador de downloads (Alt+3).
* Download personalizado: Esta opção abrirá uma caixa de diálogo que nos dará a possibilidade de escolher um formato e ver as suas propriedades. Isto é para utilizadors avançados que estão familiarizados com codecs de áudio e vídeo.
* Informações do vídeo: abrirá uma caixa de diálogo na qual poderemos visualizar informações e opções de um vídeo, como copiar diversas informações para a área de transferência, baixar e verificar informações.
* Reprodução: permitirá reproduzir o vídeo no reprodutor incorporado no TCA-Media Downloader 3 (explicado mais adiante).

Numa URL de playlist do YouTube teremos as seguintes opções:

* Baixar PlayList inteira:  adicionará a playlist inteira com todos os seus vídeos para download, com opções padrão.
* Escolha os vídeos para baixar: abrirá uma caixa de diálogo na qual poderemos verificar os vídeos que queremos baixar, dispensando aqueles que não estiverem marcados.

nesta caixa de diálogo, também temos as seguintes teclas, na lista de vídeos:

* Espaço: marca ou desmarca o item selecionado.
* Ctrl +P: o vídeo será reproduzido imediatamente.
* Ctrl +D: o vídeo será baixado imediatamente com as opções que definimos.
* Ctrl +I: dará informações sobre a posição em que estamos na playlist.
* Ctrl +F: abrirá uma caixa de diálogo para escrevermos uma posição e passarmos para ela rapidamente na lista. Isso é útil para listas que possuem muitos vídeos.
*Informações da PlayList: abrirá uma caixa de diálogo na qual poderemos visualizar informações sobre a playlist, onde teremos uma área mostrando os vídeos que essa playlist contém, bem como algumas opções.
nesta caixa de diálogo, na secção de vídeos da playlist, poderemos pressionar enter em cada vídeo e obteremos um menu de contexto com as opções que correspondem aos vídeos. Da mesma forma, temos várias teclas utilizáveis para cada item dessa lista:

* Ctrl + P: reproduzirá o vídeo imediatamente.
* Ctrl +D: fará o download do vídeo imediatamente com as opções que definimos.
* Ctrl +I: dará informações sobre a posição em que estamos na playlist.
* Ctrl +F: abrirá uma caixa de diálogo para escrevermos uma posição e passarmos para ela rapidamente na lista. É útil para listas que possuem muitos vídeos.


Na URL de um canal do YouTube teremos as seguintes opções:

* Baixar canal inteiro: adicionará todos os vídeos contidos no canal para download com as opções que escolhemos.
* escolher vídeos para baixar: abrirá uma caixa de diálogo que nos permitirá selecionar os vídeos que queremos baixar, marcando-os, descartando aqueles que não queremos. Quando esta caixa de diálogo for aberta, poderá informar que a playlist não contém vídeos. Isso pode ocorrer porque o canal possui os vídeos protegidos por direitos autorais, os vídeos estão ocultos, bloqueados pelo YouTube, protegidos por senha ou estão em playlists diferentes e não na parte principal do canal.

Nesta caixa de diálogo também temos a possibilidade de utilizar várias teclas na lista de vídeos:

* Espaço: marca ou desmarca o item selecionado.
* Ctrl +P: O vídeo será reproduzido imediatamente.
* Ctrl +D: fará o download imediato do vídeo com as opções atribuídas.
* Ctrl +I: dará informações sobre a nossa posição atual na lista de reprodução do canal principal.
* Ctrl +F: abrirá uma caixa de diálogo para escrevermos uma posição e avançarmos rapidamente para ela na lista de reprodução. É útil para listas que possuem muitos vídeos.
* Informações do canal: mostrará uma caixa de diálogo com informações sobre o canal e uma área com 2 separadores, vídeos e Playlists, onde podemos ver quais vídeos e quais playlists o canal contém, respectivamente.

Em qualquer uma dessas duas áreas podemos pressionar a tecla Enter em um item e as opções correspondentes de vídeos ou playlists serão mostradas. Na área de vídeos também poderemos usar Ctrl+p para reproduzir, Ctrl+d para baixar, Ctrl+i para saber onde estamos e Ctrl+f para ir rapidamente até o item que desejamos.

Nesta caixa de diálogo também teremos diversos botões para copiar para a área de transferência ou baixar o canal.

Se inserirmos uma URL que não pertence ao YouTube, ao pressionar enter o programa tentará encontrar conteúdo multimídia.

Se encontrar conteúdo multimídia para baixar na URL inserida, dará duas opções: Tentar baixar com formato, que tentará baixar o ficheiro com as opções que definimos, e tentar baixar original, que tentará baixar o ficheiro multimídia em seu formato original.

Se não encontrar nenhum conteúdo multimídia, avisará por meio de uma mensagem.

O campo URL pode ser focado rapidamente se estivermos no separador URL com Alt + I.
Da mesma forma, este campo de URL também pode ser limpo com Ctrl +B se estiver em foco.

As seguintes opções neste separador serão aquelas estabelecidas para futuros downloads que realizarmos, seja por URl ou por busca (explicado mais adiante).

Se continuarmos tabulando aqui, chegaremos a uma caixa de combinação chamada "selecionar formato": (Alt + F).

Nesta caixa de combinação poderemos escolher diferentes formatos suportados pelo programa, tanto de vídeo como de áudio. Além disso, a última opção da caixa é avançada, o que permitirá novas opções de download para o que escolhermos baixar.

Se tabularmos novamente, teremos a caixa de combinação solicitando que escolhamos a qualidade do áudio: (Alt + q) ou escolha uma opção avançada de formato personalizado: (Alt +C). Isto ocorrerá se tivermos selecionado a opção avançada na caixa de combinação de formatos.

Na qualidade de áudio, podemos selecionar o vitrate desejado para o áudio baixado. Isso sempre dependerá se o que tentamos baixar é permitido, caso contrário, se colocarmos uma taxa de bits alta, ele sempre tentará baixar a melhor qualidade de áudio.

Se na caixa de combinação de formatos selecionamos a opção avançada, esta caixa oferecerá 412 opções, que nem sempre funcionam em todos os áudios ou vídeos que queremos baixar. É uma questão de teste e, acima de tudo, para utilizadors avançados. É recomendado que os utilizadors comuns não toquem nesta opção.

Cada opção possui uma descrição do que tentamos baixar.

nesta caixa de combinação, temos 2 teclas de atalho:

* Ctrl + I: Falará nossa posição atual na caixa de combinação.
* Ctrl +F: abrirá uma caixa de diálogo para passarmos rapidamente para uma opção em toda a lista.
Se continuarmos a tabular, chegaremos a uma caixa de combinação chamada Escolha a composição do nome de saída: (Alt + N). Aqui poderemos escolher o nome dos ficheiros resultantes, tendo também a possibilidade de criar uma subpasta, numerar os vídeos ou áudios baixados, ou não, por enquanto.

Pressionando tab mais uma vez, chegaremos a uma caixa de seleção que nos permite escolher a pasta na qual queremos guardar os downloads (Alt + U).

Esta caixa vem desabilitada por padrão, e guardará nossos downloads na subpasta TCAMediaDownloader na pasta "music" por padrão, criando-a caso não exista.
Podemos marcar a caixa e uma janela se abrirá, permitindo-nos escolher o local personalizado para os nossos downloads. Se desmarcarmos a caixa quando ela estiver marcada, o programa será baixado na pasta padrão novamente.

Isto é tudo para a área de URL.

####Pesquisar (Alt+2)

Este separador possui apenas dois componentes:

Digite uma pesquisa (Alt +S): Aqui poderemos colocar qualquer tipo de texto e pressionar enter para obter opções.

Se pressionarmos enter com o campo vazio, aparecerá apenas uma opção: selecionar o número de resultados a mostrar, que é um submenu onde podemos escolher o número de resultados que queremos obter, podendo escolher entre 10 e 500 resultados. Esta configuração permanece guardada até que a alteremos novamente.

Se inserirmos algum texto e pressionarmos enter, teremos opções de pesquisa de vídeos, playlists ou canais, bem como a opção anterior de alterar o número de resultados desejados. Isso será exibido como um menu de contexto.

Se selecionarmos qualquer uma das 3 primeiras opções, será realizada uma pesquisa com base no termo que inserimos.

Esta caixa de pesquisa pode ser limpa rapidamente com Ctrl +B, o que limpará tanto o campo de pesquisa quanto os resultados. Também podemos limpar o campo de pesquisa com backspace e pressionar enter. Em seguida, será mostrado um menu de contexto com a opção de limpar a pesquisa, que limpará o campo e a lista de resultados, e a opção mencionada anteriormente para alterar o número de resultados.

Os menus são dinâmicos, dependendo da ação que realizamos.

Se pressionarmos tab, chegaremos a uma lista chamada resultados da pesquisa (Alt + R): Nesta lista, podemos pressionar enter, e obteremos as mesmas opções já descritas no separador URL para cada pesquisa.

Existem mais algumas opções, se for uma pesquisa de vídeo.

Podemos usar Ctrl + P para reproduzir rapidamente um vídeo, Ctrl + D para baixá-lo e, além disso, ao pressionarmos enter naquele vídeo, teremos a seguinte nova opção no menu:

Download de pesquisa múltipla: Esta opção abrirá uma caixa de diálogo na qual serão mostrados todos os resultados da pesquisa, permitindo-nos selecionar aqueles que desejamos baixar.

Esta caixa de diálogo é útil caso queiramos baixar vários vídeos de uma vez, em vez de baixar um por um.

Nesta caixa de diálogo de lista de vídeos podemos usar espaço para marcar ou desmarcar, Ctrl +R para reproduzir e Ctrl + D para baixar o item em foco. Além disso, se apertarmos enter, teremos opções de menu para vídeos, já explicadas acima.

Se pressionarmos tab, chegaremos a uma caixa de edição onde teremos que digitar o nome do download múltiplo. além de identificar o download, este nome criará uma subpasta com o que colocamos em nossa pasta de download, e tudo o que escolhermos nesta caixa de diálogo será baixado para essa subpasta.

Isto é tudo para a guia de pesquisa.

####Downloads (Alt+3)

Esse separador também é simples, com dois controlos.

Há uma lista contendo os nossos downloads, a que podemos aceder com Alt+ L, e se pressionarmos tab, há um campo somente leitura chamado status (Alt + E). Há também uma barra de progresso que indicará o status do download que escolhemos na lista.

Na lista de downloads será falado o tipo de download. vídeo, playlist, canal ou outro, bem como seu formato. O formato dependerá do que selecionamos no separador URL. Também é o nome do download.

Se pressionarmos enter durante um download, um menu com opções será mostrado. Este menu é dinâmico dependendo dos downloads e do seu status.
Se o download estiver em andamento, este menu permitirá o seguinte:

* Reproduzir (apenas downloads de vídeo)
* Abrir o link de download na web
* Copiar o link de download para a área de transferência

Se o download for concluído, as opções oferecidas serão:

* Abrir a pasta de download
* Além disso, caso haja downloads concluídos, um menu denominado ações gerais permitirá:
* Limpar downloads concluídos

* Se ocorrer um erro e tivermos o download relacionado selecionado, dará a opção de visualizar o erro, consistindo numa caixa de diálogo com o erro relacionado e a possibilidade de copiar tal mensagem de erro para a área de transferência.

No submenu de ações gerais, também teremos a opção de limpar downloads com erro, se houver.

Se pressionarmos tab, chegaremos ao campo somente leitura que mostra algumas informações sobre o status do download e o que está sendo feito.

O separador de downloads termina aqui.

###Reprodutor

Nesta secção, se pressionarmos tab e nada estiver a ser reproduzido, o programa irá para a secção seguinte (Controles), pois esta opção contém apenas os botões de reprodução quando está ativa.

Os botões são:

* Retroceder (F1)
* Reproduzir (F2) ou Pausar (F2) Dependendo do seu status.
* Avanço rápido (F3)
* Parar (F4)

Tanto no botão de retrocesso (F1) quanto no botão de avanço rápido (F3) podemos pressionar a tecla de aplicação, Shift F10 ou Ctrl + M, para obter um menu, que nos permitirá selecionar o tempo de retrocesso ou avanço rápido para a faixa que estamos a reproduzir.

A opção que escolhermos nesse menu ficará selecionada até que seja alterada novamente.

O reprodutor pode ser controlado com os atalhos indicados acima, de qualquer lugar do programa, exceto na caixa de diálogo de configurações ou atualizações.

Nestas duas caixas de diálogo, onde o player não pode ser controlado, ao serem abertas, a reprodução será pausada até que sejam fechadas.

Leve em consideração que se alguma das ações nestas caixas de diálogo precisar reiniciar o programa, a reprodução será interrompida e teremos que retomá-la se desejarmos.

###Controlos

Nesta secção, encontraremos:

####Volume: (F5/F6):
Com estas teclas, aumentaremos ou diminuiremos o volume. Se pressionarmos Alt + V e o controle estiver em foco, com as setas para esquerda, direita, para baixo ou para cima, diminuiremos ou aumentaremos o volume respectivamente.
####Velocidade: (F7/F8):
também podemos pressionar Alt + V para focar este controlo. Esta combinação alternará entre volume e velocidade, dependendo de qual dos controlos está em foco.
* Com f6 ou f7 ou as teclas de seta, diminuiremos ou aumentaremos a velocidade de reprodução. Temos que ter cuidado, pois se aumentarmos a velocidade, o buffer de reprodução pode ficar sem dados e dar uma mensagem de erro. Isso não acontece com todos os vídeos e também depende muito da conexão de internet que temos.
####Saída de áudio:
Podemos focar rapidamente esta caixa de combinação com Alt + S, mas tal controle só estará disponível se a reprodução estiver ativa, seja em reprodução ou pausada.
Poderemos escolher em qual dispositivo queremos que o som seja reproduzido.
Deve-se esclarecer que quando a reprodução é interrompida, o dispositivo volta aos padrões, portanto, se quisermos outro dispositivo para a próxima reprodução, teremos que selecioná-lo novamente. Atualmente, esta opção não pode ser guardada por motivos técnicos.
Caso uma solução seja encontrada no futuro, o utilizador poderá escolher por meio de qual dispositivo deseja que o som seja reproduzido.
####ecrã de vídeo (F11):
Se a reprodução estiver ativa, seja em reprodução ou pausada, também podemos ter acesso rápido ao controlo com Alt + P. O controlo é uma caixa de seleção que, quando marcada com espaço, nos mostrará uma ecrã cheia com o vídeo, podendo assistir seu conteúdo. Por padrão o vídeo vem desabilitado, reproduzindo apenas áudio, mas a qualquer momento e a partir de qualquer caixa de diálogo, podemos habilitar a ecrã de vídeo com F11, exceto nas caixas de diálogo de configurações e atualizações. a ecrã de vídeo também suporta F1 para retroceder, F2 para reproduzir/pausar, F3 para avançar, F4 para parar e fechar a ecrã, F5 e F6 para aumentar ou diminuir o volume, F7 e F8 para aumentar a velocidade de reprodução e teclas explicadas posteriormente. Deve-se dizer que esta ecrã pode ser fechada continuando a reprodução com escape, ou fecha automaticamente se perder o foco. Este último significa que se estivermos na ecrã do vídeo e pressionarmos Alt + Tab, a janela fechará ao perder o foco.

###Botão de menu (Alt + M):
este menu conterá diferentes ferramentas, opções e ações gerais. nesta primeira versão, contém o seguinte:

####Verificar se há atualizações:
Irá procurar por atualizações; se não houver atualizações, informará, caso contrário, será exibida uma caixa de diálogo nos dando a possibilidade de atualizar. Deve-se dizer que esta opção só pode ser invocada se não tivermos downloads ativos.
####Opções:
Abrirá uma caixa de diálogo com as configurações do programa (explicadas na secção a seguir)
####Manual:
Abre esta documentação no nosso navegador padrão.
####Visite o nosso site:
Abre a página principal do blog.
####Sobre...:
Mostra informações sobre a versão do programa, versão das bibliotecas e versão do python com a qual o programa foi compilado.
####Saída:
Sai do programa, verificando primeiro se temos downloads ativos. Neste caso seremos avisados com uma caixa de diálogo onde precisaremos escolher se realmente queremos sair. Também podemos sair com Alt + F4 da interface principal.

###Diálogo de opções

Esta caixa de diálogo possui diferentes áreas nesta primeira versão.

Ao abri-la, o foco estará em uma lista onde estão as diferentes áreas, para que nos possamos mover com as setas para cima ou para baixo.

Novas secções e opções serão adicionadas a esta caixa de diálogo à medida que o programa for incluindo novos recursos.

Quando estivermos na área desejada, se pressionarmos tab, chegaremos às opções dessa área, e poderemos percorrê-las com tab.

Nesta primeira versão são oferecidas as seguintes opções:

####Geral:
Esta área contém opções gerais, cujas funcionalidades são:

#####Alterar idioma do programa:
Pressionar este botão dará um menu com os idiomas que o programa suporta. Atualmente são suportados 85 idiomas, dos quais nesta primeira versão oficial apenas o espanhol e o inglês são oficiais e os demais idiomas são gerados por um tradutor automático. Na próxima secção deste documento explicaremos como funciona e como quem quiser pode adicionar um idioma e oficializá-lo para o programa. mais tarde falarei sobre idiomas e darei informações técnicas para tradutores.
#####Escolha o separador inicial do programa:
Nesta caixa de combinação podemos selecionar o separador que será carregado quando o programa for iniciado.
#####Minimizar para a bandeja do sistema Quando a janela principal é minimizada:
Se habilitarmos esta caixa e minimizarmos a janela, ao invés de permanecer minimizada, ela irá se esconder na bandeja do sistema, e um novo ícone com o nome TCA-Media Downloader e sua versão aparecerá. Se pressionarmos diretamente o ícone, a janela do TCA-Media Downloader será aberta; Se pressionarmos o botão esquerdo, teremos um menu para abrir ou fechar o programa, e se clicarmos duas vezes, o programa será aberto. isso terá novas opções no futuro. o ícone só aparecerá quando o programa estiver oculto. Caso seja restaurado, o ícone desaparecerá da bandeja do sistema.
####Transferências:
Aqui adicionaremos as opções referentes aos downloads.

Atualmente, temos:

#####Retomar downloads incompletos (experimental):
Se marcarmos esta caixa, uma caixa de diálogo será mostrada explicando como isso funciona, mas no geral, o que acontecerá é que, se fecharmos o programa e ainda houver downloads ativos, se colocarmos a mesma URL ou pesquisarmos e baixarmos novamente, e vestígios desse download forem detectados, em vez de recomeçar, ele tentará fazer o download de onde foi interrompido.

Deve-se dizer que esta opção está em modo experimental e não há garantia de que funcione em todos os casos.

####Reprodutor:
Aqui colocaremos o que diz respeito ao reprodutor.

Atualmente traz o seguinte:

##### reproduzir a melhor qualidade (o menu Qualidade não será mostrado ao pressionar reproduzir):
Por padrão, esta caixa está marcada, portanto, quando reproduzirmos um vídeo, será sempre reproduzida a melhor qualidade encontrada. Se desmarcarmos esta caixa, pressionar reproduzir em um vídeo nos dará um menu no qual podemos selecionar a qualidade de reprodução, baixa, média ou alta, desde que esteja disponível. em alguns vídeos, por exemplo, pode nos dar apenas qualidade baixa e média, baixa e alta, ou média e alta. tudo depende de quais qualidades são encontradas.

Isto é do agrado do utilizador. esta configuração foi adicionada para aqueles utilizadors com conexões limitadas para que possam ter a possibilidade de escolher se desmarcam a caixa, por exemplo, escolhendo baixa qualidade para salvar os dados da conexão.
#####Mostrar ecrã de vídeo durante a reprodução:
Esta caixa está desmarcada por padrão.

Se a verificarmos, quando um vídeo começar a ser reproduzido, o ecrã do vídeo será aberto automaticamente.

Neste ecrã poderemos usar teclas de reprodução de F1 a F12.

Deve-se dizer que o ecrã do vídeo fechará se perder o foco, e teremos que abri-lo novamente para continuar a assistir ao conteúdo visualmente.
####Som:
Aqui poderemos personalizar quais os sons que queremos tocar e quais os que não desejamos.

Atualmente, podemos ativar ou desativar o seguinte:

* Reproduzir som de inicialização (será reproduzido quando o programa carregar lentamente)
* Reproduzir sons de espera (será reproduzido em diálogos de espera)
* Reproduzir novo som de download (será reproduzido ao adicionar um novo download)
* Reproduzir um som de download bem-sucedido
* Reproduzir som de download com erro
* Enviar mensagens de informações de ação para o leitor de ecrã

Podemos selecionar as caixas mencionadas para que sejam usadas ou não. Todas elas vêm verificadas por padrão.


Algo deve ser dito sobre o envio de mensagens de informação de ação para o leitor de ecrã: Esta opção dará informações sobre as diferentes ações realizadas no programa, por exemplo, quando pressionamos Ctrl + B no campo URL, aparecerá campo URL limpo. Isso será falado pelo próprio leitor de ecrã.

Também nas teclas do reprodutor, aumentando ou diminuindo o volume, ou nos controles de velocidade, por exemplo, dirá aumentar o volume em 95%, ou reproduzir, pausar, avançar 30 segundos, etc.
São mensagens enviadas para o leitor de ecrã se a caixa estiver habilitada, caso contrário, essas mensagens não sairão.

São três combinações de teclas que, embora tenhamos a caixa desmarcada, serão enviadas ao leitor. Estas são:

* F9: informará o tempo decorrido e total da faixa em reprodução. Se não houver nenhum, isso nos dirá que nada está tocando.
* F10: dirá o título da faixa em reprodução, se não houver nada informará adequadamente.
* Ctrl + O: Esta combinação dará informações rápidas sobre as opções de download que definimos na guia URL.
* Ctrl + S: Esta combinação fornecerá informações sobre downloads ativos, concluídos e com erro.

estas teclas podem ser chamadas e usadas em qualquer lugar do programa, exceto em configurações e atualizações.

além disso, após as caixas de sons, temos a seguinte caixa de combinação:

#####amostra do som (selecione um som e pressione ctrl+r para o reproduzir):
Nesta caixa, se pressionarmos Ctrl + R, dará uma prévia do som, para que possamos identificar os sons do programa.

E, finalmente, esta caixa de diálogo de opções possui os botões OK e cancelar.

Se pressionarmos OK, as alterações serão guardadas e se pressionarmos cancelar, nada será alterado.

Cabe alertar que as alterações de idioma exigem que o programa seja reiniciado e que essa alteração só acontecerá se não houver downloads ativos.

##Resumo de teclas importantes

###Para o reprodutor:

* F1: Retroceder
* F2: Reproduzir/Pausar
* F3: Avanço rápido
* F4: Parar
* F5: Diminuir volume
* F6: Aumentar o volume
* F7: Desacelerar
* F8: Acelerar
* F9: Tempo decorrido/total
* F10: Título da reprodução em andamento
* F11: Ativa ou desativa o ecrã de vídeo
* F12: Habilita ou desabilita mensagens faladas pelo leitor de ecrã
* Ctrl + M: Mostra o menu para escolher o tempo de retrocesso e avanço, apenas nestes botões do reprodutor

###Em listas de vídeos:

* Ctrl + R: Reproduzir
* Ctrl + D: descarregar
* Ctrl + I: Posição na lista
* Ctrl + F: Caixa de diálogo para mover para uma posição na lista
* Enter: ação no item em foco e outras opções dependendo de onde estamos
* Espaço: somente em listas de seleção, irá marcar ou desmarcar o item em foco

###Resto das listas e campos de texto que não são de vídeo:

* Ctrl + B: Limpa campos de texto
* Enter: mostra o menu com as opções correspondentes dependendo de onde estamos

###Caixa de combinação de formato personalizado:

* Ctrl + I: informa a posição na caixa de combinação
* Ctrl + F: mostra a caixa de diálogo para escolher para onde queremos ir na caixa de combinação

###Diálogo de espera:

Na caixa de diálogo de espera que aparece cada vez que executa uma ação, há um pressionamento especial de tecla de pânico.

Essa combinação é:

Shift + Ctrl + Alt + K

Esta combinação é experimental e só deve ser usada caso o diálogo de espera demore muito e o programa não execute a ação solicitada.

Utilize apenas em casos específicos e quando esta caixa de diálogo permanecer por muito tempo.

###Outros:

* Ctrl + O: dará informações de formato, qualidade, nome e localização.

Estas são as opções que definimos no separador URL e são aquelas definidas para downloads.

* Ctrl + S: informações de status do download

dirá, com uma mensagem no nosso leitor, se há downloads ou não.

Nesse caso, informará o número de downloads ativos, concluídos e com erro.

Este pressionamento de tecla funciona em qualquer lugar do programa, exceto na caixa de diálogo de atualizações, configurações, espera ou posição.

##Informações sobre linguagens de programa
Como mencionado anteriormente, nesta primeira versão apenas os idiomas espanhol e inglês são oficiais, enquanto os outros 83 são gerados automaticamente por um tradutor automático.

Caso alguém queira contribuir com um idioma oficial, devem ser cumpridos os seguintes passos.

Todos os idiomas estão na pasta DATA/LOCALE. só precisa ir até o seu e alterar o ficheiro base.po.

Pode excluir a tradução automática e fazer a sua própria, ou corrigir a automática. Em seguida, guarde as alterações e gere o ficheiro .po. Dessa forma, o idioma refletirá as suas alterações assim que reiniciar.

Se quiser oficializar, envie-nos o base.po através dos canais de contato do blog Tecnoconocimiento Accesible.

Se o seu idioma não estiver entre os incluídos, ainda poderá adicioná-lo.

na pasta DATA/LOCALE existe um ficheiro chamado main.pot; pode abrir o ficheiro e gerar um modelo .po para o seu idioma.

Depois, basta seguir a mesma estrutura de pastas para adicionar o seu idioma e salvar o base.po com sua tradução na pasta do novo idioma que será adicionado.

Na próxima vez que abrir o programa, poderá escolher seu idioma.

Pode enviar o base.po com o novo idioma para os contatos do blog e o novo idioma será adicionado oficialmente.

Deve-se alertar que naquelas atualizações cuja descrição diz que os idiomas serão atualizados, se tivermos feito alguma alteração por conta própria, tais alterações serão substituídas pelas da atualização. portanto, recomendamos que você salve qualquer alteração feita e copie-a novamente manualmente.

caso contrário, a atualização excluirá qualquer alteração que não seja oficial.

Se as mudanças forem oficiais, elas não serão perdidas.

Deve-se dizer também que apenas serão suportadas traduções oficiais, sem garantia de que as traduções automáticas funcionem corretamente ou que sejam perfeitas. pelo contrário, é provável que cometam muitos erros, mas na maioria dos casos, pode ajudar para que o utilizador que não domina outro idioma possa utilizar parcialmente o programa no seu idioma.

## observações técnicas

na pasta DATA/LOGS, o programa guardará os ficheiros de depuração.

Estes ficheiros contêm informações sobre erros que podem ocorrer, por isso recomendamos fortemente que esses ficheiros sejam anexados ao relatar um bug.

Quando ocorrer um erro, tente ver exatamente a que horas aconteceu, pois está guardado nos ficheiros de log. então se o ficheiro tiver mais de um erro, com esses ficheiros e a hora em que o erro ocorreu fica mais fácil de detectar.

Tentamos que o programa tenha proteções para que não fique bloqueado ou inutilizável, e tentamos contemplar a maioria dos erros que podem ocorrer.

mas deve ser entendido que não é possível contemplar todos eles, portanto com as diferentes atualizações que forem realizadas tentaremos tornar o programa cada vez mais robusto.

também deve ser alertado sobre o abuso de adição de downloads. cada download que adicionamos requer recursos, portanto, se fizermos muitos downloads e nosso computador não tiver recursos suficientes, podemos bloqueá-lo.

Use com responsabilidade e levando em consideração que cada download requer memória RAM e largura de banda.

##Observações
Ocasionalmente, podemos encontrar canais que parecem não conter vídeos.
Neste caso, faremos o seguinte:

1. para voltar aos resultados da pesquisa, pressione Escape
2. No resultado do canal, pressione enter e aceda às suas informações.
3. Uma vez lá, vá para o separador “listas de canais” com ctrl + Tab
4. Aqui poderemos encontrar os canais, se houver, e escolher os vídeos para baixar desse canal.

#Créditos

Quero agradecer especialmente aos testadores beta, Gera, Gustavo, Peter, Pepe, Rosa, Romina, Rayo, Óscar, Simone e todos que provavelmente estou esquecendo. Minhas desculpas.

Da mesma forma, aos tradutores oficiais:

* Italiano: Simone Dal Maso
* Turco: Umut Korkmaz
* Inglês: Slann Tonic

#Changelog.<a name="changelog"></a>
Deve-se lembrar que nesta secção novos recursos serão adicionados sem modificar o documento principal como orientação à medida que as atualizações forem surgindo.

Portanto, uma vez familiarizados com o programa na sua primeira versão, é recomendável visitar esta secção para ver as novidades, pois aqui destacaremos as novas funcionalidades, sua descrição e atalhos de teclado.

Somente versões de atualização pertencentes a ramificações completas e de recursos serão adicionadas.

A ramificação da biblioteca incluirá correções de bugs e bibliotecas internas, sem alterar nada no manuseio do programa.

O utilizador é responsável por verificar esta secção para ser informado sobre alterações.

## Versão 3.0.1.0.

* Novo separador chamado Favoritos (Alt + 4).
Agora podemos guardar vídeos, playlists ou canais que quisermos neste separador, para acesso rápido.
Ao abrir este separador, teremos 3 secções:
Alt + F: leva-nos até a árvore onde podemos interagir com os ramos.
A árvore possui uma base chamada Favoritos, e se pressionarmos Enter, podemos apagar todo o banco de dados ou criar e restaurar um backup do banco de dados.
Existe um ramo chamado Vídeos, e se pressionarmos Enter, podemos criar listas de reprodução de vídeos. Pressionar esta opção abrirá uma janela para inserir o nome da lista de reprodução.
Depois de adicionarmos playlists de vídeos, podemos expandir o ramo e teremos sub-ramos. Se pressionarmos Enter em um sub-ramo, teremos a opção de editar, excluir ou limpar essa lista de reprodução de vídeos.
Também temos dois ramos na árvore chamados Playlists e Canais. Se alguma dessas ramificações tiver conteúdo, podemos pressionar Enter para excluir seu conteúdo.
Alt + C: leva-nos para a área de conteúdo. Nesta área, será exibido o conteúdo da playlist de vídeos, playlist ou canal selecionado.
Nesta área, se pressionarmos Enter num item, aparecerá um menu correspondente para vídeos, playlists ou canais, permitindo-nos interagir com eles.
Alt + B: Leva-nos a uma caixa de pesquisa onde podemos pesquisar dentro do ramo selecionado. Nesta caixa, podemos inserir a consulta de pesquisa em letras minúsculas ou maiúsculas e pressionar Enter para obter o resultado na área de consulta. Podemos interagir com o resultado pressionando Enter nele.
O campo de pesquisa nos permite inserir texto parcial. Por exemplo, se pesquisarmos por “TCA”, serão retornados todos os vídeos no ramo atual que contenham essas letras.
Podemos redefinir a pesquisa para os seus valores originais e restaurar rapidamente a área de conteúdo pressionando Ctrl + B na caixa de pesquisa ou excluindo o texto inserido e pressionando Enter. Além disso, se houver uma pesquisa em andamento na área de conteúdo, pressionar Ctrl + B irá redefini-la para seus valores originais.
Para adicionar conteúdo ao banco de dados, fazemos isso a partir das informações de cada separador. Por exemplo, se quisermos adicionar um vídeo a uma playlist que criamos na separador de pesquisa, quando tivermos os resultados da pesquisa, pressionamos Enter no item e clicamos em “Informações do vídeo”. Na janela aberta, haverá um botão chamado “Adicionar à Playlist de Vídeo”, que, ao ser clicado, exibirá um menu com todas as playlists de vídeos que criamos no banco de dados. Se escolhermos um, o vídeo será salvo nessa playlist.
Podemos adicionar o mesmo vídeo a várias playlists, mas ele só pode ser adicionado uma vez por playlist.
Em relação às playlists e canais, o processo é semelhante. Na caixa de diálogo de informações, há um botão chamado “Adicionar aos Favoritos”. Clicar nele adicionará a playlist ou canal à ramificação correspondente no banco de dados. O botão mudará para “Remover dos Favoritos”. A menos que excluamos a lista de reprodução ou canal do separador Favoritos ou da caixa de diálogo de informações, ele permanecerá no banco de dados.
As ramificações da lista de reprodução e do canal armazenarão apenas um item cada, mas vários itens com o mesmo nome podem ser armazenados, desde que os URLs sejam diferentes.
Na área de consulta, podemos pressionar Ctrl + I para saber a nossa posição atual e Ctrl + F para navegar rapidamente até o item desejado.
Foi adicionada a possibilidade de adicionar ao banco de dados a partir dos resultados da pesquisa.
Agora podemos pressionar Enter num vídeo, playlist ou canal nos resultados da pesquisa, e a última opção do menu de contexto nos permitirá interagir com o banco de dados de favoritos.
Teremos as mesmas opções das caixas de diálogo de vídeo, lista de reprodução ou informações do canal.

* Adicionado Ctrl + R e Ctrl + D no campo URL.
Agora, no separador URL, se inserirmos a URL de um vídeo do YouTube, podemos pressionar essas combinações para reproduzir ou baixar o vídeo sem a necessidade de abrir o menu de contexto.

* Adicionada a capacidade de ver comentários em um vídeo (experimental).
Agora, quando abrirmos a caixa de diálogo de informações do vídeo, um botão aparecerá se o vídeo tiver comentários.
O botão chama-se “Ver ou guardar Comentários” e se clicarmos nele podemos visualizar ou salvar os comentários.
Estas opções são experimentais e foi detectado que ocasionalmente podem fechar o aplicativo. Caso haja downloads em andamento, o utilizador será notificado de que poderá perder as informações que estão a ser baixadas.
Se optarmos por ver os comentários, aparecerá uma janela de extração de comentários, indicando a percentagem de comentários extraídos. Podemos cancelar a extração clicando no botão cancelar na janela.
Assim que a extração for concluída, uma janela será aberta com todos os comentários, mostrados num controlo em árvore.
Podemos expandir a árvore e navegar pelos comentários. Se um comentário tiver respostas, também podemos expandi-lo para visualizar as respostas.
Comentários longos serão marcados com ** no final, indicando que o comentário completo não cabe.
Para que o comentário seja lido em voz alta por um leitor de ecrã, existe uma combinação de teclas: Ctrl + T.
Da mesma forma, se pressionarmos a tecla Tab, entraremos numa caixa somente leitura onde teremos o comentário completo junto com o nome do comentarista, a data e o número de gostos.
Nesta janela existe um botão chamado "guardar”, que executa a mesma ação do menu de contexto da caixa de diálogo de informações do vídeo: guarda os comentários num formato HTML acessível.
A estrutura do HTML é a seguinte:
Título Nível 1 para o título do vídeo.
Título Nível 2 para o comentário principal.
Título Nível 3 para respostas a comentários.
A janela inteira possui atalhos para navegar rapidamente:
Alt + L: leva-nos à árvore de comentários.
Alt + D: leva-nos rapidamente aos detalhes do comentário em foco.
Alt + G: Guarda os comentários como um ficheiro HTML.
Alt + C, Alt + F4 ou Escape: fecha a janela.

* Novas funções em menus de contexto e melhorias.
Os menus de contexto na área de download foram corrigidos. A opção “reproduzir” não aparece mais para itens que não sejam vídeos.
Foi corrigido o problema em que o menu de download múltiplo não aparecia quando havia apenas um resultado de vídeo ou um vídeo no banco de dados.
Novas opções foram adicionadas aos menus de contexto com base no contexto, como:
Abrir na Web: Esta opção abre o vídeo, playlist ou canal selecionado no nosso navegador, levando-nos ao YouTube.
Um submenu chamado Compartilhar foi adicionado.
Este menu permite-nos partilhar a URL com Twitter, Facebook, Telegram, WhatsApp, Mastodon ou como código QR com o nosso dispositivo móvel.
Se escolhermos “Gerar código QR para abrir com celular”, uma janela será aberta no centro do ecrã exibindo um código QR. Assim que o leitor de código QR do nosso dispositivo móvel o detectar, o URL, seja de um vídeo, lista de reprodução ou canal, será aberto no nosso dispositivo.
Observe que no Facebook só permite o compartilhamento da URL, portanto não podemos adicionar texto automaticamente. Porém, no ecrã para o qual nos redireciona, podemos adicionar informações manualmente.
Para o Mastodon, solicitará a URL da instância em que estamos. Podemos guardá-lo ou modificá-lo, se desejar. Se o guardarmos, ele estará pré-definido e não teremos que adicioná-lo toda vez que quisermos compartilhar com o Mastodon.
Observe que para compartilhar em qualquer rede social, precisamos de estar logados na nossa sessão do navegador. O compartilhamento será mais fácil se tivermos os aplicativos WhatsApp e Unigram instalados.

* Adicionadas novas opções na caixa de diálogo de configurações.
Na categoria Geral, foi adicionado o seguinte:
Verificar atualizações e notificar: Nesta caixa suspensa, podemos escolher se queremos que o aplicativo verifique atualizações e nos notifique com uma notificação do Windows.
Podemos optar por desabilitar esta opção ou selecionar diferentes intervalos de tempo para o aplicativo verificar se há atualizações.
Quando uma atualização for encontrada, uma notificação do Windows informará sobre a atualização e sua versão.
Esta opção não baixa atualizações; verifica apenas atualizações nos intervalos selecionados. Para baixar atualizações, temos que verificar manualmente as atualizações.
As notificações continuarão a aparecer nos intervalos de tempo selecionados até atualizarmos o aplicativo.
Na categoria Downloads, foi adicionado o seguinte:
Tempo para extrair informações (se o tempo de extração exceder, será mostrado um erro se todas as informações não forem obtidas, válido para playlists ou canais grandes): Nesta caixa suspensa, podemos aumentar o tempo que o aplicativo leva para determinar isso não foi possível recuperar todas as informações.
Por padrão, está definido para 2 minutos, que é um tempo razoável e suficiente para a maioria das listas de reprodução e canais.
Se for necessário mais tempo, por exemplo, para playlists ou canais com mais de 5.000 vídeos, podemos aumentar o tempo de recuperação de dados.

* Adicionada proteção contra download de transmissões ao vivo em todas as caixas de diálogo.
Foi adicionada uma proteção para detectar se o URL que queremos baixar é de uma transmissão ao vivo. Nesses casos, não nos permitirá baixar a transmissão ao vivo.
Este problema foi resolvido e uma solução alternativa será fornecida em versões futuras.

* Bibliotecas internas atualizadas para melhor desempenho do aplicativo.

* Corrigidos erros internos.

* Traduções atualizadas.

## Versão 3.0.0.0.

* Versão inicial.