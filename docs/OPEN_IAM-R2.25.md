1 Histórico de Revisões [8](#histórico-de-revisões)

2 Glossário [13](#glossário)

3 Referências [13](#referências)

4 Introdução [13](#introdução)

4.1 Pilha das Camadas dos Protocolos de Comunicação
[14](#pilha-das-camadas-dos-protocolos-de-comunicação)

4.2 Camada de Tunelamento [14](#camada-de-tunelamento)

4.3 Camadas de Rede / Ligação de Dados
[14](#camadas-de-rede-ligação-de-dados)

4.4 Fluxo de Transmissões do Equipamento para o Servidor
[14](#fluxo-de-transmissões-do-equipamento-para-o-servidor)

4.4.1 Modos de Operação [14](#modos-de-operação)

4.5 Estrutura da Mensagem [15](#estrutura-da-mensagem)

4.5.1 OPEN V2 e OPEN V3 [15](#open-v2-e-open-v3)

4.5.2 OPEN V4 [17](#open-v4)

4.5.3 OPEN V5 [17](#open-v5)

4.6 Criptografia [18](#criptografia)

4.6.1 Algoritmo de criptografia RC4 [18](#algoritmo-de-criptografia-rc4)

4.7 CRC [20](#crc)

5 Dicionário de Dados [21](#dicionário-de-dados)

6 Camada de Aplicação [30](#camada-de-aplicação)

7 Mensagens da Camada de Aplicação
[31](#mensagens-da-camada-de-aplicação)

7.1 Tabela de tipos de mensagens [31](#tabela-de-tipos-de-mensagens)

7.2 Mensagens Gerais [32](#mensagens-gerais)

7.2.1 Mensagem de Acknowledge (ACK – 00h)
[32](#mensagem-de-acknowledge-ack-00h)

7.2.2 Posição (POS – 01h) [32](#posição-pos-01h)

7.2.3 Mensagem da Porta Serial para o Servidor (UPL – 02h)
[33](#mensagem-da-porta-serial-para-o-servidor-upl-02h)

7.2.4 Comandos PAN (PAN – 03h) [33](#comandos-pan-pan-03h)

7.2.5 Posição com Informação Adicional (PAI – 04h)
[33](#posição-com-informação-adicional-pai-04h)

7.2.6 Status com Informação Adicional (SAI – 05h)
[34](#status-com-informação-adicional-sai-05h)

7.2.7 Comandos (CMD – 06h) [34](#comandos-cmd-06h)

7.2.8 Mensagem do Servidor para a Porta Serial (DWL – 07h)
[34](#mensagem-do-servidor-para-a-porta-serial-dwl-07h)

7.2.9 Mensagem de Hodômetro (ODO – 08h)
[35](#mensagem-de-hodômetro-odo-08h)

7.2.10 Mensagem de Configuração de Ponto de Controle (CPC – 09h)
[35](#mensagem-de-configuração-de-ponto-de-controle-cpc-09h)

7.2.11 Mensagem de Configuração de Cerca Eletrônica (GFC – 0Ah)
[35](#mensagem-de-configuração-de-cerca-eletrônica-gfc-0ah)

7.2.12 Mensagem de Acknowledge Negativo (NACK – 0Bh)
[35](#mensagem-de-acknowledge-negativo-nack-0bh)

7.2.13 Leitura de Parâmetro (PRD – 0Ch)
[35](#leitura-de-parâmetro-prd-0ch)

7.2.14 Resposta à Leitura de Parâmetro (PRR – 0Dh)
[35](#resposta-à-leitura-de-parâmetro-prr-0dh)

7.2.15 Leitura de variável CAN via identificador SPN do protocolo SAE
J1939 (CSR- 14h)
[36](#leitura-de-variável-can-via-identificador-spn-do-protocolo-sae-j1939-csr--14h)

7.2.16 Resposta à Leitura de variável CAN via identificador SPN do
protocolo SAE J1939 (CSRR- 15h)
[36](#resposta-à-leitura-de-variável-can-via-identificador-spn-do-protocolo-sae-j1939-csrr--15h)

7.2.17 Escrita de Parâmetro (PRW – 16h)
[36](#escrita-de-parâmetro-prw-16h)

7.2.18 Alteração de protocolo de comunicação (CPM – 17h)
[36](#alteração-de-protocolo-de-comunicação-cpm-17h)

7.2.19 Informação de Rádio Base (RBI – 18h)
[36](#informação-de-rádio-base-rbi-18h)

7.2.20 Posição com Identificador do SIM Card (PSI – 19h)
[37](#posição-com-identificador-do-sim-card-psi-19h)

7.2.21 Configuração do Número de Identificação do Rastreador (IDC – 1Ah)
[37](#configuração-do-número-de-identificação-do-rastreador-idc-1ah)

7.2.22 Mensagem Encapsulada do Protocolo TALT (TAL – 1Ch)
[38](#mensagem-encapsulada-do-protocolo-talt-tal-1ch)

7.2.23 Mensagem de Lista de Variáveis (VRL – 1Dh)
[38](#mensagem-de-lista-de-variáveis-vrl-1dh)

7.2.24 Mensagem de Leitura de Variáveis (VRD – 1Eh)
[38](#mensagem-de-leitura-de-variáveis-vrd-1eh)

7.2.25 Mensagem de Resposta à Leitura de Variáveis (VRR – 1Fh)
[38](#mensagem-de-resposta-à-leitura-de-variáveis-vrr-1fh)

7.2.26 Mensagem de Informação RDS (RDI – 20h)
[39](#mensagem-de-informação-rds-rdi-20h)

7.2.27 Mensagem Encapsulada (ENC – 21h)
[39](#mensagem-encapsulada-enc-21h)

7.2.28 Mensagem de Lista de Relatórios (RPL – 22h)
[39](#mensagem-de-lista-de-relatórios-rpl-22h)

7.2.29 Mensagem de status da base LC (BSS – 23h)
[40](#mensagem-de-status-da-base-lc-bss-23h)

7.2.30 Mensagem de Status do Rastreador para Dispositivos Locais (TST –
24h)
[40](#mensagem-de-status-do-rastreador-para-dispositivos-locais-tst-24h)

7.2.31 Mensagem de Status da Antena Satelital para Dispositivos Locais
(SST – 25h)
[41](#mensagem-de-status-da-antena-satelital-para-dispositivos-locais-sst-25h)

7.2.32 Mensagem de comando para dispositivos locais (CLD – 26h)
[41](#mensagem-de-comando-para-dispositivos-locais-cld-26h)

7.2.33 Mensagem de notificação gerada por dispositivos locais (NLD –
27h)
[41](#mensagem-de-notificação-gerada-por-dispositivos-locais-nld-27h)

7.2.34 Mensagem para troca de informações via link satelital (SAT – 28h)
[42](#mensagem-para-troca-de-informações-via-link-satelital-sat-28h)

7.2.35 Mensagem para início de transferência de arquivo (BFT – 2Ah)
[42](#mensagem-para-início-de-transferência-de-arquivo-bft-2ah)

7.2.36 Mensagem para transferência de segmento de arquivo (TFS – 2Bh)
[43](#mensagem-para-transferência-de-segmento-de-arquivo-tfs-2bh)

7.2.37 Mensagem para verificação do arquivo transferido (CKF – 2Ch)
[43](#mensagem-para-verificação-do-arquivo-transferido-ckf-2ch)

7.2.38 Mensagem para finalização da transferência de arquivo (CFT – 2Dh)
[43](#mensagem-para-finalização-da-transferência-de-arquivo-cft-2dh)

7.2.39 Mensagem de Evento com Informação Adicional (EAI – 30h)
[44](#mensagem-de-evento-com-informação-adicional-eai-30h)

7.3 Mensagens do Download Remoto [44](#mensagens-do-download-remoto)

7.3.1 Iniciar Procedimento de Download (SAD – 0Eh)
[44](#iniciar-procedimento-de-download-sad-0eh)

7.3.2 Limpar Área de Download (EDA – 0Fh)
[45](#limpar-área-de-download-eda-0fh)

7.3.3 Armazenar Segmento (SSG – 10h) [45](#armazenar-segmento-ssg-10h)

7.3.4 Verificar Código (CCD – 11h) [45](#verificar-código-ccd-11h)

7.3.5 Atualizar Área do Programa (URA – 12h)
[46](#atualizar-área-do-programa-ura-12h)

7.3.6 Abandonar o Procedimento de Download (SOD – 13h)
[46](#abandonar-o-procedimento-de-download-sod-13h)

7.3.7 Retorno do Procedimento de Download (RTD – 1Bh)
[46](#retorno-do-procedimento-de-download-rtd-1bh)

7.4 Mensagens de transferência de arquivos via HTTP
[47](#mensagens-de-transferência-de-arquivos-via-http)

7.4.1 Novo arquivo disponível para download (NFA – 40h)
[47](#novo-arquivo-disponível-para-download-nfa-40h)

7.4.2 Confirmação de atualização de arquivos (CDF – 31h)
[47](#confirmação-de-atualização-de-arquivos-cdf-31h)

7.4.3 Cancelar download atual (CDC – 32h)
[47](#cancelar-download-atual-cdc-32h)

7.4.4 Checar Http File (CHF – 33h) [47](#checar-http-file-chf-33h)

7.4.5 Nova Transferência Local (NTF – 34h)
[47](#nova-transferência-local-ntf-34h)

7.4.6 Envio de pedaço de arquivo (SFC – 35h)
[48](#envio-de-pedaço-de-arquivo-sfc-35h)

7.5 Mensagens de sequenciamento de macro
[48](#mensagens-de-sequenciamento-de-macro)

7.5.1 Permissão de envio de macro (RNE – 36h)
[48](#permissão-de-envio-de-macro-rne-36h)

7.5.2 Requisição de senha de autorização (RAP – 37h)
[48](#requisição-de-senha-de-autorização-rap-37h)

7.5.3 Resposta com senha de autorização (RAR – 38h)
[48](#resposta-com-senha-de-autorização-rar-38h)

7.5.4 Checar contrassenha de autorização (CAP – 39h)
[49](#checar-contrassenha-de-autorização-cap-39h)

7.5.5 Resposta a Requisição de Macro (RRM – 3Ah)
[49](#resposta-a-requisição-de-macro-rrm-3ah)

8 Informação Adicional [49](#informação-adicional)

8.1 Estrutura do Bloco de Informação Adicional
[49](#estrutura-do-bloco-de-informação-adicional)

8.2 Identificadores de Informação Adicional
[50](#identificadores-de-informação-adicional)

8.2.1 Informação Básica de Trânsito – BTI
[51](#informação-básica-de-trânsito-bti)

8.2.2 Rotações por Minuto – RPM [52](#rotações-por-minuto-rpm)

8.2.3 Informação Básica de Telemetria - BLI
[52](#informação-básica-de-telemetria---bli)

8.2.4 Identificação do SIM Card - SCI
[53](#identificação-do-sim-card---sci)

8.2.5 Informação do acelerômetro [53](#informação-do-acelerômetro)

8.2.6 Envio da temperatura interna do módulo
[53](#envio-da-temperatura-interna-do-módulo)

8.2.7 Envio de status dos sensores analógicos
[53](#envio-de-status-dos-sensores-analógicos)

8.2.8 Envio de status dos sensores digitais
[54](#envio-de-status-dos-sensores-digitais)

8.2.9 Envio de status dos atuadores [54](#envio-de-status-dos-atuadores)

8.2.10 Envio de valor do hodômetro [54](#envio-de-valor-do-hodômetro)

8.2.11 BSLE (Base Station Location Element)
[54](#bsle-base-station-location-element)

8.2.12 Envio do nível da bateria interna
[55](#envio-do-nível-da-bateria-interna)

8.2.13 Monitoração do nível da bateria externa
[55](#monitoração-do-nível-da-bateria-externa)

8.2.14 Data e hora da última BSLE válida
[56](#data-e-hora-da-última-bsle-válida)

8.2.15 Informação do GPS [56](#informação-do-gps)

8.2.16 Velocidade do Veículo [56](#velocidade-do-veículo)

8.2.17 Tempo estimado para envio da próxima monitoração
[56](#tempo-estimado-para-envio-da-próxima-monitoração)

8.2.18 Valor do Horímetro [57](#valor-do-horímetro)

8.2.19 Status da transferência Http [57](#status-da-transferência-http)

8.2.20 Status Modo violado [57](#status-modo-violado)

8.2.21 Arquivos não sincronizados [57](#arquivos-não-sincronizados)

8.2.22 Estado de Macro [57](#estado-de-macro)

9 Eventos [57](#eventos)

9.1 Estrutura do evento [58](#estrutura-do-evento)

9.2 Reportando eventos [58](#reportando-eventos)

9.3 Tabela de tipos de eventos [58](#tabela-de-tipos-de-eventos)

9.4 Eventos de Telemetria [69](#eventos-de-telemetria)

9.4.1 Eventos de 0x0021 a 0x002B (os ímpares)
[69](#eventos-de-0x0021-a-0x002b-os-ímpares)

9.4.2 Eventos do tipo RPM (0x002D / 0x002F / 0x0031)
[70](#eventos-do-tipo-rpm-0x002d-0x002f-0x0031)

9.4.3 Eventos do tipo velocidade (0x0033 / 0x0035 / 0x0037)
[71](#eventos-do-tipo-velocidade-0x0033-0x0035-0x0037)

9.4.4 Eventos de aceleração brusca, freada brusca e freada muito brusca
(0x0040 / 0x0041 / 0x0042)
[72](#eventos-de-aceleração-brusca-freada-brusca-e-freada-muito-brusca-0x0040-0x0041-0x0042)

9.5 Evento de atualização de firmware
[73](#evento-de-atualização-de-firmware)

9.6 Eventos de pontos de controle e cercas eletrônicas
[73](#eventos-de-pontos-de-controle-e-cercas-eletrônicas)

9.6.1 Evento de entrada em ponto de controle
[73](#evento-de-entrada-em-ponto-de-controle)

9.6.2 Evento de saída de ponto de controle
[73](#evento-de-saída-de-ponto-de-controle)

9.6.3 Evento de entrada em cerca eletrônica
[73](#evento-de-entrada-em-cerca-eletrônica)

9.6.4 Evento de saída de cerca eletrônica
[73](#evento-de-saída-de-cerca-eletrônica)

9.7 Eventos relacionados ao GPS [74](#eventos-relacionados-ao-gps)

9.7.1 Evento de antena externa de GPS conectada
[74](#evento-de-antena-externa-de-gps-conectada)

9.7.2 Evento de antena externa de GPS desconectada
[74](#evento-de-antena-externa-de-gps-desconectada)

9.7.3 Evento de início da detecção de jammer GPS
[74](#evento-de-início-da-detecção-de-jammer-gps)

9.7.4 Evento de fim da detecção de jammer GPS
[74](#evento-de-fim-da-detecção-de-jammer-gps)

9.7.5 Evento de falha no hardware GPS
[74](#evento-de-falha-no-hardware-gps)

9.7.6 Evento de falha do sinal GPS [75](#evento-de-falha-do-sinal-gps)

9.7.7 Evento de requisição de dados AGPS Online
[75](#evento-de-requisição-de-dados-agps-online)

9.8 Eventos relacionados ao GSM [75](#eventos-relacionados-ao-gsm)

9.8.1 Evento de início da detecção de jammer GSM
[75](#evento-de-início-da-detecção-de-jammer-gsm)

9.8.2 Evento de fim da detecção de jammer GSM
[75](#evento-de-fim-da-detecção-de-jammer-gsm)

9.9 Outros Eventos [77](#outros-eventos)

9.9.1 Evento de configuração de hodômetro
[77](#evento-de-configuração-de-hodômetro)

9.9.2 Evento de início de velocidade obtida via CAN
[77](#evento-de-início-de-velocidade-obtida-via-can)

9.9.3 Evento de fim de velocidade obtida via CAN
[77](#evento-de-fim-de-velocidade-obtida-via-can)

9.9.4 Evento de limite de velocidade ultrapassado (com precisão)
[77](#evento-de-limite-de-velocidade-ultrapassado-com-precisão)

9.9.5 Evento de bloqueio de veículo [78](#evento-de-bloqueio-de-veículo)

9.9.6 Evento de desbloqueio de veículo
[78](#evento-de-desbloqueio-de-veículo)

9.9.7 Evento de escrita de parâmetro
[78](#evento-de-escrita-de-parâmetro)

9.10 Eventos relacionados ao acelerômetro
[79](#eventos-relacionados-ao-acelerômetro)

9.10.1 Evento de início de movimento por acelerômetro
[79](#evento-de-início-de-movimento-por-acelerômetro)

9.10.2 Evento de fim de movimento por acelerômetro
[79](#evento-de-fim-de-movimento-por-acelerômetro)

9.11 Eventos relacionados ao uso de dois SIM CARDs
[80](#eventos-relacionados-ao-uso-de-dois-sim-cards)

9.11.1 Evento de detecção de SIM CARD
[80](#evento-de-detecção-de-sim-card)

9.11.2 Evento de falha de SIM CARD [80](#evento-de-falha-de-sim-card)

9.11.3 Evento de troca de SIM CARD [80](#evento-de-troca-de-sim-card)

9.11.4 Evento informando chaveamento de operadora
[81](#evento-informando-chaveamento-de-operadora)

9.12 Eventos relacionados à antena satelital
[82](#eventos-relacionados-à-antena-satelital)

9.12.1 Evento de casamento da antena satelital
[82](#evento-de-casamento-da-antena-satelital)

9.12.2 Evento de desconexão da antena satelital
[82](#evento-de-desconexão-da-antena-satelital)

9.12.3 Evento de início de uso da antena satelital
[83](#evento-de-início-de-uso-da-antena-satelital)

9.12.4 Evento de fim de uso da antena satelital
[83](#evento-de-fim-de-uso-da-antena-satelital)

9.12.5 Evento de alerta de poucos créditos
[84](#evento-de-alerta-de-poucos-créditos)

9.12.6 Evento de erro na antena satelital
[84](#evento-de-erro-na-antena-satelital)

9.12.7 Evento de alerta de fim dos créditos
[85](#evento-de-alerta-de-fim-dos-créditos)

9.12.8 Evento de início de uso de créditos do período
[85](#evento-de-início-de-uso-de-créditos-do-período)

9.12.9 Evento de inserção de créditos
[85](#evento-de-inserção-de-créditos)

9.13 Eventos relacionados aos sensores analógicos
[87](#eventos-relacionados-aos-sensores-analógicos)

9.13.1 Evento de valor mínimo ultrapassado
[87](#evento-de-valor-mínimo-ultrapassado)

9.13.2 Evento de retorno de valor mínimo ultrapassado
[87](#evento-de-retorno-de-valor-mínimo-ultrapassado)

9.13.3 Evento de valor máximo ultrapassado
[87](#evento-de-valor-máximo-ultrapassado)

9.13.4 Evento de retorno de valor máximo ultrapassado
[88](#evento-de-retorno-de-valor-máximo-ultrapassado)

9.13.5 Evento de saída da faixa ideal para baixo
[88](#evento-de-saída-da-faixa-ideal-para-baixo)

9.13.6 Evento de entrada na faixa ideal por baixo
[88](#evento-de-entrada-na-faixa-ideal-por-baixo)

9.13.7 Evento de saída da faixa ideal para cima
[89](#evento-de-saída-da-faixa-ideal-para-cima)

9.13.8 Evento de entrada na faixa ideal por cima
[89](#evento-de-entrada-na-faixa-ideal-por-cima)

9.13.9 Evento de falha do sensor [89](#evento-de-falha-do-sensor)

9.13.10 Evento de variação máxima atingida
[89](#evento-de-variação-máxima-atingida)

9.14 Eventos relacionados aos sensores digitais
[91](#eventos-relacionados-aos-sensores-digitais)

9.14.1 Evento de sensor digital acionado
[91](#evento-de-sensor-digital-acionado)

9.14.2 Evento de sensor digital desacionado
[91](#evento-de-sensor-digital-desacionado)

9.14.3 Evento de tempo máximo de sensor digital acionado atingido
[91](#evento-de-tempo-máximo-de-sensor-digital-acionado-atingido)

9.15 Eventos relacionados aos atuadores
[92](#eventos-relacionados-aos-atuadores)

9.15.1 Evento de atuador acionado [92](#evento-de-atuador-acionado)

9.15.2 Evento de atuador desacionado
[92](#evento-de-atuador-desacionado)

9.16 Eventos relacionados ao modo de segurança
[93](#eventos-relacionados-ao-modo-de-segurança)

9.16.1 Evento de modo de segurança ativado
[93](#evento-de-modo-de-segurança-ativado)

9.16.2 Evento de modo de segurança desativado
[93](#evento-de-modo-de-segurança-desativado)

9.16.3 Evento de movimento indevido [93](#evento-de-movimento-indevido)

9.16.4 Evento de horário indevido [93](#evento-de-horário-indevido)

9.16.5 Evento de excesso de tempo parado
[93](#evento-de-excesso-de-tempo-parado)

9.16.6 Evento de âncora ativada [94](#evento-de-âncora-ativada)

9.16.7 Evento de âncora desativada [94](#evento-de-âncora-desativada)

9.16.8 Evento de entrada em âncora [94](#evento-de-entrada-em-âncora)

9.16.9 Evento de saída de âncora [94](#evento-de-saída-de-âncora)

9.16.10 Eventos relacionados ao teclado
[95](#eventos-relacionados-ao-teclado)

9.16.11 Evento de conexão de teclado [95](#evento-de-conexão-de-teclado)

9.16.12 Evento de desconexão de teclado
[95](#evento-de-desconexão-de-teclado)

9.16.13 Evento de senha de coação [95](#evento-de-senha-de-coação)

9.16.14 Evento de Ativação da Liberação do Bloqueio
[95](#evento-de-ativação-da-liberação-do-bloqueio)

9.16.15 Evento de Desativação da Liberação do Bloqueio
[95](#evento-de-desativação-da-liberação-do-bloqueio)

9.16.16 Evento de Ativação da Liberação da Trava Baú 1
[96](#evento-de-ativação-da-liberação-da-trava-baú-1)

9.16.17 Evento de Desativação da Liberação da Trava Baú 1
[96](#evento-de-desativação-da-liberação-da-trava-baú-1)

9.16.18 Evento de Ativação da Liberação da Trava Baú 2
[96](#evento-de-ativação-da-liberação-da-trava-baú-2)

9.16.19 Evento de Desativação da Liberação da Trava Baú 2
[96](#evento-de-desativação-da-liberação-da-trava-baú-2)

9.16.20 Evento de Ativação da Liberação da Trava Baú 3
[96](#evento-de-ativação-da-liberação-da-trava-baú-3)

9.16.21 Evento de Desativação da Liberação da Trava Baú 3
[96](#evento-de-desativação-da-liberação-da-trava-baú-3)

9.16.22 Evento de Ativação da Liberação da Trava de Quinta Roda
[97](#evento-de-ativação-da-liberação-da-trava-de-quinta-roda)

9.16.23 Evento de Desativação da Liberação da Trava de Quinta Roda
[97](#evento-de-desativação-da-liberação-da-trava-de-quinta-roda)

9.16.24 Evento de Login de Motorista [97](#evento-de-login-de-motorista)

9.16.25 Evento de Logout de Motorista
[97](#evento-de-logout-de-motorista)

9.17 Eventos relacionados às regras de segurança
[98](#eventos-relacionados-às-regras-de-segurança)

9.17.1 Evento de entrada em ponto de controle
[98](#evento-de-entrada-em-ponto-de-controle-1)

9.17.2 Evento de saída de ponto de controle
[98](#evento-de-saída-de-ponto-de-controle-1)

9.17.3 Evento de entrada em cerca eletrônica
[98](#evento-de-entrada-em-cerca-eletrônica-1)

9.17.4 Evento de saída de cerca eletrônica
[98](#evento-de-saída-de-cerca-eletrônica-1)

9.17.5 Evento de entrada em grupo de pontos de controle
[98](#evento-de-entrada-em-grupo-de-pontos-de-controle)

9.17.6 Evento de saída de grupo de pontos de controle
[98](#evento-de-saída-de-grupo-de-pontos-de-controle)

9.17.7 Evento de entrada em grupo de cercas eletrônicas
[99](#evento-de-entrada-em-grupo-de-cercas-eletrônicas)

9.17.8 Evento de saída de grupo de cercas eletrônicas
[99](#evento-de-saída-de-grupo-de-cercas-eletrônicas)

9.17.9 Evento de regra de segurança [99](#evento-de-regra-de-segurança)

9.18 Eventos relacionados à disponibilização de sensores e atuadores
[100](#eventos-relacionados-à-disponibilização-de-sensores-e-atuadores)

9.18.1 Evento de disponibilização de sensor analógico
[100](#evento-de-disponibilização-de-sensor-analógico)

9.18.2 Evento de indisponibilização de sensor analógico
[100](#evento-de-indisponibilização-de-sensor-analógico)

9.18.3 Evento de disponibilização de sensor digital
[100](#evento-de-disponibilização-de-sensor-digital)

9.18.4 Evento de indisponibilização de sensor digital
[100](#evento-de-indisponibilização-de-sensor-digital)

9.18.5 Evento de disponibilização de atuador
[100](#evento-de-disponibilização-de-atuador)

9.18.6 Evento de indisponibilização de atuador
[101](#evento-de-indisponibilização-de-atuador)

9.19 Eventos relacionados à transferência de arquivos
[102](#eventos-relacionados-à-transferência-de-arquivos)

9.20 Eventos relacionados ao rastreador ISCA
[103](#eventos-relacionados-ao-rastreador-isca)

9.20.1 Evento de dispositivo ligado [103](#evento-de-dispositivo-ligado)

9.20.2 Evento de dispositivo desligado
[103](#evento-de-dispositivo-desligado)

9.20.3 Evento de auto-teste [103](#evento-de-auto-teste)

9.20.4 Evento de configuração local [103](#evento-de-configuração-local)

9.20.5 Evento de fonte externa conectada
[103](#evento-de-fonte-externa-conectada)

9.20.6 Evento de fonte externa desconectada
[104](#evento-de-fonte-externa-desconectada)

9.20.7 Evento de conexão USB [104](#evento-de-conexão-usb)

9.20.8 Evento de desconexão USB [104](#evento-de-desconexão-usb)

9.20.9 Evento de escuta aberta [104](#evento-de-escuta-aberta)

9.20.10 Evento de escuta fechada [104](#evento-de-escuta-fechada)

9.20.11 Evento de buzzer acionado [105](#evento-de-buzzer-acionado)

9.20.12 Evento de buzzer desacionado
[105](#evento-de-buzzer-desacionado)

9.20.13 Evento de nível baixo de bateria
[105](#evento-de-nível-baixo-de-bateria)

9.20.14 Evento de acoplamento de dispositivo (violação)
[105](#evento-de-acoplamento-de-dispositivo-violação)

9.20.15 Evento de desacoplamento de dispositivo (violação)
[105](#evento-de-desacoplamento-de-dispositivo-violação)

9.20.16 Evento de modo de emergência ativado
[106](#evento-de-modo-de-emergência-ativado)

9.20.17 Evento de modo de emergência desativado
[106](#evento-de-modo-de-emergência-desativado)

9.20.18 Evento de chamada recebida [106](#evento-de-chamada-recebida)

9.21 Eventos de transferência de arquivos por Http
[107](#eventos-de-transferência-de-arquivos-por-http)

9.21.1 Transferência Http Concluída [107](#transferência-http-concluída)

9.21.2 Erro na transferência Http [107](#erro-na-transferência-http)

9.21.3 Arquivos Http atualizados [107](#arquivos-http-atualizados)

9.21.4 Arquivo Http baixado [107](#arquivo-http-baixado)

9.21.5 Evento de sincronismo de arquivos HTTP do dispositivo
[108](#evento-de-sincronismo-de-arquivos-http-do-dispositivo)

9.21.6 Evento de dessincronismo de arquivos HTTP do dispositivo
[108](#evento-de-dessincronismo-de-arquivos-http-do-dispositivo)

9.22 Eventos de sequenciamento de macros
[108](#eventos-de-sequenciamento-de-macros)

9.22.1 Início Modo Violado [108](#início-modo-violado)

9.22.2 Fim Modo violado [108](#fim-modo-violado)

9.22.3 Mudança de Estado do Modo Controlado
[109](#mudança-de-estado-do-modo-controlado)

9.22.4 Macro Enviada [109](#macro-enviada)

10 Parâmetros [110](#parâmetros)

10.1 Tabela de parâmetros [110](#tabela-de-parâmetros)

10.2 Parâmetros relacionados ao envio de eventos de GSM
[139](#parâmetros-relacionados-ao-envio-de-eventos-de-gsm)

10.3 Parâmetros relacionados ao envio de eventos de GPS
[139](#parâmetros-relacionados-ao-envio-de-eventos-de-gps)

10.4 Parâmetros gerais [139](#parâmetros-gerais)

10.5 Parâmetros relacionados ao uso de dois SIM CARDs
[142](#parâmetros-relacionados-ao-uso-de-dois-sim-cards)

10.6 Parâmetros relacionados à antena satelital
[146](#parâmetros-relacionados-à-antena-satelital)

10.7 Parâmetros relacionados ao Horímetro
[150](#parâmetros-relacionados-ao-horímetro)

10.8 Parâmetros relacionados ao modo de segurança
[152](#parâmetros-relacionados-ao-modo-de-segurança)

10.9 Parâmetros relacionados ao rastreador ISCA
[153](#parâmetros-relacionados-ao-rastreador-isca)

10.10 Parâmetros relacionados ao uso dos sensores analógicos
[159](#parâmetros-relacionados-ao-uso-dos-sensores-analógicos)

10.11 Parâmetros relacionados ao uso dos sensores digitais
[161](#parâmetros-relacionados-ao-uso-dos-sensores-digitais)

10.12 Parâmetros relacionados ao uso dos atuadores
[162](#parâmetros-relacionados-ao-uso-dos-atuadores)

10.13 Parâmetros relacionados ao envio de informações adicionais
[163](#parâmetros-relacionados-ao-envio-de-informações-adicionais)

11 Lista de Variáveis [164](#lista-de-variáveis)

11.1 Tabela de Variáveis [166](#tabela-de-variáveis)

12 Variáveis CAN [177](#variáveis-can)

12.1 Descrição das variáveis CAN [180](#descrição-das-variáveis-can)

13 Comandos [220](#comandos)

14 Relatórios [224](#relatórios)

15 Apêndice A [231](#apêndice-a)

16 Apêndice B [232](#apêndice-b)

16.1 Códigos de Respostas [232](#códigos-de-respostas)

16.2 Tipo de Veículo [232](#tipo-de-veículo)

16.3 USO DOS COMANDOS PAN PELOS EQUIPAMENTOS RASTREADORES
[233](#uso-dos-comandos-pan-pelos-equipamentos-rastreadores)

17 APÊNDICE C: RESUMO DO PROCEDIMENTO DE DOWNLOAD REMOTO
[234](#apêndice-c-resumo-do-procedimento-de-download-remoto)

17.1 FORMATO DO ARQUIVO EXECUTÁVEL [235](#formato-do-arquivo-executável)

#  Histórico de Revisões

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 14%" />
<col style="width: 55%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>Revisão</strong></td>
<td style="text-align: center;"><strong>Data</strong></td>
<td style="text-align: center;"><strong>Comentários</strong></td>
<td style="text-align: center;"><strong>Autor(es)</strong></td>
</tr>
<tr>
<td style="text-align: center;">R1</td>
<td style="text-align: center;">04/Fev/2011</td>
<td style="text-align: center;">Emissão inicial.</td>
<td style="text-align: center;">Roberto Fragnito, Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.1</td>
<td style="text-align: center;">12/Dez/2011</td>
<td style="text-align: center;">Inclusão de nova definição de AI para
eventos de SIM CARD.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.2</td>
<td style="text-align: center;">14/Dez/2011</td>
<td style="text-align: center;"><p>Inclusão do parâmetro para
configuração da antena satelital.</p>
<p>Inclusão da informação adicional para envio de status dos
atuadores.</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.3</td>
<td style="text-align: center;">09/Jan/2012</td>
<td style="text-align: center;">Inclusão dos eventos relacionados aos
atuadores.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.4</td>
<td style="text-align: center;">06/Fev/2012</td>
<td style="text-align: center;"><p>Inclusão da informação adicional para
envio de hodômetro.</p>
<p>Inclusão do parâmetro para controle do envio de AIs.</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.5</td>
<td style="text-align: center;">08/Fev/2012</td>
<td style="text-align: center;">Revisão e inclusão de novos
eventos.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.6</td>
<td style="text-align: center;">13/Fev/2012</td>
<td style="text-align: center;"><p>Inclusão de parâmetros:</p>
<p>0x0024: Parâmetro para configuração do envio de eventos de GPS.</p>
<p>0x0086: Parâmetro para configuração do envio de eventos de SIM
CARD.</p>
<p>0x0300: Parâmetro para ativação dos sensores analógicos (1 a 31).</p>
<p>0x0400: Parâmetro para ativação dos sensores digitais (1 a 127).</p>
<p>0x0480: Parâmetro para ativação dos atuadores (1 a 31).</p>
<p>0x0481 a 0x049F: Parâmetros para configuração dos atuadores (1 a
31).</p>
<p>0x0501 a 0x05FF: Parâmetros para configuração do envio de AI (1 a
255).</p>
<p>Adição de dois novos tipos de bloqueio:</p>
<p>6: Aviso + Progressivo com limite de velocidade.</p>
<p>7: Aviso + Progressivo sem limite de velocidade.</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.7</td>
<td style="text-align: center;">15/Mar/12</td>
<td style="text-align: center;"><p>Exclusão do campo referente à
quantidade de mensagens de todos os eventos relacionados à antena
satelital.</p>
<p>Alteração do nome do evento 0x0064 de “Evento de aviso de fim dos
créditos” para “Evento de alerta de poucos créditos”.</p>
<p>Criação do evento 0x0066: “Evento de alerta de fim dos créditos”.</p>
<p>Alteração do texto do campo 1 do parâmetro 0x0088.</p>
<p>Alteração da unidade das taxas de monitoração do parâmetro 0x0088 (de
segundos para minutos).</p>
<p>Inclusão dos parâmetros de 0x0089 a 0x008F.</p>
<p>Inclusão dos parâmetros de 0x00A0 a 0x00A3.</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.8</td>
<td style="text-align: center;">26/Mar/2012</td>
<td style="text-align: center;"><p>Alteração de todos os textos
referentes a modo carga ou modo operacional de carga para modo de
segurança.</p>
<p>Alteração da unidade do tempo de PING do parâmetro 0x0085 (de
segundos para minutos).</p>
<p>Alteração da faixa de parâmetros de 0x0301 a 0x031F para 0x0321 a
0x033F.</p>
<p>Inclusão da faixa de parâmetros de 0x0301 a 0x031F (Parâmetros para
ativação individual dos sensores analógicos).</p>
<p>Alteração da quantidade de sensores digitais suportados pelo
parâmetro 0x0400 de 127 para 95.</p>
<p>Alteração da faixa de parâmetros de 0x0401 a 0x047F para 0x0461 a
0x04BF e da quantidade sensores digitais suportados de 127 para 95.</p>
<p>Inclusão da faixa de parâmetros de 0x0401 a 0x045F (Parâmetros para
ativação individual dos sensores digitais).</p>
<p>Alteração do parâmetro 0x0480 para 0x04C0.</p>
<p>Alteração da faixa de parâmetros de 0x0481 a 0x049F para 0x04E1 a
0x04FF.</p>
<p>Inclusão da faixa de parâmetros de 0x04C1 a 0x04DF (Parâmetros para
ativação individual dos atuadores).</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.9</td>
<td style="text-align: center;">27/Mar/2012</td>
<td style="text-align: center;">Inclusão de mensagens OPEN para
comunicação com dispositivos via barramento local.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.10</td>
<td style="text-align: center;">28/Mar/2012</td>
<td style="text-align: center;"><p>Alteração dos termos “ativação”
(utilizado nos sensores e atuadores) para “disponibilização”.</p>
<p>Alteração da lógica dos parâmetros 0x0301 a 0x031F, 0x0401 a 0x047F e
0x0481 a 0x049F.</p>
<p>Excluído o campo DTG da mensagem TST (0x24).</p>
<p>Alteração do número de bytes do campo “ID” da mensagem CLD (0x26) de
1 para 2.</p>
<p>Inclusão de dois novos tipos de comando para bloqueio e desbloqueio
do veículo por acessórios (teclado).</p>
<p>Alteração do número de bytes do campo “ID” da mensagem SAT (0x28) de
1 para 2.</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.11</td>
<td style="text-align: center;">02/Abr/2012</td>
<td style="text-align: center;"><p>Correção da numeração dos tipos de
mensagem de “Mensagem para troca de informações via link satelital”.</p>
<p>Adição de um segundo campo para parâmetro na mensagem de comando para
dispositivos locais e na mensagem para troca de informações via link
satelital.</p>
<p>Adição dos eventos de início de uso de créditos no período e de
inserção de créditos.</p>
<p>Adição de um segundo campo de dados na mensagem de comando OPEN, além
de uma faixa exclusiva para comandos de teclado na tabela de
comandos.</p>
<p>Adição de eventos relacionados às regras de segurança (Pontos de
controle e cercas eletrônicas).</p>
<p>Adição de eventos relacionados à disponibilização de sensores e
atuadores.</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.12</td>
<td style="text-align: center;">04/Abr/2012</td>
<td style="text-align: center;"><p>Adição do evento de configuração de
hodômetro.</p>
<p>Adição dos eventos de senha de coação, ativação/desativação de
liberação de atuador.</p>
<p>Adição do evento de regra de segurança.</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.13</td>
<td style="text-align: center;">27/Abr/2012</td>
<td style="text-align: center;"><p>Adição de novas mensagens OPEN para
transferência de arquivos (0x2A, 0x2B, 0x2C e 0x2D).</p>
<p>Adição dos eventos de bloqueio e desbloqueio de veículo (0x0043 e
0x0044).</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.14</td>
<td style="text-align: center;">11/Mai/2012</td>
<td style="text-align: center;">Correção da mensagem OPEN CFT
(0x2D).</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.15</td>
<td style="text-align: center;">27/Jul/2012</td>
<td style="text-align: center;">Adição de nova informação adicional
(0x0C) contendo estrutura com identificadores da estação rádio base e
parâmetros para estimativa da distância entre a base e o dispositivo
móvel.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.16</td>
<td style="text-align: center;">02/Out/2012</td>
<td style="text-align: center;">Adição dos eventos de transferência de
arquivos (0x0101 a 0x01FF).</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.17</td>
<td style="text-align: center;">20/Mar/2013</td>
<td style="text-align: center;">Adição de razões de envio para AIs.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.18</td>
<td style="text-align: center;">26/Mar/2013</td>
<td style="text-align: center;"><p>Adição das mensagens para rastreador
tipo ISCA.</p>
<p>Adição do parâmetro para modo de operação (GPRS/SMS) (0x007B).</p>
<p>Adição do parâmetro para buffer LIFO/FIFO (0x007C).</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.19</td>
<td style="text-align: center;">26/Jun/2013</td>
<td style="text-align: center;"><p>Adição do parâmetro para configuração
do tempo para entrada em modo sleep (0x007D).</p>
<p>Adição do parâmetro para habilitação da escuta (0x00F5).</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.20</td>
<td style="text-align: center;">05/Ago/2013</td>
<td style="text-align: center;">Adição dos parâmetros para configuração
do tempo para entrada em modo de emergência (0x00F6 a 0x00FA).</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.21</td>
<td style="text-align: center;">24/Out/2013</td>
<td style="text-align: center;">Alteração do campo 4 do parâmetro 0x00E9
de horas para minutos.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.22</td>
<td style="text-align: center;">07/Jan/2014</td>
<td style="text-align: center;">Adição do evento de chamada recebida
(0x0211).</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.23</td>
<td style="text-align: center;">15/Jan/2014</td>
<td style="text-align: center;">Complemento do evento de chamada
recebida.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.24</td>
<td style="text-align: center;">16/Abr/2014</td>
<td style="text-align: center;">Adição do AI para envio da data e hora
da última ERB válida.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.25</td>
<td style="text-align: center;">17/Abr/2014</td>
<td style="text-align: center;"><p>Adição de novos eventos de liberação
de atuador para Trava Baú 3 e Trava de Quinta Roda.</p>
<p>Adição de comandos para PND para permissão de liberação de
atuador.</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.26</td>
<td style="text-align: center;">26/Mai/2014</td>
<td style="text-align: center;">Adição do AI com informação do GPS.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.27</td>
<td style="text-align: center;">20/Out/2014</td>
<td style="text-align: center;"><p>Adição do AI para envio da velocidade
do veículo.</p>
<p>Adição do AI para envio do tempo estimado para o próximo
posicionamento.</p>
<p>Adição dos eventos de velocidade CAN.</p>
<p>Adição do novo evento de limite de velocidade ultrapassado com maior
precisão (0x003D).</p>
<p>Adição do parâmetro para configuração apenas do valor do limite de
velocidade do evento 0x0009.</p>
<p>Adição do parâmetro para configuração completa do novo evento de
limite de velocidade ultrapassado com maior precisão.</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.28</td>
<td style="text-align: center;">21/Out/2014</td>
<td style="text-align: center;">Adição do evento para sinalização do
recebimento de uma configuração de parâmetro.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R1.29</td>
<td style="text-align: center;">30/Mar/2015</td>
<td style="text-align: center;">Modificado comando Requisição de posição
(0x0005) para envio de posição por SMS, 900Mhz e Satelital.</td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2</td>
<td style="text-align: center;">08/Mai/2015</td>
<td style="text-align: center;"><p>Reorganização do documento, reunindo
a parte nova com a descrição que estava no Wiki.</p>
<p>Inclusão dos parâmetros CAN na tabela de parâmetros.</p></td>
<td style="text-align: center;">Roberto Fragnito, Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R2.1</td>
<td style="text-align: center;">27/Mai/2015</td>
<td style="text-align: center;">Complementação da tabela de informações
adicionais.</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R2.2</td>
<td style="text-align: center;">03/Jun/2015</td>
<td style="text-align: center;"><p>Complementação da tabela de
eventos</p>
<p>Complementação da tabela de parâmetros</p>
<p>Adicionado parâmetros da aplicação Horímeto</p>
<p>Adicionado eventos da aplicação Horímetro</p>
<p>Adicionado parâmetro de habilitação do RF433Mhz</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.3</td>
<td style="text-align: center;">08/Jun/2015</td>
<td style="text-align: center;"><p>Adicionado Horímetro como uma
informação adicional</p>
<p>Adicionado Horímetro como um parâmetro (originalmente seria uma
variável)</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.4</td>
<td style="text-align: center;">18/Ago/2015</td>
<td style="text-align: center;">Correção da tabela de eventos (0x0021 a
0x002B)</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R2.5</td>
<td style="text-align: center;">30/Nov/2015</td>
<td style="text-align: center;"><p>Inclusão das versões de protocolo
OPEN V4 e V5</p>
<p>Inclusão das mensagens para leitura de dados CAN via protocolo SAE
J1939</p>
<p>Adequação das mensagens de leitura e resposta de variáveis</p>
<p>Inclusão do parâmetro para alteração do protocolo de comunicação
GPRS/SMS</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R2.6</td>
<td style="text-align: center;">31/Mar/2016</td>
<td style="text-align: center;"><p>Correção das tabelas de identificação
de equipamentos e de tipo de protocolo</p>
<p>Correção do tamanho máximo das variáveis na mensagem “Lista de
Variáveis (VRL – 1Dh)”: de 1 Byte para 2 Bytes</p>
<p>Inclusão dos eventos de teclado 0x009D e 0x009E</p>
<p>Inclusão da variável 0x001E (Identificação do motorista)</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R2.7</td>
<td style="text-align: center;">23/Nov/2021</td>
<td style="text-align: center;"><p>Inclusão das Mensagens de
transferência de arquivos via Http na seção de mesmo nome.</p>
<p>Inclusão dos eventos relacionados a transferência de arquivos via
Http(0x0212, 0x0213, 0x0214 e 0x0215)</p>
<p>Inclusão do AI de Status da transferência Http(0x14)</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.8</td>
<td style="text-align: center;">06/Dec/2021</td>
<td style="text-align: center;"><p>Inclusão das Mensagens de
sequenciamento de macro</p>
<p>Inclusão dos eventos relacionados ao sequenciamento de macros
(0x0216, 0x0217 e 0x0218)</p>
<p>Inclusão dos comandos relacionados ao sequenciamento de macros
(0x100E e 0x100F)</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.9</td>
<td style="text-align: center;">23/Dec/2021</td>
<td style="text-align: center;">Aumento do tamanho de IDD e FPR para
10bytes</td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.10</td>
<td style="text-align: center;">07/Jan/2022</td>
<td style="text-align: center;">Corrigida descrição do evento
0x0214(Erro na transferência Http)</td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.11</td>
<td style="text-align: center;">14/Jan/2022</td>
<td style="text-align: center;">Adicionado o campo TEC ao evento
0x0214(Erro na transferência Http)</td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.12</td>
<td style="text-align: center;">31/01/2022</td>
<td style="text-align: center;"><p>Modificado os índices dos eventos
relacionados a sequenciamento de macros e do evento Arquivo Http
Baixado</p>
<p>Adicionado os parâmetros 0x0097 e 0x0098</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.13</td>
<td style="text-align: center;">23/02/2022</td>
<td style="text-align: center;"><p>Alterado o Id de Novo arquivo
disponível para download</p>
<p>Removido o campo ORD e alterado nome da mensagem 0x36</p>
<p>Adicionada tabela de tipos de mensagens</p>
<p>Modificado evento de Estado do Modo Controlado Alterado</p>
<p>Acrescentado ao protocolo a mensagem Evento com informação
adicional(0x30) já utilizada em outros produtos</p>
<p>Criado os eventos de macro enviada(0x021A) e Sincronismo de arquivos
Http do dispositivo(0x021B)</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.14</td>
<td style="text-align: center;">24/02/2022</td>
<td style="text-align: center;"><p>Corrigida Id do evento de Estado do
Modo Controlado Alterado</p>
<p>Evento de sincronismo(0x021B) separado em 2 eventos, criando o evento
de dessincronismo(0x021C)</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.15</td>
<td style="text-align: center;">09/03/2022</td>
<td style="text-align: center;"><p>Corrigida descrição da mensagem de
Novo arquivo disponível para download</p>
<p>Modificada mensagem SFC(35h)</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.16</td>
<td style="text-align: center;">19/03/2022</td>
<td style="text-align: center;">Atualizado o campo status (STS) com os
flags de modo emergência e ignição por tensão em uso</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R2.17</td>
<td style="text-align: center;">08/04/2022</td>
<td style="text-align: center;"><p>Adicionados comandos relacionados ao
modo controlado</p>
<p>Modificada as mensagens de senha e contrassenha do modo controlado
para incluir o tamanho da senha/contrassenha</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.18</td>
<td style="text-align: center;">18/04/2022</td>
<td style="text-align: center;"><p>Adicionada resposta à mensagem de
requisição de Macro</p>
<p>Modificado o evento 0x219 para Aviso de Modo Violado</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.19</td>
<td style="text-align: center;">20/04/2022</td>
<td style="text-align: center;"><p>Adicionado AI de estado de macro</p>
<p>Comandos de Reinício e Desfazer do modo controlado modificados.</p>
<p>Parâmetro para habilitação de eventos de
geolocalização(0x03FF)</p></td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.20</td>
<td style="text-align: center;">26/04/2022</td>
<td style="text-align: center;">Modificado AI de estado de macro para
conter estado anterior</td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.21</td>
<td style="text-align: center;">03/05/2022</td>
<td style="text-align: center;">Removido evento de Aviso de Modo
Violado(0x0219) e removido Parâmetro Tempo de Alarme(0x0098)</td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.22</td>
<td style="text-align: center;">02/06/2022</td>
<td style="text-align: center;">Adicionado evento 0x0219 de Mudança de
Estado do Modo Controlado</td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
<tr>
<td style="text-align: center;">R2.23</td>
<td style="text-align: center;">18/09/2022</td>
<td style="text-align: center;">Adição de protocolos à tabela “Variável
CAN: Tipo do Protocolo CAN”</td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R2.24</td>
<td style="text-align: center;">13/08/2024</td>
<td style="text-align: center;"><p>Inserido o evento 0x0212 (Mensagem
recebida na porta serial)</p>
<p>Inseridos os eventos de 0x0220 a 0x0224 (relativos a botão e sensor
de luminosidade)</p>
<p>Inserido o parâmetro 0x0600 (Configuração de veículo)</p>
<p>Inseridos os parâmetros (0x00A5 a 0x00A7 e 0x00DD a 0x00DF e 0x00FC a
0x00FF)</p>
<p>Inseridos novos comandos com os IDs 0x0038 e 0x0039 e corrigidos os
respectivos parâmetros para os novos IDs 0x0048 e 0x0049</p>
<p>Adicionado novo tipo de requisição ao comando 0x0005</p></td>
<td style="text-align: center;">Thiago Nascimento</td>
</tr>
<tr>
<td style="text-align: center;">R2.25</td>
<td style="text-align: center;">05/03/2025</td>
<td style="text-align: center;">Adicionado nova variável/AI CAN (0x1029
/ 0xA9) de carga de bateria de veículo elétrico</td>
<td style="text-align: center;">Gustavo Gonzalez</td>
</tr>
</tbody>
</table>

# Glossário

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<tbody>
<tr>
<td colspan="2"
style="text-align: center;"><strong>GLOSSÁRIO</strong></td>
</tr>
<tr>
<td style="text-align: center;">APN</td>
<td style="text-align: left;">Access Point Name</td>
</tr>
<tr>
<td style="text-align: center;">DTLS</td>
<td style="text-align: left;">Datagram Transport Layer Security</td>
</tr>
<tr>
<td style="text-align: center;">GPRS</td>
<td style="text-align: left;">General Packet Radio Service</td>
</tr>
<tr>
<td style="text-align: center;">GSM</td>
<td style="text-align: left;">Global System for Mobile
Communications</td>
</tr>
<tr>
<td style="text-align: center;">IP</td>
<td style="text-align: left;">Internet Protocol</td>
</tr>
<tr>
<td style="text-align: center;">OSI</td>
<td style="text-align: left;">Open Systems Interconnection</td>
</tr>
<tr>
<td style="text-align: center;">PAN</td>
<td style="text-align: left;">Positron Area Network</td>
</tr>
<tr>
<td style="text-align: center;">PPP</td>
<td style="text-align: left;">Point-to-Point Protocol</td>
</tr>
<tr>
<td style="text-align: center;">UDP</td>
<td style="text-align: left;">User Datagram Protocol</td>
</tr>
</tbody>
</table>

# Referências

1.  PAN protocol document.

2.  RDS protocol.

# Introdução

Este documento descreve o protocolo de rastreamento PST OPEN IAM,
utilizado no sistema de rastreamento que envolve equipamentos de
rastreamento, acessórios e servidores, para aplicações Aftermarket
(IAM). O protocolo PST OPEN IAM possui as seguintes características:

- Segurança: as comunicações são protegidas pelo uso de criptografia e
  algoritmos de autenticação.

- Alto desempenho: as mensagens são otimizadas, permitindo uma rápida
  transmissão e recepção. Além disso, não compromete a largura de banda,
  reduzindo custos, espaço de armazenamento e performance computacional.

- Expansível: novas mensagens, parâmetros e variáveis podem ser
  facilmente criados e adicionados sem grandes mudanças, mantendo a
  compatibilidade com equipamentos não atualizados.

- Atualização remota: o protocolo permite uma atualização de software
  OTA (*over-the-air*) rápida e segura dos equipamentos que estão em
  campo. Esta atualização é totalmente imperceptível para o usuário e
  pode ser feita sem afetar a operação normal dos equipamentos em campo.

- Comunicação baseada no protocolo UDP, com mecanismo de confirmação
  (acknowledge) implementado na camada de aplicação.

A partir de agora, neste documento, para fins de concisão o protocolo
PST OPEN IAM será chamado simplesmente de protocolo OPEN.

## Pilha das Camadas dos Protocolos de Comunicação

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 42%" />
</colgroup>
<tbody>
<tr>
<td colspan="2" style="text-align: center;"><strong>PILHA DAS
COMUNICAÇÕES </strong></td>
</tr>
<tr>
<td style="text-align: center;">Camada de aplicação</td>
<td style="text-align: center;">OPEN</td>
</tr>
<tr>
<td style="text-align: center;">Camadas de rede/ligação de dados</td>
<td style="text-align: center;">OPEN IAM</td>
</tr>
<tr>
<td style="text-align: center;">Camada de tunelamento</td>
<td style="text-align: center;">UDP / IP V4 / GPRS – PPP</td>
</tr>
<tr>
<td style="text-align: center;">Camada física</td>
<td style="text-align: center;">GSM ou RS232</td>
</tr>
</tbody>
</table>

## Camada de Tunelamento

Camada de tunelamento é um conceito adaptado, não previsto no modelo OSI
de 7 camadas. Neste caso, o tunelamento se refere à ação de enviar
mensagens OPEN através de uma infraestrutura de comunicação existente: o
canal GPRS/GSM. Este canal possui sua própria estrutura, implementando
muitas das camadas previstas no modelo OSI. No entanto, este canal é
utilizado somente como um túnel para a troca de mensagens entre um
equipamento GSM/GPRS e um servidor central, não refletindo as
características de endereçamento e roteamento do protocolo OPEN. Este é
o motivo pelo qual o conceito de tunelamento foi aqui introduzido.

## Camadas de Rede / Ligação de Dados

As camadas de rede e ligação de dados são utilizadas para endereçar e
rotear mensagens OPEN entre diferentes equipamentos e barramentos em que
o protocolo OPEN pode ser usado.

## Fluxo de Transmissões do Equipamento para o Servidor

### Modos de Operação

**Modo de Rastreamento**

Durante o modo de rastreamento, o equipamento envia uma mensagem de
posição (MTP = 01h ou MTP = 04h) a cada intervalo TXO. O valor padrão de
TXO é 1 minuto. Se o dispositivo está fora de uma área de cobertura GSM,
ele armazena as posições em um buffer interno. Assim que o dispositivo
entra em uma área de cobertura GSM, todas as posições armazenadas no
buffer são enviadas para o servidor.

**Modo Sleep**

Quando a ignição está desligada, o equipamento entra no modo de sleep,
para economizar energia da bateria. No modo de sleep, o GPS e o GSM
podem ser desligados. No entanto, para tentar manter uma informação de
satélites válida no chip set GPS, o módulo de GPS é ligado a cada
intervalo TGP. O GPS é mantido ligado até que uma posição válida é
recebida, mas limitado a um valor máximo de XGP. O valor padrão de TGP é
3 horas, e o valor padrão de XGP é 4 minutos. Além disso, a cada
intervalo TXF o equipamento envia uma posição (MTP = 01h ou MTP = 04h)
se ele estiver dentro de uma área de cobertura GSM. Se o dispositivo
está fora de uma área de cobertura GSM, esta posição é armazenada no
buffer e será enviada assim que o GSM estiver disponível. O valor padrão
de TXF é 3 horas. Além do GPS, o módulo GSM pode ser ligado durante o
modo de sleep. O GSM é controlado pelos parâmetros XGS e TGS. XGS define
o tempo em que o GSM permanece ligado, enquanto TGS é o período do ciclo
(ou seja, o módulo GSM é ligado por um intervalo XGS a cada período
TGS). Se XGS for igual a zero, o GSM nunca é ligado enquanto a ignição
está desligada. Se XGS é maior ou igual a TGS, o GSM nunca é desligado
enquanto a ignição está desligada. Além disso, se o equipamento for
retirado do modo sleep por acionamento do sensor de movimento, ele irá
para o modo de rastreamento por um intervalo SMO. O valor padrão de SMO
é 5 minutos.

**Acknowledge**

Na comunicação do equipamento com o servidor usando UDP, é necessário
implementar um mecanismo de acknowledge na camada de aplicação. Este
mecanismo é simples: cada mensagem que é enviada de um lado deve ser
respondida com uma mensagem de ACK (MTP = 00h) ou NACK (MTP = 0Bh) pelo
outro lado. A mensagem transmitida tem um número de seqüência (4 bytes)
que deve fazer parte da mensagem de resposta (ACK ou NACK). O lado que
está enviando a mensagem não deve enviar outra mensagem para o receptor
enquanto não receber a resposta. Além disso, o transmissor deve
implementar um mecanismo de reenvio. Se o transmissor não recebe o
acknowledge de uma mensagem após um determinado tempo (UDT, time-out do
UDP), a mensagem deve ser enviada novamente, até um número máximo de
tentativas (parâmetro RTY). Os valores padrões são 30 segundos para UDT
e 5 tentativas para RTY. Após o número de tentativas expirar, o
transmissor deve considerar que o link de transmissão não está
funcionando e tomar alguma ação apropriada (por exemplo, o equipamento
pode tentar fechar a sessão GPRS e conectar-se ao servidor secundário).
Após tentar os dois servidores sem sucesso, o transmissor deve executar
um auto-reset e voltar a tentar conectar-se ao servidor primário.

## Estrutura da Mensagem

### OPEN V2 e OPEN V3

A estrutura da mensagem do protocolo OPEN nas versões 2 e 3 é
apresentada na *Figura 1*.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th colspan="10" style="text-align: center;"><strong>Estrutura da
Mensagem</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Campo</strong></td>
<td style="text-align: center;"><strong>IDN</strong></td>
<td style="text-align: center;"><strong>VER</strong></td>
<td style="text-align: center;"><strong>CYV</strong></td>
<td style="text-align: center;"><strong>ADC</strong></td>
<td style="text-align: center;"><strong>SDT</strong></td>
<td style="text-align: center;"><strong>SID</strong></td>
<td style="text-align: center;"><strong>DDT</strong></td>
<td style="text-align: center;"><strong>DID</strong></td>
<td style="text-align: center;"><strong>NRD</strong></td>
</tr>
<tr>
<td><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1<em>(o)</em></td>
<td style="text-align: center;">4<em>(o)</em></td>
<td style="text-align: center;">1<em>(o)</em></td>
<td style="text-align: center;">4<em>(o)</em></td>
<td style="text-align: center;">1<em>(o)</em></td>
</tr>
</tbody>
</table>

<table>
<caption><p><em>Figura 1 – Estrutura da mensagem do protocolo OPEN (V2 e
V3)</em></p></caption>
<colgroup>
<col style="width: 19%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr>
<th><strong>Campo</strong></th>
<th style="text-align: center;"><strong>RDT1</strong></th>
<th style="text-align: center;"><strong>RID1</strong></th>
<th style="text-align: center;"><strong>...</strong></th>
<th style="text-align: center;"><strong>RDTn</strong></th>
<th style="text-align: center;"><strong>RIDn</strong></th>
<th style="text-align: center;"><strong>Mensagem de
aplicação</strong></th>
<th style="text-align: center;"><strong>CRC</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">1<em>(o)</em></td>
<td style="text-align: center;">4<em>(o)</em></td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">1<em>(o)</em></td>
<td style="text-align: center;">4<em>(o)</em></td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

Os campos da mensagem são os seguintes (***observação***: *(o)*
significa campo opcional):

- **IDN**: número de identificação do equipamento (**Id**entification
  **N**umber). É um número que identifica de forma única o equipamento
  dentro do sistema (nenhum equipamento pode ter um **IDN** já usado por
  outro equipamento).

- **VER**: versão do protocolo (Protocol **VER**sion). Permite o
  reconhecimento da versão em uso do protocolo (a estrutura da mensagem
  pode mudar conforme a versão do protocolo). O valor atual deste campo
  pode ser 0x02 ou 0x03 (ou seja, a versão de protocolo em uso é a
  versão 2 ou a versão 3), dependendo da

- **CYV**: valor de criptografia (**C**r**Y**ptographic **V**alue). No
  contexto do algoritmo de criptografia RC4, é utilizado para definir o
  valor inicial da posição dos vetores de estado (normalmente
  referenciado como “S”) e de expansão da chave de criptografia. A
  aleatoriedade deste valor garante um reforço na segurança do algoritmo
  RC4, já que a permutação inicial do vetor de estado depende
  diretamente deste valor.

- **ADC**: campo de controle de endereçamento (**Ad**dressing
  **C**ontrol). É utilizado para definir quais dos próximos campos
  (**SDT**, **SID**, **DDT**, **DID**, **NRD**, **RDT** e **RID**s)
  estarão presentes na mensagem, uma vez que eles são opcionais.

- **SDT**: campo do tipo de equipamento de origem (**S**ource **D**evice
  **T**ype). Identifica o tipo de equipamento que gerou a mensagem.

- **SID**: campo do número de identificação do equipamento de origem
  (Source Device Identification Number). É um número de 4 bytes que
  identifica o equipamento que originou a mensagem (equipamento que
  criou e que pela primeira vez transmitiu a mensagem).

- **DDT**: campo do tipo de equipamento de destino (Destination Device
  Type). Identifica o tipo de equipamento de destino da mensagem.

- **DID**: campo do número de identificação do equipamento de destino
  (Destination Device Identification Number). É um número de 4 bytes que
  identifica o equipamento de destino da mensagem.

- **NRD**: número de equipamentos retransmissores (Number of
  Retransmitting Devices). Informa quantos equipamentos estão
  identificados na mensagem (por exemplo, se NRD = 3, há 3 campos RID na
  mensagem) Se a identificação do retransmissor está sendo exigida (esta
  exigência é definida pelo campo ADC), então os equipamentos que estão
  retransmitindo a mensagem devem inserir seus números de identificação
  no próximo campo RID disponível na mensagem e incrementar o valor do
  campo NRD.

- **RDT**: campo do tipo de equipamento retransmissor (Retransmitting
  Device Type). Identifica o tipo do equipamento que retransmitiu a
  mensagem.

- **RID**: campo do número de identificação do equipamento retransmissor
  (Retransmitting Device Identification Number). É um número de 4 bytes
  que identifica o equipamento que retransmitiu a mensagem durante o
  caminho (se a identificação dos retransmissores foi utilizada ao menos
  uma vez durante o caminho).

***Exemplo***: Imagine um equipamento receptor responsável por receber
mensagens vindas de vários sensores instalados em um determinado
ambiente. Tal equipamento pode gerar a mensagem para um servidor central
com os seguintes campos:

- ADC = 11100100 (0xE4), significando: SDT, DDT e SID existem, DID não
  existe, RDT não existe, RDI existe, outros retransmissores não
  precisam incluir seus tipos e ou números de identificação na mensagem.

- SDT = tipo do equipamento: sensor.

- DDT = tipo do equipamento: servidor.

- SID = número de identificação do sensor (cada sensor possui um número
  de identificação).

- DID = não necessário, pois o servidor (destino) não possui um número
  de identificação.

- NRD = 1.

- RDT = não transmitido.

- RDI = número de identificação do equipamento receptor.

As descrições mais detalhadas de todos estes campos encontram-se na
seção *D.* O algoritmo de criptografia utilizado é o RC4, aplicado
apenas na parte da camada de aplicação da mensagem. O CRC deve ser
calculado sobre toda a mensagem.

### OPEN V4

A estrutura da mensagem do protocolo OPEN na versão 4 é apresentada na
*Figura 1*2.

<table style="width:100%;">
<colgroup>
<col style="width: 22%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th colspan="9" style="text-align: center;"><strong>Estrutura da
Mensagem</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Campo</strong></td>
<td style="text-align: center;"><strong>IDN</strong></td>
<td style="text-align: center;"><strong>VER</strong></td>
<td style="text-align: center;"><strong>CYV*</strong></td>
<td style="text-align: center;"><strong>ADC</strong></td>
<td style="text-align: center;"><strong>SDT</strong></td>
<td style="text-align: center;"><strong>SID</strong></td>
<td style="text-align: center;"><strong>DDT</strong></td>
<td style="text-align: center;"><strong>DID</strong></td>
</tr>
<tr>
<td><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1<em>(o)</em></td>
<td style="text-align: center;">4<em>(o)</em></td>
<td style="text-align: center;">1<em>(o)</em></td>
<td style="text-align: center;">4<em>(o)</em></td>
</tr>
</tbody>
</table>

<table>
<caption><p><em>Figura 2 – Estrutura da mensagem do protocolo OPEN
V4</em></p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 68%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th><strong>Campo</strong></th>
<th style="text-align: center;"><strong>Mensagem de
aplicação</strong></th>
<th style="text-align: center;"><strong>CRC</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

O campo **VER** deve trazer o valor **0x04**. O significado dos campos é
exatamente o mesmo daqueles de mesmo nome descritos no OPEN V2 e V3. No
entanto, há uma pequena mudança em relação ao campo **CYV**, cujo valor
real deve ser obtido por meio da inversão de seus 4 bits mais
significativos com os 4 bits menos significativos. ***Ex***: **CYV\* =
0x6A =\> CYV = 0xA6**.

Os campos para equipamentos retransmissores deixam de existir. O
algoritmo de criptografia utilizado é o RC4, aplicado apenas na parte da
camada de aplicação da mensagem. O CRC deve ser calculado sobre toda a
mensagem.

### OPEN V5

A estrutura da mensagem do protocolo OPEN na versão 5 é apresentada na
Figura *1*3.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr>
<th colspan="11" style="text-align: center;"><strong>Estrutura da
Mensagem</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Campo</strong></td>
<td style="text-align: center;"><strong>IDN</strong></td>
<td style="text-align: center;"><strong>VER</strong></td>
<td style="text-align: center;"><strong>CYV**</strong></td>
<td style="text-align: center;"><strong>CIN</strong></td>
<td style="text-align: center;"><strong>CSI</strong></td>
<td style="text-align: center;"><strong>ADC</strong></td>
<td style="text-align: center;"><strong>SDT</strong></td>
<td style="text-align: center;"><strong>SID</strong></td>
<td style="text-align: center;"><strong>DDT</strong></td>
<td style="text-align: center;"><strong>DID</strong></td>
</tr>
<tr>
<td><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1<em>(o)</em></td>
<td style="text-align: center;">4<em>(o)</em></td>
<td style="text-align: center;">1<em>(o)</em></td>
<td style="text-align: center;">4<em>(o)</em></td>
</tr>
</tbody>
</table>

<table>
<caption><p><em>Figura 3 – Estrutura da mensagem do protocolo OPEN
V5</em></p></caption>
<colgroup>
<col style="width: 22%" />
<col style="width: 58%" />
<col style="width: 11%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr>
<th><strong>Campo</strong></th>
<th style="text-align: center;"><strong>Mensagem de
aplicação</strong></th>
<th style="text-align: center;"><strong>CRCapp</strong></th>
<th style="text-align: center;"><strong>CRC</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

O campo **VER** deve trazer o valor **0x05.** O valor real de **CYV**
deve ser obtido por meio do complemento de 2 do valor apresentado na
mensagem. ***Ex***: **CYV\*\* = 0x6A =\> CYV = 0x96**.

O significado dos demais campos é exatamente o mesmo daqueles de mesmo
nome descritos no OPEN V2 e V3. No entanto, surgem dois novos campos
(**CIN** e **CSI**) que devem ser utilizados, respectivamente, para
sinalização de um índice e de um sub-índice referente à chave de
criptografia utilizada. Em termos práticos, este recurso possibilita a
utilização de chaves de criptografia exclusivas por dispositivo ou grupo
de dispositivos, permitindo ao servidor uma rápida identificação da
chave relacionada à mensagem recebida. Do ponto de vista do dispositivo,
mensagens originadas no servidor e destinadas ao próprio dispositivo
deverão ser descartadas em caso de incompatibilidade entre chave de
criptografia, índice e sub-índice presentes na mensagem e as informações
contidas na memória do mesmo.

Os campos para equipamentos retransmissores, a exemplo do OPEN V4,
também não existem. O algoritmo de criptografia utilizado é o RC4,
aplicado sobre a camada de aplicação da mensagem e o respectivo CRC. Uma
vez feita a encriptação do conjunto “Mensagem de aplicação + CRCapp”, o
CRC da mensagem OPEN V5 deve ser calculado sobre toda a mensagem.

## Criptografia

O algoritmo de criptografia utilizado nas diferentes versões do
protocolo OPEN (V2, V3, V4 e V5) é o RC4. Em cada versão, deve ser
considerado o byte presente no campo “CYV” como elemento determinante da
posição inicial dentro do vetor de estados que dará início ao ciclo de
permutações. Não há regras para a escolha do valor deste campo, sendo
responsabilidade apenas do criador da mensagem.

A chave de criptografia a ser utilizada dependerá de cada versão de
protocolo, sendo possível haver apenas uma por versão ou várias. Por
questões de segurança, as chaves de criptografia não são apresentadas
neste documento.

### Algoritmo de criptografia RC4

RC4 is a stream cipher designed in 1987 by Ron Rivest for RSA Security.
It is a variable keysize stream cipher with byte-oriented operations.
The algorithm is based on the use of a random permutation. Eight to
sixteen machine operations are required per output byte, and the cipher
can be expected to run very quickly in software. RC4 was kept as a trade
secret by RSA Security. In September 1994, the RC4 algorithm was
anonymously posted on the Internet on the Cypherpunks anonymous
remailers list.

The RC4 algorithm is remarkably simply and quite easy to explain. A
variable-length key of from 1 to 256 bytes (8 to 2048 bits) is used to
initialize a 256-byte state vector S, with elements S\[0\], S\[1\], …,
S\[255\]. At all times, S contains a permutation of all 8-bit numbers
from 0 through 255. For encryption and decryption, a byte k is generated
from S by selecting one of the 255 entries in a systematic fashion. As
each value of k is generated, the entries in S are once again permuted.

**<u>Initialization of S</u>**

To begin, the entries of S are set equal to the values from 0 through
255 in ascending order; that is; S\[0\] = 0, S\[1\] = 1, …, S\[255\] =
255. A temporary vector, T, is also created. If the length of the key K
is 256 bytes, then K is transferred to T. Otherwise, for a key of length
keylen bytes, the first keylen elements of T are copied from K and then
K is repeated as many times as necessary to fill out T. These
preliminary operations can be summarized as follows:

**/\* Initialization \*/**

**for** i = 0 **to** 255 **do**

S\[i\] = i

T\[i\] = K\[i **mod** keylen\];

Next we use T to produce the initial permutation of S. This involves
starting with S\[**CYV**\] and going through to S (256 times), and, for
each S\[i\], swapping S\[i\] with another byte in S according to a
scheme dictated by T\[i\]:

**/\* Initial Permutation of S \*/**

j = **CYV**;

**for** i = 0 **to** 255 **do**

> j = (j + S\[**CYV** + i\] + T\[**CYV** + i\]) **mod** 256;
>
> Swap (S\[**CYV** + i\], S\[j\]);

Because the only operation on S is a swap, the only effect is a
permutation. S still contains all the numbers from 0 through 255.

**<u>Stream Generation</u>**

Once the S vector is initialized, the input key is no longer used.
Stream generation involves starting with S\[**CYV**\] and going through
to S (256 times), and, for each S\[i\], swapping S\[i\] with another
byte in S according to a scheme dictated by the current configuration of
S. After S\[255\] is eached, the process continues, starting over again
at S\[0\]:

**/\* Stream Generation \*/**

i, j = **CYV**;

**while** (true)

> i = (i + 1) **mod** 256;
>
> j = (j + S\[i\]) **mod** 256;
>
> **Swap** (S\[i\], S\[j\]);
>
> t = (S\[i\] + S\[j\]) **mod** 256;
>
> k = S\[t\];

To encrypt, XOR the value k with the next byte of plaintext. To decrypt,
XOR the value k with the next byte of ciphertext.

## CRC

O CRC usado nas mensagens é a versão CCITT, com o seguinte polinômio:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;"><strong>Polinômio</strong></td>
</tr>
<tr>
<td style="text-align: center;"> X16 + X12 + X5 + X0 (0x1021)</td>
</tr>
</tbody>
</table>

Para início, o valor do CRC usado é 0x0000 (CRC/CCITT – Xmodem).

# Dicionário de Dados

Esta seção contém definições dos campos utilizados nas mensagens do
protocolo PST OPEN.

- **ACT:** Ação do evento (0 = nenhuma, 1 = entrada, 2 = saída, 3 =
  ambos).

- **ADC**: Controle de endereçamento (1 byte). Trata-se de um campo de
  bits que define quais campos de endereço estarão presentes na
  mensagem.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<tbody>
<tr>
<td colspan="2" style="text-align: center;"><strong>Controle de
endereçamento (ADC)</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Bit</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;"> 0: Campo SDT ausente; 1: Campo SDT
presente.</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;"> 0: Campo SID ausente; 1: Campo SID
presente</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;"> 0: Campo DDT ausente; 1: Campo DDT
presente</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"> 0: Campo DID ausente; 1: Campo DID
presente</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"> 0: Campos RDT ausentes; 1: Campos RDT
presentes</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"> 0: Campos RID ausentes; 1: Campos RID
presentes</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"> 0: Não incluir campos RID; 1: Campos
RID devem ser incluídos a partir de agora</td>
</tr>
<tr>
<td style="text-align: center;">0</td>
<td style="text-align: center;"> Livre</td>
</tr>
</tbody>
</table>

- **AID**: Dados de informação adicional (tamanho variável). Este campo
  contém os dados que representam a informação adicional, sendo o
  tamanho definido pelo campo AIS. Veja *Informação Adicional*.

- **AII: **Identificador do tipo de informação adicional (1 byte). Este
  campo define o tipo de informação adicional que está sendo enviada.
  Veja *Informação Adicional*.

- **AIS: **Tamanho da informação adicional (1 byte). Este campo define o
  tamanho dos dados da informação adicional. Veja *Informação
  Adicional*.

- **ALT**: Altitude, em metros acima do nível do mar (2 bytes).

- **APW**: Contrassenha de autorização utilizada para verificar se o
  teclado está autorizado remotamente a executar uma ação quer requer
  uma autorização externa.

- **APWS**: Tamanho da contrassenha de autorização

- **AVS**: Velocidade média desde a última transmissão (1 byte). Este
  campo é utilizado na informação adicional do tipo BTI (Informação
  básica de trânsito). Para maiores detalhes, veja *Informação
  Adicional*.

- **BLE**: Blocos a serem apagados (2 bytes). Este campo é usado para
  informar ao equipamento quais blocos de sua área de armazenamento de
  download devem ser apagados. Esta informação depende da estrutura
  interna de cada equipamento (a maneira como a área de download está
  organizada). O valor 0 significa que toda a área de download deve ser
  apagada.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<tbody>
<tr>
<td colspan="2" style="text-align: center;"><strong>Blocos a serem
apagados (BLE)</strong></td>
</tr>
<tr>
<td rowspan="2" style="text-align: center;"><strong>Valor</strong></td>
<td style="text-align: center;"><strong>Microcontrolador</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>STR712FR2</strong></td>
</tr>
<tr>
<td style="text-align: center;">0</td>
<td style="text-align: center;">Apagar toda a área</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Apagar o bloco 1 (B0F6, 64 kBytes)</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Apagar o bloco 2 (B0F7, 64 kBytes)</td>
</tr>
<tr>
<td style="text-align: center;">&gt; 2</td>
<td style="text-align: center;">Inválido</td>
</tr>
</tbody>
</table>

- **BTI:** Informação básica de trânsito. Veja *Informação Adicional*.

- **CHU**: Segmento de arquivo que está sendo transferido (tamanho
  variável definido por CSZ).

- **CID**: Número de identificação do ponto de controle (0 a 255).

- **CKY**: Chave de criptografia (16 bytes). Quando usada, é uma chave
  de 128 bits para criptografia.

- **CRC**: Código de redundância cíclica (2 bytes).

- **CSG**: Segmento de código (tamanho variável). Conjunto de bytes
  correspondentes ao código do segmento.

- **CSZ**: Tamanho do segmento de arquivo que está sendo transferido

- **CVD**: Valor do código de validação (2 bytes). Trata-se de um CRC de
  16 bits do código inteiro a ser verificado.

- **CYV**: Valor de criptografia (1 byte). É uma chave para o algoritmo
  de criptografia RC4.

- **DDT**: Tipo do equipamento de destino (1 byte). É um parâmetro do
  tipo DTY (veja DTY).

- **DER**: Data e hora de fim do relatório (4 bytes). Define o instante
  em que a captura de dados para o relatório foi finalizada. O formato é
  o A.M.D.h.m.s., de acordo com a definição na tabela abaixo.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 76%" />
</colgroup>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Formato
A.M.D.h.m.s.</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Bits</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">A</td>
<td style="text-align: center;">31 a 26</td>
<td style="text-align: center;">Ano. 6 bits (0 a 63), representando 2000
a 2063</td>
</tr>
<tr>
<td style="text-align: center;">M</td>
<td style="text-align: center;">25 a 22</td>
<td style="text-align: center;">Mês. 4 bits (1 a 12)</td>
</tr>
<tr>
<td style="text-align: center;">D</td>
<td style="text-align: center;">21 a 17</td>
<td style="text-align: center;">Dia. 5 bits (1 a 31)</td>
</tr>
<tr>
<td style="text-align: center;">h</td>
<td style="text-align: center;">16 a 12</td>
<td style="text-align: center;">Hora. 5 bits (0 a 23)</td>
</tr>
<tr>
<td style="text-align: center;">m</td>
<td style="text-align: center;">11 a 6</td>
<td style="text-align: center;">Minuto. 6 bits (0 a 59)</td>
</tr>
<tr>
<td style="text-align: center;">s</td>
<td style="text-align: center;">5 a 0</td>
<td style="text-align: center;">Segundo. 6 bits (0 a 59)</td>
</tr>
</tbody>
</table>

- **DID**: Número de identificação do equipamento de destino (4 bytes).
  Este é o número de identificação do equipamento para o qual a mensagem
  é destinada.

- **DIR**: Direção (1 byte). Esta é a direção do veículo calculada pelo
  GPS (em unidades de 2 graus). A faixa válida está entre 0 e 358 graus.
  0 grau significa Norte e 90 graus significa Leste.

- **DSR**: Data e hora de início do relatório (4 bytes). É um campo do
  tipo A.M.D.h.m.s. e define o instante em que a captura de dados para o
  relatório foi iniciada.

- **DTE**: Data e hora do evento (4 bytes). É um campo do tipo
  A.M.D.h.m.s.

- **DTS**: Data e hora do início da viagem (4 bytes). É um campo do tipo
  A.M.D.h.m.s.

- **DTG**: Data e hora dadas pelo GPS (4 bytes). O formato é o
  A.M.D.h.m.s.

- **DTY**: Tipo de equipamento (1 byte). Identifica o tipo de
  equipamento relacionado com a mensagem. Veja tabela a seguir.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: center;"><strong>Tabela de tipos de
equipamentos</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Tipo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">0x00</td>
<td style="text-align: center;">Qualquer tipo de equipamento</td>
</tr>
<tr>
<td style="text-align: center;">0x01</td>
<td style="text-align: center;">Servidor de módulo</td>
</tr>
<tr>
<td style="text-align: center;">0x02</td>
<td style="text-align: center;">Rastreador convencional</td>
</tr>
<tr>
<td style="text-align: center;">0x03</td>
<td style="text-align: center;">Teclado logístico</td>
</tr>
<tr>
<td style="text-align: center;">0x04</td>
<td style="text-align: center;">BS100 (LC Base Station Hub
(900MHz))</td>
</tr>
<tr>
<td style="text-align: center;">0x05</td>
<td style="text-align: center;">Módulo de telemetria</td>
</tr>
<tr>
<td style="text-align: center;">0x06</td>
<td style="text-align: center;">Rastreador LC</td>
</tr>
<tr>
<td style="text-align: center;">0x07</td>
<td style="text-align: center;">BS110 (LC Base Station RF Front End (900
MHz))</td>
</tr>
<tr>
<td style="text-align: center;">0x08</td>
<td style="text-align: center;">Ferramenta de comunicação serial</td>
</tr>
<tr>
<td style="text-align: center;">0x09</td>
<td style="text-align: center;">Módulo expansor para dados CAN
(TE300)</td>
</tr>
<tr>
<td style="text-align: center;">0x20</td>
<td style="text-align: center;">Servidor de teclado</td>
</tr>
<tr>
<td style="text-align: center;">0x21 a 0x3F</td>
<td style="text-align: center;">Reservado para aplicações do
servidor</td>
</tr>
</tbody>
</table>

- **ECM**: Mensagem encapsulada (tamanho definido pelo parâmetro SEM).
  Trata-se de uma mensagem de qualquer protocolo que é completamente
  encapsulada numa mensagem OPEN. Normalmente, mensagens encapsuladas
  são usadas para transportar mensagens de outros protocolos por meio de
  um barramento local e também para um servidor que se comunica pelo
  protocolo PST OPEN.

- **ECK**: Chave de criptografia do algoritmo RC4 utilizada para
  criptografar o arquivo(9bytes).

- **EVD**: Dados do evento (tamanho variável). Veja *Eventos*.

- **EVT**: Tipo do evento (2 bytes). Veja *Eventos*.

- **FEN**: Codificação do arquivo (1byte). Por enquanto o único valor
  possível é 00, que significa arquivo completo

- **FTY**: Tipo do arquivo(1 byte). Valores possíveis de 0 a 99.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">0</th>
<th>TOC(Table of Contents)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td>Waypoints</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td>Fences</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td>Security Rules</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td>Macros</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td>Drivers</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td>Forms</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td>AGPS</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td>Open Encapsulated</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td>Parameters</td>
</tr>
<tr>
<td style="text-align: center;">99</td>
<td>Tracking device Firmware</td>
</tr>
</tbody>
</table>

- **FID**: Número de identificação da cerca eletrônica (1 byte, 0 a
  255).

- **FPR**: Identificação única do arquivo no servidor Http(10bytes).

- **GNI**: Informação geral (8 bytes). Informação geral do módulo
  (parâmetro de índice 0x0021).

- **GPC**: Condição do GPS (4 bytes). O formato é o hh.vv.ss.nn, como
  mostra a tabela a seguir.

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 22%" />
<col style="width: 56%" />
</colgroup>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Condição do GPS
(GPC)</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Bits</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">hh</td>
<td style="text-align: center;">31 a 25</td>
<td style="text-align: center;">HDOP</td>
</tr>
<tr>
<td style="text-align: center;">vv</td>
<td style="text-align: center;">24 a 16</td>
<td style="text-align: center;">VDOP</td>
</tr>
<tr>
<td style="text-align: center;">ss</td>
<td style="text-align: center;">15 a 8</td>
<td style="text-align: center;">SDOP</td>
</tr>
<tr>
<td style="text-align: center;">nn</td>
<td style="text-align: center;">7 a 0</td>
<td style="text-align: center;">Número de satélites</td>
</tr>
</tbody>
</table>

- **HSH:** Hash do arquivo utilizando o algoritmo HMAC-SHA256 codificado
  em Base64(44bytes)

- **IAC**: Endereço inicial do código a ser verificado (4 bytes).

- **IAD**: Endereço inicial do código descarregado (4 bytes).

- **IAS**: Endereço inicial do segmento (4 bytes). Este é o endereço de
  32 bits do primeiro byte do segmento.

- **IDD**: Identificação do download(10bytes). Identificação única de um
  download que pode consistir em um ou mais arquivos.

- **IDN**: Número de identificação do equipamento (4 bytes).

- **IDV**: Identificação de violação. (2 bytes)

- **IP**: Endereço IP.

- **LAT**: Latitude (4 bytes). Esta é a latitude da posição de um
  veículo. O formato é apresentado na tabela a seguir.

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 17%" />
<col style="width: 55%" />
</colgroup>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Latitude
(LAT)</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Bits</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">Minutos</td>
<td style="text-align: center;">31 a 16</td>
<td style="text-align: center;">Posição em minutos (1 minuto = 1/60
grau)</td>
</tr>
<tr>
<td style="text-align: center;">Minutos/10k</td>
<td style="text-align: center;">15 a 0</td>
<td style="text-align: center;">Minutos/10k</td>
</tr>
<tr>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Positivo: Hemisfério Norte</td>
</tr>
<tr>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Negativo: Hemisfério Sul</td>
</tr>
<tr>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Faixa válida: -90 a 90 graus</td>
</tr>
</tbody>
</table>

- **LDC**: Índice do último pedaço de arquivo baixado (2 bytes).

- **LMC**: Estado anterior do modo controlado(2 bytes)

- **LNG**: Longitude (4 bytes). Esta é a longitude da posição de um
  veículo. O formato é apresentado na tabela a seguir.

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 17%" />
<col style="width: 54%" />
</colgroup>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Longitude
(LNG)</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Bits</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">Minutos</td>
<td style="text-align: center;">31 a 16</td>
<td style="text-align: center;">Posição em minutos (1 minuto = 1/60
grau)</td>
</tr>
<tr>
<td style="text-align: center;">Minutos/10k</td>
<td style="text-align: center;">15 a 0</td>
<td style="text-align: center;">Minutos/10k</td>
</tr>
<tr>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Positivo: Hemisfério Leste</td>
</tr>
<tr>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Negativo: Hemisfério Oeste</td>
</tr>
<tr>
<td style="text-align: center;"> </td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Faixa válida: -180 a 180 graus</td>
</tr>
</tbody>
</table>

- **MCR:** Estado de macro do modo controlado(2bytes).

- **MID:** Macro ID(2bytes).

- **MST**: Sub-tipo de mensagem (1 byte).

- **MTP**: Tipo de mensagem (1 byte).  Usado para identificar cada tipo
  de mensagem.

- **MTY**: Tipo da Macro(1 byte)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 78%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: center;"><strong>Tipos de
macros</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tipo</strong></td>
<td><strong>Descrição</strong></td>
</tr>
<tr>
<td>0x00</td>
<td>Nenhum</td>
</tr>
<tr>
<td>0x01</td>
<td>Servidor para PND</td>
</tr>
<tr>
<td>0x02</td>
<td>PND para Servidor</td>
</tr>
<tr>
<td>0x03</td>
<td>RT para PND</td>
</tr>
<tr>
<td>0x04</td>
<td>Inicio Controlada</td>
</tr>
<tr>
<td>0x05</td>
<td>Fim Controlada</td>
</tr>
<tr>
<td>0x06</td>
<td>Controlada</td>
</tr>
<tr>
<td>0x07</td>
<td>Inicio Especial</td>
</tr>
<tr>
<td>0x08</td>
<td>Fim Especial</td>
</tr>
<tr>
<td>0x09</td>
<td>Informação</td>
</tr>
</tbody>
</table>

- **NAI**: Número de informações adicionais (1 byte). Este campo define
  a quantidade de campos de informação adicional que estão sendo
  enviados. Se NAI = 0, significa que nenhuma informação adicional está
  sendo enviada. Se NAI = 2 (por exemplo), significa que dois tipos de
  informação adicional estão sendo enviados. Veja *Informação*
  *Adicional*.

- **NCH**: Números de pedaços do arquivo(2bytes). Valores de 1 a 9999.

- **NDF**: Número de arquivos dessincronizados(1byte).

- **NRB**: Número de estações rádio-base na vizinhança do módulo sobre
  as quais estão sendo enviadas informações.

- **NRD**: Número de equipamentos retransmissores (1 byte). Este é o
  número de equipamentos retransmissores que estão identificados na
  mensagem (por exemplo, se NRD = 3, há 3 campos RID na mensagem). Se a
  identificação do retransmissor está sendo exigida (esta exigência é
  definida pelo campo ADC), então os equipamentos que estão
  retransmitindo a mensagem devem inserir seus números de identificação
  no próximo campo RID disponível na mensagem e incrementar o valor do
  campo NRD.

- **NRP**: Número de relatórios (1 byte). Este é o número de relatórios
  que estão sendo enviados na mensagem.

- **NSI**: Número de sub-índices (2 bytes).

- **NVI**: Número de violações(1 byte)

- **NVR**: Número de variáveis na mensagem (1 byte).

- **PCT**: Tipo de protocolo (1 byte). Veja tabela a seguir.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: center;"><strong>Tabela de tipos de
protocolo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Tipo</strong></td>
<td><strong>Descrição</strong></td>
</tr>
<tr>
<td>0x00</td>
<td>OPEN PORTO</td>
</tr>
<tr>
<td>0x01</td>
<td>OPEN IAM V1</td>
</tr>
<tr>
<td>0x02</td>
<td>OPEN IAM V2</td>
</tr>
<tr>
<td>0x03</td>
<td>OPEN IAM V3</td>
</tr>
<tr>
<td>0x04</td>
<td>OPEN IAM V4</td>
</tr>
<tr>
<td>0x05</td>
<td>OPEN IAM V5</td>
</tr>
<tr>
<td>0x06</td>
<td>LC</td>
</tr>
<tr>
<td>0x07</td>
<td>PAC (Positron Accessory Communication Protocol)</td>
</tr>
<tr>
<td>0x08 a 0x0F</td>
<td><strong>Reservado</strong></td>
</tr>
<tr>
<td>0x10</td>
<td>RLT</td>
</tr>
<tr>
<td>0x11</td>
<td>TALT</td>
</tr>
<tr>
<td>0x12</td>
<td>OPEN OEM sem enc.</td>
</tr>
<tr>
<td>0x13</td>
<td>OPEN OEM com enc.</td>
</tr>
<tr>
<td>0x80</td>
<td>ACP 245</td>
</tr>
<tr>
<td>0xFF</td>
<td><strong>Protocolo inválido</strong></td>
</tr>
</tbody>
</table>

- **PD1**: Dados PAN 1 (1 byte).

- **PD2**: Dados PAN 2 (1 byte). Utilizado em mensagens com dados PAN de
  16 bits. Para mensagens com dados PAN de 8 bits, este campo deve ser
  ignorado.

- **PID**: Identificador PAN (1 byte).

- **PMD**: Valor do parâmetro (tamanho variável). O tamanho do parâmetro
  é indicado pelo campo PMS.

- **PMI**: Índice do parâmetro a ser lido ou escrito (2 bytes).

- **PMS**: Tamanho do parâmetro a ser lido ou escrito (1 byte).

- **POD**: Hodômetro parcial, em metros (4 bytes, 0 a 4M km). O
  hodômetro parcial é limpo toda vez que a ignição é ligada.

- **PSI**: Sub-índice do parâmetro (2 bytes). Se um sub-índice 0 é
  usado, significa que todas as instâncias do parâmetro devem ser
  acessadas.

- **PT**: Porta (parte do endereço IP).

- **RAD**: Raio do ponto de controle, em unidades de 10 m (0 a 650 km).

- **RBD**: Dados das estações rádio-base (13 bytes).

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 19%" />
<col style="width: 67%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;"><strong>RBD – Dados da
rádio-base</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Dado</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">MCC</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Código do país (Mobile Country
Code)</td>
</tr>
<tr>
<td style="text-align: center;">MNC</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Código da Operadora (Mobile Network
Code)</td>
</tr>
<tr>
<td style="text-align: center;">LAC</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Código da área de localização (Location
Area Code)</td>
</tr>
<tr>
<td style="text-align: center;">CELL</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Identificador da Célula (CELL ID)</td>
</tr>
<tr>
<td style="text-align: center;">BSIC</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Código de identificação da estação (Base
station identity code)</td>
</tr>
<tr>
<td style="text-align: center;">ARFCN</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do Canal de Freqüência Absoluto
da portadora BCCH (Absolute Frequency Channel Number of the BCCH
Carrier)</td>
</tr>
<tr>
<td style="text-align: center;">RSSI</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Nível de sinal recebido da portadora
BCCH (Received signal level of the BCCH carrier). Valores válidos: 0 a
63</td>
</tr>
<tr>
<td style="text-align: center;">C1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Coeficiente para re-seleção da estação
base (Coefficient for base station reselection)</td>
</tr>
<tr>
<td style="text-align: center;">C2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Coeficiente para re-seleção da estação
base (Coefficient for base station reselection)</td>
</tr>
</tbody>
</table>

- **RDT**: Tipo de equipamento retransmissor (1 byte). É um parâmetro do
  tipo DTY (veja DTY). Normalmente este parâmetro é usado em mensagens
  transportadas por meio de um barramento local, identificando o tipo de
  equipamento que retransmitiu a mensagem.

- **RID**: Número de identificação do equipamento retransmissor (4
  bytes). Este é o número de identificação do equipamento que está
  retransmitindo a mensagem.

- **RPD**: Campo de dados do relatório (tamanho variável). Este campo
  possui o tamanho definido pelo campo SRD.

- **RPI**: Campo de identificador de relatório (2 bytes). Este campo
  define o tipo de relatório.

- **RSC**: Código de resposta (2 bytes) (veja *Códigos de Respostas*).

- **SDT**: Tipo de equipamento de origem (1 byte). É um parâmetro do
  tipo DTY (veja DTY).

- **SEM**: Tamanho da mensagem encapsulada (2 bytes).

- **SEQ**: Número de sequência da mensagem (4 bytes).

- **SIC**: Sub índice do pedaço de arquivo. Utilizado para quebrar um
  pedaço de arquivo em pedaços menores

- **SID**: Número de identificação do equipamento de origem (4 bytes).
  Este é o número de identificação do equipamento que originou a
  mensagem (equipamento que criou e que pela primeira vez transmitiu a
  mensagem).

- **SMV**: Status do modo violado(1 byte). Não violado(00) ou Violado
  (01).

- **SPD**: Velocidade (1 byte). Trata-se da velocidade do veículo, em
  nós (aproximadamente 1,852 km/h).

- **SRD**: Tamanho do campo de dados do relatório (1 byte).

- **STP**: Tipo da origem (1 byte). Tipo de mensagem que originou a
  resposta.

- **STS**: Status (1 byte).  Trata-se de um campo de bits que contêm
  várias informações, como descrito na tabela a seguir.

<table>
<colgroup>
<col style="width: 31%" />
<col style="width: 10%" />
<col style="width: 57%" />
</colgroup>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Status
(STS)</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Bit</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">Ignição</td>
<td style="text-align: center;">7</td>
<td style="text-align: center;">0: Ignição desligada; 1: Ignição
ligada</td>
</tr>
<tr>
<td style="text-align: center;">Bateria principal</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">0: Módulo desconectado da bateria
principal; 1: Conectado</td>
</tr>
<tr>
<td style="text-align: center;">Botão de assistência</td>
<td style="text-align: center;">5</td>
<td style="text-align: center;">0: Botão de assistência não pressionado;
1: Botão de assistência pressionado</td>
</tr>
<tr>
<td style="text-align: center;">Estado do bloqueio</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">0: Estado desbloqueado; 1: Estado
bloqueado</td>
</tr>
<tr>
<td style="text-align: center;">Sinal de GPS</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">0: Ruim; 1: Bom</td>
</tr>
<tr>
<td style="text-align: center;">Sensor de movimento</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">0: Veículo parado; 1: Veículo em
movimento</td>
</tr>
<tr>
<td style="text-align: center;">Modo emergência</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0: Desativado; 1: Ativado</td>
</tr>
<tr>
<td style="text-align: center;">Ignição por tensão em uso</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">0: Não; 1: Sim</td>
</tr>
</tbody>
</table>

- **SVD**: Número de validação de segmento. Trata-se de um CRC de 16
  bits do segmento de código.

- **SZC**: Tamanho do código a ser verificado, em bytes (4 bytes).

- **SZS**: Tamanho do segmento (1 byte). É o tamanho do segmento menos
  1, em bytes. Recomenda-se o uso de um tamanho múltiplo de 4.

- **TEC**: Código de erro de transferência de arquivo Http. Tamanho 1
  byte. Definido pela tabela abaixo:

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: center;"><strong>TEC</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Valor</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">0x00</td>
<td style="text-align: center;">Erro desconhecido</td>
</tr>
<tr>
<td style="text-align: center;">0x01</td>
<td style="text-align: center;">Arquivo desconhecido</td>
</tr>
<tr>
<td style="text-align: center;">0x02</td>
<td style="text-align: center;">Id download desconhecido</td>
</tr>
<tr>
<td style="text-align: center;">0x03</td>
<td style="text-align: center;">Atualização negada</td>
</tr>
<tr>
<td style="text-align: center;">0x04</td>
<td style="text-align: center;">Hash incompatível</td>
</tr>
<tr>
<td style="text-align: center;">0x05</td>
<td style="text-align: center;">Chunk externo recusado</td>
</tr>
<tr>
<td style="text-align: center;">0x06</td>
<td style="text-align: center;">Arquivo externo recusado</td>
</tr>
<tr>
<td style="text-align: center;">0x07</td>
<td style="text-align: center;">Atualização externa recusada</td>
</tr>
<tr>
<td style="text-align: center;">0x08</td>
<td style="text-align: center;">Timeout de transferência</td>
</tr>
<tr>
<td style="text-align: center;">0x08</td>
<td style="text-align: center;">Troca de dispositivo</td>
</tr>
</tbody>
</table>

- **TKY**: Chave calculada pelo rastreador para pedido de autorização
  externa de alguma ação bloqueada

- **TKYS**: Tamanho da chave calculada pelo rastreador

- **TOD**: Hodômetro total, em metros (4 bytes, 0 a 4M km).

- **TST**: Status das entradas de telemetria (1 byte). É um campo de
  bits que representam o status das entradas de telemetria, como
  descrito na tabela a seguir.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 10%" />
<col style="width: 58%" />
</colgroup>
<tbody>
<tr>
<td colspan="3" style="text-align: center;"><strong>Status das entradas
de telemetria (TST)</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Bit</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">Limpador de para-brisa</td>
<td style="text-align: center;">7</td>
<td style="text-align: center;">0: Desligado; 1: Ligado</td>
</tr>
<tr>
<td style="text-align: center;">Freio motor</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">0: Em repouso; 1: Acionado</td>
</tr>
<tr>
<td style="text-align: center;">Freio de serviço</td>
<td style="text-align: center;">5</td>
<td style="text-align: center;">0: Em repouso; 1: Acionado</td>
</tr>
<tr>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Sempre 0</td>
</tr>
<tr>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Sempre 0</td>
</tr>
<tr>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Sempre 0</td>
</tr>
<tr>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Sempre 0</td>
</tr>
<tr>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;">0</td>
<td style="text-align: center;">Sempre 0</td>
</tr>
</tbody>
</table>

- **TTR**: Tempo total durante o qual os dados do relatório foram
  coletados, em segundos (4 bytes).

- **VER**: Número de versão de protocolo (1 byte). O número atual é 3.

- **VRD**: Valor (dado) da variável. O tamanho deste campo é dado por
  VRS.

- **VRI**: Índice da variável (2 bytes). Índice da variável na lista.

- **VRS**: Tamanho da variável (1 byte). Tamanho da variável, em bytes.

- **VTC**: Número de vértices (1 byte, mínimo 3 e máximo 18).

- **VTM**: Tempo de pré-violação(Modo alarme).(2 bytes)

- **VTY**: Tipo de veículo (1 byte). Usado para indicar o tipo de
  veículo (veja *Tipo de Veículo*).

# Camada de Aplicação

Na comunicação do equipamento com o servidor usando UDP, é necessário
implementar um mecanismo de acknowledge na camada de aplicação. Este
mecanismo é simples: cada mensagem que é enviada de um lado deve ser
respondida com uma mensagem de ACK (MTP = 00h) ou NACK (MTP = 0Bh) pelo
outro lado. A mensagem transmitida tem um número de seqüência (4 bytes)
que deve fazer parte da mensagem de resposta (ACK ou NACK). O lado que
está enviando a mensagem não deve enviar outra mensagem para o receptor
enquanto não receber a resposta.

Além disso, o transmissor deve implementar um mecanismo de reenvio. Se o
transmissor não recebe o acknowledge de uma mensagem após um determinado
tempo (UDT, time-out do UDP), a mensagem deve ser enviada novamente, até
um número máximo de tentativas (parâmetro RTY). Os valores padrões são
30 segundos para UDT e 5 tentativas para RTY. Após o número de
tentativas expirar, o transmissor deve considerar que o link de
transmissão não está funcionando e tomar alguma ação apropriada (por
exemplo, o equipamento pode tentar fechar a sessão GPRS e conectar-se ao
servidor secundário). Após tentar os dois servidores sem sucesso, o
transmissor deve executar um auto-reset e voltar a tentar conectar-se ao
servidor primário.

# Mensagens da Camada de Aplicação

## Tabela de tipos de mensagens

<table>
<colgroup>
<col style="width: 5%" />
<col style="width: 11%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;"><strong>Tabela de tipos de
mensagens</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>MTP</strong></td>
<td style="text-align: center;"><strong>Mensagem</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">00h</td>
<td style="text-align: center;">ACK</td>
<td style="text-align: center;">Mensagem de Acknowledge</td>
</tr>
<tr>
<td style="text-align: center;">01h</td>
<td style="text-align: center;">POS</td>
<td style="text-align: center;">Posição</td>
</tr>
<tr>
<td style="text-align: center;">02h</td>
<td style="text-align: center;">UPL</td>
<td style="text-align: center;">Mensagem da Porta Serial para o
Servidor</td>
</tr>
<tr>
<td style="text-align: center;">03h</td>
<td style="text-align: center;">PAN</td>
<td style="text-align: center;">Comandos PAN</td>
</tr>
<tr>
<td style="text-align: center;">04h</td>
<td style="text-align: center;">PAI</td>
<td style="text-align: center;">Posição com Informação Adicional</td>
</tr>
<tr>
<td style="text-align: center;">05h</td>
<td style="text-align: center;">SAI</td>
<td style="text-align: center;">Status com Informação Adicional</td>
</tr>
<tr>
<td style="text-align: center;">06h</td>
<td style="text-align: center;">CMD</td>
<td style="text-align: center;">Comandos</td>
</tr>
<tr>
<td style="text-align: center;">07h</td>
<td style="text-align: center;">DWL</td>
<td style="text-align: center;">Mensagem do Servidor para a Porta
Serial</td>
</tr>
<tr>
<td style="text-align: center;">08h</td>
<td style="text-align: center;">ODO</td>
<td style="text-align: center;">Mensagem de Hodômetro</td>
</tr>
<tr>
<td style="text-align: center;">09h</td>
<td style="text-align: center;">CPC</td>
<td style="text-align: center;">Mensagem de Configuração de Ponto de
Controle</td>
</tr>
<tr>
<td style="text-align: center;">0Ah</td>
<td style="text-align: center;">GFC</td>
<td style="text-align: center;">Mensagem de Configuração de Cerca
Eletrônica</td>
</tr>
<tr>
<td style="text-align: center;">0Bh</td>
<td style="text-align: center;">NACK</td>
<td style="text-align: center;">Mensagem de Acknowledge Negativo</td>
</tr>
<tr>
<td style="text-align: center;">0Ch</td>
<td style="text-align: center;">PRD</td>
<td style="text-align: center;">Leitura de Parâmetro</td>
</tr>
<tr>
<td style="text-align: center;">0Dh</td>
<td style="text-align: center;">PRR</td>
<td style="text-align: center;">Resposta à Leitura de Parâmetro</td>
</tr>
<tr>
<td style="text-align: center;">0Eh</td>
<td style="text-align: center;">SAD</td>
<td style="text-align: center;">Iniciar Procedimento de Download</td>
</tr>
<tr>
<td style="text-align: center;">0Fh</td>
<td style="text-align: center;">EDA</td>
<td style="text-align: center;">Limpar Área de Download</td>
</tr>
<tr>
<td style="text-align: center;">10h</td>
<td style="text-align: center;">SSG</td>
<td style="text-align: center;">Armazenar Segmento</td>
</tr>
<tr>
<td style="text-align: center;">11h</td>
<td style="text-align: center;">CCD</td>
<td style="text-align: center;">Verificar Código</td>
</tr>
<tr>
<td style="text-align: center;">12h</td>
<td style="text-align: center;">URA</td>
<td style="text-align: center;">Atualizar Área do Programa</td>
</tr>
<tr>
<td style="text-align: center;">13h</td>
<td style="text-align: center;">SOD</td>
<td style="text-align: center;">Abandonar o Procedimento de
Download</td>
</tr>
<tr>
<td style="text-align: center;">14h</td>
<td style="text-align: center;">CS</td>
<td style="text-align: center;">Leitura de variável CAN via
identificador SPN do protocolo SAE J1939</td>
</tr>
<tr>
<td style="text-align: center;">15h</td>
<td style="text-align: center;">CSR</td>
<td style="text-align: center;">Resposta à Leitura de variável CAN via
identificador SPN do protocolo SAE J1939</td>
</tr>
<tr>
<td style="text-align: center;">16h</td>
<td style="text-align: center;">PRW</td>
<td style="text-align: center;">Escrita de Parâmetro</td>
</tr>
<tr>
<td style="text-align: center;">17h</td>
<td style="text-align: center;">CPM</td>
<td style="text-align: center;">Alteração de protocolo de
comunicação</td>
</tr>
<tr>
<td style="text-align: center;">18h</td>
<td style="text-align: center;">RBI</td>
<td style="text-align: center;">Informação de Rádio Base</td>
</tr>
<tr>
<td style="text-align: center;">19h</td>
<td style="text-align: center;">PSI</td>
<td style="text-align: center;">Posição com Identificador do SIM
Card</td>
</tr>
<tr>
<td style="text-align: center;">1Ah</td>
<td style="text-align: center;">IDC</td>
<td style="text-align: center;">Configuração do Número de Identificação
do Rastreador</td>
</tr>
<tr>
<td style="text-align: center;">1Bh</td>
<td style="text-align: center;">RTD</td>
<td style="text-align: center;">Retorno do Procedimento de Download</td>
</tr>
<tr>
<td style="text-align: center;">1Ch</td>
<td style="text-align: center;">TAL</td>
<td style="text-align: center;">Mensagem Encapsulada do Protocolo
TALT</td>
</tr>
<tr>
<td style="text-align: center;">1Dh</td>
<td style="text-align: center;">VRL</td>
<td style="text-align: center;">Mensagem de Lista de Variáveis</td>
</tr>
<tr>
<td style="text-align: center;">1Eh</td>
<td style="text-align: center;">VRD</td>
<td style="text-align: center;">Mensagem de Leitura de Variáveis</td>
</tr>
<tr>
<td style="text-align: center;">1Fh</td>
<td style="text-align: center;">VRR</td>
<td style="text-align: center;">Mensagem de Resposta à Leitura de
Variáveis</td>
</tr>
<tr>
<td style="text-align: center;">20h</td>
<td style="text-align: center;">RDI</td>
<td style="text-align: center;">Mensagem de Informação RDS</td>
</tr>
<tr>
<td style="text-align: center;">21h</td>
<td style="text-align: center;">ENC</td>
<td style="text-align: center;">Mensagem Encapsulada</td>
</tr>
<tr>
<td style="text-align: center;">22h</td>
<td style="text-align: center;">RPL</td>
<td style="text-align: center;">Mensagem de Lista de Relatórios</td>
</tr>
<tr>
<td style="text-align: center;">23h</td>
<td style="text-align: center;">BSS</td>
<td style="text-align: center;">Mensagem de status da base LC</td>
</tr>
<tr>
<td style="text-align: center;">24h</td>
<td style="text-align: center;">TST</td>
<td style="text-align: center;">Mensagem de Status do Rastreador para
Dispositivos Locais</td>
</tr>
<tr>
<td style="text-align: center;">25h</td>
<td style="text-align: center;">SST</td>
<td style="text-align: center;">Mensagem de Status da Antena Satelital
para Dispositivos Locais</td>
</tr>
<tr>
<td style="text-align: center;">26h</td>
<td style="text-align: center;">CLD</td>
<td style="text-align: center;">Mensagem de comando para dispositivos
locais</td>
</tr>
<tr>
<td style="text-align: center;">27h</td>
<td style="text-align: center;">NLD</td>
<td style="text-align: center;">Mensagem de notificação gerada por
dispositivos locais</td>
</tr>
<tr>
<td style="text-align: center;">28h</td>
<td style="text-align: center;">SAT</td>
<td style="text-align: center;">Mensagem para troca de informações via
link satelital</td>
</tr>
<tr>
<td style="text-align: center;">2Ah</td>
<td style="text-align: center;">BFT</td>
<td style="text-align: center;">Mensagem para início de transferência de
arquivo</td>
</tr>
<tr>
<td style="text-align: center;">2Bh</td>
<td style="text-align: center;">TFS</td>
<td style="text-align: center;">Mensagem para transferência de segmento
de arquivo</td>
</tr>
<tr>
<td style="text-align: center;">2Ch</td>
<td style="text-align: center;">CKF</td>
<td style="text-align: center;">Mensagem para verificação do arquivo
transferido</td>
</tr>
<tr>
<td style="text-align: center;">2Dh</td>
<td style="text-align: center;">CFT</td>
<td style="text-align: center;">Mensagem para finalização da
transferência de arquivo</td>
</tr>
<tr>
<td style="text-align: center;">2Eh</td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Livre</td>
</tr>
<tr>
<td style="text-align: center;">2Fh</td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Livre</td>
</tr>
<tr>
<td style="text-align: center;">30h</td>
<td style="text-align: center;">EAI</td>
<td style="text-align: center;">Mensagem de Evento com Informação
Adicional</td>
</tr>
<tr>
<td style="text-align: center;">31h</td>
<td style="text-align: center;">CDF</td>
<td style="text-align: center;">Confirmação de atualização de
arquivos</td>
</tr>
<tr>
<td style="text-align: center;">32h</td>
<td style="text-align: center;">CDC</td>
<td style="text-align: center;">Cancelar download atual</td>
</tr>
<tr>
<td style="text-align: center;">33h</td>
<td style="text-align: center;">CHF</td>
<td style="text-align: center;">Checar Http File</td>
</tr>
<tr>
<td style="text-align: center;">34h</td>
<td style="text-align: center;">NTF</td>
<td style="text-align: center;">Nova Transferência Local</td>
</tr>
<tr>
<td style="text-align: center;">35h</td>
<td style="text-align: center;">SFC</td>
<td style="text-align: center;">Envio de pedaço de arquivo</td>
</tr>
<tr>
<td style="text-align: center;">36h</td>
<td style="text-align: center;">RNE</td>
<td style="text-align: center;">Permissão de envio de macro</td>
</tr>
<tr>
<td style="text-align: center;">37h</td>
<td style="text-align: center;">RAP</td>
<td style="text-align: center;">Requisição de senha de autorização</td>
</tr>
<tr>
<td style="text-align: center;">38h</td>
<td style="text-align: center;">RAR</td>
<td style="text-align: center;">Resposta com senha de autorização</td>
</tr>
<tr>
<td style="text-align: center;">39h</td>
<td style="text-align: center;">CAP</td>
<td style="text-align: center;">Checar contrassenha de autorização</td>
</tr>
<tr>
<td style="text-align: center;">3Ah</td>
<td style="text-align: center;">RRM</td>
<td style="text-align: center;">Resposta à permissão de envio de
macro</td>
</tr>
<tr>
<td style="text-align: center;">40h</td>
<td style="text-align: center;">NFA</td>
<td style="text-align: center;">Novo arquivo disponível para
download</td>
</tr>
<tr>
<td style="text-align: center;">FFh</td>
<td style="text-align: center;"> </td>
<td style="text-align: center;">Reservado para ELD</td>
</tr>
</tbody>
</table>

## Mensagens Gerais

### Mensagem de Acknowledge (ACK – 00h)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 18%" />
</colgroup>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>ACK: MTP =
00h</strong></td>
</tr>
<tr>
<td style="text-align: left;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">MST</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: left;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">6</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada pelo receptor com o mesmo número sequencial e
IDN da mensagem à qual ele está respondendo.

### Posição (POS – 01h)

<table style="width:100%;">
<colgroup>
<col style="width: 21%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr>
<td colspan="11" style="text-align: center;"><strong>POS: MTP =
01h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">DTG</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">SPD</td>
<td style="text-align: center;">DIR</td>
<td style="text-align: center;">ALT</td>
<td style="text-align: center;">GPC</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">EVT</td>
<td style="text-align: center;">EVI</td>
<td style="text-align: center;">STS</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">32</td>
</tr>
</tbody>
</table>

Esta mensagem é usada para enviar a informação de posição do equipamento
ao servidor ou a outro equipamento. Esta mensagem também pode ser usada
para enviar informação de evento, porém apenas para eventos em que o
identificador (EVT) esteja na faixa de 0x00 a 0x1F. Eventos dentro dessa
faixa possuem um campo para informações sobre o evento (EVI) com tamanho
limitado a 1 byte. Esta restrição é devido ao fato de que a mensagem POS
não é flexível, e, quando ela foi criada, os eventos deveriam ter apenas
1 byte de informação. Com o avanço do protocolo, houve a necessidade de
uma mensagem mais flexível. Para os novos equipamentos, é recomendado
usar a mensagem “Posição com Informação Adicional” (PAI). PAI é uma
mensagem mais flexível e pode enviar informações adicionais,
juntamente com a posição, incluindo os eventos cujo tamanho da
informação do evento (EVI) seja superior a 1 byte.

### Mensagem da Porta Serial para o Servidor (UPL – 02h)

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>UPL: MTP =
02h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">LSP</td>
<td style="text-align: center;">SPS</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">n</td>
<td style="text-align: center;">7 + n</td>
</tr>
</tbody>
</table>

**LSP**: comprimento da mensagem SPS (até 512 bytes).

**SPS** é uma mensagem da porta serial de entrada para o servidor, no
formato binário.

### Comandos PAN (PAN – 03h)

<table style="width:100%;">
<colgroup>
<col style="width: 34%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>PAN: MTP =
03h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">PID</td>
<td style="text-align: center;">PD1</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">7</td>
</tr>
</tbody>
</table>

### Posição com Informação Adicional (PAI – 04h)

<table style="width:100%;">
<colgroup>
<col style="width: 18%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr>
<td colspan="13" style="text-align: center;"><strong>PAI: MTP =
04h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">DTG</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">SPD</td>
<td style="text-align: center;">DIR</td>
<td style="text-align: center;">ALT</td>
<td style="text-align: center;">GPC</td>
<td style="text-align: center;">STS</td>
<td style="text-align: center;">NAI</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">AII1</td>
<td style="text-align: center;">AIS1</td>
<td style="text-align: center;">AID1</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">AIIn</td>
<td style="text-align: center;">AISn</td>
<td style="text-align: center;">AIDn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><em>AIS1</em></td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><em>AISn</em></td>
<td style="text-align: center;">31+NAI*2+AIS1+ ... +AISn</td>
</tr>
</tbody>
</table>

Esta mensagem é usada para enviar a informação de posição do equipamento
ao servidor ou a outros equipamentos, junto com outra informação
adicional. A mensagem PAI foi criada com o intuito de prover ao
equipamento uma forma mais flexível de enviar informações periódicas (a
antiga mensagem POS, que é um formato de mensagem fixo, não permite
qualquer flexibilização). Com este formato flexível, a mensagem PAI pode
enviar uma série de informações adicionais, além da posição. Por
exemplo, ela pode ser usada para enviar uma informação de evento,
informação de trânsito, etc. Para novos projetos, é recomendado o uso da
mensagem PAI ao invés da mensagem POS.

O campo **NAI** (Número de informações adicionais) define quantos, se
for o caso, campos de informação adicional estão sendo enviados na
mensagem. Se NAI=0, significa que nenhuma informação adicional está
sendo enviada na mensagem (consequentemente, este é o último campo da
mensagem). Se NAI=2, por exemplo, significa que 2 tipos de informação
adicional estão sendo enviados na mensagem.

O campo **AIIx** (Identificador da informação adicional) define o tipo
de informação adicional que está sendo enviada.

O campo **AISx** (Tamanho da informação adicional) define o tamanho do
respectivo campo de dados da informação adicional.

O campo **AIDx** (Dado da informação adicional) contém o dado da
informação adicional. Para maiores detalhes sobre os tipos de informação
adicional, veja *Informação Adicional*.

### Status com Informação Adicional (SAI – 05h)

<table>
<colgroup>
<col style="width: 36%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>SAI: MTP =
05h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">STS</td>
<td style="text-align: center;">NAI</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 29%" />
</colgroup>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">AII1</td>
<td style="text-align: center;">AIS1</td>
<td style="text-align: center;">AID1</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">AIIn</td>
<td style="text-align: center;">AISn</td>
<td style="text-align: center;">AIDn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><em>AIS1</em></td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><em>AISn</em></td>
<td style="text-align: center;">31+NAI*2+AIS1+ ... +AISn</td>
</tr>
</tbody>
</table>

A exemplo da mensagem PAI, esta mensagem oferece a mesma flexibilidade
vista anteriormente, porém exclui as informações referentes ao GPS que,
por sua vez, podem ser adicionados na forma de AI. Dessa forma,
equipamentos que não possuem um receptor GPS podem enviar esta mensagem
apenas com as informações do AI para dados de ERB, por exemplo.

### Comandos (CMD – 06h)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<tbody>
<tr>
<td colspan="7" style="text-align: center;"><strong>CMD: MTP =
06h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">CMT</td>
<td style="text-align: center;">CDT1</td>
<td style="text-align: center;">CDT2</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho[Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">11</td>
</tr>
</tbody>
</table>

Esta mensagem é utilizada quando o servidor envia um comando para o
dispositivo que deve responder a mensagem com um ACK, informando se o
comando foi aceito (sucesso) ou não.

**CMT** (Tipo do comando): este campo define o tipo do comando.

**CDT1 e CDT2** (Dados do comando): estes campos contêm os dados
relativos ao comando.

Para mais informações sobre comandos, ver a seção *COMANDOS*.

### Mensagem do Servidor para a Porta Serial (DWL – 07h)

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>DWL: MTP =
07h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">LSP</td>
<td style="text-align: center;">SPS</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">n</td>
<td style="text-align: center;">7 + n</td>
</tr>
</tbody>
</table>

### Mensagem de Hodômetro (ODO – 08h)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 10%" />
</colgroup>
<tbody>
<tr>
<td colspan="11" style="text-align: center;"><strong>ODO: MTP =
08h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">DTS</td>
<td style="text-align: center;">TOD</td>
<td style="text-align: center;">POD</td>
<td style="text-align: center;">EVT</td>
<td style="text-align: center;">EVI</td>
<td style="text-align: center;">STS</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">24</td>
</tr>
</tbody>
</table>

### Mensagem de Configuração de Ponto de Controle (CPC – 09h)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr>
<td colspan="9" style="text-align: center;"><strong>CPC: MTP =
09h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">CID</td>
<td style="text-align: center;">ACT</td>
<td style="text-align: center;">RAD</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">17</td>
</tr>
</tbody>
</table>

### Mensagem de Configuração de Cerca Eletrônica (GFC – 0Ah)

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr>
<td colspan="10" style="text-align: center;"><strong>GFC: MTP =
0Ah</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">FID</td>
<td style="text-align: center;">ACT</td>
<td style="text-align: center;">VTC</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">9 + <em>VTC</em>*8</td>
</tr>
</tbody>
</table>

### Mensagem de Acknowledge Negativo (NACK – 0Bh)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>NACK: MTP =
0Bh</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">STP</td>
<td style="text-align: center;">RSC</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">8</td>
</tr>
</tbody>
</table>

### Leitura de Parâmetro (PRD – 0Ch)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr>
<td colspan="9" style="text-align: center;"><strong>PRD: MTP =
0Ch</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">PMI</td>
<td style="text-align: center;">NSI</td>
<td style="text-align: center;">PSI1</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">PSIn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">9 + 2.NSI</td>
</tr>
</tbody>
</table>

### Resposta à Leitura de Parâmetro (PRR – 0Dh)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr>
<td colspan="9" style="text-align: center;"><strong>PRR: MTP =
0Dh</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">PMI</td>
<td style="text-align: center;">PMS</td>
<td style="text-align: center;">NSI</td>
<td style="text-align: center;">PSI1</td>
<td style="text-align: center;">PMD1</td>
<td style="text-align: center;">...</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">PMS</td>
<td style="text-align: center;">...</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 40%" />
</colgroup>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">PSIn</td>
<td style="text-align: center;">PMDn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">PMS</td>
<td style="text-align: center;">11 + 2.NSI + NSI.PMS</td>
</tr>
</tbody>
</table>

### Leitura de variável CAN via identificador SPN do protocolo SAE J1939 (CSR- 14h)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr>
<td colspan="8" style="text-align: center;"><strong>CSR: MTP =
14h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">NSPN</td>
<td style="text-align: center;">SPNI1</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">SPNIn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">6 + 4.NSPN</td>
</tr>
</tbody>
</table>

### Resposta à Leitura de variável CAN via identificador SPN do protocolo SAE J1939 (CSRR- 15h)

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr>
<td colspan="8" style="text-align: center;"><strong>CSRR: MTP =
15h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">NSPN</td>
<td style="text-align: center;">SPNI1</td>
<td style="text-align: center;">SPNS1</td>
<td style="text-align: center;">SPND1</td>
<td style="text-align: center;">...</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">S1</td>
<td style="text-align: center;">...</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 38%" />
</colgroup>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">SPNIn</td>
<td style="text-align: center;">SPNSn</td>
<td style="text-align: center;">SPNDn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Sn</td>
<td style="text-align: center;">6 + 5.NSPN + S1 +...+ Sn</td>
</tr>
</tbody>
</table>

### Escrita de Parâmetro (PRW – 16h)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr>
<td colspan="9" style="text-align: center;"><strong>PRW: MTP =
16h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">PMI</td>
<td style="text-align: center;">PMS</td>
<td style="text-align: center;">NSI</td>
<td style="text-align: center;">PSI1</td>
<td style="text-align: center;">PMD1</td>
<td style="text-align: center;">...</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">PMS</td>
<td style="text-align: center;">...</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 40%" />
</colgroup>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">PSIn</td>
<td style="text-align: center;">PMDn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">PMS</td>
<td style="text-align: center;">11 + 2.NSI + NSI.PMS</td>
</tr>
</tbody>
</table>

### Alteração de protocolo de comunicação (CPM – 17h)

### Informação de Rádio Base (RBI – 18h)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td colspan="10" style="text-align: center;"><strong>RBI: MTP =
18h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">NRB</td>
<td style="text-align: center;">RBD1</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">RBDn</td>
<td style="text-align: center;">STS</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">13</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">13</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">11 + NRB.13</td>
</tr>
</tbody>
</table>

O objetivo desta mensagem é enviar ao servidor informações sobre as
estações rádio base nas regiões em que o módulo está trafegando. Esta
mensagem pode ser enviada periodicamente pelo módulo, caso esteja
configurado para isso. Normalmente o módulo está configurado para não
enviar esta mensagem.

### Posição com Identificador do SIM Card (PSI – 19h)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr>
<td colspan="12" style="text-align: center;"><strong>PSI: MTP =
19h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">SCI</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">DTG</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">SPD</td>
<td style="text-align: center;">DIR</td>
<td style="text-align: center;">ALT</td>
<td style="text-align: center;">GPC</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">EVT</td>
<td style="text-align: center;">EVI</td>
<td style="text-align: center;">STS</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">40</td>
</tr>
</tbody>
</table>

**SCI:** Número de identificação do SIM Card, no formato BCD.

Esta mensagem é usada pelo equipamento para enviar mensagens de posição
quando o seu identificador for inválido. Identificador inválido
significa que o identificador gravado em sua memória não volátil é
inválido (normalmente o equipamento possui alguma forma de verificar se
os dados gravados em sua memória não volátil são válidos). Quando esta
situação ocorrer, o equipamento deve enviar este tipo de mensagem de
posição, e o ID desta mensagem deve ser 0 (00 00 00 00h). Este
comportamento permite ao servidor descobrir rapidamente os equipamentos
que estejam com identificador inválido. Note-se que, nesta situação, o
equipamento continua enviando as informações de posição normalmente,
usando esta mensagem ao invés da mensagem de posição (tipo 01h ou tipo
04h). A ação a ser tomada na ocorrência desta situação é de
responsabilidade do servidor. Normalmente, o servidor deve enviar uma
mensagem de configuração do número de identificação do equipamento
(IDN), restaurando o funcionamento normal do mesmo.

### Configuração do Número de Identificação do Rastreador (IDC – 1Ah)

<table>
<colgroup>
<col style="width: 34%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>IDC: MTP =
1Ah</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">SCI</td>
<td style="text-align: center;">NID</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">17</td>
</tr>
</tbody>
</table>

**NID:** Novo número de identificação do equipamento.

Esta mensagem é usada para trocar o número de identificação do
equipamento. Além disso, esta mensagem é usada quando se deseja
recuperar o equipamento de uma situação em que ele esteja com um número
de identificação inválido ou incorreto. Como esta é uma operação
potencialmente perigosa, pois pode gerar uma inconsistência na base de
dados, ela só será aceita pelo equipamento nas seguintes condições:

- Se o número de identificação atual do equipamento for inválido: o
  equipamento somente aceitará a operação se o IDN da mensagem for 0 (00
  00 00 00h) e o número do SIM Card da mensagem for equivalente ao
  número do seu SIM Card.

- Se o identificador atual do equipamento for incorreto: o equipamento
  somente aceitará a operação se o IDN da mensagem for equivalente ao
  seu IDN atual e o número do SIM Card da mensagem for equivalente ao
  número do seu SIM Card.

**Observação:** IDN inválido significa que o IDN gravado na memória não
volátil do equipamento é inválido (o equipamento deve possuir uma forma
de verificar se os dados gravados em sua memória não volátil são
válidos). IDN incorreto significa que o IDN gravado na memória não
volátil do equipamento é válido, porém o servidor detectou que, por
algum motivo, este IDN é incorreto (por exemplo, IDN duplicado).

### Mensagem Encapsulada do Protocolo TALT (TAL – 1Ch)

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 18%" />
</colgroup>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>TAL: MTP =
1Ch</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">MTA</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">n</td>
<td style="text-align: center;">5 + n</td>
</tr>
</tbody>
</table>

**MTA:** Mensagem encapsulada do protocolo TALT.

Esta mensagem é usada para permitir ao servidor enviar ou receber
mensagens do barramento TALT. TALT é um protocolo antigo usado por um
equipamento de rastreamento para se comunicar com seus acessórios (ele
não está sendo usado em novos projetos).

### Mensagem de Lista de Variáveis (VRL – 1Dh)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 4%" />
</colgroup>
<tbody>
<tr>
<td colspan="13" style="text-align: center;">VRL : MTP = 1Dh</td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">DTG</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">SPD</td>
<td style="text-align: center;">NVR</td>
<td style="text-align: center;">VRI1</td>
<td style="text-align: center;">VRS1</td>
<td style="text-align: center;">VRD1</td>
<td style="text-align: center;">...</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">VRS1</td>
<td style="text-align: center;">...</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 48%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">VRIn</td>
<td style="text-align: center;">VRSn</td>
<td style="text-align: center;">VRDn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">VRSn</td>
<td style="text-align: center;">23 + 4.NVR + VRS1 + .. + VRSn</td>
</tr>
</tbody>
</table>

A mensagem de lista de variáveis (VRL) é utilizada quando se necessita o
envio periódico do valor de uma determinada variável (como temperatura,
nível da bateria, etc). Trata-se de um recurso importante para testes,
por exemplo. Para mais informações veja [Variables Lists – OPEN IAM
Protocol](http://wiki.cps.pst/wiki/lib/fckeditor/editor/tiki-index.php?page=Variables%20Lists%20-%20OPEN%20IAM%20Protocol).

### Mensagem de Leitura de Variáveis (VRD – 1Eh)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 19%" />
</colgroup>
<tbody>
<tr>
<td colspan="8" style="text-align: center;"><strong>VRD: MTP =
1Eh</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">NVR</td>
<td style="text-align: center;">VRI1</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">VRIn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">6 + 2.NSPN</td>
</tr>
</tbody>
</table>

A mensagem VRD é utilizada quando o servidor deseja ler alguma
informação ou um grupo de informações (uma variável ou diversas
variáveis) do módulo. O módulo envia como resposta a mensagem VRR.

### Mensagem de Resposta à Leitura de Variáveis (VRR – 1Fh)

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr>
<td colspan="8" style="text-align: center;"><strong>VRR: MTP =
1Fh</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">NVR</td>
<td style="text-align: center;">VRI1</td>
<td style="text-align: center;">VRS1</td>
<td style="text-align: center;">VRD1</td>
<td style="text-align: center;">...</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">VRS1</td>
<td style="text-align: center;">...</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 45%" />
</colgroup>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">VRIn</td>
<td style="text-align: center;">VRSn</td>
<td style="text-align: center;">VRDn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">VRSn</td>
<td style="text-align: center;">6 + 4.NVR + VRS1 +...+ VRSn</td>
</tr>
</tbody>
</table>

A mensagem VRR é uma resposta a uma mensagem VRD e contém o valor das
variáveis requisitadas. Variáveis permanentemente indisponíveis devem
ser sinalizadas com o respectivo identificador (VRI) e o campo VRS =
0x0000, eliminando a presença do campo de dados (VRD). Variáveis
temporariamente indisponíveis, seja por falta de atualização ou mesmo
erro de leitura, devem ser sinalizadas com o valor 0xFFFF no campo VRS e
também neste caso o campo de dados deve ser omitido.

### Mensagem de Informação RDS (RDI – 20h)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 11%" />
</colgroup>
<tbody>
<tr>
<td colspan="11" style="text-align: center;"><strong>RDI: MTP =
20h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">CTC</td>
<td style="text-align: center;">RSSI</td>
<td style="text-align: center;">SNR</td>
<td style="text-align: center;">STS</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">22</td>
</tr>
</tbody>
</table>

**CTC:** Freqüência do canal atualmente sintonizado (76 a 108 MHz, em
unidades de 10 kHz).

**RSSI:** Nível de sinal recebido na freqüência sintonizada (em unidades
de dBuV, valores válidos: 0 a 127)

**SNR:** (Signal-to-noise ratio) = Relação sinal ruído na freqüência
sintonizada (em dB, valores válidos: 0 a 127).

Esta mensagem é usada para enviar ao servidor informações sobre a
freqüência RDS sintonizada. Esta mensagem pode ser enviada
periodicamente pelo módulo, caso esteja configurado para isso.
Normalmente o módulo está configurado para não enviar esta mensagem.

### Mensagem Encapsulada (ENC – 21h)

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 16%" />
</colgroup>
<tbody>
<tr>
<td colspan="7" style="text-align: center;"><strong>ENC: MTP =
21h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">PCT</td>
<td style="text-align: center;">SEM</td>
<td style="text-align: center;">ECM</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><em>SEM</em></td>
<td style="text-align: center;">8 + <em>SEM</em></td>
</tr>
</tbody>
</table>

Esta mensagem é usada para encapsular uma mensagem de qualquer protocolo
e enviá-la por meio do barramento local ou para o servidor central.
Qualquer protocolo de aplicação usado pela PST pode ser encapsulado
nesta mensagem, incluindo o próprio protocolo aberto PST OPEN.

### Mensagem de Lista de Relatórios (RPL – 22h)

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<tbody>
<tr>
<td colspan="11" style="text-align: center;"><strong>RPL: MTP =
22h</strong></td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">DTG</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">SPD</td>
<td style="text-align: center;">DSR</td>
<td style="text-align: center;">DER</td>
<td style="text-align: center;">TTR</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 35%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: center;">NRP</td>
<td style="text-align: center;">RPI1</td>
<td style="text-align: center;">SRD1</td>
<td style="text-align: center;">RPD1</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">RPIn</td>
<td style="text-align: center;">SRDn</td>
<td style="text-align: center;">RPDn</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><em>SRD1</em></td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><em>SRDn</em></td>
<td style="text-align: center;">35 + NRP*3 + SRD1 + .. + SRDn</td>
</tr>
</tbody>
</table>

A mensagem de lista de relatórios (RPL) é usada para enviar os
relatórios que são configurados no equipamento. Para maiores
informações, veja *Relatórios*.

### Mensagem de status da base LC (BSS – 23h)

### Mensagem de Status do Rastreador para Dispositivos Locais (TST – 24h)

Esta mensagem é enviada periodicamente pela porta serial e contém
informações a respeito do módulo rastreador, podendo ser utilizada por
dispositivos locais que queiram estabelecer comunicação com o servidor
e/ou com o próprio rastreador.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="12">TST: MTP = 24h</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">SPD</td>
<td style="text-align: center;">DIR</td>
<td style="text-align: center;">ALT</td>
<td style="text-align: center;">GPC</td>
<td style="text-align: center;">STS2</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td>Tamanho[Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">27</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr>
<th colspan="4">STS2</th>
</tr>
</thead>
<tbody>
<tr>
<td>Sub-campos</td>
<td>Tamanho [Bits]</td>
<td>Posição do(s) bit(s)</td>
<td>Descrição</td>
</tr>
<tr>
<td>Ignição</td>
<td>1</td>
<td>15</td>
<td>0 = desligada; 1 = ligada.</td>
</tr>
<tr>
<td rowspan="8">Estado do bloqueio do rastreador</td>
<td rowspan="8">3</td>
<td rowspan="8">12 a 14</td>
<td>000: desbloqueado</td>
</tr>
<tr>
<td style="text-align: left;">001: bloqueado pelo PAN</td>
</tr>
<tr>
<td style="text-align: left;">010: bloqueio passivo</td>
</tr>
<tr>
<td style="text-align: left;">011: bloqueado localmente</td>
</tr>
<tr>
<td style="text-align: left;">100: bloqueado pela central</td>
</tr>
<tr>
<td style="text-align: left;">101:00:00</td>
</tr>
<tr>
<td style="text-align: left;">110:00:00</td>
</tr>
<tr>
<td style="text-align: left;">111:00:00</td>
</tr>
<tr>
<td>Botão de Assistência</td>
<td>1</td>
<td>11</td>
<td>1: botão de assistência pressionado</td>
</tr>
<tr>
<td rowspan="2">Bateria Auxiliar</td>
<td rowspan="2">1</td>
<td rowspan="2">10</td>
<td>0: não está usando bateria auxiliar</td>
</tr>
<tr>
<td style="text-align: left;">1: está usando bateria auxiliar</td>
</tr>
<tr>
<td rowspan="4">Status do GPRS</td>
<td rowspan="4">2</td>
<td rowspan="4">8 e 9</td>
<td>00: Sem Cobertura GSM</td>
</tr>
<tr>
<td style="text-align: left;">01: Com GSM, sem GPRS</td>
</tr>
<tr>
<td style="text-align: left;">10: Com GSM e GPRS</td>
</tr>
<tr>
<td style="text-align: left;">11: Conexão GPRS estabelecida</td>
</tr>
<tr>
<td>Índice de Qualidade do GSM</td>
<td>4</td>
<td>4 a 7</td>
<td>Valores válidos: 0 a 15</td>
</tr>
<tr>
<td rowspan="2">Índice de Qualidade do GPS</td>
<td rowspan="2">4</td>
<td rowspan="2">0 a 3</td>
<td>Equivalente ao parâmetro HDOP do GPS</td>
</tr>
<tr>
<td style="text-align: left;">Valores válidos: 0 a 15 (satura em
15)</td>
</tr>
<tr>
<td>Tamanho Total</td>
<td colspan="3">2 Bytes</td>
</tr>
</tbody>
</table>

### Mensagem de Status da Antena Satelital para Dispositivos Locais (SST – 25h)

Esta mensagem é enviada periodicamente pela porta serial e contém
informações a respeito das condições da antena satelital que porventura
esteja conectada ao módulo rastreador.

<table style="width:100%;">
<colgroup>
<col style="width: 25%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th colspan="7" style="text-align: center;">SST: MTP = 25h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">S_MDE</td>
<td style="text-align: center;">S_AVY</td>
<td style="text-align: center;">S_MTP</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho[Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">9</td>
</tr>
</tbody>
</table>

- **S_MDE**: Modo de funcionamento da antena satelital

  - 0: Desabilitada.

  - 1: Habilitada como backup.

  - 2: Habilitada como redundância.

- **S_AVY**: Disponibilidade da antena satelital

  - 0: Indisponível.

  - 1: Disponível.

- **S_MTP**: Tipos de mensagens com permissão para envio via link
  satelital

  - Bit 0: Macros do dispositivo para a central.

  - Bit 1: Macros da central para o dispositivo.

  - Bit 2: Evento gerado pelo dispositivo local.

  - Bit 3: Comando enviado para o dispositivo local.

  - Bit 4 ao Bit 15: 0.

### Mensagem de comando para dispositivos locais (CLD – 26h)

Esta mensagem é enviada quando é necessário o envio de algum comando
para um dispositivo local.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th colspan="7" style="text-align: center;">CLD: MTP = 26h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">ID</td>
<td style="text-align: center;">PRM1</td>
<td style="text-align: center;">PRM2</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho[Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">11</td>
</tr>
</tbody>
</table>

### Mensagem de notificação gerada por dispositivos locais (NLD – 27h)

Esta mensagem é enviada por dispositivos locais para o módulo rastreador
quando há a necessidade de informar a respeito da ocorrência de algum
evento.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;">NLD: MTP = 27h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">NTP</td>
<td style="text-align: center;">PRM</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho[Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">8</td>
</tr>
</tbody>
</table>

- NTP: Tipo da notificação.

  - 01: Macro do dispositivo para a central

  - 02: Macro da central para o dispositivo

  - 03: Evento gerado pelo dispositivo local.

### Mensagem para troca de informações via link satelital (SAT – 28h)

Esta mensagem é trocada entre o módulo rastreador e dispositivos locais
para estabelecimento de comunicação entre dispositivo e servidor via
link satelital.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th colspan="12" style="text-align: center;">SAT: MTP = 28h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">S_TYP</td>
<td style="text-align: center;">ID</td>
<td style="text-align: center;">PRM1</td>
<td style="text-align: center;">PRM2</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">STS2</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho[Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">26</td>
</tr>
</tbody>
</table>

- S_TYP: Tipo da mensagem

  - 01: Macros do dispositivo para a central

  - 02: Macros da central para o dispositivo

  - 03: Evento gerado pelo dispositivo local

  - 04: Comando enviado para o dispositivo local

### Mensagem para início de transferência de arquivo (BFT – 2Ah)

Esta mensagem é enviada do servidor para o módulo rastreador para
sinalizar o início da transferência de um determinado arquivo de dados.

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;">BFT: MTP = 2Ah</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">FD</td>
<td style="text-align: center;">SZF</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho[Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">10</td>
</tr>
</tbody>
</table>

- FD: Tipo do arquivo a ser transferido (Para detalhes sobre cada tipo
  de arquivo, ver apêndice)

  - 01: Arquivo com pontos de controle para regras de segurança

  - 02: Arquivo com cercas eletrônicas para regras de segurança

  - 03: Arquivo com regras de segurança

- SZF: Tamanho total do arquivo

### Mensagem para transferência de segmento de arquivo (TFS – 2Bh)

Esta mensagem é enviada do servidor para o módulo rastreador para
transferência de um segmento de um determinado arquivo de dados.

<table style="width:100%;">
<colgroup>
<col style="width: 26%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th colspan="8" style="text-align: center;">TFS: MTP = 2Bh</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">FD</td>
<td style="text-align: center;">SFS</td>
<td style="text-align: center;">OFS</td>
<td style="text-align: center;">DFS</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho[Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">SFS</td>
<td style="text-align: center;">12+SFS</td>
</tr>
</tbody>
</table>

- FD: Tipo do arquivo a ser transferido (Para detalhes sobre cada tipo
  de arquivo, ver apêndice)

  - 01: Arquivo com pontos de controle para regras de segurança

  - 02: Arquivo com cercas eletrônicas para regras de segurança

  - 03: Arquivo com regras de segurança

- SFS: Tamanho do segmento de arquivo

- OFS: Offset do segmento de arquivo (O offset de início é sempre zero)

- DFS: Dados do segmento de arquivo

### Mensagem para verificação do arquivo transferido (CKF – 2Ch)

Esta mensagem é enviada do servidor para o módulo rastreador para
verificação do arquivo transferido.

<table>
<colgroup>
<col style="width: 29%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th colspan="7" style="text-align: center;">CKF: MTP = 2Ch</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">FD</td>
<td style="text-align: center;">SZF</td>
<td style="text-align: center;">CVD</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho[Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">12</td>
</tr>
</tbody>
</table>

- FD: Tipo do arquivo a ser transferido (Para detalhes sobre cada tipo
  de arquivo, ver apêndice).

  - 01: Arquivo com pontos de controle para regras de segurança.

  - 02: Arquivo com cercas eletrônicas para regras de segurança.

  - 03: Arquivo com regras de segurança.

- SZF: Tamanho total do arquivo.

- CVD: Código de validação do arquivo transferido. CRC de 16 bits do
  arquivo inteiro.

### Mensagem para finalização da transferência de arquivo (CFT – 2Dh)

Esta mensagem é enviada do servidor para o módulo rastreador sinalizando
que o módulo pode usar os novos dados.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th colspan="12" style="text-align: center;">CFT: MTP = 2Dh</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">NFD</td>
<td style="text-align: center;">FD</td>
<td style="text-align: center;">SZF</td>
<td style="text-align: center;">CVD</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">FD</td>
<td style="text-align: center;">SZF</td>
<td style="text-align: center;">CVD</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho[Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">6 + 7*NFD</td>
</tr>
</tbody>
</table>

- NFD: Número de tipos de arquivo.

- FD: Tipo do arquivo a ser transferido (Para detalhes sobre cada tipo
  de arquivo, ver apêndice).

  - 01: Arquivo com pontos de controle para regras de segurança.

  - 02: Arquivo com cercas eletrônicas para regras de segurança.

  - 03: Arquivo com regras de segurança.

- SZF: Tamanho total do arquivo.

- CVD: Código de validação do arquivo transferido. CRC de 16 bits do
  arquivo inteiro.

### Mensagem de Evento com Informação Adicional (EAI – 30h)

Esta mensagem é enviada entre o módulo rastreador e outro dispositivo em
ambos os sentidos e deve ser confirmado o recebimento com a mensagem
ACK(MTP=00h)

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr>
<th colspan="7" style="text-align: center;"><strong>EAI: MTP =
30h</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">DTE</td>
<td style="text-align: center;">EVT</td>
<td style="text-align: center;">EVD</td>
<td style="text-align: center;">NAI</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Variável</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr>
<th>Campo</th>
<th style="text-align: center;">AII1</th>
<th style="text-align: center;">AIS1</th>
<th style="text-align: center;">AID1</th>
<th style="text-align: center;">...</th>
<th style="text-align: center;">AIIn</th>
<th style="text-align: center;">AISn</th>
<th style="text-align: center;">AIDn</th>
<th style="text-align: center;">TOTAL</th>
</tr>
</thead>
<tbody>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><em>AIS1</em></td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><em>AISn</em></td>
<td style="text-align: center;">12+Variável+NAI*2+AIS1+...AISn</td>
</tr>
</tbody>
</table>

## Mensagens do Download Remoto

Estas mensagens são usadas para alterar remotamente o código executável
(“software embarcado”) do equipamento (isso é comumente chamado de
“atualização over-the-air”).

### Iniciar Procedimento de Download (SAD – 0Eh)

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<tbody>
<tr>
<td colspan="6" style="text-align: center;">SAD: MTP = 0Eh</td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">IP</td>
<td style="text-align: center;">PT</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">11</td>
</tr>
</tbody>
</table>

- **IP, PT**: IP e porta do servidor de download.

Esta mensagem é enviada pelo servidor ao equipamento, indicando que ele
iniciará uma sessão de download de código. O comportamento do
equipamento após receber essa mensagem depende das características dele
(alguns equipamentos provavelmente podem trabalhar normalmente durante o
procedimento de download, enquanto outros podem precisar alterar para
algum estado especial). Além disso, se o servidor de download for
diferente do servidor normal de rastreamento, o IP e a porta do servidor
de download são informados nesta mensagem. O equipamento deve responder
à esta mensagem com um ACK, para aceitar o download ou um NACK, (neste
caso, o código de resposta informará o motivo pelo qual o download não
foi aceito).

### Limpar Área de Download (EDA – 0Fh)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr>
<td colspan="5" style="text-align: center;">EDA: MTP – 0Fh</td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">BLE</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">7</td>
</tr>
</tbody>
</table>

Esta mensagem é usada para solicitar ao equipamento que apague sua área
de armazenamento de download, como forma de preparação para o início do
recebimento de um download. O equipamento deve responder a esta mensagem
com um ACK, em caso de sucesso ou um NACK (neste caso, o código de
resposta informará o motivo pelo qual não foi apagado com sucesso).

### Armazenar Segmento (SSG – 10h)

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 8%" />
<col style="width: 13%" />
</colgroup>
<tbody>
<tr>
<td colspan="8" style="text-align: center;">SSG: MTP – 10h</td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">SZS</td>
<td style="text-align: center;">IAS</td>
<td style="text-align: center;">CSG</td>
<td style="text-align: center;">SVD</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">SZS+1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">13 + SZS</td>
</tr>
</tbody>
</table>

Os campos IAS, CSG e SVD são criptografados. O algoritmo de criptografia
é uma operação XOR de todos os bytes nestes campos com o primeiro byte
do campo CSG (a operação XOR não é aplicada a este primeiro byte, já que
neste caso seu conteúdo seria perdido).

Como o código a ser baixado pode ser de tamanho grande, é melhor
dividi-lo em vários segmentos e enviar um segmento por mensagem. Esta
mensagem é usada para enviar cada segmento.

Se o equipamento aceitar o segmento, ele responderá com um ACK. O
segmento é aceito se:

- A mensagem foi recebida corretamente.

- O segmento é válido.

- O equipamento é capaz de armazenar o segmento em um lugar correto na
  área de armazenamento de download.

Se o segmento não for aceito, o equipamento responderá com um NACK,
informando a causa do problema no campo de código de resposta.

### Verificar Código (CCD – 11h)

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr>
<td colspan="8" style="text-align: center;">CCD: MTP – 11h</td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">IAC</td>
<td style="text-align: center;">SZC</td>
<td style="text-align: center;">CVD</td>
<td style="text-align: center;">CKY</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">16</td>
<td style="text-align: center;">31</td>
</tr>
</tbody>
</table>

Os campos IAC, SZC e CVD são criptografados. O algoritmo de criptografia
é uma operação XOR de todos os bytes nestes campos com o primeiro byte
do campo CKY.

Depois que todos os segmentos foram enviados ao equipamento com sucesso,
o servidor envia esta mensagem ao equipamento, a fim de que ele possa
verificar se o código completo foi recebido corretamente. O equipamento
responde a esta mensagem com um ACK se o código baixado for válido ou
com um NACK, se o código baixado for inválido (código de resposta:
falha).

### Atualizar Área do Programa (URA – 12h)

<table style="width:100%;">
<colgroup>
<col style="width: 29%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 14%" />
</colgroup>
<tbody>
<tr>
<td colspan="8" style="text-align: center;">URA: MTP – 12h</td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">CVD</td>
<td style="text-align: center;">IAD</td>
<td style="text-align: center;">SZC</td>
<td style="text-align: center;">CKY</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">16</td>
<td style="text-align: center;">31</td>
</tr>
</tbody>
</table>

Os campos CVD, IAD e SZC são criptografados. O algoritmo de criptografia
é uma operação XOR de todos os bytes nestes campos com o primeiro byte
do campo CKY.

Depois que todos os segmentos são enviados para o equipamento e a
mensagem CCD é respondida pelo equipamento com sucesso, o servidor envia
esta mensagem para indicar que o equipamento pode atualizar seu código.
Depois de receber esta mensagem, o equipamento verifica novamente a
validade do código baixado. O dispositivo responde a esta mensagem com
um ACK se o código baixado for válido ou com um NACK, se o código
baixado for inválido (código de resposta: falha). Depois de enviar o
ACK, o equipamento iniciará a atualização do código.

### Abandonar o Procedimento de Download (SOD – 13h)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr>
<td colspan="4" style="text-align: center;">SOD: MTP – 13h</td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

O servidor envia esta mensagem ao equipamento quando, por qualquer
motivo, ele quer encerrar o procedimento de download sem concluí-lo.
Depois de receber esta mensagem, o equipamento deve voltar ao modo
normal. Esta mensagem é respondida com um ACK (o equipamento não tem
nenhuma razão para negar este pedido).

### Retorno do Procedimento de Download (RTD – 1Bh)

<table>
<colgroup>
<col style="width: 38%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<tbody>
<tr>
<td colspan="6" style="text-align: center;">RTD: MTP – 1Bh</td>
</tr>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">GNI</td>
<td style="text-align: center;">RSC</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">15</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada pelo módulo ao servidor quando ele quer deixar o
procedimento de download e voltar a conectar-se com o servidor de
rastreamento. O código de resposta enviado na mensagem indica o
resultado do download (sucesso ou falha).

## Mensagens de transferência de arquivos via HTTP

O procedimento de transferência de arquivos via HTTP está descrito no
documento HTTP File Transfer Protocol.

### Novo arquivo disponível para download (NFA – 40h)

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th colspan="10" style="text-align: center;">NFA: MTP = 40h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">HSH</td>
<td style="text-align: center;">IDD</td>
<td style="text-align: center;">FEN</td>
<td style="text-align: center;">FTY</td>
<td style="text-align: center;">ECK</td>
<td style="text-align: center;">NCH</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">44</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">9</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">72</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada pelo servidor ao módulo para indicar a
existência de um novo arquivo para download no servidor HTTP. O módulo
deve confirmar o recebimento com um ACK(MTP=00h).

### Confirmação de atualização de arquivos (CDF – 31h)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">CDF: MTP = 31h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">IDD</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">15</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada pelo servidor ao módulo para que os módulos
passem a utilizar os arquivos descritos nesse download (IDD). O módulo
deve confirmar o recebimento com um ACK(MTP=00h).

### Cancelar download atual (CDC – 32h)

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">CDC: MTP = 32h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">IDD</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">15</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada pelo servidor ao módulo para cancelar a
transferência indicada pelo IDD. O módulo deve confirmar o recebimento
com um ACK(MTP=00h).

### Checar Http File (CHF – 33h)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 16%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;">CHF: MTP = 33h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">FPR</td>
<td style="text-align: center;">FTY</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">16</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada para checar se o módulo possui o arquivo
indicado em memória. O módulo deve responder com um ACK(MTP=00h) caso
tenha o arquivo, ou responder com um NACK(MTP=0Bh) caso não tenha o
arquivo.

### Nova Transferência Local (NTF – 34h)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th colspan="10" style="text-align: center;">NTF: MTP = 34h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">HSH</td>
<td style="text-align: center;">IDD</td>
<td style="text-align: center;">FEN</td>
<td style="text-align: center;">FTY</td>
<td style="text-align: center;">FPR</td>
<td style="text-align: center;">NCH</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">44</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">73</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada para indicar o início de uma nova transferência
de arquivo localmente. O módulo deve confirmar o recebimento com um
ACK(MTP=00h).

### Envio de pedaço de arquivo (SFC – 35h)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="8" style="text-align: center;">SFC: MTP = 35h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">LDC</td>
<td style="text-align: center;">SIC</td>
<td style="text-align: center;">CSZ</td>
<td style="text-align: center;">CHU</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">CSZ</td>
<td style="text-align: center;">10+CSV</td>
</tr>
</tbody>
</table>

Esta mensagem contém um pedaço do arquivo que está sendo transferido
localmente. O módulo deve confirmar o recebimento com um ACK(MTP=00h).

## Mensagens de sequenciamento de macro

### Permissão de envio de macro (RNE – 36h)

<table style="width:100%;">
<colgroup>
<col style="width: 34%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;">Requisição de Macro: MTP =
36h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">MCR</td>
<td style="text-align: center;">MTY</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">8</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada pelo teclado para o rastreador para pedir
permissão para o envio de uma macro controlada. Isso ocorre, pois,
macros com condições geográficas podem ser negadas. O módulo deve
confirmar o recebimento com um ACK(MTP=00h) caso a permissão seja
aceita, e com um NACK(MTP=0Bh) caso a permissão seja negada.

### Requisição de senha de autorização (RAP – 37h)

<table>
<colgroup>
<col style="width: 41%" />
<col style="width: 19%" />
<col style="width: 17%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th colspan="4" style="text-align: center;">RAP: MTP = 37h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada pelo teclado para o rastreador para pedir a
senha de autorização para confirmação remota. O rastreador deve
responder com a mensagem RAR(MTP=38h) descrita abaixo.

### Resposta com senha de autorização (RAR – 38h)

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;">RAR: MTP = 38h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">TKYS</td>
<td style="text-align: center;">TKY</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">TKYS</td>
<td style="text-align: center;">6 + TKYS</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada pelo rastreador para o teclado com a chave em
resposta à requisição RAP(MTP=37h)

### Checar contrassenha de autorização (CAP – 39h)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;">CAP: MTP = 39h</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td style="text-align: center;">APWS</td>
<td style="text-align: center;">APW</td>
<td style="text-align: center;">TOTAL</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">APWS</td>
<td style="text-align: center;">6 + APWS</td>
</tr>
</tbody>
</table>

Esta mensagem é enviada pelo teclado para o rastreador para pedir que o
rastreador verifique a contrassenha de autorização remota. O módulo deve
confirmar com um ACK(MTP=00h) caso a contrassenha esteja correta, ou
negar com um NACK(MTP=0Bh) caso esteja incorreta.

### Resposta a Requisição de Macro (RRM – 3Ah)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 3%" />
<col style="width: 14%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr>
<th colspan="9" style="text-align: center;">RRM: MTP = 3Ah</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SEQ</td>
<td style="text-align: center;">MTP</td>
<td>NVI</td>
<td>OPEN ID 1</td>
<td>PST PRM1 1</td>
<td>...</td>
<td>OPEN ID n</td>
<td>PST PRM1 n</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td>...</td>
<td style="text-align: right;">2</td>
<td style="text-align: right;">2</td>
</tr>
</tbody>
</table>

Essa mensagem é enviada em resposta à mensagem de Permissão de envio de
macro (MTP = 36h). Se o número de violações (NVI) é 0, os campos
seguintes não estarão presentes.

# Informação Adicional

Informação adicional é uma interessante ferramenta do protocolo PST
OPEN. Esta ferramenta permite a construção de mensagens com formato
flexível. O mecanismo básico desta ferramenta se resume à adição de
campos de informação adicional de maneira identificada às mensagens.
Pelo fato da construção desta informação adicional seguir regras, o
equipamento receptor pode facilmente interpretar a mensagem.

## Estrutura do Bloco de Informação Adicional

Um bloco de informação adicional é composto por 3 campos, descritos na
tabela a seguir:

<table>
<colgroup>
<col style="width: 42%" />
<col style="width: 19%" />
<col style="width: 19%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th colspan="4"><strong>Informação Adicional</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Campo</strong></td>
<td style="text-align: center;"><strong>AII</strong></td>
<td style="text-align: center;"><strong>AIS</strong></td>
<td style="text-align: center;"><strong>AID</strong></td>
</tr>
<tr>
<td><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><em>AIS</em></td>
</tr>
</tbody>
</table>

- **AII** é o campo que contém o identificador da informação adicional
  (1 byte).

- **AIS** é o campo que contém o tamanho da informação adicional (1
  byte).

- **AID **é o campo que contém o dado da informação adicional e seu
  tamanho é definido pelo campo ***AIS***.

Há ainda um outro campo não descrito nesta seção, mas que é parte da
estrutura da informação adicional. Trata-se do ***NAI***, Número de
Informação Adicional. Este campo define quantos blocos de informação
adicional estão sendo adicionados à mensagem. O campo NAI possui tamanho
de 1 byte e antecede os blocos de informação adicional. Se NAI=0,
significa que nenhuma informação adicional está sendo enviada na
mensagem (consequentemente, este é o último campo da mensagem). Se
NAI=2, por exemplo, significa que 2 tipos de informação adicional estão
sendo enviados na mensagem.

Um exemplo de uma mensagem que usa o mecanismo de informação adicional é
a PAI (Posição com informação adicional). A parte fixa desta mensagem
contém dados de posição do equipamento, similarmente à mensagem POS. No
entanto, diferentemente da mensagem POS, a PAI pode carregar blocos de
informação adicional, permitindo a construção de mensagens flexíveis.
Para maiores detalhes sobre estas mensagens, veja ***Erro! Fonte de
referência não encontrada.***.

**Exemplo**

A tabela abaixo mostra uma estrutura com 2 blocos de informação
adicional. O primeiro bloco contém um evento de botão de assistência e o
segundo uma informação básica de trânsito (carro de passeio com uma
velocidade média de 30 nós).

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="8"
style="text-align: center;"><strong>Exemplo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><strong>Campo</strong></td>
<td><strong>NAI</strong></td>
<td><strong>AII1</strong></td>
<td><strong>AIS1</strong></td>
<td><strong>AID1</strong></td>
<td><strong>AII2</strong></td>
<td><strong>AIS2</strong></td>
<td><strong>AID2</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Tamanho [Bytes]</strong></td>
<td>1</td>
<td>1</td>
<td>1</td>
<td><em>AIS1</em> = 3</td>
<td>1</td>
<td>1 </td>
<td><em>AIS2</em> = 2 </td>
</tr>
<tr>
<td style="text-align: left;"><strong>Valor</strong></td>
<td>0x02</td>
<td>0x01</td>
<td>0x03 </td>
<td>0x0001 0xFF</td>
<td>0x02</td>
<td>0x02</td>
<td>0x01 0x1F</td>
</tr>
</tbody>
</table>

## Identificadores de Informação Adicional

O identificador de informação adicional permite ao receptor uma
interpretação rápida e fácil do bloco de informação adicional recebido.
A tabela abaixo mostra os possíveis tipos de informação adicional.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 29%" />
<col style="width: 19%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr>
<th colspan="4" style="text-align: center;"><strong>Tabela de Tipos de
Informação Adicional</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Valor do
identificador</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tamanho do campo de dados
[Bytes]</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
</tr>
<tr>
<td style="text-align: center;">0x00</td>
<td style="text-align: center;">Reservado</td>
<td style="text-align: center;">-</td>
<td style="text-align: left;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x01</td>
<td style="text-align: center;">Evento</td>
<td style="text-align: center;">Variável</td>
<td style="text-align: left;"><a
href="http://wiki.cps.pst/wiki/lib/fckeditor/editor/tiki-index.php?page=Events%20-%20OPEN%20IAM%20Protocol">Veja</a>
<em>Eventos</em></td>
</tr>
<tr>
<td style="text-align: center;">0x02</td>
<td style="text-align: center;">Informação básica de trânsito</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Informação básica de trânsito contém
dados sobre o tipo de veículo e sua velocidade média.</td>
</tr>
<tr>
<td style="text-align: center;">0x03</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">RPM do motor do veículo.</td>
</tr>
<tr>
<td style="text-align: center;">0x04</td>
<td style="text-align: center;">Informação básica de telemetria</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;">Contém dados sobre o comportamento do
veículo relacionado a um evento específico.</td>
</tr>
<tr>
<td style="text-align: center;">0x05</td>
<td style="text-align: center;">Identificação do SIM Card</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;">Contém o número IMSI do SIM Card
inserido no equipamento.</td>
</tr>
<tr>
<td style="text-align: center;">0x06</td>
<td style="text-align: center;">Informação do acelerômetro</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Contém a informação da aceleração nos 3
eixos</td>
</tr>
<tr>
<td style="text-align: center;">0x07</td>
<td style="text-align: center;">Temperatura interna do módulo</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Contém a temperatura medida por um
sensor no interior do produto</td>
</tr>
<tr>
<td style="text-align: center;">0x08</td>
<td style="text-align: center;">Status dos sensores analógicos</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Contém o valor da grandeza medida por
determinado sensor analógico</td>
</tr>
<tr>
<td style="text-align: center;">0x09</td>
<td style="text-align: center;">Status dos sensores digitais</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Contém o status de um sensor
digital</td>
</tr>
<tr>
<td style="text-align: center;">0x0A</td>
<td style="text-align: center;">Status dos atuadores</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Contém o status de um atuador</td>
</tr>
<tr>
<td style="text-align: center;">0x0B</td>
<td style="text-align: center;">Valor do hodômetro</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Contém o valor do hodômetro do
veículo</td>
</tr>
<tr>
<td style="text-align: center;">0x0C</td>
<td style="text-align: center;">BSLE (Base Station Location
Element)</td>
<td style="text-align: center;">9</td>
<td style="text-align: center;">Contém a informação das ERBs alcançadas
pelo sinal GSM</td>
</tr>
<tr>
<td style="text-align: center;">0x0D</td>
<td style="text-align: center;">Nível da bateria interna</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Contém o nível da bateria interna do
produto</td>
</tr>
<tr>
<td style="text-align: center;">0x0E</td>
<td style="text-align: center;">Monitoração do nível da bateria
externa</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Contém informações a respeito do nível
de tensão da fonte de alimentação externa</td>
</tr>
<tr>
<td style="text-align: center;">0x0F</td>
<td style="text-align: center;">Data e hora da última BSLE válida</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Contém data e hora do último grupo de
informações das ERBs</td>
</tr>
<tr>
<td style="text-align: center;">0x10</td>
<td style="text-align: center;">Informação do GPS</td>
<td style="text-align: center;">20</td>
<td style="text-align: center;">Contém informação da posição fornecida
pelo receptor GPS</td>
</tr>
<tr>
<td style="text-align: center;">0x11</td>
<td style="text-align: center;">Velocidade do Veículo</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Contém a velocidade do veículo</td>
</tr>
<tr>
<td style="text-align: center;">0x12</td>
<td style="text-align: center;">Tempo estimado para envio da próxima
monitoração</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Contém o tempo estimado para envio da
próxima monitoração</td>
</tr>
<tr>
<td style="text-align: center;">0x13</td>
<td style="text-align: center;">Horímetro</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Contém o valor do horímetro em
segundos</td>
</tr>
<tr>
<td style="text-align: center;">0x19</td>
<td style="text-align: center;">Status da transferência Http</td>
<td style="text-align: center;">11</td>
<td style="text-align: center;">Contém IDD, FTY e LDC</td>
</tr>
<tr>
<td style="text-align: center;">0x1A</td>
<td style="text-align: center;">Status Modo Violado</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>0x00 = Não violado</p>
<p>0x01 = Violado</p></td>
</tr>
<tr>
<td style="text-align: center;">0x1B</td>
<td style="text-align: center;">Arquivos não sincronizados</td>
<td style="text-align: center;">1 + Variável</td>
<td style="text-align: center;">Indica a quantidade e quais arquivos não
estão sincronizados pelo dispositivo</td>
</tr>
<tr>
<td style="text-align: center;">0x1C</td>
<td style="text-align: center;">Estado de Macro</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Contém MCR e LMC, os valores serão 0000
caso o módulo não esteja no modo controlado.</td>
</tr>
<tr>
<td style="text-align: center;">0x80 a 0xFF</td>
<td style="text-align: center;">Reservado para Variáveis CAN</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

### Informação Básica de Trânsito – BTI

A informação básica de trânsito é usada para transmitir informação
simples sobre as condições de trânsito na área em que o veículo se
encontra. Esta informação é formada por dois campos, sendo eles o tipo
de veículo e a velocidade média, como mostra a tabela abaixo.

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th colspan="4" style="text-align: center;">0x02 - Informação Básica de
Trânsito - BTI</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">VTY</td>
<td style="text-align: center;">AVS</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

- VTY: Tipo de veículo (1 byte). Veja Tipo de Veículo e Parâmetros para
  a configuração do parâmetro.

- AVS: Velocidade média desde a última transmissão (1 byte), em nós. O
  período sobre o qual a média é calculada é o período entre as
  transmissões das mensagens de posição.

A informação básica de trânsito é uma maneira simples de prover
informação sobre o trânsito na área em que o veículo se encontra.
Basicamente, o rastreador instalado no veículo coleta valores de
velocidade e calcula as médias em cada período de transmissão. O campo
do tipo de veículo informa se, por exemplo, o veículo em questão é um
carro de passeio, uma motocicleta, um caminhão, etc.

### Rotações por Minuto – RPM

Este tipo informa o valor das RPM (rotações por minuto) do motor de um
veículo. Formado por apenas 1 campo.

<table>
<colgroup>
<col style="width: 55%" />
<col style="width: 22%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;">0x03 - Rotações por Minuto -
RPM</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

- RPM: Valor RPM do motor de um veículo (2 bytes). A faixa válida vai de
  0 a 65.535 RPM. Este campo representa o valor RPM médio calculado
  sobre um determinado número de amostras que é especificado pelo
  parâmetro “Configuração da Leitura de Rotação” (veja Parâmetros).

### Informação Básica de Telemetria - BLI

Este tipo é usado para informar as condições de direção antes e após o
acontecimento de um evento específico. Toda a informação pode ser
dividida em várias partes (uma para cada segundo de dado) e estas, por
sua vez, enviadas como blocos de informação adicional adicionadas a uma
ou mais mensagens.

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr>
<th colspan="8" style="text-align: center;">0x04 - Informação Básica de
Telemetria - BLI</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SPY</td>
<td style="text-align: center;">ROT</td>
<td style="text-align: center;">TST</td>
<td style="text-align: center;">EVT</td>
<td style="text-align: center;">EST</td>
<td style="text-align: center;">TME</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">8</td>
</tr>
</tbody>
</table>

- SPY: Valor da velocidade do veículo (1 byte). Faixa válida de 0 a 255
  nós. Este campo representa a velocidade do veículo no instante
  indicado pelo campo TME.

- ROT: Valor RPM do motor de um veículo (2 bytes). A faixa válida vai de
  0 a 65.535 RPM. Este campo representa o valor RPM no instante indicado
  pelo campo TME.

- TST: Status das entradas de telemetria (1 byte). Para maiores
  detalhes, veja **Erro! Fonte de referência não encontrada.**.

- EVT: Tipo do evento (2 bytes). Este campo define o evento ao qual a
  informação adicional enviada está relacionada. Veja Eventos.

- EST: Status do evento (1 byte). Este campo define o momento do evento:
  0 – evento não ocorrido ou 1 – evento ocorrido.

- TME: Tempo dos dados (1 byte). Faixa válida de 0 a 255 segundos. Este
  campo representa o instante antes ou após o acontecimento do evento,
  dependendo da indicação do campo EST.

### Identificação do SIM Card - SCI

Este tipo informa o número IMSI (**International Mobile Subscriber
Identity**) do SIM Card inserido no módulo. Normalmente, a mensagem que
contém este tipo de informação é enviada sempre que for estabelecida uma
conexão com o servidor.

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 21%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;">0x05 - Identificação do SIM
Card - SCI</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SCI</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">8</td>
<td style="text-align: center;">8</td>
</tr>
</tbody>
</table>

- SCI: Número IMSI (International Mobile Subscriber Identity) do SIM
  Card com 15 dígitos, enviado no formato BCD.

### Informação do acelerômetro

<table style="width:100%;">
<colgroup>
<col style="width: 39%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x06 – Informação do
acelerômetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Eixo X</td>
<td style="text-align: center;">Eixo Y</td>
<td style="text-align: center;">Eixo Z</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">6</td>
</tr>
</tbody>
</table>

- As informações em cada eixo são disponibilizadas na unidade “mg” e no
  formato de complemento de 2.

### Envio da temperatura interna do módulo

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 18%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;">0x07 - Temp. Interna do
Módulo</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">TMP</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

- TMP – Temperatura interna do módulo (número inteiro sinalizado como
  complemento de 2).

### Envio de status dos sensores analógicos

<table>
<colgroup>
<col style="width: 55%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr>
<th colspan="4" style="text-align: center;">0x08 - Sensores
Analógicos</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SNS</td>
<td style="text-align: center;">INF</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

- SNS – Número do sensor.

- INF – Valor lido do sensor (número inteiro sinalizado como complemento
  de 2).

### Envio de status dos sensores digitais

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x09 - Sensores
Digitais</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SNS</td>
<td style="text-align: center;">LGS</td>
<td style="text-align: center;">STS</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

- SNS – Número do sensor.

- LGS – Lógica do sensor (0 – Ativo em nível baixo / 1 – Ativo em nível
  alto).

- STS – Status do sensor (0 – Repouso / 1 – Acionado).

### Envio de status dos atuadores

<table>
<colgroup>
<col style="width: 45%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0A - Atuadores</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">ATD</td>
<td style="text-align: center;">LGS</td>
<td style="text-align: center;">STS</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

- ATD – Número do atuador.

- LGS – Lógica do atuador (0 – Ativo em nível baixo / 1 – Ativo em nível
  alto).

- STS – Status do atuador (0 – Repouso / 1 – Acionado).

### Envio de valor do hodômetro

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 18%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;">0x0B - Hodômetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">HOD</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

- HOD – Valor do hodômetro do veículo em metros.

### BSLE (Base Station Location Element)

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
</colgroup>
<thead>
<tr>
<th colspan="12" style="text-align: center;">0x0C - BSLE</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">MCC</td>
<td style="text-align: center;">MNC</td>
<td style="text-align: center;">LAC</td>
<td style="text-align: center;">CI</td>
<td style="text-align: center;">NCC</td>
<td style="text-align: center;">BCC</td>
<td style="text-align: center;">TAV</td>
<td style="text-align: center;">TA</td>
<td style="text-align: center;">RSSIV</td>
<td style="text-align: center;">RSSI</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bits]</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">16</td>
<td style="text-align: center;">16</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">6</td>
<td style="text-align: center;">72</td>
</tr>
</tbody>
</table>

- MCC (Mobile Country Code) – Código de identificação do país (Valor
  decimal, 3 dígitos \<0-999\>)

- MNC (Mobile Network Code) – Código de identificação da rede (Valor
  decimal, 3 dígitos \<0-999\>)

- LAC (Location Area Code) – Código de identificação da área (Valor
  hexadecimal, \<0-FFFF\>)

- CI (Cell Identity) – Identificador da célula (Valor hexadecimal,
  \<0-FFFF\>)

- NCC (Network Color Code) – Código identificador da estação rádio base
  (operadora), \<0-7\>

- BCC (Base station Color Code) – Código identificador da estação rádio
  base, \<0-7\>

- TAV – Validade do parâmetro TA (0, inválido; 1, válido).

- TA (Timing Advance) – Distância estimada, em unidades de 553,5 metros
  (Valor decimal, 2 dígitos \<0-63\>):

  - TA 0 = 0 m a 553,5 m

  - TA 1 = 553,5 m a 1107 m

  - TA 2 = 1107 m a 1660,5 m

  - :

  - TA 63 = 34,87 km a 35,42 km

- RSSIV – Validade do parâmetro RSSI (0, inválido; 1, válido).

- RSSI (Received Signal Strength Indication) – Potência do sinal
  recebido, em dBm (Valor decimal, 2 dígitos \<0-63\>):

  - RSSI 0 = menor que -110 dBm.

  - RSSI 1 = -110 dBm a -109 dBm.

  - RSSI 2 = -109 dBm a -108 dBm.

  - :

  - RSSI 62 = -49 dBm a -48 dBm.

  - RSSI 63 = maior que -48 dBm.

### Envio do nível da bateria interna

<table>
<colgroup>
<col style="width: 61%" />
<col style="width: 18%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;">0x0D – Nível da bateria
interna</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">BAT</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

- BAT – Nível da bateria interna em níveis (máximo de 200). A quantidade
  de níveis depende do dispositivo. Ficam reservados os seguintes
  indicadores:

  - 0xFD: Bateria sendo carregada

  - 0xFE: Bateria carregada

  - 0xFF: Status inválido

### Monitoração do nível da bateria externa

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 15%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0E – Nível da bateria
externa</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">OFFSET</td>
<td style="text-align: center;">VALOR</td>
<td style="text-align: center;">DUR</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">6</td>
</tr>
</tbody>
</table>

### Data e hora da última BSLE válida 

<table>
<colgroup>
<col style="width: 43%" />
<col style="width: 19%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;">0x0F – Data e hora da última
BSLE válida</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">DTB</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

- DTB – Data e hora da última informação válida contendo dados das ERBs.
  Formato Y.M.D.h.m.s.

### Informação do GPS 

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th colspan="9" style="text-align: center;">0x10 – Informação do
GPS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">DTG</td>
<td style="text-align: center;">LAT</td>
<td style="text-align: center;">LNG</td>
<td style="text-align: center;">SPD</td>
<td style="text-align: center;">DIR</td>
<td style="text-align: center;">ALT</td>
<td style="text-align: center;">GPC</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">20</td>
</tr>
</tbody>
</table>

### Velocidade do Veículo 

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 18%" />
<col style="width: 18%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th colspan="4" style="text-align: center;">0x11 – Velocidade do
veículo</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">SPD2</td>
<td style="text-align: center;">SPDS</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td style="text-align: center;">Tamanho [Bytes]</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

- SPD2: Velocidade do veículo, em km/h x 256.

- SPDS: Origem da leitura da velocidade do veículo:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">SPDS</th>
<th style="text-align: center;">Descrição</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">0x00</td>
<td>Indefinido</td>
</tr>
<tr>
<td style="text-align: center;">0x01</td>
<td>GPS</td>
</tr>
<tr>
<td style="text-align: center;">0x02</td>
<td>Sensor de velocidade</td>
</tr>
<tr>
<td style="text-align: center;">0x03</td>
<td>CAN baseado nas rodas</td>
</tr>
<tr>
<td style="text-align: center;">0x04</td>
<td>CAN baseado no tacógrafo</td>
</tr>
</tbody>
</table>

### Tempo estimado para envio da próxima monitoração 

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 19%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr>
<th colspan="3">0x12 – Tempo estimado para envio da próxima
monitoração</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">TNP</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">3</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

- TNP: Tempo estimado para envio da próxima monitoração, em segundos (De
  0 a 16777215 segundos).

### Valor do Horímetro

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 19%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr>
<th colspan="3">0x13 – Valor do Horímetro</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">HM</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

- HM: Valor do horímetro em segundos

### Status da transferência Http

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th colspan="5">0x19 – Status da transferência Http</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">IDD</td>
<td style="text-align: center;">FTY</td>
<td style="text-align: center;">LDC</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">10</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Status Modo violado

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 23%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th colspan="3">0x1A – Status modo violado</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">Status</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

Onde Status:

0x00 – Não violado

0x01 - Violado

### Arquivos não sincronizados

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 11%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="6">0x1B – Arquivos não sincronizados</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">NDF</td>
<td style="text-align: center;">FTY1</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">FTYn</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1 + NDF</td>
</tr>
</tbody>
</table>

### Estado de Macro

<table>
<colgroup>
<col style="width: 54%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th colspan="4">0x1C – Estado de Macro</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td style="text-align: center;">MCR</td>
<td style="text-align: center;">LMC</td>
<td style="text-align: center;">Total</td>
</tr>
<tr>
<td>Tamanho [Bytes]</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

# Eventos

Os eventos são uma característica muito importante do protocolo PST
OPEN. Os eventos são utilizados pelos equipamentos de campo para
informar ao servidor ou a outros equipamentos a ocorrência de alguma
condição que está sob monitoramento constante. Por exemplo, um evento de
alerta de velocidade é utilizado para informar que o carro está acima do
limite de velocidade estabelecido (neste caso, o rastreador instalado no
carro está constantemente monitorando a velocidade do carro e, quando o
limite é ultrapassado, o rastreador gera o evento). Os eventos são
assíncronos e são transmitidos (para o servidor, por exemplo)
imediatamente após a sua ocorrência.

## Estrutura do evento

A estrutura de um evento é mostrada na figura abaixo.

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 22%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;"><strong>Estrutura do
evento</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Campo</strong></td>
<td style="text-align: center;"><strong>EVT</strong></td>
<td style="text-align: center;"><strong>EVD</strong></td>
</tr>
<tr>
<td><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Variável</td>
</tr>
</tbody>
</table>

- EVT: Tipo do evento (2 bytes). Este campo define o tipo do evento. Os
  tipos de eventos são definidos na tabela de tipos de eventos nesta
  seção.

- EVD: Dados do evento (tamanho variável). Este campo contém os dados
  sobre o evento. O seu tamanho depende do tipo do evento, conforme
  mostrado na tabela de tipos de eventos.

## Reportando eventos

Os eventos são reportados utilizando o mecanismo de informação adicional
(veja *Informação Adicional*). Quando um evento deve ser reportado, a
informação do evento é organizada em uma estrutura de evento e então
anexada a uma mensagem que usa o mecanismo de informação adicional.
Normalmente, a mensagem usada para este fim é a ***PAI*** (Posição com
informações adicionais). A figura abaixo mostra como a estrutura do
evento é combinada com a informação adicional.

<table style="width:100%;">
<colgroup>
<col style="width: 39%" />
<col style="width: 15%" />
<col style="width: 14%" />
<col style="width: 13%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Informação adicional
- Evento</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Campo</strong></td>
<td style="text-align: center;"><strong>AII</strong></td>
<td style="text-align: center;"><strong>AIS</strong></td>
<td style="text-align: center;"><strong>EVT</strong></td>
<td style="text-align: center;"><strong>EVD</strong></td>
</tr>
<tr>
<td><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">n</td>
</tr>
<tr>
<td><strong>Valor</strong></td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">2+n</td>
<td style="text-align: center;">...</td>
<td style="text-align: center;">...</td>
</tr>
</tbody>
</table>

Neste caso, o campo ***AID*** da estrutura de informação adicional
contém a estrutura do evento, que é formada pelos campos ***EVT*** e
***EVD***. O campo ***AIS*** contém o tamanho da estrutura do evento.
Portanto, o tamanho de ***EVD*** pode ser calculado como (***AIS** -
2*).

*Importante*: A mensagem ***POS*** pode ser utilizada para relatar os
tipos de eventos na faixa de 0x0000 a 0x001F. Os eventos dentro desta
faixa devem ter apenas 1 ou nenhum byte de dado do evento. A mensagem
***POS*** descreve o evento dentro dessa faixa enviando apenas o byte
menos significativo do tipo de evento e 1 byte do dado do evento. Isso é
necessário por razões de compatibilidade, já que ***POS*** é uma
mensagem de formato fixo e, quando foi criada, o objetivo era o de
relatar os eventos usando sempre 2 bytes. Como o sistema evoluiu e esta
regra de reportar de eventos com 2 bytes era muito restritiva, o
protocolo tornou-se mais flexível com a criação da mensagem ***PAI***,
enquanto a mensagem ***POS*** manteve essa restrição.

## Tabela de tipos de eventos

A tabela abaixo mostra os tipos de eventos atualmente existentes no
sistema. Esta tabela fornece apenas uma breve descrição do evento. Para
alguns eventos, uma melhor descrição é fornecida abaixo da tabela ou no
link dado.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 39%" />
<col style="width: 36%" />
<col style="width: 13%" />
</colgroup>
<tbody>
<tr>
<td colspan="4" style="text-align: center;"><strong>Tabela de tipos de
eventos</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Tipo de evento</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Dados do evento</strong></td>
<td style="text-align: center;"><strong>Tamanho dos dados do evento
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">0x0000</td>
<td style="text-align: center;">Nenhum evento (envia uma mensagem
normal)</td>
<td style="text-align: center;">0xFF (0xFF significa valor
indefinido)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0001</td>
<td style="text-align: center;">Botão de assistência pressionado</td>
<td style="text-align: center;">0xFF ou número do botão</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0002</td>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x0003</td>
<td style="text-align: center;">Teste de produção</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0004</td>
<td style="text-align: center;">Movimento com ignição desligada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0005</td>
<td style="text-align: center;">Porta aberta fora do ponto de
controle</td>
<td style="text-align: center;">Valor das entradas de alarmes</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0006</td>
<td style="text-align: center;">Acionamento das luzes de emergência</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0007</td>
<td style="text-align: center;">PAN</td>
<td style="text-align: center;">Tipo do evento PAN</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0008</td>
<td style="text-align: center;">Bateria backup acionada</td>
<td style="text-align: center;">0xFF ou tensão da bateria backup (em
unidades de 0.2 V)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0009</td>
<td style="text-align: center;">Limite de velocidade excedido</td>
<td style="text-align: center;">Valor da velocidade (em nós)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x000A</td>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x000B</td>
<td style="text-align: center;">Sensor de movimento acionado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x000C</td>
<td style="text-align: center;">Entrada em ponto de controle</td>
<td style="text-align: center;">Número do ponto de controle (CPN)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x000D</td>
<td style="text-align: center;">Saída de ponto de controle</td>
<td style="text-align: center;">Número do ponto de controle (CPN)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x000E</td>
<td style="text-align: center;">Entrada em cerca eletrônica</td>
<td style="text-align: center;">Número da cerca eletrônica (GFN)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x000F</td>
<td style="text-align: center;">Saída de cerca eletrônica</td>
<td style="text-align: center;">Número da cerca eletrônica (GFN)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0010</td>
<td style="text-align: center;">Erro do GPS</td>
<td style="text-align: center;"><p>0: Reservado</p>
<p>1: No Comm (sem comunicação com o módulo GPS)</p>
<p>2: No Fix (a posição não pode ser calculada)</p>
<p>3 a 255: Disponível para uso futuro</p></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0011</td>
<td style="text-align: center;">Ignição foi ligada</td>
<td style="text-align: center;">0xFF ou tensão da ignição (em unidades
de 0.2 V)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0012</td>
<td style="text-align: center;">Ignição foi desligada</td>
<td style="text-align: center;">0xFF ou tensão da ignição (em unidades
de 0.2 V)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0013</td>
<td style="text-align: center;">Fonte principal entrou em uso</td>
<td style="text-align: center;">0xFF ou tensão da bateria principal (em
unidades de 0.2 V)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0014</td>
<td style="text-align: center;">Excesso de aceleração <em><strong>(*não
deve ser usado para novos projetos)</strong></em></td>
<td style="text-align: center;">Valor da aceleração, em m/s<sup>2</sup>
(-128 to 127)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0015</td>
<td style="text-align: center;">Mensagem de atualização de hodômetro
(viagem em curso)</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0016</td>
<td style="text-align: center;">Hodômetro de final de viagem</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0017</td>
<td style="text-align: center;">Antena GPS externa conectada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0018</td>
<td style="text-align: center;">Antena GPS externa desconectada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0019</td>
<td style="text-align: center;">Jamming GPS iniciado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x001A</td>
<td style="text-align: center;">Jamming GPS concluído</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x001B</td>
<td style="text-align: center;">Erro de hardware GPS</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x001C</td>
<td style="text-align: center;">Falha de sinal GPS</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x001D</td>
<td style="text-align: center;">Detecção de Jamming GPS iniciada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x001E</td>
<td style="text-align: center;">Detecção de Jamming GPS concluído</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x001F</td>
<td style="text-align: center;">GPS Assistido requerido</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0020</td>
<td style="text-align: center;">Limpador de para-brisa ligado</td>
<td style="text-align: center;">0xFF (informa que o limpador de
para-brisa foi ligado).</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0021</td>
<td style="text-align: center;">Limpador de para-brisa desligado</td>
<td style="text-align: center;">Informa que o limpador de para-brisa foi
desligado</td>
<td style="text-align: center;">16</td>
</tr>
<tr>
<td style="text-align: center;">0x0022</td>
<td style="text-align: center;">Freio motor acionado</td>
<td style="text-align: center;">0xFF (informa que o freio motor foi
acionado)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0023</td>
<td style="text-align: center;">Freio motor liberado</td>
<td style="text-align: center;">Informa que o freio motor foi
liberado</td>
<td style="text-align: center;">16</td>
</tr>
<tr>
<td style="text-align: center;">0x0024</td>
<td style="text-align: center;">Freio de serviço acionado</td>
<td style="text-align: center;">0xFF (Informa que o freio de serviço foi
acionado).</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0025</td>
<td style="text-align: center;">Freio de serviço liberado</td>
<td style="text-align: center;">Informa que o freio de serviço foi
liberado</td>
<td style="text-align: center;">16</td>
</tr>
<tr>
<td style="text-align: center;">0x0026</td>
<td style="text-align: center;">Veículo (motor) parado com ignição
ligada</td>
<td style="text-align: center;">0xFF (Informa que o tempo limite do
motor parado com ignição ligada expirou).</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0027</td>
<td style="text-align: center;">Veículo (motor) parado com ignição
ligada totalizado</td>
<td style="text-align: center;">Informa o fim do período com motor
parado e ignição ligada</td>
<td style="text-align: center;">16</td>
</tr>
<tr>
<td style="text-align: center;">0x0028</td>
<td style="text-align: center;">Excesso de marcha lenta atingido</td>
<td style="text-align: center;">0xFF (Informa que o tempo limite do
motor na condição de marcha lenta expirou)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0029</td>
<td style="text-align: center;">Excesso de marcha lenta atingido
totalizado</td>
<td style="text-align: center;">Informa o fim do período com o motor na
condição de marcha lenta</td>
<td style="text-align: center;">16</td>
</tr>
<tr>
<td style="text-align: center;">0x002A</td>
<td style="text-align: center;">Motor com rotação em neutro
atingido</td>
<td style="text-align: center;">0xFF (Informa que o motor está operando
em condição neutra)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x002B</td>
<td style="text-align: center;">Motor com rotação em neutro atingido
totalizado</td>
<td style="text-align: center;">Informa o fim do período com motor
operando na condição neutra.</td>
<td style="text-align: center;">16</td>
</tr>
<tr>
<td style="text-align: center;">0x002C</td>
<td style="text-align: center;">Limite de RPM excedido</td>
<td style="text-align: center;">0xFF (Informa que o limite de RPM
(rotações por minuto) foi excedido</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x002D</td>
<td style="text-align: center;">Limite de RPM excedido totalizado</td>
<td style="text-align: center;">Informa o fim do limite de RPM
excedido</td>
<td style="text-align: center;">18</td>
</tr>
<tr>
<td style="text-align: center;">0x002E</td>
<td style="text-align: center;">Limite de RPM excedido com limpador de
para-brisa ligado</td>
<td style="text-align: center;">0xFF (Informa que o limite de RPM
(rotações por minuto) com limpador de para-brisa lidado foi
excedido)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x002F</td>
<td style="text-align: center;">Fim do limite de RPM excedido com
limpador de para-brisa ligado</td>
<td style="text-align: center;">Informa o fim do limite de RPM excedido
com limpador de para-brisa ligado</td>
<td style="text-align: center;">18</td>
</tr>
<tr>
<td style="text-align: center;">0x0030</td>
<td style="text-align: center;">Limite de RPM excedido com freio motor
acionado</td>
<td style="text-align: center;">0xFF (Informa que o limite de RPM
(rotações por minuto) com freio motor acionado foi excedido)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0031</td>
<td style="text-align: center;">Fim do limite de RPM excedido com freio
motor acionado</td>
<td style="text-align: center;">Informa o fim do limite de RPM excedido
com freio motor acionado</td>
<td style="text-align: center;">18</td>
</tr>
<tr>
<td style="text-align: center;">0x0032</td>
<td style="text-align: center;">Limite de velocidade atingido com baixa
rotação (“banguela”)</td>
<td style="text-align: center;">0xFF (Informa que o limite de velocidade
foi atingido na condição de baixa rotação)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0033</td>
<td style="text-align: center;">Fim do limite de velocidade atingido com
baixa rotação (“banguela”)</td>
<td style="text-align: center;">Informa o fim do limite de velocidade
atingido na condição de baixa rotação</td>
<td style="text-align: center;">17</td>
</tr>
<tr>
<td style="text-align: center;">0x0034</td>
<td style="text-align: center;">Limite de velocidade especial
atingido</td>
<td style="text-align: center;">0xFF (Informa que o limite de velocidade
especial foi atingido)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0035</td>
<td style="text-align: center;">Limite de velocidade especial
concluído</td>
<td style="text-align: center;">Informa o fim do limite de velocidade
especial</td>
<td style="text-align: center;">17</td>
</tr>
<tr>
<td style="text-align: center;">0x0036</td>
<td style="text-align: center;">Limite de velocidade atingido com
limpador de para-brisa ligado</td>
<td style="text-align: center;">0xFF (Informa que o limite de velocidade
com limpador de para-brisa ligado foi atingido)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0037</td>
<td style="text-align: center;">Fim do limite de velocidade atingido com
limpador de para-brisa ligado</td>
<td style="text-align: center;">Informa o fim do limite de velocidade
atingido com limpador de para-brisa</td>
<td style="text-align: center;">17</td>
</tr>
<tr>
<td style="text-align: center;">0x0038</td>
<td style="text-align: center;">Sensor de velocidade habilitado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0039</td>
<td style="text-align: center;">Sensor de velocidade desabilitado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x003A</td>
<td style="text-align: center;">Configuração de hodômetro</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">9</td>
</tr>
<tr>
<td style="text-align: center;">0x003B</td>
<td style="text-align: center;">Velocidade CAN habilitada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x003C</td>
<td style="text-align: center;">Velocidade CAN desabilitada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x003D</td>
<td style="text-align: center;">Limite de velocidade ultrapassado (com
precisão)</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x003E</td>
<td style="text-align: center;">Vibração</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x003F</td>
<td style="text-align: center;">Movimento <em>Tilt</em></td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0040</td>
<td style="text-align: center;">Aceleração brusca</td>
<td style="text-align: center;">Informa que o limite de aceleração foi
excedido</td>
<td style="text-align: center;">17</td>
</tr>
<tr>
<td style="text-align: center;">0x0041</td>
<td style="text-align: center;">Freada brusca</td>
<td style="text-align: center;">Informa que o limite de frenagem brusca
foi excedido</td>
<td style="text-align: center;">17</td>
</tr>
<tr>
<td style="text-align: center;">0x0042</td>
<td style="text-align: center;">Freada muito brusca</td>
<td style="text-align: center;">Informa que o limite de frenagem muito
brusca foi excedido</td>
<td style="text-align: center;">17</td>
</tr>
<tr>
<td style="text-align: center;">0x0043</td>
<td style="text-align: center;">Bloqueio de veículo</td>
<td style="text-align: center;">0xFF (Informa que o veículo foi
bloqueado)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0044</td>
<td style="text-align: center;">Desbloqueio de veículo</td>
<td style="text-align: center;">0xFF (Informa que o veículo foi
desbloqueado)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0045</td>
<td style="text-align: center;">Sensor de violação</td>
<td style="text-align: center;">0xFF (Informa que o sensor foi
violado)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0046</td>
<td style="text-align: center;">Início de movimento por
acelerômetro</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0047</td>
<td style="text-align: center;">Fim de movimento por acelerômetro</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0048</td>
<td style="text-align: center;">Início de alerta de excesso de
velocidade a seco</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0049</td>
<td style="text-align: center;">Fim de alerta de excesso de velocidade a
seco</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x004A</td>
<td style="text-align: center;">Início de alerta de excesso de
velocidade sob chuva</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x004B</td>
<td style="text-align: center;">Fim de alerta de excesso de velocidade
sob chuva</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x004C</td>
<td style="text-align: center;">Velocidade abaixo de um determinado
valor</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x004D</td>
<td style="text-align: center;">Velocidade acima de um determinado
valor</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x004E a 0x004F</td>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x0050</td>
<td style="text-align: center;">Detecção de SIM CARD</td>
<td style="text-align: center;">Informa que SIM Card foi detectado</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">0x0051</td>
<td style="text-align: center;">Falha de SIM CARD</td>
<td style="text-align: center;">Informa falha no SIM card</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">0x0052</td>
<td style="text-align: center;">Troca de SIM CARD</td>
<td style="text-align: center;">Informa a troca de SIM card</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">0x0053</td>
<td style="text-align: center;">Chaveamento de operadora</td>
<td style="text-align: center;">Informa o chaveamento de operadora</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">0x0054 a 0x005F</td>
<td style="text-align: center;">Reservado para o produto ELD</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x0060</td>
<td style="text-align: center;">Casamento da antena satelital</td>
<td style="text-align: center;">Informa o casamento de uma antena
satelital</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0061</td>
<td style="text-align: center;">Desconexão da antena satelital</td>
<td style="text-align: center;">Informa a desconexão da antena
satelital</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0062</td>
<td style="text-align: center;">Início de uso da antena satelital</td>
<td style="text-align: center;">Informa o início de uso da antena
satelital</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0063</td>
<td style="text-align: center;">Fim de uso da antena satelital</td>
<td style="text-align: center;">Informa o fim de uso da antena
satelital</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0064</td>
<td style="text-align: center;">Alerta de poucos créditos</td>
<td style="text-align: center;">Informa que há poucos créditos na antena
satelital</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0065</td>
<td style="text-align: center;">Erro na antena satelital</td>
<td style="text-align: center;">Informa erro na antena satelital</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0066</td>
<td style="text-align: center;">Fim dos créditos da antena
satelital</td>
<td style="text-align: center;">Informa o fim dos créditos da antena
satelital</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0067</td>
<td style="text-align: center;">Início de uso de créditos do
período</td>
<td style="text-align: center;">Informa o início do uso de créditos do
período</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0068</td>
<td style="text-align: center;">Inserção de créditos na antena
satelital</td>
<td style="text-align: center;">Informa a inserção de créditos na antena
satelital</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0069 a 0x006F</td>
<td style="text-align: center;">Reservado para o produto ELD</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x0070</td>
<td style="text-align: center;">Valor mínimo da entrada analógica
ultrapassado para baixo</td>
<td style="text-align: center;">Informa se o valor mínimo da entrada foi
ultrapassado para baixo</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0071</td>
<td style="text-align: center;">Valor mínimo da entrada analógica
ultrapassado para cima</td>
<td style="text-align: center;">Informa se o valor mínimo da entrada foi
ultrapassado para cima</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0072</td>
<td style="text-align: center;">Valor máximo de entrada analógica
ultrapassado para cima</td>
<td style="text-align: center;">Informa se o valor máximo da entrada foi
ultrapassado para cima</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0073</td>
<td style="text-align: center;">Valor máximo de entrada analógica
ultrapassado para baixo</td>
<td style="text-align: center;">Informa se o valor máximo da entrada foi
ultrapassado para baixo</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0074</td>
<td style="text-align: center;">Saída da faixa ideal para baixo do valor
da entrada analógica</td>
<td style="text-align: center;">Informa se o valor passou a estar abaixo
da faixa ideal</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0075</td>
<td style="text-align: center;">Entrada na faixa ideal por baixo do
valor da entrada analógica</td>
<td style="text-align: center;">Informa se o valor superou o limite
inferior da faixa ideal</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0076</td>
<td style="text-align: center;">Saída da faixa ideal para cima do valor
da entrada analógica</td>
<td style="text-align: center;">Informa se o valor passou a estar acima
da faixa ideal</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0077</td>
<td style="text-align: center;">Entrada na faixa ideal por cima do valor
da entrada analógica</td>
<td style="text-align: center;">Informa se o valor passou a estar abaixo
do limite superior da faixa ideal</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0078</td>
<td style="text-align: center;">Falha no sensor analógico</td>
<td style="text-align: center;">Informa se houve alguma falha no
sensor</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0079</td>
<td style="text-align: center;">Variação máxima do sensor analógico
atingida</td>
<td style="text-align: center;">Informa se a variação do sensor
analógico atingiu o valor máximo</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x007A</td>
<td style="text-align: center;">Sensor digital acionado</td>
<td style="text-align: center;">Informa se um sensor digital foi
acionado</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x007B</td>
<td style="text-align: center;">Sensor digital desacionado</td>
<td style="text-align: center;">Informa se um sensor digital foi
desacionado</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x007C</td>
<td style="text-align: center;">Tempo máximo de sensor digital acionado
atingido</td>
<td style="text-align: center;">Informa se o sensor digital ficou
acionado pelo tempo máximo</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x007D</td>
<td style="text-align: center;">Atuador acionado</td>
<td style="text-align: center;">Informa se um atuador foi acionado</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x007E</td>
<td style="text-align: center;">Atuador desacionado</td>
<td style="text-align: center;">Informa se um atuador foi
desacionado</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x007F</td>
<td style="text-align: center;">Firmware atualizado (Novo)</td>
<td style="text-align: center;">Informa modelo, versão de hardware,
versão de software e versão de bootloader</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">0x0080</td>
<td style="text-align: center;">Modo de segurança ativado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0081</td>
<td style="text-align: center;">Modo de segurança desativado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0082</td>
<td style="text-align: center;">Movimento indevido</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0083</td>
<td style="text-align: center;">Horário indevido</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0084</td>
<td style="text-align: center;">Excesso de tempo parado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0085</td>
<td style="text-align: center;">Âncora ativada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0086</td>
<td style="text-align: center;">Âncora desativada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0087</td>
<td style="text-align: center;">Entrada em âncora</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0088</td>
<td style="text-align: center;">Saída de âncora</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0089</td>
<td style="text-align: center;">Escrita de parâmetro</td>
<td style="text-align: center;">Informa se um parâmetro foi escrito</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x008A</td>
<td style="text-align: center;">Evento de início de Horímetro</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x008B</td>
<td style="text-align: center;">Evento de fim de Horímetro</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x008C</td>
<td style="text-align: center;">Evento de limiar de Horímetro
ultrapassado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x008D</td>
<td style="text-align: center;">Evento de nível mínimo da bateria
externa atingido</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x008E</td>
<td style="text-align: center;">Evento de nível máximo da bateria
externa atingido</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x008F</td>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x0090</td>
<td style="text-align: center;">Conexão de teclado</td>
<td style="text-align: center;">Informa se um teclado foi conectado ao
rastreador</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0091</td>
<td style="text-align: center;">Desconexão de teclado</td>
<td style="text-align: center;">Informa se o teclado foi desconectado do
rastreador</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0092</td>
<td style="text-align: center;">Senha de coação</td>
<td style="text-align: center;">Informa que a senha de coação foi
utilizada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0093</td>
<td style="text-align: center;">Ativação da Liberação do Bloqueio</td>
<td style="text-align: center;">Informa que a liberação do bloqueio foi
ativada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0094</td>
<td style="text-align: center;">Desativação da liberação do
bloqueio</td>
<td style="text-align: center;">Informa que a liberação do bloqueio foi
desativada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0095</td>
<td style="text-align: center;">Ativação da liberação da trava baú
1</td>
<td style="text-align: center;">Informa que a liberação da trava baú 1
foi ativada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0096</td>
<td style="text-align: center;">Desativação da Liberação da Trava de Baú
1</td>
<td style="text-align: center;">Informa que a liberação da trava baú 1
foi desativada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0097</td>
<td style="text-align: center;">Ativação da Liberação da Trava de Baú
2</td>
<td style="text-align: center;">Informa que a liberação da trava baú 2
foi ativada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0098</td>
<td style="text-align: center;">Desativação da Liberação da Trava de Baú
2</td>
<td style="text-align: center;">Informa que a liberação da trava baú 2
foi desativada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0099</td>
<td style="text-align: center;">Ativação da Liberação da Trava de Baú
3</td>
<td style="text-align: center;">Informa que a liberação da trava baú 3
foi ativada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x009A</td>
<td style="text-align: center;">Desativação da Liberação da Trava de Baú
3</td>
<td style="text-align: center;">Informa que a liberação da trava baú 3
foi desativada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x009B</td>
<td style="text-align: center;">Ativação da Liberação da Trava de Quinta
Roda</td>
<td style="text-align: center;">Informa que a liberação da trava de
quinta roda 1 foi ativada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x009C</td>
<td style="text-align: center;">Desativação da Liberação da Trava de
Quinta Roda</td>
<td style="text-align: center;">Informa que a liberação da trava de
quinta roda foi desativada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x009D</td>
<td style="text-align: center;">Login de Motorista por teclado</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x009E</td>
<td style="text-align: center;">Logout de Motorista por teclado</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x009F</td>
<td style="text-align: center;">Conexão de um RFID</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x00A0</td>
<td style="text-align: center;">Desconexão de um RFID</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x00A1</td>
<td style="text-align: center;">Leitura de cartão de um RFID</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x00A2</td>
<td style="text-align: center;">Sincronização de FD</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x00A3</td>
<td style="text-align: center;">Login de Motorista (Universal)</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">2+n</td>
</tr>
<tr>
<td style="text-align: center;">0x00A4</td>
<td style="text-align: center;">Logout de Motorista (Universal)</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">2+n</td>
</tr>
<tr>
<td style="text-align: center;">0x00A5</td>
<td style="text-align: center;">Limite velocidade com baixa RPM
concluído</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x00A6</td>
<td style="text-align: center;">Limite de velocidade especial
concluído</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x00A7</td>
<td style="text-align: center;">Limite de velocidade com limpador de
para-brisa concluído</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x00A8</td>
<td style="text-align: center;">Evento PND "Heart Beat"</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x00A9 a 0x00AF</td>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x00B0</td>
<td style="text-align: center;">Entrada em ponto de controle</td>
<td style="text-align: center;">Informa entrada em um ponto de
controle</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00B1</td>
<td style="text-align: center;">Saída de ponto de controle</td>
<td style="text-align: center;">Informa saída de um ponto de
controle</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00B2</td>
<td style="text-align: center;">Entrada em cerca eletrônica</td>
<td style="text-align: center;">Informa entrada em cerca eletrônica</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00B3</td>
<td style="text-align: center;">Saída de cerca eletrônica</td>
<td style="text-align: center;">Informa saída de cerca eletrônica</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00B4</td>
<td style="text-align: center;">Entrada em grupo de pontos de
controle</td>
<td style="text-align: center;">Informa entrada em grupo de pontos de
controle</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00B5</td>
<td style="text-align: center;">Saída de grupo de pontos de
controle</td>
<td style="text-align: center;">Informa saída de grupo de pontos de
controle</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00B6</td>
<td style="text-align: center;">Entrada em grupo de cercas
eletrônicas</td>
<td style="text-align: center;">Informa entrada em grupo de cercas
eletrônicas</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00B7</td>
<td style="text-align: center;">Saída de grupo de cercas
eletrônicas</td>
<td style="text-align: center;">Informa saída de grupo de cercas
eletrônicas</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00B8</td>
<td style="text-align: center;">Regra de segurança</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00B9 a 0x00CF</td>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x00D0</td>
<td style="text-align: center;">Disponibilização de sensor
analógico</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00D1</td>
<td style="text-align: center;">Indisponibilização de sensor
analógico</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00D2</td>
<td style="text-align: center;">Disponibilização de sensor digital</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00D3</td>
<td style="text-align: center;">Indisponibilização de sensor
digital</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00D4</td>
<td style="text-align: center;">Disponibilização de atuador</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00D5</td>
<td style="text-align: center;">Indisponibilização de atuador</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00D6 a 0x00DF</td>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x00E0 a 0x00EF</td>
<td style="text-align: center;">Reservado para ELD</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x00F0 a 0x0100</td>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x0101 a 0x01FF</td>
<td style="text-align: center;">Transferência de arquivo concluída</td>
<td style="text-align: center;">Informa o final de uma transferência de
arquivo</td>
<td style="text-align: center;">6</td>
</tr>
<tr>
<td style="text-align: center;">0x0200</td>
<td style="text-align: center;">Dispositivo ligado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0201</td>
<td style="text-align: center;">Dispositivo desligado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0202</td>
<td style="text-align: center;">Auto-teste</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0203</td>
<td style="text-align: center;">Configuração local</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0204</td>
<td style="text-align: center;">Fonte externa conectada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0205</td>
<td style="text-align: center;">Fonte externa desconectada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0206</td>
<td style="text-align: center;">Conexão USB</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0207</td>
<td style="text-align: center;">Desconexão USB</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0208</td>
<td style="text-align: center;">Escuta aberta</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0209</td>
<td style="text-align: center;">Escuta fechada</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x020A</td>
<td style="text-align: center;">Buzzer acionado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x020B</td>
<td style="text-align: center;">Buzzer desacionado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x020C</td>
<td style="text-align: center;">Bateria baixa</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x020D</td>
<td style="text-align: center;">Acoplamento do dispositivo
(violação)</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x020E</td>
<td style="text-align: center;">Desacoplamento do dispositivo
(violação)</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x020F</td>
<td style="text-align: center;">Modo de emergência ativado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0210</td>
<td style="text-align: center;">Modo de emergência desativado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0211</td>
<td style="text-align: center;">Chamada recebida</td>
<td style="text-align: center;">Informa que dispositivo recebeu uma
chamada</td>
<td style="text-align: center;">24</td>
</tr>
<tr>
<td style="text-align: center;">0x0212</td>
<td style="text-align: center;">Mensagem recebida na porta serial</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0213</td>
<td style="text-align: center;">Transferência Http Concluída</td>
<td style="text-align: center;">Informa IDD</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">0x0214</td>
<td style="text-align: center;">Erro na transferência HTTP</td>
<td style="text-align: center;">Informa IDD, FTY e TEC</td>
<td style="text-align: center;">12</td>
</tr>
<tr>
<td style="text-align: center;">0x0215</td>
<td style="text-align: center;">Arquivos HTTP atualizados</td>
<td style="text-align: center;">Informa IDD</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">0x0216</td>
<td style="text-align: center;">Arquivo Http Baixado</td>
<td style="text-align: center;">Informa IDD e FTY</td>
<td style="text-align: center;">11</td>
</tr>
<tr>
<td style="text-align: center;">0x0217</td>
<td style="text-align: center;">Início Modo Violado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0218</td>
<td style="text-align: center;">Fim Modo Violado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0219</td>
<td style="text-align: center;">Mudança de Estado Modo Controlado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x021A</td>
<td style="text-align: center;">Macro Enviada</td>
<td style="text-align: center;">Informa MID, MTY</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x021B</td>
<td style="text-align: center;">Sincronismo de arquivos HTTP do
dispositivo</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x021C</td>
<td style="text-align: center;">Dessincronismo de arquivos HTTP do
dispositivo</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x021D a 0x021F</td>
<td style="text-align: center;">Livre (Reservado para transferência
HTTP)</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x0220</td>
<td style="text-align: center;">Botão pressionado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0221</td>
<td style="text-align: center;">Sensor de luminosidade habilitado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0222</td>
<td style="text-align: center;">Sensor de luminosidade desabilitado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0223</td>
<td style="text-align: center;">Sensor de luminosidade acionado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0224</td>
<td style="text-align: center;">Sensor de luminosidade desacionado</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0225 a 0x07FF</td>
<td style="text-align: center;">Livre</td>
<td style="text-align: center;"></td>
<td style="text-align: center;"></td>
</tr>
</tbody>
</table>

## Eventos de Telemetria

### Eventos de 0x0021 a 0x002B (os ímpares)

Estes eventos são enviados no final de um período durante o qual uma
determinada condição foi mantida. Esses eventos podem ser configurados
através dos respectivos parâmetros de configuração de eventos (veja
*Parâmetros* - 0x005C a 0x0061). Os dados são descritos na tabela
abaixo.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 49%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>EVD - Dados dos
Eventos de 0x0021 a 0x002B (os ímpares)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Este é o intervalo de tempo durante o
qual o evento ocorreu.</p>
<p>Faixa válida: 0 a 65.535 segundos</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor da velocidade máxima atingida
durante o evento.</p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor RPM lido no momento da
velocidade máxima atingida.</p>
<p>Faixa válida: 0 a 65.535 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Valor RPM máximo alcançado durante o
evento.</p>
<p>Faixa válida: 0 a 65.535 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;"><p>Valor da velocidade lida no momento
do valor RPM máximo atingido.</p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;"><p>Hodômetro total inicial (início do
evento).</p>
<p>Faixa válida: 0 a 4M km</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">metros</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;"><p>Hodômetro total final (fim do
evento).</p>
<p>Faixa válida: 0 a 4M km</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">metros</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">16</td>
</tr>
<tr>
<td colspan="5" style="text-align: center;"><strong>Campos opcionais
(para novos projetos)</strong></td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;"><p>Valor RPM mínimo alcançado durante o
evento.</p>
<p>Faixa válida: 0 a 65.535 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td style="text-align: center;"><p>Valor RPM médio durante a ocorrência
do evento.</p>
<p>Faixa válida: 0 a 65.535 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: center;"><p>Valor da velocidade mínima atingida
durante o evento.</p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td style="text-align: center;"><p>Valor da velocidade média durante a
ocorrência do evento.</p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">22</td>
</tr>
</tbody>
</table>

### Eventos do tipo RPM (0x002D / 0x002F / 0x0031)

Estes eventos são enviados no final de um período durante o qual um
limite de rotação foi excedido. Esses eventos podem ser configurados
através dos respectivos parâmetros de configuração de eventos (veja
*Parâmetros* - 0x0062 to 0x0064). Os dados desses eventos são formados
por 8 campos, de acordo com a tabela abaixo.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 50%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>EVD - Dados dos
Eventos do tipo RPM (0x002D / 0x002F / 0x0031)</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Este é o intervalo de tempo durante o
qual o evento ocorreu.</p>
<p>Faixa válida: 0 a 65.535 segundos</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor da velocidade máxima atingida
durante a ocorrência do evento.</p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor RPM lido no momento da
velocidade máxima atingida.</p>
<p>Faixa válida: 0 a 65.535 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Valor RPM máximo alcançado durante a
ocorrência do evento.</p>
<p>Faixa válida: 0 a 65.535 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;"><p>Valor da velocidade lida no momento
do valor RPM máximo atingido.</p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;"><p>Hodômetro total inicial (início do
evento).</p>
<p>Faixa válida: 0 a 4M km</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">metros</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;"><p>Hodômetro total final (fim do
evento).</p>
<p>Faixa válida: 0 a 4M km</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">metros</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;"><p>Valor limite de RPM considerado por
este evento.</p>
<p>Faixa válida: 0 a 65.535 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">18</td>
</tr>
</tbody>
</table>

### Eventos do tipo velocidade (0x0033 / 0x0035 / 0x0037)

Estes eventos são enviados no final de um período durante o qual um
limite de velocidade foi excedido. Esses eventos podem ser configurados
através dos respectivos parâmetros de configuração de eventos (veja
*Parâmetros* - 0x0065 to 0x0067). Os dados desse evento são formados por
8 campos, como mostra a tabela abaixo.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 49%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>EVD - Dados dos
Eventos do tipo velocidade (0x0033 / 0x0035 / 0x0037)</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Este é o intervalo de tempo durante o
qual o evento ocorreu.</p>
<p>Faixa válida: 0 a 65.535 segundos</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor da velocidade máxima atingida
durante a ocorrência do evento.</p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor RPM lido no momento da
velocidade máxima atingida.</p>
<p>Faixa válida: 0 a 65.535 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Valor RPM máximo alcançado durante a
ocorrência do evento.</p>
<p>Faixa válida: 0 a 65.535 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;"><p>Valor da velocidade lida no momento
do valor RPM máximo atingido.</p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;"><p>Hodômetro total inicial (início do
evento).</p>
<p>Faixa válida: 0 a 4M km</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">metros</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;"><p>Hodômetro total final (fim do
evento).</p>
<p>Faixa válida: 0 a 4M km</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">metros</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;"><p>Valor limite de velocidade
considerado por este evento.</p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">17</td>
</tr>
</tbody>
</table>

### Eventos de aceleração brusca, freada brusca e freada muito brusca (0x0040 / 0x0041 / 0x0042)

Esses eventos são utilizados para informar que limites de aceleração ou
de freada foram excedidos. Esses eventos podem ser configurados através
dos respectivos parâmetros de configuração de eventos (veja
*Parâmetros* - 0x0070 to 0x0072). Os dados desses eventos são formados
por 8 campos, de acordo com a tabela abaixo.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 50%" />
<col style="width: 15%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>EVD - Dados dos
Eventos de acelerômetro (0x0040 / 0x0041 / 0x0042)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Este é o intervalo de tempo durante o
qual o evento ocorreu.</p>
<p>Faixa válida: 0 a 65.535 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor da aceleração (ou
desaceleração) máxima atingida durante a ocorrência do evento.</p>
<p>Faixa válida: 0 a 65.535 cm/s<sup>2</sup></p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">cm/s<sup>2</sup></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor RPM máximo alcançado durante a
ocorrência do evento.</p>
<p>Faixa válida: 0 a 65.535 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Valor da velocidade inicial (início
do evento). </p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;"><p>Valor da velocidade final (fim do
evento). </p>
<p>Faixa válida: 0 a 255 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;"><p>Hodômetro total inicial (início do
evento).</p>
<p>Faixa válida: 0 a 4M km</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">metros</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;"><p>Hodômetro total final (fim do
evento).</p>
<p>Faixa válida: 0 a 4M km</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">metros</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;"><p>O valor limite de aceleração (ou
desaceleração) considerado por este evento.</p>
<p>Faixa válida: 0 a 65.535 cm/s<sup>2</sup></p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">cm/s<sup>2</sup></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">17</td>
</tr>
</tbody>
</table>

## Evento de atualização de firmware

**Envio**: Sempre que houver uma atualização de firmware do rastreador.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x000A - Evento de
atualização de firmware</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

## Eventos de pontos de controle e cercas eletrônicas

### Evento de entrada em ponto de controle

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x000C - Evento de
entrada em ponto de controle</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do ponto</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de saída de ponto de controle

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 39%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x000D - Evento de
saída de ponto de controle</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do ponto</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de entrada em cerca eletrônica

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x000E - Evento de
entrada em cerca eletrônica</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número da cerca</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de saída de cerca eletrônica

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x000F - Evento de
saída de cerca eletrônica</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número da cerca</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

## Eventos relacionados ao GPS

### Evento de antena externa de GPS conectada

**Envio**: Sempre que uma antena externa de GPS for conectada.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0017 - Evento de
antena externa de GPS conectada</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de antena externa de GPS desconectada

**Envio**: Sempre que uma antena externa de GPS for desconectada.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0018 - Evento de
antena externa de GPS desconectada</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de início da detecção de jammer GPS

**Envio**: Sempre que houver a notificação de detecção de jammer.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0019 - Evento de
início da detecção de jammer GPS</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de fim da detecção de jammer GPS

**Envio**: Sempre que a notificação de detecção de jammer cessar.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x001A - Evento de
fim da detecção de jammer GPS</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de falha no hardware GPS

**Envio**: Sempre que a comunicação com o hardware GPS apresentar
problemas.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x001B - Evento de
falha no hardware GPS</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de falha do sinal GPS

**Envio**: Sempre que o sinal de GPS estiver inválido.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x001C - Evento de
falha do sinal GPS</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de requisição de dados AGPS Online

**Envio**: Sempre que os limites para requisição de dados forem
atingidos.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x001F - Evento de
requisição de dados AGPS Online</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

## Eventos relacionados ao GSM

### Evento de início da detecção de jammer GSM

**Envio**: Sempre que houver a notificação de detecção de jammer.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x001D - Evento de
início da detecção de jammer GSM</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de fim da detecção de jammer GSM

**Envio**: Sempre que a notificação de detecção de jammer cessar.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x001E - Evento de
fim da detecção de jammer GSM</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

## Outros Eventos

### Evento de configuração de hodômetro

**Envio**: Sempre que houver uma configuração do valor do hodômetro.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x003A - Evento de
configuração de hodômetro</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Tipo da configuração</p>
<p>0: Local (Teclado)</p>
<p>1: Remota (Over-the-air)</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Antigo valor do hodômetro</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">m</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Novo valor do hodômetro</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">m</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">9</td>
</tr>
</tbody>
</table>

### Evento de início de velocidade obtida via CAN

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x003B - Evento de
início de velocidade obtida via CAN</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de fim de velocidade obtida via CAN

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x003C - Evento de
fim de velocidade obtida via CAN</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de limite de velocidade ultrapassado (com precisão)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x003D- Evento de
limite de velocidade ultrapassado (com precisão)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Valor da velocidade no momento da
infração</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Km/h x 256</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

### Evento de bloqueio de veículo

**Envio**: Sempre que houver o acionamento da saída de bloqueio.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0043 - Evento de
bloqueio de veículo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de desbloqueio de veículo

**Envio**: Sempre que houver o desacionamento da saída de bloqueio.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0044 - Evento de
desbloqueio de veículo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de escrita de parâmetro

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0089 - Evento de
escrita de parâmetro</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Indíce do parâmetro enviado</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

## Eventos relacionados ao acelerômetro

### Evento de início de movimento por acelerômetro

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0046 - Evento de
início de movimento por acelerômetro</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de fim de movimento por acelerômetro

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5"><strong>0x0047 - Evento de fim de movimento por
acelerômetro</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td>1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

## Eventos relacionados ao uso de dois SIM CARDs

### Evento de detecção de SIM CARD

**Envio**: Sempre que for detectado um SIM CARD em uma posição do
"holder" antes vazia ou não funcional.

<table style="width:100%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 36%" />
<col style="width: 24%" />
<col style="width: 10%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0050 - Evento de
detecção de SIM CARD</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Código da Operadora</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">IMSI do SIM CARD (Formato BCD)</td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Informação adicional</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">10</td>
</tr>
</tbody>
</table>

### Evento de falha de SIM CARD

**Envio**: Sempre que for detectada falha na inicialização ou no
registro do SIM CARD.

<table style="width:100%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 36%" />
<col style="width: 24%" />
<col style="width: 10%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0051 - Evento de
falha de SIM CARD</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Código da Operadora</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">IMSI do SIM CARD (Formato BCD)</td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Informação adicional</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">10</td>
</tr>
</tbody>
</table>

### Evento de troca de SIM CARD

**Envio**: Sempre que for detectada uma operadora diferente daquela
antes detectada para aquela posição do "holder".

<table style="width:100%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 36%" />
<col style="width: 24%" />
<col style="width: 10%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0052 - Evento de
troca de SIM CARD</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Código da Operadora</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">IMSI do SIM CARD (Formato BCD)</td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Informação adicional</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">10</td>
</tr>
</tbody>
</table>

### Evento informando chaveamento de operadora

**Envio**: Sempre que houver um chaveamento de um SIM CARD para o outro.

<table style="width:100%;">
<colgroup>
<col style="width: 8%" />
<col style="width: 36%" />
<col style="width: 24%" />
<col style="width: 10%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0053 - Evento de
chaveamento de operadora</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Código da Operadora</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">IMSI do SIM CARD (Formato BCD)</td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Informação adicional</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">10</td>
</tr>
</tbody>
</table>

**<u>Informação Adicional</u>**

<table>
<colgroup>
<col style="width: 78%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Informação
adicional</strong></th>
<th style="text-align: center;"><strong>Código</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Não definido</td>
<td style="text-align: center;">0x00</td>
</tr>
<tr>
<td>Falha na inicialização do SIM CARD</td>
<td style="text-align: center;">0x01</td>
</tr>
<tr>
<td>Falha no registro do SIM CARD</td>
<td style="text-align: center;">0x02</td>
</tr>
<tr>
<td>Falha de cobertura da operadora</td>
<td style="text-align: center;">0x03</td>
</tr>
<tr>
<td>Envio de "PING"</td>
<td style="text-align: center;">0x04</td>
</tr>
<tr>
<td>Retorno de envio de "PING"</td>
<td style="text-align: center;">0x05</td>
</tr>
<tr>
<td>Tempo máximo de uso do SIM CARD secundário</td>
<td style="text-align: center;">0x06</td>
</tr>
</tbody>
</table>

**<u>  
</u>**

## Eventos relacionados à antena satelital

### Evento de casamento da antena satelital

**Envio**: Sempre que houver uma nova antena instalada ou em caso de
troca de antena.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0060 - Evento de
casamento da antena satelital</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da antena (ISN)</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Fabricante/Modelo da antena</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Firmware da antena</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Controle do byte de status do sinal</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Status do sinal (Traffic Channel,
GPS)<br />
*Bit 0 - GPS<br />
*Bit 1 - Traffic Channel</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Quantidade de bytes disponíveis</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de desconexão da antena satelital

**Envio**: Em caso de não recebimento de resposta ao "ping" do módulo,
servindo para identificar a retirada ou violação da antena. Antes do
envio do evento o módulo deve enviar um comando para reset da antena, se
estiver disponível.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0061 - Evento de
desconexão da antena satelital</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da antena (ISN)</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Fabricante/Modelo da antena</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Firmware da antena</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Controle do byte de status do sinal</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Status do sinal (Traffic Channel,
GPS)<br />
*Bit 0 - GPS<br />
*Bit 1 - Traffic Channel</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Quantidade de bytes disponíveis</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de início de uso da antena satelital

**Envio**: Sempre que for iniciada uma transmissão via antena satelital.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0062 - Evento de
início de uso da antena satelital</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da antena (ISN)</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Fabricante/Modelo da antena</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Firmware da antena</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Controle do byte de status do sinal</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Status do sinal (Traffic Channel,
GPS)<br />
*Bit 0 - GPS<br />
*Bit 1 - Traffic Channel</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Quantidade de bytes disponíveis</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de fim de uso da antena satelital

**Envio**: Sempre que for finalizada uma transmissão via antena
satelital.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0063 - Evento de
fim de uso da antena satelital</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da antena (ISN)</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Fabricante/Modelo da antena</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Firmware da antena</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Controle do byte de status do sinal</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Status do sinal (Traffic Channel,
GPS)<br />
*Bit 0 - GPS<br />
*Bit 1 - Traffic Channel</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Quantidade de bytes disponíveis</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de alerta de poucos créditos

**Envio**: Sempre que for atingido o limite configurado para este alerta
(parâmetro 0x008D).

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0064 - Evento de
alerta de poucos créditos</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da antena (ISN)</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Fabricante/Modelo da antena</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Firmware da antena</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Controle do byte de status do sinal</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Status do sinal (Traffic Channel,
GPS)<br />
*Bit 0 - GPS<br />
*Bit 1 - Traffic Channel</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Quantidade de bytes disponíveis</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de erro na antena satelital

**Envio**: Sempre que for houver falha no GPS ou no link satelital da
antena (envio a cada 10 minutos, em caso de persistência do erro).

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0065 - Evento de
erro na antena satelital</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da antena (ISN)</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Fabricante/Modelo da antena</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Firmware da antena</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Controle do byte de status do sinal</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Status do sinal (Traffic Channel,
GPS)<br />
*Bit 0 - GPS<br />
*Bit 1 - Traffic Channel</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Quantidade de bytes disponíveis</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de alerta de fim dos créditos

**Envio**: Sempre que o saldo de créditos (pacote + adicionais) chegar a
zero.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0066 - Evento de
alerta de fim dos créditos</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da antena (ISN)</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Fabricante/Modelo da antena</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Firmware da antena</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Controle do byte de status do sinal</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Status do sinal (Traffic Channel,
GPS)<br />
*Bit 0 - GPS<br />
*Bit 1 - Traffic Channel</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Quantidade de bytes disponíveis</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de início de uso de créditos do período

**Envio**: Sempre que for iniciado um novo período.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0067 - Evento de
início de uso de créditos do período</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da antena (ISN)</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Fabricante/Modelo da antena</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Firmware da antena</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Controle do byte de status do sinal</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Status do sinal (Traffic Channel,
GPS)<br />
*Bit 0 - GPS<br />
*Bit 1 - Traffic Channel</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Quantidade de bytes disponíveis</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de inserção de créditos

**Envio**: Sempre que houver inserção de novos créditos.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0068 - Evento de
inserção de créditos</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da antena (ISN)</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Fabricante/Modelo da antena</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Firmware da antena</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Controle do byte de status do sinal</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Status do sinal (Traffic Channel,
GPS)<br />
*Bit 0 - GPS<br />
*Bit 1 - Traffic Channel</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Quantidade de bytes disponíveis</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

## Eventos relacionados aos sensores analógicos

### Evento de valor mínimo ultrapassado

**Envio**: Sempre que o valor lido pelo sensor ficar abaixo do valor
mínimo configurado.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0070 - Evento de
valor mínimo ultrapassado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor analógico</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor limite considerado</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor no momento do evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

### Evento de retorno de valor mínimo ultrapassado

**Envio**: Sempre que o valor lido pelo sensor voltar a ficar acima do
valor mínimo configurado.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0071 - Evento de
retorno de valor mínimo ultrapassado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor analógico</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor limite considerado</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor no momento do evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Tempo de duração do evento</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Valor mínimo durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Valor máximo durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Valor médio durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de valor máximo ultrapassado

**Envio**: Sempre que o valor lido pelo sensor ultrapassar o valor
máximo configurado.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0072 - Evento de
valor máximo ultrapassado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor analógico</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor limite considerado</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor no momento do evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

### Evento de retorno de valor máximo ultrapassado

**Envio**: Sempre que o valor lido pelo sensor voltar a ficar abaixo do
valor máximo configurado.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0073 - Evento de
retorno de valor máximo ultrapassado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor analógico</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor limite considerado</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor no momento do evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Tempo de duração do evento</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Valor mínimo durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Valor máximo durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Valor médio durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de saída da faixa ideal para baixo

**Envio**: Sempre que o valor lido pelo sensor ficar abaixo da faixa
ideal configurada.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0074 - Evento de
saída da faixa ideal para baixo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor analógico</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor limite considerado</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor no momento do evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

### Evento de entrada na faixa ideal por baixo

**Envio**: Sempre que o valor lido pelo sensor voltar para a faixa ideal
após ter ficado abaixo dela.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0075 - Evento de
entrada na faixa ideal por baixo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor analógico</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor limite considerado</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor no momento do evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Tempo de duração do evento</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Valor mínimo durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Valor máximo durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Valor médio durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de saída da faixa ideal para cima

**Envio**: Sempre que o valor lido pelo sensor ficar acima da faixa
ideal configurada.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0076 - Evento de
saída da faixa ideal para cima</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor analógico</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor limite considerado</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor no momento do evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

### Evento de entrada na faixa ideal por cima

**Envio**: Sempre que o valor lido pelo sensor voltar para a faixa ideal
após ter ficado acima dela.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0077 - Evento de
entrada na faixa ideal por cima</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor analógico</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor limite considerado</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor no momento do evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Tempo de duração do evento</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Valor mínimo durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Valor máximo durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Valor médio durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

### Evento de falha do sensor

**Envio**: Sempre que o sensor apresentar uma falha (zero ou saturação).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0078 - Evento de
falha do sensor</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor analógico</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor limite considerado</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor no momento do evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

### Evento de variação máxima atingida

**Envio**: Sempre que o sensor apresentar uma variação maior do que
aquela configurada para um determinado intervalo de tempo.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0079 - Evento de
variação máxima atingida</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor analógico</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor limite considerado</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor no momento do evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Tempo de duração do evento</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Valor mínimo durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Valor máximo durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Valor médio durante o evento</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;"></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

## Eventos relacionados aos sensores digitais

### Evento de sensor digital acionado

**Envio**: Sempre que o sensor sair da condição de repouso.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x003F - Evento de
sensor digital acionado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor digital</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Lógica do sensor</p>
<p>0: Ativo em nível baixo</p>
<p>1: Ativo em nível alto</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

### Evento de sensor digital desacionado

**Envio**: Sempre que o sensor retornar à condição de repouso.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x007B - Evento de
sensor digital desacionado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor digital</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Lógica do sensor</p>
<p>0: Ativo em nível baixo</p>
<p>1: Ativo em nível alto</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Tempo de duração do evento</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de tempo máximo de sensor digital acionado atingido

**Envio**: Sempre que o sensor digital permanecer acionado por um tempo
maior que o permitido.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x007C - Evento de
tempo máximo de sensor digital acionado atingido</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor digital</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Lógica do sensor</p>
<p>0: Ativo em nível baixo</p>
<p>1: Ativo em nível alto</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Tempo de duração do evento</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

## Eventos relacionados aos atuadores

### Evento de atuador acionado

**Envio**: Sempre que o atuador sair da condição de repouso
(acionamento).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 38%" />
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5"><strong>0x007D - Evento de atuador
acionado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Campo</strong></td>
<td><strong>Significado</strong></td>
<td><strong>Tipo do dado</strong></td>
<td><strong>Unidade</strong></td>
<td><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td>1</td>
<td>Número do atuador</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td><p>Lógica do atuador</p>
<p>0: Ativo em nível baixo</p>
<p>1: Ativo em nível alto</p>
<p>2: PWM</p></td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;"><strong>Total</strong></td>
<td>2</td>
</tr>
</tbody>
</table>

### Evento de atuador desacionado

**Envio**: Sempre que o atuador retornar à condição de repouso.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x007E - Evento de
atuador desacionado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do atuador</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Lógica do atuador</p>
<p>0: Ativo em nível baixo</p>
<p>1: Ativo em nível alto</p>
<p>2: PWM</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Tempo de duração do evento</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

## Eventos relacionados ao modo de segurança

### Evento de modo de segurança ativado

**Envio**: Sempre que o módulo for configurado para modo de segurança.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0080 - Evento de
modo de segurança ativado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de modo de segurança desativado

**Envio**: Sempre que o módulo for retirado do modo de segurança.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0081 - Evento de
modo carga de segurança</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de movimento indevido

**Envio**: Sempre que for constatado um movimento indevido.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0082 - Evento de
movimento indevido</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de horário indevido

**Envio**: Sempre que for constatado o uso do veículo em horário
indevido.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0083 - Evento de
horário indevido</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de excesso de tempo parado

**Envio**: Sempre que for constatado excesso de tempo parado.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0084 - Evento de
excesso de tempo parado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de âncora ativada

**Envio**: Sempre que o módulo receber um comando para ativar âncora.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0085 - Evento
âncora ativada</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de âncora desativada

**Envio**: Sempre que o módulo receber um comando para desativar âncora.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0086 - Evento de
âncora desativada</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de entrada em âncora

**Envio**: Sempre que for constatada entrada em âncora.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0087 - Evento de
entrada em âncora</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de saída de âncora

**Envio**: Sempre que for constatada a saída da âncora.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0088 - Evento de
saída de âncora</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;"><strong>Total</strong></td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Eventos relacionados ao teclado

### Evento de conexão de teclado

**Envio**: Sempre que um teclado for detectado.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0090 - Evento de
conexão de teclado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Indentificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de desconexão de teclado

**Envio**: Sempre que um teclado for desconectado.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0091 - Evento de
desconexão de teclado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Indentificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de senha de coação

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0092 - Evento de
senha de coação</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Indentificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Ativação da Liberação do Bloqueio

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0093 - Evento de
Ativação da Liberação do Bloqueio</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Desativação da Liberação do Bloqueio

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0094 - Evento de
Desativação da Liberação do Bloqueio</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Ativação da Liberação da Trava Baú 1

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0095 - Evento de
Ativação da Liberação da Trava Baú 1</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Desativação da Liberação da Trava Baú 1

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0096 - Evento de
Desativação da Liberação da Trava Baú 1</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Ativação da Liberação da Trava Baú 2

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0097 - Evento de
Ativação da Liberação da Trava Baú 2</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Desativação da Liberação da Trava Baú 2

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0098 - Evento de
Desativação da Liberação da Trava Baú 2</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Ativação da Liberação da Trava Baú 3

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0099 - Evento de
Ativação da Liberação da Trava Baú 3</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Desativação da Liberação da Trava Baú 3

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x009A - Evento de
Desativação da Liberação da Trava Baú 3</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Ativação da Liberação da Trava de Quinta Roda

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x009B - Evento de
Ativação da Liberação da Trava de Quinta Roda</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Desativação da Liberação da Trava de Quinta Roda

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x009C - Evento de
Desativação da Liberação da Trava de Quinta Roda</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Login de Motorista

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x009D - Evento de
Login de Motorista</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

### Evento de Logout de Motorista

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x009E - Evento de
Logout de Motorista</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

## Eventos relacionados às regras de segurança

### Evento de entrada em ponto de controle

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00B0 - Evento de
entrada em ponto de controle</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do ponto</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

### Evento de saída de ponto de controle

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00B1 - Evento de
saída de ponto de controle</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do ponto</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

### Evento de entrada em cerca eletrônica

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00B2 - Evento de
entrada em cerca eletrônica</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da cerca</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

### Evento de saída de cerca eletrônica

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00B3 - Evento de
saída de cerca eletrônica</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da cerca</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

### Evento de entrada em grupo de pontos de controle

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00B4 - Evento de
entrada em grupo de pontos de controle</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do grupo</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

### Evento de saída de grupo de pontos de controle

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00B5 - Evento de
saída de grupo de pontos de controle</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do grupo</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

### Evento de entrada em grupo de cercas eletrônicas

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00B6 - Evento de
entrada em grupo de cercas eletrônicas</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Indentificação do grupo</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

### Evento de saída de grupo de cercas eletrônicas

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00B7 - Evento de
saída de grupo de cercas eletrônicas</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do grupo</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

### Evento de regra de segurança

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00B8 - Evento de
regra de segurança</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação da regra executada</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

## Eventos relacionados à disponibilização de sensores e atuadores

### Evento de disponibilização de sensor analógico

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00D0 - Evento de
disponibilização de sensor analógico</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de indisponibilização de sensor analógico

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00D1 - Evento de
indisponibilização de sensor analógico</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de disponibilização de sensor digital

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00D2 - Evento de
disponibilização de sensor digital</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de indisponibilização de sensor digital

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00D3 - Evento de
indisponibilização de sensor digital</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de disponibilização de atuador

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00D4 - Evento de
disponibilização de atuador</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de indisponibilização de atuador

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x00D5 - Evento de
indisponibilização de atuador</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número do sensor</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

## Eventos relacionados à transferência de arquivos

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0101 a 0x01FF -
Evento de transferência de arquivo concluída</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tamanho total do arquivo</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Código de validação do arquivo</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">7</td>
</tr>
</tbody>
</table>

**Evento 0x0101 -\> Tipo de arquivo 1** (Arquivo com pontos de controle
para regras de segurança)

**Evento 0x0102 -\> Tipo de arquivo 2** (Arquivo com cercas eletrônicas
para regras de segurança)

**Evento 0x0103 -\> Tipo de arquivo 3** (Arquivo com regras de
segurança)

.

.

.

**Evento 0x01XX -\> Tipo de arquivo XX**

## Eventos relacionados ao rastreador ISCA

### Evento de dispositivo ligado

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0200 - Evento de
dispositivo ligado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de dispositivo desligado

**Envio**:

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0201 - Evento de
dispositivo desligado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de auto-teste

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0202 - Evento de
auto-teste</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de configuração local

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0203 - Evento de
configuração local</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de fonte externa conectada

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0204 - Evento de
fonte externa conectada</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de fonte externa desconectada

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0205 - Evento de
fonte externa desconectada</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de conexão USB

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0206 - Evento de
conexão USB</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de desconexão USB

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0207 - Evento de
desconexão USB</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de escuta aberta

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0208 - Evento de
escuta aberta</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de escuta fechada

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0209 - Evento de
escuta fechada</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de buzzer acionado

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x020A - Evento de
buzzer acionado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de buzzer desacionado

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x020B - Evento de
buzzer desacionado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de nível baixo de bateria

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x020C - Evento de
nível baixo de bateria</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de acoplamento de dispositivo (violação)

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x020D - Evento de
acomplamento de dispositivo (violação)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de desacoplamento de dispositivo (violação)

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x020E - Evento de
desacomplamento de dispositivo (violação)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de modo de emergência ativado

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x020F - Evento de
modo de emergência ativado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Motivo:</p>
<p>0x01 – Botão do usuário</p>
<p>0x02 – Botão de desacoplamento (violação)</p>
<p>0x03 – Jammer GSM</p>
<p>0x04 – Jammer GPS</p>
<p>0x05 – Comando</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de modo de emergência desativado

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0210 - Evento de
modo de emergência desativado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Motivo:</p>
<p>0x01 – Botão do usuário</p>
<p>0x02 – Botão de desacoplamento (violação)</p>
<p>0x03 – Jammer GSM</p>
<p>0x04 – Jammer GPS</p>
<p>0x05 – Comando</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Evento de chamada recebida

**Envio:**

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0211 - Evento de
chamada recebida</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Data e hora de início da chamada.
Formato: Y.M.D.h.m.s.</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Data e hora de término da chamada.
Formato: Y.M.D.h.m.s.</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Número do telefone que originou a
chamada.no formato BCD:</p>
<p>DDI+DDD+Número</p>
<p>DDI: 3 dígitos</p>
<p>DDD:3 dígitos</p>
<p>Número: 10 dígitos</p>
<p>Exemplo: 0550110998765432</p>
<p>(MSB) 0x05 0x50 0x11 0x09 0x98</p>
<p>0x76 0x54 0x32 (LSB)</p></td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">IMSI do SIM CARD que recebeu a chamada
(Formato BCD)</td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">24</td>
</tr>
</tbody>
</table>

## Eventos de transferência de arquivos por Http

### Transferência Http Concluída

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0213 - Evento
transferência Http concluída</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">IDD</td>
<td style="text-align: center;">Array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">10</td>
</tr>
</tbody>
</table>

### Erro na transferência Http

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0214 – Erro na
transferência Http</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">IDD</td>
<td style="text-align: center;">Array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">FTY</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">TEC</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">12</td>
</tr>
</tbody>
</table>

### Arquivos Http atualizados

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0215 – Arquivos
Http atualizados</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">IDD</td>
<td style="text-align: center;">Array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">10</td>
</tr>
</tbody>
</table>

### Arquivo Http baixado

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0216 - Evento
arquivo Http baixado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">IDD</td>
<td style="text-align: center;">Array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">FTY</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">11</td>
</tr>
</tbody>
</table>

### Evento de sincronismo de arquivos HTTP do dispositivo

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 38%" />
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x021B - Evento de
sincronismo de arquivos HTTP do dispositivo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

Esse evento pode ser enviado do rastreador para o dispositivo para
informar que o dispositivo se encontra sincronizado.

### Evento de dessincronismo de arquivos HTTP do dispositivo

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 38%" />
<col style="width: 16%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x021C - Evento de
dessincronismo de arquivos HTTP do dispositivo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

Esse evento pode ser enviado do rastreador para o dispositivo para
informar que o dispositivo se encontra dessincronizado. Pode também ser
enviado do dispositivo para o rastreador caso o dispositivo não tenha
certeza de seu sincronismo. Esse evento então irá disparar uma checagem
de sincronismo entre o dispositivo e o rastreador.

## Eventos de sequenciamento de macros

### Início Modo Violado

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0217 - Início Modo
Violado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

Deve ser enviado ao servidor toda vez que o rastreador entrar no modo
violado.

### Fim Modo violado

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0218 - Fim Modo
Violado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Identificação do teclado</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

Deve ser enviado ao servidor toda vez que o rastreador entrar no modo
violado.

### Mudança de Estado do Modo Controlado

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 41%" />
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x0219 – Mudança de
Estado Modo Controlado</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">0xFF</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

### Macro Enviada

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 19%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>0x021A – Macro
Enviada</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">MID</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">MTY</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

Este evento é enviado pelo Teclado para informar que uma Macro(e seu
tipo) foi enviada.

# Parâmetros

Os equipamentos do sistema de rastreamento possuem uma série de
parâmetros que podem ser lidos e/ou escritos. Esses parâmetros são
usados para controlar ou configurar os equipamentos. Cada parâmetro é
acessado por meio de índices e sub-índices. Os sub-índices são usados
para acessar uma determinada instância do parâmetro. Por exemplo, para
acessar o ponto de controle 6, o índice a ser utilizado é 0x002D e o
sub-índice é 6. A primeira instância de cada parâmetro é acessada
através de um sub-índice (a faixa de valores do sub-índice vai de 1 a
65.535). O sub-índice 1 deve ser usado para acessar os parâmetros que
possuem apenas uma instância. A mensagem de leitura de parâmetro
(**PRD**) pode usar sub-índice 0 para requisitar a leitura de todas as
instâncias do parâmetro.

A tabela a seguir mostra os parâmetros que são atualmente considerados
no sistema. Esta tabela fornece apenas uma breve descrição dos
parâmetros. Para alguns parâmetros uma melhor descrição é fornecida após
a tabela ou no link fornecido.

## Tabela de parâmetros

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 67%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="4"
style="text-align: center;"><strong>Parâmetros</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Índice</strong></td>
<td style="text-align: center;"><strong>Tipo</strong></td>
<td style="text-align: center;"><strong>Parâmetro</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">0x0000 a 0x001F</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">Reservado</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x0020</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">IDN – Número de identificação do
equipamento</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0021</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;"><p>Informações Gerais:</p>
<ul>
<li><p>Tipo de equipamento (2 bytes)</p></li>
<li><p>Versão de hardware (2 bytes)</p></li>
<li><p>Versão de software (2 bytes)</p></li>
<li><p>Versão de <em>Bootloader</em> (2 bytes)</p></li>
</ul></td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">0x0022</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">Marca de teste e instalação</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0023</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do envio de eventos de GSM
(jammer)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0024</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para configuração do envio de
eventos de GPS</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0025</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><em>Debounce</em> para leitura de tensão
da fonte principal, em milissegundos. Valor mínimo: 10 ms. Valor padrão:
10000 ms.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0026</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Precisão do GPS (HDOP). O valor máximo
da precisão do GPS (HDOP) abaixo do qual a coordenada é considerada
válida. Valor padrão: 6.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0027</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração de evento PAN:</p>
<ul>
<li><p>Identificador PAN (1 byte)</p></li>
<li><p>Dado PAN (1 byte)</p></li>
<li><p>Máscara para dado do PAN (1 byte)</p></li>
<li><p>Bits de configuração (1 byte):</p></li>
</ul>
<ul>
<li><p>Bit 7: envia mensagem imediatamente na ocorrência do
evento</p></li>
<li><p>Bit 6: envia mensagem imediatamente na ausência de evento (1
minuto)</p></li>
<li><p>Bit 5: envia mensagem por SMS</p></li>
<li><p>Bit 4: Habilita a espera de 1 minuto antes de enviar o
evento</p></li>
<li><p>Bits de 3 a 0: disponíveis para uso futuro</p></li>
</ul></td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0028</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Tempo de <em>debounce</em> para os
pontos de controle, em segundos. Este é o intervalo de tempo que o
equipamento aguarda para confirmar o evento de ponto de controle. Valor
padrão: 10 s.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0029</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: left;">Tempo de
<em>debounce</em> para cercas eletrônicas, em segundos. Este é o
intervalo de tempo que o equipamento aguarda para confirmar o evento
de cerca eletrônica. Valor padrão: 10s.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x002A</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">DCT: Tempo de desconexão na ausência de
tráfego, em minutos. É o intervalo de tolerância sem tráfego no canal
GPRS antes que seja gerada uma desconexão. Valor padrão: 2 minutos.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x002B</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">SCA: Centro de serviço SMS. Número do
telefone da SCA (para comunicação SMS)</td>
<td style="text-align: center;">6</td>
</tr>
<tr>
<td style="text-align: center;">0x002C</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de bateria
<em>backup</em> acionada: 0 = desabilitado, 1 = habilitado (padrão)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x002D</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração dos pontos de
controle</p>
<ul>
<li><p>ACT (1 byte): Ação do evento (0: nenhuma; 1: entrada; 2:saída;
3:ambos)</p></li>
<li><p>RAD (2 bytes): Raio do ponto, em unidades de 10 m (0 a 650
km)</p></li>
<li><p>LAT (4 bytes): Latitude do centro do ponto</p></li>
<li><p>LNG (4 bytes): Longitude do centro do ponto</p></li>
</ul></td>
<td style="text-align: center;">11</td>
</tr>
<tr>
<td style="text-align: center;">0x002E</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração da cerca eletrônica</p>
<ul>
<li><p>ACT (1 byte): Ação do evento (0: nenhuma; 1: entrada; 2:saída;
3:ambos)</p></li>
<li><p>VTC (2 bytes): Número de vértices (atualmente, o número máximo de
vértices permitido é 18)</p></li>
<li><p>LAT (4 bytes): Latitude do vértice</p></li>
<li><p>LNG (4 bytes): Longitude do vértice</p></li>
<li><p>LAT/LNG para outros vértices...</p></li>
</ul></td>
<td style="text-align: center;">3+8*VTC</td>
</tr>
<tr>
<td style="text-align: center;">0x002F</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de movimento com
ignição desligada: 0 = desabilitado (padrão), 1 = habilitado</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0030</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de erro de GPS: 0
= desabilitado, 1 = habilitado (padrão)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0031</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de botão de
assistência: 0 = desabilitado, 1 = habilitado (padrão)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0032</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de porta aberta
fora do ponto de controle: 0 = desabilitado (padrão), 1 =
habilitado</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0033</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de luzes de
emergência: 0 = desabilitado (padrão), 1 = habilitado</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0034</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração de evento de limite de
velocidade excedido (Veja detalhes a seguir)</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x0035</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de teste de
produção: 0 = desabilitado; 1 = habilitado (padrão)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0036</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de teste de
instalação: 0 = desabilitado, 1 = habilitado (padrão)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0037</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração do APN:</p>
<ul>
<li><p>LGA: Tamanho do APN (1 byte). Tamanho (em bytes) do nome</p></li>
<li><p>APN (n bytes): Nome</p></li>
<li><p>LGL: Tamanho do <em>login</em> (1 byte). Tamanho (em bytes) do
<em>login</em> do APN</p></li>
<li><p>LGN (m bytes): <em>Login</em></p></li>
<li><p>LGP: Tamanho da senha (1 byte). Tamanho (em bytes) da senha do
APN</p></li>
<li><p>PSS (k bytes). Senha</p></li>
</ul>
<p>Configuração do servidor:</p>
<ul>
<li><p>Endereço IP do servidor primário (4 bytes)</p></li>
<li><p>Porta do servidor primário (2 bytes)</p></li>
<li><p>Endereço IP do servidor secundário (4 bytes)</p></li>
<li><p>Porta do servidor secundário (2 bytes)</p></li>
</ul></td>
<td style="text-align: center;">15+n+m+k</td>
</tr>
<tr>
<td style="text-align: center;">0x0038</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração de bloqueio:</p>
<p>Modo de bloqueio (1 byte):</p>
<ul>
<li><p>0: desativado</p></li>
<li><p>1: bloqueio progressivo (início imediato)</p></li>
<li><p>2: bloqueio somente com ignição desligada (padrão)</p></li>
<li><p>3: bloqueio somente com ignição desligada e sinal de GPS
válido</p></li>
</ul>
<p>Velocidade limite abaixo da qual o bloqueio é permitido, em nós (1
byte) Valor mínimo: 10 nós (padrão) e Valor máximo: 100 nós</p>
<p>Habilitação (1 byte): 0 = desabilitado, 1 = habilitado
(padrão) </p></td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x0039</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do bloqueio por acessórios:
0 = desabilitado (padrão), 1 = habilitado</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x003A</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do bloqueio passivo: 0 =
desabilitado (padrão), 1 = habilitado</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x003B</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do acionamento de setas: 0
= desabilitado (padrão), 1 = habilitado</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x003C</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração do hodômetro:</p>
<ul>
<li><p>Valor inicial do hodômetro, em metros (4 bytes). Valor padrão:
0</p></li>
<li><p>Intervalo de transmissão do hodômetro durante a viagem, em
minutos (1 byte). Valor padrão: 10 minutos</p></li>
<li><p>Inicialização do hodômetro (1 byte):</p></li>
</ul>
<ul>
<li><p>0: não inicializar</p></li>
<li><p>1: inicializar com o valor do primeiro campo</p></li>
</ul>
<ul>
<li><p>Habilitação (1 byte): 0 = desabilitado (padrão), 1 =
habilitado  </p></li>
</ul></td>
<td style="text-align: center;">7</td>
</tr>
<tr>
<td style="text-align: center;">0x003D</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração do sensor de
movimento:</p>
<ul>
<li><p>Habilitação (1 byte): 0 = desabilitado, 1 = habilitado
(padrão) </p></li>
<li><p>Número de pulsos para <em>debounce</em> (1 byte). Valor padrão: 3
pulsos </p></li>
</ul></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x003E</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração do servidor:</p>
<ul>
<li><p>Endereço IP do servidor primário (4 bytes)</p></li>
<li><p>Porta do servidor primário (2 bytes)</p></li>
</ul></td>
<td style="text-align: center;">6</td>
</tr>
<tr>
<td style="text-align: center;">0x003F</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração do APN:</p>
<ul>
<li><p>LGA: Tamanho do APN (1 byte). Tamanho (em bytes) do nome</p></li>
<li><p>APN (n bytes): Nome</p></li>
<li><p>LGL: Tamanho do <em>login</em> (1 byte). Tamanho (em bytes) do
<em>login</em> do APN</p></li>
<li><p>LGN (m bytes): <em>Login</em></p></li>
<li><p>LGP: Tamanho da senha (1 byte). Tamanho (em bytes) da senha do
APN</p></li>
<li><p>PSS (k bytes). Senha </p></li>
</ul></td>
<td style="text-align: center;">3+n+m+k</td>
</tr>
<tr>
<td style="text-align: center;">0x0040</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Telefone do servidor SMS. É o número
de telefone que o equipamento deve usar para enviar mensagens SMS:</p>
<ul>
<li><p>Código do país (2 bytes)</p></li>
<li><p>Código da operadora (1 byte)</p></li>
<li><p>Número de telefone (8 bytes) </p></li>
</ul></td>
<td style="text-align: center;">11</td>
</tr>
<tr>
<td style="text-align: center;">0x0041</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">TXO: Intervalo de transmissão com
ignição ligada, em segundos. Valor padrão: 60 segundos. TXO = 0
significa que não há transmissão</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0042</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">TXF: Intervalo de transmissão com
ignição desligada, em minutos (ou seja, é o intervalo do "ping"). Valor
padrão: 180 minutos (3 horas). TXF = 0 significa que não há
transmissão.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0043</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Controle do módulo GPS:</p>
<ul>
<li><p>TGP (2 bytes): Intervalo de tempo para ligar o módulo GPS com a
ignição desligada (em minutos). Valor padrão: 180 minutos (3
horas)</p></li>
<li><p>XGP (2 bytes): Intervalo de tempo em que o módulo GPS permanece
ligado com a ignição desligada (em segundos). Valor padrão: 240 segundos
(4 minutos)</p></li>
</ul>
<p>XGP = 0: O módulo GPS nunca é ligado com a ignição desligada</p>
<p>XGP &gt;= TGP: O módulo GPS nunca é desligado com a ignição
desligada </p></td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0044</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Controle do módulo GSM:</p>
<ul>
<li><p>TGS (2 bytes): Intervalo de tempo para ligar o módulo GSM com a
ignição desligada (em minutos). Valor padrão: 180 minutos (3
horas)</p></li>
<li><p>XGS (2 bytes): Intervalo de tempo em que o módulo GSM permanece
ligado com a ignição desligada (em segundos). Valor padrão: 30
minutos</p></li>
</ul>
<p>XGS = 0: O módulo GSM nunca é ligado com a ignição desligada</p>
<p>XGS &gt;= TGS: O módulo GSM nunca é desligado com a ignição
desligada  </p></td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0045</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>SMO: Intervalo de tempo, em
segundos, durante o qual o equipamento permanece conectado (enviando
posições com o módulo GPS e o módulo GSM ligados) após sair do modo
<em>sleep</em> por interrupção do sensor de movimento.</p>
<p>Valor padrão: 300 segundos (5 minutos). Valor mínimo: 120 segundos (2
minutos).</p>
<p>SMO = 0 significa que o módulo não enviará posições (apenas o
evento). </p></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0046</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">UDT: <em>Time-out</em> da mensagem UDP
de acknowledge, em segundos. Valor padrão: 30 segundos. Valor mínimo: 5
segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0047</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>RTY: Número de tentativas de
transmissão da mensagem antes de mudar para outro servidor.</p>
<p>Valor padrão: 5. Valor mínimo: 5</p></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0048</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">SCID (parâmetro do SIM Card), em formato
BCD.</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">0x0049</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">CIMI (parâmetro do SIM Card), em formato
BCD.</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">0x004A</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Senha do SIM Card (PIN). Para SIM Cards
que não são TIM ou Claro, esta senha deve ser usada se o SIM Card
estiver bloqueado. Este parâmetro é uma palavra de 10 caracteres. Para
SIM Cards TIM e Claro, esta senha está implícita no código.</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">0x004B</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração da mensagem da estação
rádio-base:</p>
<ul>
<li><p>Transmissão da mensagem da estação rádio-base (1 byte):</p></li>
</ul>
<ul>
<li><p>0: desabilitado (padrão)</p></li>
<li><p>1: habilitado</p></li>
</ul>
<ul>
<li><p>Período de transmissão, em minutos (1 byte). Valor padrão: 10
minutos</p></li>
</ul></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x004C</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>DWT: <em>Time-out</em> do
procedimento de download, em minutos.</p>
<p>Valor padrão: 60 minutos. Valor mínimo: 15 minutos</p></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x004D</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>ABT: Intervalo de transmissão durante
o uso da bateria <em>backup</em>, em segundos.</p>
<p>Valor padrão: 60 segundos. Valor mínimo: 15 segundos.</p>
<p>ABT = 0 significa que não há transmissão.</p></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x004E</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração da mensagem RDS:</p>
<ul>
<li><p>Transmissão da mensagem RDS (1 byte):</p></li>
</ul>
<ul>
<li><p>0: desabilitado (padrão)</p></li>
<li><p>1: habilitado</p></li>
</ul>
<ul>
<li><p>Período de transmissão, em segundos (2 bytes). Valor padrão: 30
segundos</p></li>
</ul></td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x004F</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Tolerância para o evento de limite de
velocidade excedido. (Veja detalhes a seguir)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0050</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">MSAM: Máximo tamanho da mensagem de
aplicação</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0051</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">SNVL: Máximo número de listas de
variáveis</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0052</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">SNVRL: Máximo número de variáveis por
lista</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0053</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">NRLS: Máximo número de listas de
relatórios</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0054</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">NRSPL: Máximo número de relatórios por
lista</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0055</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Define se a comunicação entre o
módulo GPS e o microcontrolador é replicada na porta local (UART).</p>
<p>0 : comunicação não replicada</p>
<p>1 : sinal TX do microcontrolador é replicado</p>
<p>2 : sinal RX do microcontrolador é replicado</p>
<p>3 : TX e RX são replicados </p></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0056</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Define se a comunicação entre o
módulo GSM e o microcontrolador é replicada na porta local (UART).</p>
<p>0 : comunicação não replicada</p>
<p>1 : sinal TX do microcontrolador é replicado</p>
<p>2 : sinal RX do microcontrolador é replicado</p>
<p>3 : TX e RX são replicados  </p></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0057</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">Tipos suportados de informação
adicional</td>
<td style="text-align: center;">32</td>
</tr>
<tr>
<td style="text-align: center;">0x0058</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração dos tipos de informação
adicional</td>
<td style="text-align: center;">32</td>
</tr>
<tr>
<td style="text-align: center;">0x0059</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração da leitura de rotação</td>
<td style="text-align: center;">7</td>
</tr>
<tr>
<td style="text-align: center;">0x005A</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração da faixa ideal de
rotação</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x005B</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração da faixa de marcha lenta do
motor</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x005C</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de limpador de
para-brisa</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x005D</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de freio
motor</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x005E</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de freio de
serviço</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x005F</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de motor parado
com ignição ligada</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x0060</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de motor em
marcha lenta</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x0061</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de motor com
aceleração em neutro</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x0062</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de limite de RPM
excedido</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0063</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de RPM com chuva
excedido</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0064</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de RPM com freio
motor excedido</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0065</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de banguela</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0066</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de limite de
velocidade especial excedido</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0067</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de limite de
velocidade com chuva excedido</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0068</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Calibração do sensor de velocidade</td>
<td style="text-align: center;">11</td>
</tr>
<tr>
<td style="text-align: center;">0x0069</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do valor limite para evento
de limite de velocidade</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x006A</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de limite de
velocidade ultrapassado (com precisão)</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x006B a 0x006D</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">Reservado</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x006E</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de vibração</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x006F</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de movimento
<em>tilt</em></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0070</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de aceleração
brusca</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0071</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de freada
brusca</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0072</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de freada muito
brusca</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0073</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Configuração do tipo de veículo</p>
<p>Tipo de veículo (Veja <em>Tipo de Veículo</em>). Valor padrão:
0</p></td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0074</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração da informação básica de
telemetria</td>
<td style="text-align: center;">6</td>
</tr>
<tr>
<td style="text-align: center;">0x0075</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">TXFs: Configuração do intervalo
escalonado de transmissão com ignição desligada</td>
<td style="text-align: center;">7</td>
</tr>
<tr>
<td style="text-align: center;">0x0076</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>TSBY: <em>Time-out</em> do modo
<em>standby</em>, em minutos</p>
<p>Valor padrão: 2880 minutos (48 horas)</p>
<p>TSBY = 0 significa modo <em>sleep</em> normal</p></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0077</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;"><p>Define o <em>baud rate</em> usado na
comunicação serial com outros equipamentos por meio das portas externas.
Para mais de uma porta, este parâmetro pode ser configurado com
sub-índices, em que cada um está relacionado a uma porta externa do
equipamento.</p>
<p><em>Baud rate</em>, em kbps (4 bytes). Valores permitidos: 115200,
57600, 38400, 19200, 9600</p>
<p>0: O valor padrão será usado</p></td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0078</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Tempo máximo de conexão GPRS (em
segundos)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0079</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Número máximo de mensagens enviadas sob
requisição a cada conexão</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x007A</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Tempo de inatividade do acelerômetro (em
segundos)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x007B</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do meio de envio de
mensagens (GPRS/SMS)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x007C</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração da ordem de envio das
mensagens (Buffer LIFO/FIFO)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x007D</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Tempo para entrada em modo sleep (em
segundos)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x007E</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para alteração do protocolo de
comunicação GPRS/SMS</td>
<td style="text-align: center;">5+m+n</td>
</tr>
<tr>
<td style="text-align: center;">0x007F</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">Reservado</td>
<td style="text-align: center;"></td>
</tr>
<tr>
<td style="text-align: center;">0x0080</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para configuração de
APN/IP/Porta com Operadora</td>
<td style="text-align: center;">32+n1+m1+k1+n2+m2+k2</td>
</tr>
<tr>
<td style="text-align: center;">0x0081</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para configuração de
APN/IP/Porta com Operadora (Mem 1)</td>
<td style="text-align: center;">16+n1+m1+k1</td>
</tr>
<tr>
<td style="text-align: center;">0x0082</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para configuração de
APN/IP/Porta com Operadora (Mem 2)</td>
<td style="text-align: center;">16+n2+m2+k2</td>
</tr>
<tr>
<td style="text-align: center;">0x0083</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para configuração da
prioridade de operadoras</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0084</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para gerenciamento dos SIM
CARDs</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0085</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para gerenciamento do SIM CARD
secundário</td>
<td style="text-align: center;">9</td>
</tr>
<tr>
<td style="text-align: center;">0x0086</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para configuração do envio de
eventos de SIM CARD</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0087</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">Reservado</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x0088</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para configuração da antena
satelital</td>
<td style="text-align: center;">13</td>
</tr>
<tr>
<td style="text-align: center;">0x0089</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para alteração temporária do
tipo de habilitação da antena satelital</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x008A</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para alteração temporária do
tempo limite sem conexão GPRS para início do envio de posições via
satélite</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x008B</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para alteração temporária da
taxa de monitoração via satélite com ignição ligada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x008C</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para alteração temporária da
taxa de monitoração via satélite com ignição desligada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x008D</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para configuração do pacote de
mensagens</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">0x008E</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para adição de bytes
(mensagens) adicionais</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x008F</td>
<td style="text-align: center;">RO</td>
<td style="text-align: center;">Parâmetro para leitura de informações a
respeito do uso do pacote de dados</td>
<td style="text-align: center;">19</td>
</tr>
<tr>
<td style="text-align: center;">0x0090</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro de configuração de modo de
funcionamento do Horímetro</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0091</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro de definição da entrada
Digital do Horímetro</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0092</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro de configuração da entrada de
frequência do Horímetro</td>
<td style="text-align: center;">10</td>
</tr>
<tr>
<td style="text-align: center;">0x0093</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro de Limite Inicial de
Velocidade do Horímetro</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0094</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro de Limite Inicial de Rotação
do Horímetro</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0095</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro de Configuração de Eventos do
Horímetro</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x0096</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro do valor do Horímetro</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0097</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro endereço do bucket</td>
<td style="text-align: center;">99</td>
</tr>
<tr>
<td style="text-align: center;">0x0098 a 0x009F</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">Reservado</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x00A0</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para habilitação dos eventos
do modo de segurança</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00A1</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para habilitação do modo de
segurança</td>
<td style="text-align: center;">3</td>
</tr>
<tr>
<td style="text-align: center;">0x00A2</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para alteração da taxa de
monitoração GPRS com ignição ligada durante o modo de segurança</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00A3</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para alteração da taxa de
monitoração GPRS com ignição desligada durante o modo de segurança</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00A4</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de âncora</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">000A5</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Reservado para configuração do RFID</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x00A6</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração da atuação em saída
mediante detecção de jammer (Número da saída [1 byte])</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00A7</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do modo de Segurança para
recepção de SMS -&gt; Nível de segurança (0: Desabilitado; 1: Sem
segurança; 2: Nível 1; 3: Nível 2); Resposta (0: não envia resposta; 1:
para o mesmo número que originou; 2: para o número cadastrado para envio
(Parâmetro 0x002B); 3: para ambos); Senha (4 dígitos)</td>
<td style="text-align: center;">6</td>
</tr>
<tr>
<td style="text-align: center;">0x00A8 a 0x00DC</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">Reservado</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x00DD</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação flexível do receptor de GPS
(1 campo de 0 a 672: Se 0, desabilitado; Se 1, 1 vez a cada toda
posição; ...Se 672, 1 vez a cada 672 posições que resulta em 1 vez a
cada 7 dias com taxa de 15 min)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00DE</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação do sensor de luminosidade
(Campo 1 [1 byte]: Sensibilidade (0 a 2, em que 0 significa
desabilitado, 1 pouco sensível e 2 muito sensível); Campo 2 [2 bytes]:
Debounce para detecção[s] 0 a 600; Campo 3 [2 bytes]: Debounce para não
detecção[s] 0 a 600)</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x00DF</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para habilitação da função
desativação por botão da isca (0: Desabilitada; 1: Habilitada)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00E0</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de configuração
local</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00E1</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de conexão de
fonte externa</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00E2</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de conexão
USB</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00E3</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de escuta</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00E4</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de acionamento de
buzzer</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00E5</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do evento de bateria
baixa</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00E6</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do envio de evento do botão
de desacoplamento (violação)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00E7</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do modo de emergência:</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00E8</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração dos telefones para chamadas
(6 números em strings de 13 caracteres, Ex: 55 11 99876 5432)</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">0x00E9</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Taxas de monitoração (Em movimento
[segundos], em repouso [minutos], Em emergência [segundos], Atualização
de configuração [horas])</td>
<td style="text-align: center;">8</td>
</tr>
<tr>
<td style="text-align: center;">0x00EA</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">GPS assistido (Tempo para 1a requisição
[segundos], Peridiocidade das requisições [segundos])</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x00EB a 0x00EF</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">Reservado</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x00F0</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação do receptor de GPS</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00F1</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação do modem GSM</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00F2</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação da triangulação por ERB</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00F3</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação da comunicação em 900
MHz</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00F4</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação do acelerômetro</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00F5</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação da escuta</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00F6</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do tempo para entrada em
modo de emergência por botão do usuário (assistência)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00F7</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do tempo para entrada em
modo de emergência por botão de desacoplamento (violação)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00F8</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do tempo para entrada em
modo de emergência por jammer GSM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00F9</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do tempo para entrada em
modo de emergência por jammer GPS</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00FA</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração do tempo para entrada em
modo de emergência por comando</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00FB</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação do RF 433MHz</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00FC</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação da funcionalidade de bateria
interna (bateria backup)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00FD</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação da funcionalidade de
detecção de ignição</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x00FE</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração da transmissão de posição
devido a mudança de direção</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x00FF</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Habilitação do RF 433 MHz (Novo) -&gt;
Campo 1: Tempo em modo normal [s] (1 byte) / Campo 2: Tempo em modo
emergência [s] (1 byte)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0100</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração de listas de variáveis</td>
<td style="text-align: center;">7 + NVR*2</td>
</tr>
<tr>
<td style="text-align: center;">0x0200</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Configuração de listas de
relatórios</td>
<td style="text-align: center;">3 + NRP*2</td>
</tr>
<tr>
<td style="text-align: center;">0x0300</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para disponibilização dos
sensores analógicos (1 a 31)</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0301 a 0x031F</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetros para disponibilização
individual dos sensores analógicos (1 a 31)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0321 a 0x033F</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetros de configuração dos eventos
dos sensores analógicos (1 a 31)</td>
<td style="text-align: center;">30</td>
</tr>
<tr>
<td style="text-align: center;">0x03FF</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para habilitar eventos de
geolocalização</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0400</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para disponibilização dos
sensores digitais (1 a 95)</td>
<td style="text-align: center;">12</td>
</tr>
<tr>
<td style="text-align: center;">0x0401 a 0x045F</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetros para disponibilização
individual dos sensores digitais (1 a 95)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0461 a 0x04BF</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetros para configuração dos
sensores digitais (1 a 95)</td>
<td style="text-align: center;">6</td>
</tr>
<tr>
<td style="text-align: center;">0x04C0</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para disponibilização dos
atuadores (1 a 31)</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x04C1 a 0x04DF</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetros para disponibilização
individual dos atuadores (1 a 31)</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x04E1 a 0x04FF</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetros para configuração dos
atuadores (1 a 31)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0501 a 0x05FF</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetros para configuração do envio de
AI (1 a 255)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0600</td>
<td style="text-align: center;">R/W</td>
<td style="text-align: center;">Parâmetro para configuração de
veículo</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

**  
**

**Configuração do evento de limite de velocidade excedido - Parâmetro
0x0034**

Este parâmetro é usado para a configuração do evento de limite de
velocidade excedido (veja *Eventos*). O evento é gerado sempre que o
veículo excede o limite de velocidade configurado. O parâmetro é formado
por 3 campos, descritos a seguir.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de limite de velocidade excedido - Parâmetro 0x0034</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Valor do limite de velocidade. O
evento é gerado se o limite de velocidade é atingido ou
ultrapassado.</p>
<p>Faixa válida: 0 a 255 nós</p>
<p>Valor padrão: 43 nós (~ 80 km/h)</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor de histerese. Uma vez gerado o
evento, outro evento somente pode ser gerado se a velocidade permanecer
abaixo do valor: (Limite – Histerese). Faixa válida: 0 a 255 nós</p>
<p>Valor padrão: 4 nós (~ 8 km/h)</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento habilitado</p></li>
<li><p>2 a 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

**Tolerância para o evento de limite de velocidade excedido - Parâmetro
0x004F**

Este parâmetro é usado para configurar o tempo de tolerância acima do
limite de velocidade antes que o evento de infração seja gerado.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 54%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Tolerância para o
evento de limite de velocidade excedido - Parâmetro 0x004F</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Tempo que o veículo deve permanecer
acima do limite de velocidade para a confirmação do evento.</p>
<p>Faixa válida: 0 a 255 segundos</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

**Tipos suportados de informação adicional - Parâmetro 0x0057**

Este parâmetro é um vetor de campos de bits, totalizando 256 bits (32
bytes). É utilizado para informar quais tipos de informação adicional
são suportados pelo equipamento (veja *Informação Adicional*). Trata-se
de um parâmetro de leitura apenas.

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 52%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Tipos suportados de
informação adicional - Parâmetro 0x0057</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Vetor de campos de bits usado para
informar quais tipos de informação adicional são suportados pelo
equipamento. Cada bit corresponde a um tipo de informação adicional. O
primeiro bit do vetor corresponde ao índice 0 e assim por diante.</p>
<ul>
<li><p>bit = 0: informação adicional não suportada pelo
equipamento</p></li>
<li><p>bit = 1: informação adicional suportada pelo equipamento</p></li>
</ul></td>
<td style="text-align: center;">vetor de unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">32</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">32</td>
</tr>
</tbody>
</table>

**Configuração dos tipos de informação adicional - Parâmetro 0x0058**

Este parâmetro é um vetor de campos de bits, totalizando 256 bits (32
bytes). É utilizado para configurar quais tipos de informação adicional
estão habilitados a serem enviados com a mensagem ***PAI*** (veja
*Informação Adicional*). Nota: uma mensagem adicional somente pode ser
habilitada se for suportada pelo equipamento. Se o equipamento recebe
uma mensagem ***PRW*** tentando habilitar um tipo de informação não
suportado, então ele responderá com uma mensagem ***NACK***.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 10%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração dos
tipos de informação adicional - Parâmetro 0x0058</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Vetor de campos de bits usado para
configurar os tipos de informação adicional a serem enviados com a
mensagem <em><strong>PAI</strong></em>. Cada bit corresponde a um tipo
de informação adicional. O primeiro bit do vetor corresponde ao índice 0
e assim por diante.</p>
<ul>
<li><p>bit = 0: informação adicional desabilitada</p></li>
</ul>
<ul>
<li><p>bit = 1: informação adicional habilitada</p></li>
</ul></td>
<td style="text-align: center;">vetor de unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">32</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">32</td>
</tr>
</tbody>
</table>

**Configuração da leitura de rotação - Parâmetro 0x0059**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração da
leitura de rotação - Parâmetro 0x0059</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Constante de leitura de rotação
RPK1.</p>
<p>O valor da rotação é calculado da seguinte forma:</p>
<p><em><strong>Valor RPM = (( f*RPK1 ) / RPK2) + RPK3</strong></em></p>
<p>onde f = freqüência da rotação lida na entrada.</p>
<p>Faixa válida: 0 a 65.535</p>
<p>Valor padrão: 1</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Constante de leitura de rotação
RPK2.</p>
<p>Faixa válida: 0 a 65.535</p>
<p>Valor padrão: 1</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Constante de leitura de rotação
RPK3.</p>
<p>Faixa válida: 0 a 65.535</p>
<p>Valor padrão: 0</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Número de amostras que devem ser
usadas para o cálculo da rotação média, quando a informação adicional
correspondente estiver habilitada. Normalmente, valores de rotação e
velocidade são armazenados a cada segundo em um vetor de120
elementos.</p>
<p>Faixa válida: 1 a 120</p>
<p>Valor padrão: 8</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">7</td>
</tr>
</tbody>
</table>

**Configuração da faixa ideal de rotação - Parâmetro 0x005A**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração da
faixa ideal de rotação - Parâmetro 0x005A</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Valor do limite inferior de
rotação.</p>
<p>Faixa válida: 0 a 65.535 RPM</p>
<p>Valor padrão: 1.000 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor do limite superior de
rotação.</p>
<p>Faixa válida: 0 a 65.535 RPM</p>
<p>Valor padrão: 2.000 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Configuração da faixa de marcha lenta do motor - Parâmetro 0x005B**

Este parâmetro é usado para configurar a faixa de marcha lenta do motor.
O motor é considerado em marcha lenta se a velocidade e a rotação são
iguais ou menores que os limites definidos por este parâmetro.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração da
faixa de marcha lenta do motor - Parâmetro 0x005B</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Valor da velocidade usada para a
determinação da condição do veículo. Abaixo desta velocidade, o veículo
é considerado parado.</p>
<p>Faixa válida: 0 a 255 nós</p>
<p>Valor padrão: 5 nós (~ 10 km/h)</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor da máxima rotação para a
condição de marcha lenta.</p>
<p>Faixa válida: 0 a 65.535 RPMValor padrão: 800 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

**Configuração do evento de limpador de para-brisa - Parâmetro 0x005C**

Este parâmetro é usado para configurar o evento de limpador de
para-brisa (veja *Eventos*).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de limpador de para-brisa - Parâmetro 0x005C</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente quando o limpador de para-brisa é
ligado</p></li>
<li><p>2: evento gerado somente quando o limpador de para-brisa é
desligado</p></li>
<li><p>3: evento gerado quando o limpador de para-brisa é ligado e
desligado</p></li>
<li><p>4 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p><em>Debounce</em> para limpador de
para-brisa desligado. Tempo durante o qual o limpador de para-brisa deve
permanecer desligado, após ter estado ligado, para que seja considerado
realmente desligado.</p>
<p>Faixa válida: 0 a 255 segundos</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p><em>Debounce</em> para limpador de
para-brisa ligado. Tempo durante o qual o limpador de para-brisa deve
permanecer ligado, após ter estado desligado, para que seja considerado
realmente ligado.</p>
<p>Faixa válida: 0 a 255 segundos</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

**Configuração do evento de freio motor - Parâmetro 0x005D**

Este parâmetro é usado para configurar o evento de freio motor (veja
*Eventos*).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de freio motor - Parâmetro 0x005D</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente quando o freio motor é acionado</p></li>
<li><p>2: evento gerado somente quando o freio motor é liberado</p></li>
<li><p>3: evento gerado quando o freio motor é acionado e
liberado</p></li>
<li><p>4 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p><em>Debounce</em> para freio motor
liberado. Tempo durante o qual o freio motor deve permanecer liberado,
após ter sido acionado, para que seja considerado realmente
liberado.</p>
<p>Faixa válida: 0 a 255 segundos</p>
<p>Valor padrão: 5 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p><em>Debounce</em> para freio motor
acionado. Tempo durante o qual o freio motor deve permanecer acionado,
após ter sido liberado, para que seja considerado realmente
acionado.</p>
<p>Faixa válida: 0 a 255 segundos</p>
<p>Valor padrão: 5 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

**Configuração do evento de freio de serviço - Parâmetro 0x005E**

Este parâmetro é usado para configurar o evento de freio de serviço
(veja *Eventos*).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de freio de serviço - Parâmetro 0x005E</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente quando o freio de serviço é
acionado</p></li>
<li><p>2: evento gerado somente quando o freio de serviço é
liberado</p></li>
<li><p>3: evento gerado quando o freio de serviço é acionado e
liberado</p></li>
<li><p>4 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p><em>Debounce</em> para freio de
serviço liberado. Tempo durante o qual o freio de serviço deve
permanecer liberado, após ter sido acionado, para que seja considerado
realmente liberado.</p>
<p>Faixa válida: 0 a 255 segundos</p>
<p>Valor padrão: 5 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p><em>Debounce</em> para freio de
serviço acionado. Tempo durante o qual o freio de serviço deve
permanecer acionado, após ter sido liberado, para que seja considerado
realmente acionado.</p>
<p>Faixa válida: 0 a 255 segundos</p>
<p>Valor padrão: 5 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

**Configuração do evento de motor parado com ignição ligada - Parâmetro
0x005F**

Este parâmetro é usado para configurar o evento de motor parado com
ignição ligada (veja *Eventos*).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de motor parado com ignição ligada - Parâmetro
0x005F</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente no início</p></li>
<li><p>2: evento gerado somente no fim</p></li>
<li><p>3: evento gerado no início e no fim</p></li>
<li><p>4 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Tempo que o veículo deve permanecer
com o motor parado e a ignição ligada para que o evento seja gerado.</p>
<p>Faixa válida: 0 a 65.535 segundos</p>
<p>Valor padrão: 180 segundos</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

**Configuração do evento de motor em marcha lenta - Parâmetro 0x0060**

Este parâmetro é usado para configurar o evento de motor em marcha lenta
(veja *Eventos*).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de motor em marcha lenta - Parâmetro 0x0060</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente no início</p></li>
<li><p>2: evento gerado somente no fim</p></li>
<li><p>3: evento gerado no início e no fim</p></li>
<li><p>4 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Tempo que o veículo deve permanecer
com o motor em marcha lenta para que o evento seja gerado.</p>
<p>Faixa válida: 0 a 65.535 segundos</p>
<p>Valor padrão: 180 segundos</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

**Configuração do evento de motor com aceleração em neutro - Parâmetro
0x0061**

Este parâmetro é usado para configurar o evento de motor com aceleração
em neutro (veja *Eventos*).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de motor com aceleração em neutro - Parâmetro
0x0061</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente no início</p></li>
<li><p>2: evento gerado somente no fim</p></li>
<li><p>3: evento gerado no início e no fim</p></li>
<li><p>4 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Tempo que o veículo deve permanecer
com o motor com aceleração em vazio para que o evento seja gerado.</p>
<p>Faixa válida: 0 a 65.535 segundos</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

**Configuração do evento de limite de RPM excedido - Parâmetro 0x0062**

Este parâmetro é usado para configurar o evento de limite de RPM
excedido (veja *Eventos*).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de limite de RPM excedido - Parâmetro 0x0062</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente no início</p></li>
<li><p>2: evento gerado somente no fim</p></li>
<li><p>3: evento gerado no início e no fim</p></li>
<li><p>4 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor do limite de rotação. O evento
é gerado se o valor limite for atingido ou ultrapassado durante um tempo
igual ou maior do que o tempo de <em>debounce.</em></p>
<p>Faixa válida: 0 a 65.535 RPM</p>
<p>Valor padrão: 2300 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor de histerese. Uma vez gerado o
evento, outro evento somente poderá ser gerado após a rotação atingir um
valor abaixo de (100 - Histerese)% do valor limite, durante um período
de tempo maior ou igual ao tempo de <em>debounce</em>.</p>
<p>Faixa válida: 0 a 100%</p>
<p>Valor padrão: 5%</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Tempo de <em>debounce</em>. Este é o
tempo em que o valor de rotação deve permanecer além do valor limite
para que o evento seja gerado. Também é aplicado para a histerese.</p>
<p>Faixa válida: 0 a 255 segundos (0 significa ausência de
<em>debounce</em>)</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

**Configuração do evento de limite de RPM com chuva excedido - Parâmetro
0x0063**

Este parâmetro é usado para configurar o evento de limite de RPM com
chuva (limpador de para-brisa ligado) excedido (veja *Eventos*). Este
evento é gerado sempre que o número de rotações do motor ultrapassar o
valor limite sob condição de chuva definido neste parâmetro.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de limite de RPM com chuva excedido - Parâmetro
0x0063</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente no início</p></li>
<li><p>2: evento gerado somente no fim</p></li>
<li><p>3: evento gerado no início e no fim</p></li>
<li><p>4 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor do limite de rotação. O evento
é gerado se o valor limite for atingido ou ultrapassado durante um tempo
igual ou maior do que o tempo de <em>debounce.</em></p>
<p>Faixa válida: 0 a 65.535 RPM</p>
<p>Valor padrão: 2400 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor de histerese. Uma vez gerado o
evento, outro evento somente poderá ser gerado após a rotação atingir um
valor abaixo de (100 - Histerese)% do valor limite, durante um período
de tempo maior ou igual ao tempo de <em>debounce</em>.</p>
<p>Faixa válida: 0 a 100%</p>
<p>Valor padrão: 5%</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Tempo de <em>debounce</em>. Este é o
tempo em que o valor de rotação deve permanecer além do valor limite
para que o evento seja gerado. Também é aplicado para a histerese.</p>
<p>Faixa válida: 0 a 255 segundos (0 significa ausência de
<em>debounce</em>)</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

**Configuração do evento de limite de RPM com freio motor excedido -
Parâmetro 0x0064**

Este parâmetro é usado para configurar o evento de limite de RPM com
freio motor excedido (veja *Eventos*). Este evento é gerado sempre que o
número de rotações do motor ultrapassar o valor limite para freio motor
acionado definido neste parâmetro.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de limite de RPM com freio motor excedido - Parâmetro
0x0064</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente no início</p></li>
<li><p>2: evento gerado somente no fim</p></li>
<li><p>3: evento gerado no início e no fim</p></li>
<li><p>4 a 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor do limite de rotação. O evento
é gerado se o valor limite for atingido ou ultrapassado durante um tempo
igual ou maior do que o tempo de <em>debounce.</em></p>
<p>Faixa válida: 0 a 65.535 RPM</p>
<p>Valor padrão: 2500 RPM</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor de histerese. Uma vez gerado o
evento, outro evento somente poderá ser gerado após a rotação atingir um
valor abaixo de (100 - Histerese)% do valor limite, durante um período
de tempo maior ou igual ao tempo de <em>debounce</em>.</p>
<p>Faixa válida: 0 a 100%</p>
<p>Valor padrão: 5%</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Tempo de <em>debounce</em>. Este é o
tempo em que o valor de rotação deve permanecer além do valor limite
para que o evento seja gerado. Também é aplicado para a histerese.</p>
<p>Faixa válida: 0 a 255 segundos (0 significa ausência de
<em>debounce</em>)</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

**Configuração do evento de banguela - Parâmetro 0x0065**

Este parâmetro é usado para configurar o evento de banguela (veja
*Eventos*). Este evento é gerado sempre que o veículo excede o limite de
velocidade configurado, enquanto o valor das rotações do motor permanece
dentro da faixa de marcha lenta (veja o parâmetro "**Configuração do
evento de motor em marcha lenta***"*).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de banguela - Parâmetro 0x0065</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente no início</p></li>
<li><p>2: evento gerado somente no fim</p></li>
<li><p>3: evento gerado no início e no fim</p></li>
<li><p>4 a 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor do limite de velocidade. O
evento é gerado se o valor limite for atingido ou ultrapassado durante
um tempo igual ou maior do que o tempo de <em>debounce.</em></p>
<p>Faixa válida: 0 a 255 nós</p>
<p>Valor padrão: 22 nós (~ 40 km/h)</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor de histerese. Uma vez gerado o
evento, outro evento somente poderá ser gerado após a velocidade atingir
um valor abaixo de (100 - Histerese)% do valor limite, durante um
período de tempo maior ou igual ao tempo de <em>debounce</em>.</p>
<p>Faixa válida: 0 a 100%</p>
<p>Valor padrão: 5%</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Tempo de <em>debounce</em>. Este é o
tempo em que o valor da velocidade deve permanecer além do valor limite
para que o evento seja gerado. Também é aplicado para a histerese.</p>
<p>Faixa válida: 0 a 255 segundos (0 significa ausência de
<em>debounce</em>)</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Configuração do evento de limite de velocidade especial excedido -
Parâmetro 0x0066**

Este parâmetro é usado para configurar o evento limite de velocidade
especial excedido (veja *Eventos*). Este evento é gerado sempre que o
veículo excede um determinado limite de velocidade.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de limite de velocidade especial excedido - Parâmetro
0x0066</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente no início</p></li>
<li><p>2: evento gerado somente no fim</p></li>
<li><p>3: evento gerado no início e no fim</p></li>
<li><p>4 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor do limite de velocidade. O
evento é gerado se o valor limite for atingido ou ultrapassado durante
um tempo igual ou maior do que o tempo de <em>debounce.</em></p>
<p>Faixa válida: 0 a 255 nós</p>
<p>Valor padrão: 44 nós (~ 80 km/h)</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor de histerese. Uma vez gerado o
evento, outro evento somente poderá ser gerado após a velocidade atingir
um valor abaixo de (100 - Histerese)% do valor limite, durante um
período de tempo maior ou igual ao tempo de <em>debounce</em>.</p>
<p>Faixa válida: 0 a 100%</p>
<p>Valor padrão: 5%</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Tempo de <em>debounce</em>. Este é o
tempo em que o valor da velocidade deve permanecer além do valor limite
para que o evento seja gerado. Também é aplicado para a histerese.</p>
<p>Faixa válida: 0 a 255 segundos (0 significa ausência de
<em>debounce</em>)</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Configuração do evento de limite de velocidade com chuva excedido -
Parâmetro 0x0067**

Este parâmetro é usado para configurar o evento limite de velocidade com
chuva (limpador de para-brisa ligado) excedido (veja *Eventos*). Este
evento é gerado sempre que o veículo excede um determinado limite de
velocidade sob condição de chuva.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de limite de velocidade com chuva excedido - Parâmetro
0x0067</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: evento desabilitado (valor padrão)</p></li>
<li><p>1: evento gerado somente no início</p></li>
<li><p>2: evento gerado somente no fim</p></li>
<li><p>3: evento gerado no início e no fim</p></li>
<li><p>4 a 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor do limite de velocidade. O
evento é gerado se o valor limite for atingido ou ultrapassado durante
um tempo igual ou maior do que o tempo de <em>debounce.</em></p>
<p>Faixa válida: 0 a 255 nós</p>
<p>Valor padrão: 33 nós (~ 60 km/h)</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor de histerese. Uma vez gerado o
evento, outro evento somente poderá ser gerado após a velocidade atingir
um valor abaixo de (100 - Histerese)% do valor limite, durante um
período de tempo maior ou igual ao tempo de <em>debounce</em>.</p>
<p>Faixa válida: 0 a 100%</p>
<p>Valor padrão: 5%</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Tempo de <em>debounce</em>. Este é o
tempo em que o valor da velocidade deve permanecer além do valor limite
para que o evento seja gerado. Também é aplicado para a histerese.</p>
<p>Faixa válida: 0 a 255 segundos (0 significa ausência de
<em>debounce</em>)</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Calibração do sensor de velocidade - Parâmetro 0x0068**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Calibração do sensor
de velocidade - Parâmetro 0x0068</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Constante (pulsos/km).</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Dado válido: "0" significa
inválido.</p>
<p>Valor padrão: 0</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Permissão para auto-calibração: "0"
para permitido e "&gt;0" para não permitido.</p>
<p>Valor padrão: 0</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Distância de calibração, em
metros.</p>
<p>Valor padrão: 500 m</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">metros</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;"><p>Variação da direção, em graus.</p>
<p>Valor padrão: 30 graus</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">graus</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;"><p>Velocidade de calibração, em nós.</p>
<p>Valor padrão: 10 nós</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">11</td>
</tr>
</tbody>
</table>

**Configuração do evento de vibração - Parâmetro 0x006E**

Este parâmetro é usado para configurar o evento de vibração (veja
*Eventos*). Este evento é gerado quando o equipamento deixa o modo
*sleep* por ocasião de uma vibração sentida pelo acelerômetro.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 51%" />
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de vibração - Parâmetro 0x006E</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do Dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação da função:</p>
<ul>
<li><p>0: função <em>wake-up</em> desabilitada</p></li>
<li><p>1: função <em>wake-up</em> habilitada (valor padrão) 2 to 255:
não definido, tratado como desabilitada</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Habilitação do evento:</p>
<ul>
<li><p>0: evento desabilitado</p></li>
<li><p>1: evento habilitado (valor padrão)</p></li>
<li><p>2 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Número de pulsos de debounce.</p>
<p>Faixa válida: 0 a 255.</p>
<p>Valor padrão: 3 pulsos.</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Tempo de tolerância. Tempo aguardado
por um evento de ignição ligada para que seja enviado o evento de
vibração. Se a ignição for ligada antes do fim deste tempo, o evento de
vibração não será enviado.</p>
<p>Faixa válida: 0 a 65.535 segundos (0 significa que o evento será
enviado imediatamente)</p>
<p>Valor padrão: 0 segundos</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

**Configuração do evento de aceleração brusca - Parâmetro 0x0070**

Este parâmetro é usado para configurar o evento de aceleração brusca
(veja *Eventos*). O evento é gerado quando a aceleração de um veículo
excede um determinado limite por um determinado tempo.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5"><strong>Configuração do evento de aceleração brusca -
Parâmetro 0x0070</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Campo</strong></td>
<td><strong>Significado</strong></td>
<td><strong>Tipo do dado</strong></td>
<td><strong>Unidade</strong></td>
<td><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td><p>Habilitação do evento:</p>
<ul>
<li><p>0: evento desabilitado</p></li>
<li><p>1: evento habilitado (valor padrão)</p></li>
<li><p>2 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td><p>Valor do limite de aceleração. O evento é gerado quando o valor
da aceleração atinge ou ultrapassa limite, durante um tempo igual ou
maior do que o tempo de <em>debounce</em>.</p>
<p>Faixa válida: 0 a 65.535 cm/s<sup>2</sup></p>
<p>Valor padrão: 600 cm/s<sup>2</sup> (6 m/s<sup>2</sup>)</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">cm/s<sup>2</sup></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td><p>Valor de histerese. Uma vez gerado o evento, outro evento somente
poderá ser gerado após a aceleração atingir um valor abaixo de (100 -
Histerese)% do valor limite, durante um período de tempo maior ou igual
ao tempo de <em>debounce</em>.</p>
<p>Faixa válida: 0 a 100%</p>
<p>Valor padrão: 10%</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td><p>Tempo de <em>debounce</em>. Este é o tempo em que o valor da
aceleração deve permanecer além do valor limite para que o evento seja
gerado. Também é aplicado para a histerese.</p>
<p>Faixa válida: 0 a 255 segundos (0 significa ausência de
<em>debounce</em>)</p>
<p>Valor padrão: 1 segundo</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

**Configuração do evento de freada brusca - Parâmetro 0x0071**

Este parâmetro é usado para configurar o evento de freada brusca (veja
*Eventos*). O evento é gerado quando a desaceleração de um veículo
excede um determinado limite por um determinado tempo.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de freada brusca - Parâmetro 0x0071</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação do evento:</p>
<ul>
<li><p>0: evento desabilitado</p></li>
<li><p>1: evento habilitado (valor padrão)</p></li>
<li><p>2 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor do limite de desaceleração. O
evento é gerado quando o valor da desaceleração atinge ou ultrapassa
limite, durante um tempo igual ou maior do que o tempo de
<em>debounce</em>.</p>
<p>Faixa válida: 0 a 65.535 cm/s<sup>2</sup></p>
<p>Valor padrão: 400 cm/s<sup>2</sup> (4 m/s<sup>2</sup>)</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">cm/s<sup>2</sup></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor de histerese. Uma vez gerado o
evento, outro evento somente poderá ser gerado após a desaceleração
atingir um valor abaixo de (100 - Histerese)% do valor limite, durante
um período de tempo maior ou igual ao tempo de <em>debounce</em>.</p>
<p>Faixa válida: 0 a 100%</p>
<p>Valor padrão: 10%</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Tempo de <em>debounce</em>. Este é o
tempo em que o valor da desaceleração deve permanecer além do valor
limite para que o evento seja gerado. Também é aplicado para a
histerese.</p>
<p>Faixa válida: 0 a 255 segundos (0 significa ausência de
<em>debounce</em>)</p>
<p>Valor padrão: 1 segundo</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

**Configuração do evento de freada muito brusca - Parâmetro 0x0072**

Este parâmetro é usado para configurar o evento de freada muito brusca
(veja *Eventos*). O evento é gerado quando a desaceleração de um veículo
excede um determinado limite por um determinado tempo.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 50%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
evento de freada muito brusca - Parâmetro 0x0072</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação do evento:</p>
<ul>
<li><p>0: evento desabilitado</p></li>
<li><p>1: evento habilitado (valor padrão)</p></li>
<li><p>2 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor do limite de desaceleração. O
evento é gerado quando o valor da desaceleração atinge ou ultrapassa
limite, durante um tempo igual ou maior do que o tempo de
<em>debounce</em>.</p>
<p>Faixa válida: 0 a 65.535 cm/s<sup>2</sup></p>
<p>Valor padrão: 500 cm/s<sup>2</sup> (5 m/s<sup>2</sup>)</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">cm/s<sup>2</sup></td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Valor de histerese. Uma vez gerado o
evento, outro evento somente poderá ser gerado após a desaceleração
atingir um valor abaixo de (100 - Histerese)% do valor limite, durante
um período de tempo maior ou igual ao tempo de <em>debounce</em>.</p>
<p>Faixa válida: 0 a 100%</p>
<p>Valor padrão: 10%</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Tempo de <em>debounce</em>. Este é o
tempo em que o valor da desaceleração deve permanecer além do valor
limite para que o evento seja gerado. Também é aplicado para a
histerese.</p>
<p>Faixa válida: 0 a 255 segundos (0 significa ausência de
<em>debounce</em>)</p>
<p>Valor padrão: 1 segundo</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

**Configuração da informação básica de telemetria - Parâmetro 0x0074**

Este parâmetro é usado para configurar o tipo de informação adicional
“Informação básica de telemetria” (veja  *Informação Adicional*).

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração da
informação básica de telemetria - Parâmetro 0x0074</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Primeiro evento que é capaz de gerar
informação adicional do tipo “Informação de básica de telemetria. Valor
padrão: 0x006F (Evento de movimento <em>Tilt</em>)</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Primeiro evento que é capaz de gerar
informação adicional do tipo “Informação de básica de telemetria. Valor
padrão: 0x0072 (Freada muito brusca)</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Tempo de informação antes do
evento.</p>
<p>Faixa válida: 0 a 120 segundos</p>
<p>Valor padrão: 110 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Tempo de informação após o
evento.</p>
<p>Faixa válida: 0 a 120 segundos</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">6</td>
</tr>
</tbody>
</table>

**Configuração do intervalo escalonado de transmissão com ignição
desligada - Parâmetro 0x0075**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração do
intervalo escalonado de transmissão com ignição desligada - Parâmetro
0x0075</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação:</p>
<ul>
<li><p>0: função desabilitada</p></li>
<li><p>1: função habilitada (valor padrão – o antigo parâmetro
<em><strong>TXF</strong></em> é automaticamente desabilitado)</p></li>
<li><p>2 a 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Valor do intervalo de tempo dentro do
qual o primeiro intervalo de transmissão com ignição desligada será
utilizado.</p>
<p>Faixa válida: 5 a 65.535 minutos</p>
<p>Valor padrão: 48 horas</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Primeiro intervalo de transmissão com
ignição desligada.</p>
<p>Faixa válida: 5 a 65.535 minutos</p>
<p>Valor padrão: 6 ou 12 horas, dependendo do tipo de veículo</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Segundo intervalo de transmissão com
ignição desligada.</p>
<p>Faixa válida: 5 a 65.535 minutos</p>
<p>Valor padrão: 12 ou 24 horas, dependendo do tipo de veículo</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">7</td>
</tr>
</tbody>
</table>

**Configuração de listas de relatórios - Parâmetro 0x0200**

Este parâmetro é usado para configurar as listas de relatórios. (Veja
*Relatórios*)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>Configuração de
listas de relatórios - Parâmetro 0x0200</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Significado</strong></td>
<td style="text-align: center;"><strong>Tipo do dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>RLE: Habilitação da lista de
relatórios:</p>
<ul>
<li><p>0: desabilitado (valor padrão)</p></li>
<li><p>1:habilitado</p></li>
<li><p>2 to 255: não definido, tratado como desabilitado</p></li>
</ul></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Tempo de debounce para as transições
de ignição ligada e ignição desligada. Este é o tempo durante o qual o
sinal de ignição deve permanecer no novo estado (ligado ou desligado) a
fim de que a transição seja confirmada. </p>
<p>Faixa válida: 0 a 255 segundos (0 significa ausência de
<em>debounce</em>)</p>
<p>Valor padrão: 10 segundos</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">NRP: Número de relatórios na lista</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Vetor de RPIs (índices dos
relatórios)</td>
<td style="text-align: center;">vetor de unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">NRP*2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">3 + NRP*2</td>
</tr>
</tbody>
</table>

## Parâmetros relacionados ao envio de eventos de GSM

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5">0x0023 - Parâmetro para configuração do envio de eventos
de GSM</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td>Significado</td>
<td>Tipo do dado</td>
<td>Unidade</td>
<td>Tamanho [Bytes]</td>
</tr>
<tr>
<td>1</td>
<td><p>Habilitação de eventos:</p>
<p>Bit 0 – Habilita evento 0x001D</p>
<p>Bit 1 – Habilita evento 0x001E</p></td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td colspan="4">Total</td>
<td>1</td>
</tr>
</tbody>
</table>

## Parâmetros relacionados ao envio de eventos de GPS

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0024 - Parâmetro para
configuração do envio de eventos de GPS</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td>Significado</td>
<td>Tipo do dado</td>
<td>Unidade</td>
<td>Tamanho [Bytes]</td>
</tr>
<tr>
<td>1</td>
<td><p>Habilitação de eventos:<br />
Bit 0 – Habilita evento 0x0017</p>
<p>Bit 1 – Habilita evento 0x0018</p>
<p>Bit 2 – Habilita evento 0x0019</p>
<p>Bit 3 – Habilita evento 0x001A</p>
<p>Bit 4 – Habilita evento 0x001B</p>
<p>Bit 5 – Habilita evento 0x001C</p></td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td colspan="4">Total</td>
<td>1</td>
</tr>
</tbody>
</table>

## Parâmetros gerais

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0069 - Parâmetro para
configuração do valor limite para evento de limite de velocidade</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Valor considerado para o evento de
limite de velocidade</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x006A – Configuração do
evento de limite de velocidade ultrapassado (com precisão)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação do envio do evento:</p>
<p>0: Desabilitado</p>
<p>1: Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;">Valor do limite de velocidade (Default:
80 km/h -&gt; 20480)</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Km/h x 256</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;">Valor da histerese (Default: 10%)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;"></td>
<td style="text-align: center;">Debouncing (Default: 5 s)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0078 - Parâmetro para
configuração do tempo máximo de conexão GPRS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo máximo de conexão GPRS</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0079 - Parâmetro para
configuração do número máximo de mensagens por conexão GPRS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número máximo de mensagens enviadas por
conexão GPRS</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x007A - Parâmetro para
configuração do tempo de inatividade do acelerômetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo para detecção de inatividade do
acelerômetro (ausência de pulsos)</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x007B - Parâmetro para
configuração do meio de envio de mensagens: GPRS e/ou SMS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Meio de envio de mensagens:</p>
<p>0: Desabilitado</p>
<p>1: Somente GPRS</p>
<p>2: Somente SMS</p>
<p>3: GPRS + SMS (backup: apenas quando falhar o envio por GPRS)</p>
<p>4: GPRS + SMS (redundância: as mensagens são sempre enviadas pelos 2
meios)</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x007C - Parâmetro para
configuração da ordem de envio das mensagens: Buffer LIFO/FIFO</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Ordem de envio das mensagens:</p>
<p>0: LIFO</p>
<p>1: FIFO</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x007D - Parâmetro para
configuração do tempo para entrada em modo sleep</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo para entrada em modo sleep</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x007E - Parâmetro para
alteração do protocolo de comunicação GPRS/SMS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Versão do protocolo</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Índice da chave de criptografia (se
aplicável)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Sub-índice da chave de criptografia (se
aplicável)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Tamanho da chave de criptografia (se
aplicável)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Chave de criptografia (se
aplicável)</td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">n</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Tamanho da chave de assinatura (se
aplicável)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Chave de assinatura (se aplicável)</td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">m</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">5+n+m</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x03FF - Parâmetros para
habilitar eventos de geolocalização</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Disponibilização do sensor
digital:</p>
<p>0: Indisponível</p>
<p>1: Disponível</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

## Parâmetros relacionados ao uso de dois SIM CARDs

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 36%" />
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr>
<th colspan="5">0x0080 - Parâmetro para configuração de APN/IP/Porta com
Operadora</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td>Significado</td>
<td>Tipo do dado</td>
<td>Unidade</td>
<td>Tamanho [Bytes]</td>
</tr>
<tr>
<td>1</td>
<td>Código da operadora de celular 1</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>Tamanho da APN1 (n1)</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>3</td>
<td>APN1</td>
<td>array of unsigned int 8</td>
<td>-</td>
<td>n1</td>
</tr>
<tr>
<td>4</td>
<td>Tamanho do Login1 (m1)</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>5</td>
<td>Login1</td>
<td>array of unsigned int 8</td>
<td>-</td>
<td>m1</td>
</tr>
<tr>
<td>6</td>
<td>Tamanho da Senha1 (k1)</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>7</td>
<td>Senha1</td>
<td>array of unsigned int 8</td>
<td>-</td>
<td>k1</td>
</tr>
<tr>
<td>8</td>
<td>IP 1_1</td>
<td>unsigned int 32</td>
<td>-</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>Porta 1_1</td>
<td>unsigned int 16</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>10</td>
<td>IP 1_2</td>
<td>unsigned int 32</td>
<td>-</td>
<td>4</td>
</tr>
<tr>
<td>11</td>
<td>Porta 1_2</td>
<td>unsigned int 16</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>12</td>
<td>Código da operadora de celular 2</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>13</td>
<td>Tamanho da APN2 (n2)</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>14</td>
<td>APN2</td>
<td>array of unsigned int 8</td>
<td>-</td>
<td>n2</td>
</tr>
<tr>
<td>15</td>
<td>Tamanho do Login2 (m2)</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>16</td>
<td>Login2</td>
<td>array of unsigned int 8</td>
<td>-</td>
<td>m2</td>
</tr>
<tr>
<td>17</td>
<td>Tamanho da Senha2 (k2)</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>18</td>
<td>Senha2</td>
<td>array of unsigned int 8</td>
<td>-</td>
<td>k2</td>
</tr>
<tr>
<td>19</td>
<td>IP 2_1</td>
<td>unsigned int 32</td>
<td>-</td>
<td>4</td>
</tr>
<tr>
<td>20</td>
<td>Porta 2_1</td>
<td>unsigned int 16</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>21</td>
<td>IP 2_2</td>
<td>unsigned int 32</td>
<td>-</td>
<td>4</td>
</tr>
<tr>
<td>22</td>
<td>Porta 2_2</td>
<td>unsigned int 16</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td colspan="4">Total</td>
<td>32+n1+m1+k1+<br />
n2+m2+k2</td>
</tr>
</tbody>
</table>

Os 2 parâmetros a seguir são apropriados para envio de SMS:

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 37%" />
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th colspan="5">0x0081 - Parâmetro para configuração de APN/IP/Porta com
Operadora (Mem 1)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td>Significado</td>
<td>Tipo do dado</td>
<td>Unidade</td>
<td>Tamanho [Bytes]</td>
</tr>
<tr>
<td>1</td>
<td>Código da operadora de celular 1</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td>Tamanho da APN1 (n1)</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>3</td>
<td>APN1</td>
<td>array of unsigned int 8</td>
<td>-</td>
<td>n1</td>
</tr>
<tr>
<td>4</td>
<td>Tamanho do Login1 (m1)</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>5</td>
<td>Login1</td>
<td>array of unsigned int 8</td>
<td>-</td>
<td>m1</td>
</tr>
<tr>
<td>6</td>
<td>Tamanho da Senha1 (k1)</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>7</td>
<td>Senha1</td>
<td>array of unsigned int 8</td>
<td>-</td>
<td>k1</td>
</tr>
<tr>
<td>8</td>
<td>IP 1_1</td>
<td>unsigned int 32</td>
<td>-</td>
<td>4</td>
</tr>
<tr>
<td>9</td>
<td>Porta 1_1</td>
<td>unsigned int 16</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td>10</td>
<td>IP 1_2</td>
<td>unsigned int 32</td>
<td>-</td>
<td>4</td>
</tr>
<tr>
<td>11</td>
<td>Porta 1_2</td>
<td>unsigned int 16</td>
<td>-</td>
<td>2</td>
</tr>
<tr>
<td colspan="4">Total</td>
<td>16+n1+m1+k1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 37%" />
<col style="width: 25%" />
<col style="width: 9%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0082 - Parâmetro para
configuração de APN/IP/Porta com Operadora (Mem 2)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Código da operadora de celular 2</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Tamanho da APN2 (n2)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">APN2</td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">n2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Tamanho do Login2 (m2)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Login2</td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">m2</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Tamanho da Senha2 (k2)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Senha2</td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">k2</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;">IP 2_1</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td style="text-align: center;">Porta 2_1</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: center;">IP 2_2</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td style="text-align: center;">Porta 2_2</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">16+n2+m2+k2</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 40%" />
<col style="width: 17%" />
<col style="width: 10%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0083 - Parâmetro para
configuração da prioridade de operadoras</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Código da operadora de celular 1</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Código da operadora de celular 2</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Código da operadora de celular 3</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Código da operadora de celular 4</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Código da operadora de celular 5</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0084 - Parâmetro para
gerenciamento dos SIM CARDs</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo limite sem comunicação de uma
operadora antes de comutar de SIM CARD</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Distância limite sem comunicação de uma
operadora antes de comutar de SIM CARD</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">50 metros</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0085 - Parâmetro para
gerenciamento do SIM CARD secundário</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação do SIM CARD
secundário:</p>
<p>0: Desabilitado</p>
<p>1: Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Tempo limite de comunicação com o SIM
CARD secundário (Durante falha do SIM 1)</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Distância limite de comunicação com o
SIM CARD secundário (Durante falha do SIM 1)</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">50 metros</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Tempo limite sem utilização do SIM CARD
secundário (PING)</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Duração do PING</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">9</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0086 - Parâmetro para
configuração do envio de eventos de SIM CARD</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação de eventos:<br />
Bit 0 – Habilita evento 0x0050</p>
<p>Bit 1 – Habilita evento 0x0051</p>
<p>Bit 2 – Habilita evento 0x0052</p>
<p>Bit 3 – Habilita evento 0x0053</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

## Parâmetros relacionados à antena satelital

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0088 - Parâmetro para
configuração da antena satelital</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação da antena satelital:</p>
<p>0: Desabilitado</p>
<p>1: Habilitado como backup</p>
<p>2: Habilitado como redundância</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Tempo limite sem conexão GPRS para
início do envio de posições via satélite</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Distância limite sem conexão GPRS para
início do envio de posições via satélite</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">50 metros</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Tempo limite após o retorno da conexão
GPRS para fim do uso da antena satelital</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Distância limite após o retorno da
conexão GPRS para fim do uso da antena satelital</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">50 metros</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Taxa de monitoração via satélite com
ignição ligada</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Taxa de monitoração via satélite com
ignição desligada</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">13</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5">0x0089 - Parâmetro para alteração temporária do tipo de
habilitação da antena satelital</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td>Significado</td>
<td>Tipo do dado</td>
<td>Unidade</td>
<td>Tamanho [Bytes]</td>
</tr>
<tr>
<td>1</td>
<td><p>Habilitação da antena satelital:</p>
<p>0: Desabilitado</p>
<p>1: Habilitado como backup</p>
<p>2: Habilitado como redundância</p></td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td>2</td>
<td><p>Tempo de uso do valor alterado</p>
<p>(após este tempo o valor será restaurado para aquele configurado pelo
parâmetro 0x0088)</p></td>
<td>unsigned int 16</td>
<td>minutos</td>
<td>2</td>
</tr>
<tr>
<td colspan="4">Total</td>
<td>3</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5">0x008A - Parâmetro para alteração temporária do tempo
limite sem conexão GPRS para início do envio de posições via
satélite</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td>Significado</td>
<td>Tipo do dado</td>
<td>Unidade</td>
<td>Tamanho [Bytes]</td>
</tr>
<tr>
<td>1</td>
<td>Tempo limite sem conexão GPRS para início do envio de posições via
satélite</td>
<td>unsigned int 16</td>
<td>segundos</td>
<td>2</td>
</tr>
<tr>
<td>2</td>
<td><p>Tempo de uso do valor alterado</p>
<p>(após este tempo o valor será restaurado para aquele configurado pelo
parâmetro 0x0088)</p></td>
<td>unsigned int 16</td>
<td>minutos</td>
<td>2</td>
</tr>
<tr>
<td colspan="4">Total</td>
<td>4</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x008B - Parâmetro para
alteração temporária da taxa de monitoração via satélite com ignição
ligada</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Taxa de monitoração via satélite com
ignição ligada</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Tempo de uso do valor alterado</p>
<p>(após este tempo o valor será restaurado para aquele configurado pelo
parâmetro 0x0088)</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x008C - Parâmetro para
alteração temporária da taxa de monitoração via satélite com ignição
desligada</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Taxa de monitoração via satélite com
ignição desligada</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Tempo de uso do valor alterado</p>
<p>(após este tempo o valor será restaurado para aquele configurado pelo
parâmetro 0x0088)</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x008D - Parâmetro para
configuração do pacote de mensagens</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Permissões (0 = Não, 1 = Sim):</p>
<p>Bit 0: Permissão para alterar as informações do parâmetro (o flag
será limpo após o uso das informações)</p>
<p>Bit 1: Permissão para utilização de saldo acumulado (soma do saldo do
período anterior ao saldo do novo período)</p>
<p>Bit 2: Permissão para utilização cíclica das informações do período
corrente para novos períodos (Se “0”, um novo período somente será
iniciado mediante nova configuração)</p>
<p>Bit 3: Permissão para utilização imediata das novas informações (se
“0”, apenas no próximo dia de início do período é que as informações
serão utilizadas e o flag será alterado para “1”; se “1”, considera
período com novas informações iniciado)</p>
<p>Bit 7: Ativação do período (se “0”, desabilita imediatamente o
período; se “1” e no caso do Bit 2 = 0, este flag será limpo ao término
do período)</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Número máximo de bytes que podem ser
enviados no período (pacote)</p>
<p>Limite: 0 ~ 4294967295</p>
<p>Default: Zero</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;"><p>Dia do mês em que é iniciado o
período definido para a comunicação satelital</p>
<p>Valor: Entre 1 e 31</p>
<p>Default: 1</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;"><p>Dia do mês em que é finalizado o
período definido para a comunicação satelital</p>
<p>Valor: Entre 1 e 31</p>
<p>Default: 31</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;"><p>Bytes de tolerância que podem ser
enviados além do pacote</p>
<p>Limite: 0 ~ 65535</p>
<p>Default: Zero</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;"><p>Parcela percentual restante do total
de bytes (pacote + adicionais + saldo anterior) que dispara o envio do
evento que alerta sobre a proximidade do fim dos créditos (Bytes de
tolerância não serão considerados)</p>
<p>Valor: Entre 0 e 100%</p>
<p>Default: 10%</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">10</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x008E - Parâmetro para
adição de bytes (mensagens) adicionais</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Número de bytes (mensagens) adicionais a
serem somados ao saldo de créditos disponível</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x008F - Parâmetro para
leitura de informações a respeito do uso do pacote de dados</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Informação sobre o período</p>
<p>0 = Não Ativo</p>
<p>1 = Ativo</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Início do período</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Fim do período</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Saldo de bytes adicionais pendentes
(somente serão contabilizados quando o período estiver ativo)</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Total de bytes (pacote + adicionais +
saldo anterior) considerados para o período</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Bytes enviados</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Total de bytes de tolerância
considerados para o período</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;">Bytes de tolerância enviados</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">19</td>
</tr>
</tbody>
</table>

## Parâmetros relacionados ao Horímetro

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0090 - Parâmetro de
configuração de modo de funcionamento do Horímetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação dos modos:</p>
<p>Bit 0: Ignição</p>
<p>Bit 1: Entrada Digital</p>
<p>Bit 2: Entrada de Frequência</p>
<p>Bit 3: Velocidade GPS</p>
<p>Bit 4: Velocidade Sensor</p>
<p>Bit 5: Velocidade CAN</p>
<p>Bit 6: Rotação Sensor</p>
<p>Bit 7: Rotação CAN</p>
<p>Bits 8 a 15: livres para uso futuro.</p>
<p>Valor do bit = 0: modo desabilitado.</p>
<p>Valor do bit = 1: modo habilitado.</p>
<p>Valor padrão do parâmetro: 0 (horímetro desligado - nenhuma medição
efetuada).</p></td>
<td style="text-align: center;">Bitfield</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0091 - Parâmetro de
definição da entrada Digital do Horímetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Entrada física do equipamento</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0092 - Parâmetro de
configuração da entrada de frequência do Horímetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Entrada física do equipamento</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Estado do filtro de frequência.</p>
<p>0: filtro desligado.</p>
<p>1: filtro ligado.</p>
<p>Valor padrão: 0 (filtro desligado).</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Frequência de Corte Inferior</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">Hz</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Frequência de Corte Superior</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">Hz</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">10</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0093 - Parâmetro de Limite
Inicial de Velocidade do Horímetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Limite inicial de velocidade</p>
<p>Valor padrão: 10 km/h.</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">1/256 Km/h</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0094 - Parâmetro de Limite
Inicial de Rotação do Horímetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Limite inicial de rotação</p>
<p>Valor padrão: 100 RPM.</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0095 - Parâmetro de
Configuração de Eventos do Horímetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação dos Eventos:</p>
<p>Bit 0: início de horímetro.</p>
<p>Bit 1: final de horímetro.</p>
<p>Bit 2: limiar de horímetro.</p>
<p>Bits 3 a 7: livres para uso futuro.</p>
<p>Valor do bit = 0: evento desabilitado.</p>
<p>Valor do bit = 1: evento habilitado.</p>
<p>Valor padrão: 0 (Eventos desabilitados)</p></td>
<td style="text-align: center;">Bitfield</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Usado somente quando o horímetro está
configurado para gerar evento no modo limiar. Este valor, em segundos,
define o valor do limiar (assim, quando o horímetro atinge o valor
definido por este limiar, um evento é gerado).</p>
<p>Faixa válida: <em>0 a 0xFF FF FF FF</em> (faixa de valores válidos do
horímetro).</p></td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">Segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0096 - Valor do
Horímetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Valor do Horímetro</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">Segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

## Parâmetros relacionados ao modo de segurança

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00A0 - Parâmetro para
habilitação dos eventos do modo de segurança</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Habilitação de eventos:<br />
Bit 0 - Habilita evento 0x0080<br />
Bit 1 - Habilita evento 0x0081</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00A1 - Parâmetro para
habilitação do modo de segurança</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação do modo de segurança:</p>
<p>0: Desabilitado</p>
<p>1: Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Tempo de permanência no modo de
segurança</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">3</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00A2 - Parâmetro para
alteração da taxa de monitoração GPRS com ignição ligada durante o modo
de segurança</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Taxa de monitoração GPRS com ignição
ligada durante o modo de segurança</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00A3 - Parâmetro para
alteração da taxa de monitoração GPRS com ignição desligada durante o
modo de segurança</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Taxa de monitoração GPRS com ignição
desligada durante o modo de segurança</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00A4 - Parâmetro para
configuração dos eventos de âncora</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação de eventos:<br />
Bit 0 - Habilita evento 0x0085<br />
Bit 1 - Habilita evento 0x0086</p>
<p>Bit 2 - Habilita evento 0x0087</p>
<p>Bit 3 - Habilita evento 0x0088</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

## Parâmetros relacionados ao rastreador ISCA

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00E0 - Parâmetro para
configuração do evento de configuração local</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação do evento (0x0203):<br />
0x00 – Desabilitado</p>
<p>0x01 - Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00E1 - Parâmetro para
configuração dos eventos de conexão de fonte externa</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Habilitação dos eventos:<br />
Bit 0 - Habilita evento 0x0204<br />
Bit 1 - Habilita evento 0x0205</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5">0x00E2 - Parâmetro para configuração dos eventos de
conexão USB</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td>Significado</td>
<td>Tipo do dado</td>
<td>Unidade</td>
<td>Tamanho [Bytes]</td>
</tr>
<tr>
<td>1</td>
<td>Habilitação dos eventos:<br />
Bit 0 - Habilita evento 0x0206<br />
Bit 1 - Habilita evento 0x0207</td>
<td>unsigned int 8</td>
<td>-</td>
<td>1</td>
</tr>
<tr>
<td colspan="4">Total</td>
<td>1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00E3 - Parâmetro para
configuração dos eventos de escuta</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Habilitação dos eventos:<br />
Bit 0 - Habilita evento 0x0208<br />
Bit 1 - Habilita evento 0x0209</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00E4 - Parâmetro para
configuração dos eventos de acionamento de buzzer</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Habilitação dos eventos:<br />
Bit 0 - Habilita evento 0x020A<br />
Bit 1 - Habilita evento 0x020B</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00E5 - Parâmetro para
configuração do evento de bateria baixa</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação do evento (0x020C):<br />
0x00 – Desabilitado</p>
<p>0x01 - Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00E6 - Parâmetro para
configuração dos eventos de botão de desacoplamento (violação)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Habilitação dos eventos:<br />
Bit 0 - Habilita evento 0x020D<br />
Bit 1 - Habilita evento 0x020E</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 40%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00E7 - Parâmetro para
configuração do modo de emergência</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação dos motivos de entrada em
modo de emergência:<br />
0x00 – Modo desabilitado</p>
<p>Bit 0 – Botão do usuário (assistência)</p>
<p>Bit 1 – Botão de desacoplamento (violação)</p>
<p>Bit 2 – Jammer GSM</p>
<p>Bit 3 – Jammer GPS</p>
<p>Bit 4 – Comando</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Habilitação dos eventos de entrada e
saída do modo de emergência:<br />
0x00 – Nenhum evento</p>
<p>Bit 0 – Botão do usuário (assistência)</p>
<p>Bit 1 – Botão de desacoplamento (violação)</p>
<p>Bit 2 – Jammer GSM</p>
<p>Bit 3 – Jammer GPS</p>
<p>Bit 4 – Comando</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5">0x00E8 - Parâmetro para configuração dos números de
telefones para chamadas (máx. 6)</th>
</tr>
</thead>
<tbody>
<tr>
<td>Campo</td>
<td>Significado</td>
<td>Tipo do dado</td>
<td>Unidade</td>
<td>Tamanho [Bytes]</td>
</tr>
<tr>
<td>1</td>
<td><p>Número de telefone no formato BCD:</p>
<p>DDI+DDD+Número<br />
DDI: 3 dígitos</p>
<p>DDD:3 dígitos</p>
<p>Número: 10 dígitos</p>
<p>Exemplo: 0550110998765432</p>
<p>(MSB) 0x05 0x50 0x11 0x09 0x98 0x76 0x54 0x32 (LSB)</p></td>
<td>Array of unsigned int 8</td>
<td>-</td>
<td>8</td>
</tr>
<tr>
<td colspan="4">Total (Sub-Índice)</td>
<td>8</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00E9 - Parâmetro para
configuração das taxas de monitoração</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Taxa de monitoração em movimento</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Taxa de monitoração em repouso</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Taxa de monitoração emergência</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Taxa de monitoração para atualização de
configuração</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">8</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00EA - Parâmetro para
configuração do GPS assistido</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo sem GPS válido para a primeira
requisição</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Periodicidade das requisições</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00F0 - Parâmetro para
habilitação do receptor de GPS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>0x00 – Desabilitado</p>
<p>0x01 - Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00F1 - Parâmetro para
habilitação do modem GSM</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>0x00 – Desabilitado</p>
<p>0x01 - Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00F2 - Parâmetro para
habilitação da triangulação por ERB</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>0x00 – Desabilitado</p>
<p>0x01 - Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00F3 - Parâmetro para
habilitação da comunicação em 900 MHz</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>0x00 – Desabilitado</p>
<p>0x01 - Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00F4 - Parâmetro para
habilitação do acelerômetro</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>0x00 – Desabilitado</p>
<p>0x01 - Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00F5 - Parâmetro para
habilitação da escuta</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>0x00 – Desabilitado</p>
<p>0x01 - Habilitado</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00F6 - Tempo para entrada
em modo de emergência por botão do usuário (assistência)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo para entrada em modo de
emergência</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00F7 - Tempo para entrada
em modo de emergência por botão de desacoplamento (violação)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo para entrada em modo de
emergência</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00F8 - Tempo para entrada
em modo de emergência por jammer GSM</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo para entrada em modo de
emergência</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00F9 - Tempo para entrada
em modo de emergência por jammer GPS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo para entrada em modo de
emergência</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

<table style="width:100%;">
<colgroup>
<col style="width: 9%" />
<col style="width: 33%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x00FA - Tempo para entrada
em modo de emergência por comando</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo para entrada em modo de
emergência</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">Minutos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

## Parâmetros relacionados ao uso dos sensores analógicos

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0300 - Parâmetro para
disponibilização dos sensores analógicos (1 a 31)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Vetor de bytes em que cada bit
representa um sensor analógico:</p>
<p>[Byte3,Byte2,Byte1,Byte0]</p>
<p>Ex: Sensor 1 disponível:</p>
<p>Byte3 ao Byte1 = 0x00</p>
<p>Byte 0 = 0x02</p>
<p>OBS: Bit “0” do Byte0 não é atribuído a nenhum sensor</p></td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0301 a 0x031F - Parâmetros
para disponibilização individual dos sensores analógicos (1 a 31)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Disponibilização do sensor
analógico:</p>
<p>0: Indisponível</p>
<p>1: Disponível</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 47%" />
<col style="width: 16%" />
<col style="width: 10%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0321 a 0x033F – Parâmetros
de configuração dos eventos dos sensores analógicos (1 a 31)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação de eventos:<br />
Bit 0 - Habilita evento 0x0070<br />
Bit 1 - Habilita evento 0x0071<br />
Bit 2 - Habilita evento 0x0072<br />
Bit 3 - Habilita evento 0x0073<br />
Bit 4 - Habilita evento 0x0074<br />
Bit 5 - Habilita evento 0x0075<br />
Bit 6 - Habilita evento 0x0076<br />
Bit 7 - Habilita evento 0x0077<br />
Bit 8 - Habilita evento 0x0078<br />
Bit 9 - Habilita evento 0x0079</p>
<p>Bit 15 - Habilita envio de status</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Valor mínimo (-32767 a 32767)</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Valor máximo (-32767 a 32767)</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Valor mínimo ideal (-32767 a 32767)</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Valor máximo ideal (-32767 a 32767)</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td style="text-align: center;">Variação negativa máxima permitida (0 a
-32767)</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td style="text-align: center;">Intervalo de tempo para variação
negativa máxima</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td style="text-align: center;">Variação positiva máxima permitida (0 a
32767)</td>
<td style="text-align: center;">signed int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td style="text-align: center;">Intervalo de tempo para variação
positiva máxima</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td style="text-align: center;">Histerese para o evento 0x0071</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td style="text-align: center;">Histerese para o evento 0x0073</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">12</td>
<td style="text-align: center;">Histerese para o evento 0x0075</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">13</td>
<td style="text-align: center;">Histerese para o evento 0x0077</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">14</td>
<td style="text-align: center;">Debounce para eventos 0x0070 e
0x0071</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">15</td>
<td style="text-align: center;">Debounce para eventos 0x0072 e
0x0073</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">16</td>
<td style="text-align: center;">Debounce para eventos 0x0074 e
0x0075</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">17</td>
<td style="text-align: center;">Debounce para eventos 0x0076 e
0x0077</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">30</td>
</tr>
</tbody>
</table>

##  Parâmetros relacionados ao uso dos sensores digitais

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0400 - Parâmetro para
disponibilização dos sensores digitais (1 a 95)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Vetor de bytes em que cada bit
representa um sensor digital:</p>
<p>[Byte11, Byte10,...,Byte0]</p>
<p>Ex: Sensor 1 disponível:</p>
<p>Byte11 ao Byte1 = 0x00</p>
<p>Byte 0 = 0x02</p>
<p>OBS: Bit “0” do Byte0 não é atribuído a nenhum sensor
digital</p></td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">12</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">12</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0401 a 0x045F - Parâmetros
para disponibilização individual dos sensores digitais (1 a 95)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Disponibilização do sensor
digital:</p>
<p>0: Indisponível</p>
<p>1: Disponível</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0461 a 0x04BF - Parâmetros
para configuração dos sensores digitais (1 a 95)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Habilitação de eventos:<br />
Bit 0 - Habilita evento 0x007A<br />
Bit 1 - Habilita evento 0x007B<br />
Bit 2 - Habilita evento 0x007C</p>
<p>Bit 7 - Habilita envio de status</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Lógica do sensor<br />
0: Ativo em nível baixo<br />
1: Ativo em nível alto<br />
255: Indefinido</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Tempo máximo de acionamento
permitido</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td style="text-align: center;">Debounce para eventos 0x007A</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td style="text-align: center;">Debounce para eventos 0x007B</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">6</td>
</tr>
</tbody>
</table>

##  Parâmetros relacionados ao uso dos atuadores

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x04C0 - Parâmetro para
disponibilização dos atuadores (1 a 31)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Vetor de bytes em que cada bit
representa um atuador:</p>
<p>[Byte3,Byte2,Byte1,Byte0]</p>
<p>Ex: Atuador 1 disponível:</p>
<p>Byte3 ao Byte1 = 0x00</p>
<p>Byte 0 = 0x02</p>
<p>OBS: Bit “0” do Byte0 não é atribuído a nenhum atuador</p></td>
<td style="text-align: center;">array of unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x04C1 a 0x04DF - Parâmetros
para disponibilização individual dos atuadores (1 a 31)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Disponibilização do atuador:</p>
<p>0: Indisponível</p>
<p>1: Disponível</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">1</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x04E1 a 0x04FF - Parâmetros
para configuração dos atuadores (1 a 31)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Habilitação de eventos:<br />
Bit 0 - Habilita evento 0x007D<br />
Bit 1 - Habilita evento 0x007E<br />
Bit 7 - Habilita envio de status</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;"><p>Lógica do atuador</p>
<p>0: Ativo em nível baixo</p>
<p>1: Ativo em nível alto</p>
<p>2: PWM</p>
<p>255: Indefinido</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

##  Parâmetros relacionados ao envio de informações adicionais

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 34%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;">0x0501 a 0x05FF - Parâmetros
para configuração do envio de AI (1 a 255)</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Significado</td>
<td style="text-align: center;">Tipo do dado</td>
<td style="text-align: center;">Unidade</td>
<td style="text-align: center;">Tamanho [Bytes]</td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Forma de envio da informação:<br />
Bit 0 – Evento de ign. ligada<br />
Bit 1 – Evento de ign. desligada</p>
<p>Bit 2 – Início de conexão SVR</p>
<p>Bit 3 – Fim de conexão SVR</p>
<p>Bit 4 – TXO (Posicionamento com ignição ligada)</p>
<p>Bit 5 – TXF (Posicionamento com ignição desligada)</p>
<p>Bit 6 – Todos os eventos</p>
<p>Bit 7 – BLI (Eventos de freada muito brusca e tombamento)</p>
<p>Bit 8 – Início de movimento por acelerômetro</p>
<p>Bit 9 – Fim de movimento por acelerômetro</p></td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: center;">Total</td>
<td style="text-align: center;">2</td>
</tr>
</tbody>
</table>

# Lista de Variáveis

  O conceito de Lista de Variáveis provê um mecanismo para transmitir
periodicamente valores de dados que tenham um comportamento dinâmico
(por exemplo, temperatura, tensão da bateria, etc). Com este mecanismo,
é possível monitorar remotamente o comportamento de variáveis de
interesse. As listas de variáveis são totalmente configuráveis. Este
protocolo especifica uma quantidade máxima de 16 listas de variáveis,
mas o número real de listas de variáveis suportadas depende dos recursos
do equipamento (e é possível que um determinado equipamento não suporte
lista de variáveis).

A quantidade máxima de variáveis em um alista é de 256. Novamente, o
número de variáveis suportadas depende dos recursos do equipamento. Os
principais pontos que limitam a quantidade de variáveis por lista são a
disponibilidade de memória não volátil (para armazenamento da
configuração das listas de variáveis), a quantidade de memória RAM e o
tamanho da mensagem de comunicação. Como o equipamento comunica-se com o
servidor através de IP (Internet Protocol), o tamanho máximo da mensagem
é definido pela capacidade da pilha TCP/IP implementado no equipamento.
Em geral, é esperado que o equipamento suporte mensagens da camada de
aplicação de pelo menos 256 bytes.

 A quantidade real de listas de variáveis suportadas pelo equipamento é
definida pelo parâmetro “Número de Lista de variáveis Suportadas”
(“Number of supported variables lists “ - NSVL). A quantidade máxima de
variáveis por lista é definida pelo parâmetro “Número de Variáveis
Suportadas por Lista” (“Number of supported variables per list” -
NSVRL). O tamanho máximo da mensagem de aplicação é definido pelo
parâmetro “Tamanho Máximo da Mensagem de Aplicação” (“Maximum size of
application message” - MSAM). Todos estes parâmetros são do tipo “Apenas
Leitura” (“Read Only”) e podem ser acessados pela tabela de parâmetros.

Para configurar uma lista de variáveis, os seguintes campos devem ser
definidos: 

- EVL: Habilitação da Lista de Variáveis (Enable variable list).

- DST: Destino da Lista de variáveis (Destination of variable list).

- VTIOn: Intervalo de transmissão da lista de variáveis quando a ignição
  está ligada (Variable List Transmission interval when Ignition on).

- VTIOff: Intervalo de transmissão da lista de variáveis quando a
  ignição está desligada (Variable List Transmission interval when
  Ignition off).

- NVR: número de variáveis na lista (number of variables in list).

- IVRi : índices das variáveis (indexes of variables).

Se o número de variáveis suportadas na lista é maior que o número de
variáveis pedidas, os outros índices das variáveis são preenchidos com 0
(índice 0 significa que não há variável configurada).

Para configurar uma lista de variáveis no equipamento, o servidor deve
enviar uma mensagem de Escrita de Parâmetro (“Parameter Write - PWR”)
para o equipamento, especificando o índice da lista de variáveis e os
valores dos seus campos. O equipamento deve responder com uma mensagem
de ACK, especificando no código de resposta se tudo está correto e se
ele aceita a configuração (código de resposta: sucesso) ou não (neste
caso o código de resposta deve informar a causa da falha).

 Exemplo: configurar uma lista de variáveis com as seguintes condições:

- Transmitir os valores de temperatura interna e tensões da bateria
  principal e interna.

- Índice da lista de variáveis (na tabela de parâmetros): 0x0100.

- Taxa de transmissão com ignição ligada: 1 minuto.

- Taxa de transmissão com ignição desligada: sem transmissão.

Assim, os valores da estrutura da lista de variáveis seriam:

 

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: center;">Exemplo - Lista de
Variáveis</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Campo</td>
<td style="text-align: center;">Valor</td>
</tr>
<tr>
<td style="text-align: center;">EVL</td>
<td style="text-align: center;">0x01 (Lista de variáveis
habilitada)</td>
</tr>
<tr>
<td style="text-align: center;">DST</td>
<td style="text-align: center;">0x00 (Apenas no canal serial
externo)</td>
</tr>
<tr>
<td style="text-align: center;">VTIOn</td>
<td style="text-align: center;">0x003C (transmissão com ignição ligada:
a cada 60 s)</td>
</tr>
<tr>
<td style="text-align: center;">VTIOff</td>
<td style="text-align: center;">0x0000 (sem transmissão com ignição
desligada)</td>
</tr>
<tr>
<td style="text-align: center;">NVR</td>
<td style="text-align: center;">0x03 (3 variáveis nesta lista)</td>
</tr>
<tr>
<td style="text-align: center;">IVR</td>
<td style="text-align: center;"><p>0x0002 (índice da variável de
temperatura interna)</p>
<p>0x0003 (índice da variável de tensão da bateria principal)</p>
<p>0x0004 (índice da variável de tensão da bateria interna)</p></td>
</tr>
</tbody>
</table>

 A mensagem para enviar esta configuração (Parameter Write, PWR, tipo =
0x16) seria:

 

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Campo</th>
<th style="text-align: center;">SEQ</th>
<th style="text-align: center;">MTP</th>
<th style="text-align: center;">PMI</th>
<th style="text-align: center;">PMS</th>
<th style="text-align: center;">NSI</th>
<th style="text-align: center;">PSI</th>
<th style="text-align: center;">PMD</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Conteúdo</td>
<td style="text-align: center;">xx xx xx xx</td>
<td style="text-align: center;">0x16</td>
<td style="text-align: center;">0x0100</td>
<td style="text-align: center;">0x000C</td>
<td style="text-align: center;">0x0001</td>
<td style="text-align: center;">0x0001</td>
<td style="text-align: center;">0x 01 00 00 3C 00 00 03 00 02 00 03 00
04</td>
</tr>
</tbody>
</table>

 

 E a mensagem da lista de variáveis (tipo = 0x1D) que será enviada pelo
equipamento será:

 

 

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 6%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 5%" />
<col style="width: 6%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Campo</th>
<th style="text-align: center;">SEQ</th>
<th style="text-align: center;">MTP</th>
<th style="text-align: center;">DTE</th>
<th style="text-align: center;">DTG</th>
<th style="text-align: center;">LAT</th>
<th style="text-align: center;">LNG</th>
<th style="text-align: center;">SPD</th>
<th style="text-align: center;">NVR</th>
<th style="text-align: center;">IVR1</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Conteúdo</td>
<td style="text-align: center;">xx xx xx xx</td>
<td style="text-align: center;">0x1D</td>
<td style="text-align: center;">xx xx xx xx</td>
<td style="text-align: center;">xx xx xx xx</td>
<td style="text-align: center;">xx xx xx xx</td>
<td style="text-align: center;">xx xx xx xx</td>
<td style="text-align: center;">xx</td>
<td style="text-align: center;">0x03</td>
<td style="text-align: center;">0x0002</td>
</tr>
</tbody>
</table>

 

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Campo</th>
<th style="text-align: center;">SVR1</th>
<th style="text-align: center;">VVR1</th>
<th style="text-align: center;">IVR2</th>
<th style="text-align: center;">SVR2</th>
<th style="text-align: center;">VVR2</th>
<th style="text-align: center;">IVR3</th>
<th style="text-align: center;">SVR3</th>
<th style="text-align: center;">VVR3</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Conteúdo</td>
<td style="text-align: center;">0x0001</td>
<td style="text-align: center;">xx</td>
<td style="text-align: center;">0x0003</td>
<td style="text-align: center;">0x0002</td>
<td style="text-align: center;">xx xx</td>
<td style="text-align: center;">0x0004</td>
<td style="text-align: center;">0x0002</td>
<td style="text-align: center;">xxxx</td>
</tr>
</tbody>
</table>

## Tabela de Variáveis

Variáveis são informações com comportamento dinâmico, obtidas a partir
da medição de alguma grandeza física no equipamento. A tabela de
variáveis é usada para organizar todas as variáveis e garantir um método
padrão de acesso às mesmas. Cada variável tem um determinado índice, que
pode ser usado para acessá-la (variáveis são informações de somente
leitura, elas não podem ser escritas). A tabela de variáveis é
apresentada a seguir.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 80%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;"><strong>Tabela de
Variáveis</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>Índice</strong></td>
<td style="text-align: center;"><strong>Descrição da
Variável</strong></td>
<td style="text-align: center;"><p><strong>Tamanho</strong></p>
<p><strong>[Bytes]</strong></p></td>
</tr>
<tr>
<td style="text-align: center;">0x0000</td>
<td style="text-align: center;">Indefinida.</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x0001</td>
<td style="text-align: center;">Temperatura interna do módulo.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0002</td>
<td style="text-align: center;">Carga da bateria backup.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0003</td>
<td style="text-align: center;">Tensão da bateria backup.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0004</td>
<td style="text-align: center;">Tensão da bateria principal.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0005</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x0006</td>
<td style="text-align: center;">Índice da posição mais antiga.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0007</td>
<td style="text-align: center;">Índice da posição mais nova.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0008</td>
<td style="text-align: center;">Quantidade de posições armazenadas.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0009</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x000A</td>
<td style="text-align: center;">Índice do evento mais antigo.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x000B</td>
<td style="text-align: center;">Índice do evento mais novo.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x000C</td>
<td style="text-align: center;">Quantidade de eventos armazenados.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x000D</td>
<td style="text-align: center;">Data atual.</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x000E</td>
<td style="text-align: center;">Status do bloqueio.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x000F</td>
<td style="text-align: center;">Taxa de erros de bits (Bit error
rate).</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0010</td>
<td style="text-align: center;">Status do SIM Card.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0011</td>
<td style="text-align: center;">Nível do sinal GSM.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0012</td>
<td style="text-align: center;">Status da conexão GPRS.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0013</td>
<td style="text-align: center;">Status da conexão da antena GPS
externa.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0014</td>
<td style="text-align: center;">Status do GPS.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0015</td>
<td style="text-align: center;">Status da bateria backup.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0016</td>
<td style="text-align: center;">Status da fonte de energia.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0017</td>
<td style="text-align: center;">Estado do download de software.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x0018</td>
<td style="text-align: center;">Velocidade medida pelo GPS.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x0019</td>
<td style="text-align: center;">Velocidade medida pelo sensor de
velocidade.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x001A</td>
<td style="text-align: center;">Rotação.</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td style="text-align: center;">0x001B</td>
<td style="text-align: center;">Status da ignição.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x001C</td>
<td style="text-align: center;">Status do botão de assistência.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x001D</td>
<td style="text-align: center;">Indicador de carga da bateria.</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">0x001E</td>
<td style="text-align: center;">Identificação do motorista</td>
<td style="text-align: center;">2 + n</td>
</tr>
</tbody>
</table>

**  
**

**Temperatura Interna do Módulo - Índice 0x0001**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 35%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável:
Temperatura Interna do Módulo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0001</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Temperatura interna do módulo.</td>
<td style="text-align: center;">signed int 8 </td>
<td style="text-align: center;">ºC</td>
<td style="text-align: center;">-128ºC a 127ºC</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Carga da Bateria Backup – Índice 0x0002**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 35%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Carga da
Bateria Backup</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0002</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Carga da bateria backup.</p>
<p>0%: descarregada.</p>
<p>100%: totalmente carregada.</p></td>
<td style="text-align: center;">unsigned int 8 </td>
<td style="text-align: center;">%</td>
<td style="text-align: center;">0 a 100%</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Tensão da Bateria Backup - Índice 0x0003**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Tensão da
Bateria Backup</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0003</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tensão da bateria backup.</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">mV</td>
<td style="text-align: center;">0 a 65.535 mV</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Tensão da Bateria Principal - Índice 0x0004**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Tensão da
Bateria Principal</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0004</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tensão da bateria principal.</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">mV</td>
<td style="text-align: center;">0 a 65.535 mV</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Índice da Posição Mais Antiga - Índice 0x0006**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Índice da
Posição Mais Antiga</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0006</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Este é o índice da entrada mais antiga
na fila de posições (posições que ainda não foram transmitidas ao
servidor).</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">0 a (SGA – 1)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Índice da Posição Mais Nova - Índice 0x0007**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Índice da
Posição Mais Nova</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0007</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Este é o índice da entrada mais nova na
fila de posições (posições que ainda não foram transmitidas ao
servidor).</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">0 a (SGA – 1)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Quantidade de Posições Armazenadas – Índice 0x0008**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Quantidade
de Posições Armazenadas</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0008</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Este é o valor da quantidade total de
posições que estão armazenadas na fila de posições (posições que ainda
não foram transmitidas ao servidor).</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">0 a (SGA – 1)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Índice do Evento Mais Antigo – Índice 0x000A**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Índice do
Evento Mais Antigo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x000A</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Este é o índice da entrada mais antiga
na fila de eventos (eventos que ainda não foram transmitidas ao
servidor).</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">0 a (SEA – 1)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Índice do Evento Mais Novo – Índice 0x000B**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Índice do
Evento Mais Novo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x000B</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Este é o índice da entrada mais nova na
fila de eventos (eventos que ainda não foram transmitidas ao
servidor).</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">0 a (SEA – 1)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Quantidade de Eventos Armazenados – Índice 0x000C**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Quantidade
de Eventos Armazenados</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x000C</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Este é o valor da quantidade total de
eventos que estão armazenados na fila de eventos (eventos que ainda não
foram transmitidas ao servidor).</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">0 a (SEA – 1)</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Data Atual - Índice 0x000D**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Data
Atual</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x000D</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Data e hora atuais do equipamento.</td>
<td style="text-align: center;">DateTime</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>4</strong></td>
</tr>
</tbody>
</table>

**Status do Bloqueio - Índice 0x000E**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Status do
Bloqueio</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x000E</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Status do bloqueio.</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Taxa de Erros de Bits (Bit Error Rate) - Índice 0x000F**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Taxa de
Erros de Bits</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x000F</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Taxa de erros de bits.</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Status do SIM Card - Índice 0x0010**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Status do
SIM Card</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0010</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Status do SIM card.</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Nível do Sinal GSM - Índice 0x0011**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Nível do
Sinal GSM</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0011</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Nível do sinal GSM.</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Status da Conexão GPRS – Índice 0x0012**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Status da
Conexão GPRS</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0012</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Status da conexão GPRS.</p>
<p>0: não conectado.</p>
<p>1: detectado, mas não ligado (“attached).</p>
<p>2: executando autenticação.</p>
<p>3: conectado.</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Status da Conexão da Antena GPS Externa - Índice 0x0013**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Status da
Conexão da Antena GPS Externa</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0013</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Status da conexão da antena GPS
externa.</p>
<p>0: não conectada.</p>
<p>≠ 0: conectada.</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Status do GPS - Índice 0x0014**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Status do
GPS.</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0014</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Status do GPS.</p>
<p>0: funcionando corretamente.</p>
<p>1: sem comunicação.</p>
<p>2: sem receber satélites (“no fix”).</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Status da Bateria Backup - Índice 0x0015**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Status da
Bateria Backup</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0015</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Status da bateria backup.</p>
<p>0: não inserida.</p>
<p>1: inserida, mas não funcional.</p>
<p>2: inserida e funcional.</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Status da Fonte de Alimentação - Índice 0x0016**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Status da
Fonte de Alimentação</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0016</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Status da Fonte de Alimentação.</p>
<p>0: bateria principal.</p>
<p>1: bateria backup.</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Estado do Download de Software - Índice 0x0017**

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 42%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Estado do
Download de Software</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0017</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Estado do download de software.</p>
<p>0: DOWNLOAD_INVALID<br />
1: DOWNLOAD_OFF<br />
2: DOWNLOAD_WAIT_START<br />
3: DOWNLOAD_RECEIVING<br />
4: DOWNLOAD_UPDATE_RUN_AREA<br />
5: DOWNLOAD_WAIT_STOP<br />
6: DOWNLOAD_WAIT_STOP_DISCONNECT<br />
7: DOWNLOAD_DISCONNECT<br />
8: DOWNLOAD_DONE</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Velocidade Medida por GPS - Índice 0x0018**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Velocidade
Medida por GPS</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0018</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Velocidade medida por GPS.</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">1/256 km/h</td>
<td style="text-align: center;">0 a 250.996 km/h</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Velocidade Medida por Sensor - Índice 0x0019**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Velocidade
Medida por Sensor</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x0019</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Velocidade medida por sensor.</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">1/256 km/h</td>
<td style="text-align: center;">0 a 250.996 km/h</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Rotação do Motor - Índice 0x001A**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Rotação do
Motor</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x001A</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Rotação do motor do veículo.</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">0 a 65.535 RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2</strong></td>
</tr>
</tbody>
</table>

**Status da Ignição - Índice 0x001B**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Status da
Ignição</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x001B</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Status da Ignição.</p>
<p>0: ignição desligada.</p>
<p>1: ignição ligada.</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Status do Botão de Assistência - Índice 0x001C**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Status do
Botão de Assistência</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x001C</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Status do botão de assistência.</p>
<p>0: não pressionado.</p>
<p>1: pressionado.</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Indicador de Carga da Bateria - Índice 0x001D**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável: Indicador
de Carga da Bateria</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x001D</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Indicador de carga da bateria:</p>
<p>0: bateria não carregando.</p>
<p>1: bateria carregando.</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>1</strong></td>
</tr>
</tbody>
</table>

**Identificação do motorista - Índice 0x001E**

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 36%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 16%" />
<col style="width: 11%" />
</colgroup>
<thead>
<tr>
<th colspan="6" style="text-align: center;"><strong>Variável:
Identificação do motorista</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="6" style="text-align: center;"><strong>Índice =
0x001E</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Faixa Válida</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><p>Tipo do identificador:</p>
<p>0: Inválido</p>
<p>1: Identificador PST (10 dígitos numéricos: 0 a 4294967295).</p>
<p>2 a 255: Reservado.</p></td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Tamanho do identificador</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Identificador (Formato ASCII)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">n</td>
</tr>
<tr>
<td colspan="5" style="text-align: right;"><strong>Total</strong></td>
<td style="text-align: center;"><strong>2 + n</strong></td>
</tr>
</tbody>
</table>

**  
**

# Variáveis CAN

Variáveis CAN são variáveis obtidas a partir da monitoração do
barramento CAN do veículo. Conforme o tipo e modelo do veículo, é usado
um determinado tipo de protocolo no barramento CAN. Os tipos mais comuns
são os seguintes:

- Veículos comerciais (caminhões, caminhonetes, ônibus): FMS / J1939.

- Veículos de passeio: ISO15765 (barramento presente no conector OBD do
  veículo).

Além dos protocolos padrões, cada veículo pode usar também um protocolo
proprietário. Normalmente os protocolos padrão e proprietário convivem
sem conflitos no barramento. Os protocolos proprietários normalmente tem
informações adicionais àquelas existentes no protocolo padrão.

Para evitar que a complexidade de tipos de protocolo CAN sejam
carregadas até o Servidor (Gateway), o equipamento deve detectar
automaticamente o tipo de protocolo CAN e mapear suas informações em
variáveis padrões, que podem então ser enviadas ao Gateway.

Assim, as informações dos diversos tipos de protocolos CAN foram
mapeadas e listadas em uma tabela. Estas informações são mapeadas na
tabela de variáveis e também na tabela de informações adicionais, para
que elas possam ser acessadas por qualquer um dos 2 mecanismos (lista de
variáveis e informação adicional).

Na lista de variáveis, as informações CAN são mapeadas na faixa de
índices 0x1000 a 0x1FFF (resultando em 4096 índices disponíveis). Na
tabela de informações adicionais, as informações CAN ocupam a faixa de
índices 0x80 a 0xFF (resultando em 128 índices disponíveis). Índices não
usados no momento permanecerão livres para uso futuro, em qualquer uma
das duas tabelas.

O espaço reservado para as variáveis CAN na tabela de informações
adicionais é menor pois esta tabela tem somente 256 posições disponíveis
(o índice desta tabela tem o tamanho de 1 byte, assim os índices
possíveis vão de 0x00 a 0xFF). Já a tabela de variáveis tem 65.536
posições disponíveis (o índice desta tabela tem o tamanho de 2 bytes,
assim os índices possíveis vão de 0x0000 a 0xFFFF). Desta forma, na
tabela de variáveis foi possível alocar um espaço maior para s variáveis
CAN.

Portanto, se mais de 128 variáveis CAN forem mapeadas no protocolo,
somente as primeiras 128 poderão ser acessadas pelos dois mecanismos
(informação adicional e lista de variáveis). As demais poderiam ser
acessadas somente pelo mecanismo de lista de variáveis, a não ser que
uma mudança futura no protocolo possa mapear mais informações
adicionais).

A seguir é apresentada a tabela de variáveis CAN. Esta tabela apresenta
os índices correspondentes de cada variável CAN nas tabelas de variáveis
e de informações adicionais. Após a tabela são apresentados detalhes de
cada variável, tais como identificadores correspondentes nos diversos
protocolos CAN, descrições, formatos, faixas válidas, etc.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 42%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr>
<th colspan="4" style="text-align: center;"><strong>Variáveis
CAN</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Índice na Tabela de Variáveis</td>
<td style="text-align: center;">Índice na Tabela de Informações
Adicionais</td>
<td style="text-align: center;">Nome da Variável</td>
<td style="text-align: center;">Nome Original da variável no Protocolo
CAN (Inglês)</td>
</tr>
<tr>
<td style="text-align: center;">0x1000</td>
<td style="text-align: center;">0x80</td>
<td style="text-align: center;">Tipo do protocolo CAN</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x1001</td>
<td style="text-align: center;">0x81</td>
<td style="text-align: center;">Velocidade medida pelo tacógrafo</td>
<td style="text-align: center;">Tachograph vehicle speed</td>
</tr>
<tr>
<td style="text-align: center;">0x1002</td>
<td style="text-align: center;">0x82</td>
<td style="text-align: center;">Velocidade medida por sensor na
roda</td>
<td style="text-align: center;"><p>Wheel based speed</p>
<p>Vehicle speed sensor</p></td>
</tr>
<tr>
<td style="text-align: center;">0x1003</td>
<td style="text-align: center;">0x83</td>
<td style="text-align: center;">Rotação do Motor</td>
<td style="text-align: center;"><p>Engine speed,</p>
<p>Engine RPM</p></td>
</tr>
<tr>
<td style="text-align: center;">0x1004</td>
<td style="text-align: center;">0x84</td>
<td style="text-align: center;">Odômetro Total</td>
<td style="text-align: center;">High resolution total vehicle
distance</td>
</tr>
<tr>
<td style="text-align: center;">0x1005</td>
<td style="text-align: center;">0x85</td>
<td style="text-align: center;">Horímetro Total</td>
<td style="text-align: center;">Engine total hours of operation</td>
</tr>
<tr>
<td style="text-align: center;">0x1006</td>
<td style="text-align: center;">0x86</td>
<td style="text-align: center;">Nível de combustível no tanque</td>
<td style="text-align: center;">Fuel level</td>
</tr>
<tr>
<td style="text-align: center;">0x1007</td>
<td style="text-align: center;">0x87</td>
<td style="text-align: center;">Taxa de Consumo Instantâneo de
Combustível</td>
<td style="text-align: center;">Instantaneous fuel economy</td>
</tr>
<tr>
<td style="text-align: center;">0x1008</td>
<td style="text-align: center;">0x88</td>
<td style="text-align: center;">Quantidade total de combustível
consumida, desde o início de operação do veículo</td>
<td style="text-align: center;">Engine total fuel used</td>
</tr>
<tr>
<td style="text-align: center;">0x1009</td>
<td style="text-align: center;">0x89</td>
<td style="text-align: center;">Taxa de consumo de combustível por
tempo</td>
<td style="text-align: center;">Fuel rate</td>
</tr>
<tr>
<td style="text-align: center;">0x100A</td>
<td style="text-align: center;">0x8A</td>
<td style="text-align: center;">Temperatura do Líquido de Arrefecimento
do Motor (Líquido do Radiador)</td>
<td style="text-align: center;">Engine coolant temperature</td>
</tr>
<tr>
<td style="text-align: center;">0x100B</td>
<td style="text-align: center;">0x8B</td>
<td style="text-align: center;">Temperatura do Óleo do Motor</td>
<td style="text-align: center;">Engine oil temperature</td>
</tr>
<tr>
<td style="text-align: center;">0x100C</td>
<td style="text-align: center;">0x8C</td>
<td style="text-align: center;">Temperatura do Ponto de Entrada de Ar do
Motor</td>
<td style="text-align: center;">Intake air temperature</td>
</tr>
<tr>
<td style="text-align: center;">0x100D</td>
<td style="text-align: center;">0x8D</td>
<td style="text-align: center;">Temperatura Ambiente</td>
<td style="text-align: center;">Ambient air temperature</td>
</tr>
<tr>
<td style="text-align: center;">0x100E</td>
<td style="text-align: center;">0x8E</td>
<td style="text-align: center;">Carga percentual do motor na velocidade
atual</td>
<td style="text-align: center;"><p>Engine percent load at current
speed</p>
<p>Driver’s demand engine – percent torque</p></td>
</tr>
<tr>
<td style="text-align: center;">0x100F</td>
<td style="text-align: center;">0x8F</td>
<td style="text-align: center;">Torque real do motor</td>
<td style="text-align: center;">Actual engine percent torque</td>
</tr>
<tr>
<td style="text-align: center;">0x1010</td>
<td style="text-align: center;">0x90</td>
<td style="text-align: center;">Torque real do freio auxiliar</td>
<td style="text-align: center;">Actual retarder – percent torque</td>
</tr>
<tr>
<td style="text-align: center;">0x1011</td>
<td style="text-align: center;">0x91</td>
<td style="text-align: center;">Modo de freio auxiliar em uso</td>
<td style="text-align: center;">Retarder torque mode</td>
</tr>
<tr>
<td style="text-align: center;">0x1012</td>
<td style="text-align: center;">0x92</td>
<td style="text-align: center;">Posição do pedal do acelerador</td>
<td style="text-align: center;">Accelerator pedal position</td>
</tr>
<tr>
<td style="text-align: center;">0x1013</td>
<td style="text-align: center;">0x93</td>
<td style="text-align: center;">Pressão do ar nos circuitos dos freios
de serviço</td>
<td style="text-align: center;">Service Brake Air pressure circuit
1/2</td>
</tr>
<tr>
<td style="text-align: center;">0x1014</td>
<td style="text-align: center;">0x94</td>
<td style="text-align: center;">Nível do tanque do fluído de exaustão do
diesel</td>
<td style="text-align: center;">After treatment 1 Diesel Exhaust Fluid
Tank 1 Level</td>
</tr>
<tr>
<td style="text-align: center;">0x1015</td>
<td style="text-align: center;">0x95</td>
<td style="text-align: center;">Status do piloto automático, PTO e
pedais de embreagem e freio</td>
<td style="text-align: center;"><p>Cruise control active, PTO state,
Clutch switch and Brake switch</p>
<p>Auxiliary Input Status</p></td>
</tr>
<tr>
<td style="text-align: center;">0x1016</td>
<td style="text-align: center;">0x96</td>
<td style="text-align: center;">Indicadores de status (espias)</td>
<td style="text-align: center;">Telltale Status</td>
</tr>
<tr>
<td style="text-align: center;">0x1017</td>
<td style="text-align: center;">0x97</td>
<td style="text-align: center;">Peso total do veículo</td>
<td style="text-align: center;">Gross Combination Vehicle Weight</td>
</tr>
<tr>
<td style="text-align: center;">0x1018</td>
<td style="text-align: center;">0x98</td>
<td style="text-align: center;">Peso total no eixo</td>
<td style="text-align: center;">Axle Weight</td>
</tr>
<tr>
<td style="text-align: center;">0x1019</td>
<td style="text-align: center;">0x99</td>
<td style="text-align: center;">Distância até próxima revisão</td>
<td style="text-align: center;">Service Distance</td>
</tr>
<tr>
<td style="text-align: center;">0x101A</td>
<td style="text-align: center;">0x9A</td>
<td style="text-align: center;">Número de identificação do veículo</td>
<td style="text-align: center;">Vehicle identification Number</td>
</tr>
<tr>
<td style="text-align: center;">0x101B</td>
<td style="text-align: center;">0x9B</td>
<td style="text-align: center;">Identificação dos motoristas</td>
<td style="text-align: center;">Driver 1/2 identification</td>
</tr>
<tr>
<td style="text-align: center;">0x101C</td>
<td style="text-align: center;">0x9C</td>
<td style="text-align: center;">Status dos motoristas</td>
<td style="text-align: center;">Driver 1/2 working State, Driver 1/2
card, Driver 1/2 time related states</td>
</tr>
<tr>
<td style="text-align: center;">0x101D</td>
<td style="text-align: center;">0x9D</td>
<td style="text-align: center;">Excesso de velocidade medido pelo
tacógrafo</td>
<td style="text-align: center;">Vehicle overspeed</td>
</tr>
<tr>
<td style="text-align: center;">0x101E</td>
<td style="text-align: center;">0x9E</td>
<td style="text-align: center;">Evento do tacógrafo</td>
<td style="text-align: center;">System Event</td>
</tr>
<tr>
<td style="text-align: center;">0x101F</td>
<td style="text-align: center;">0x9F</td>
<td style="text-align: center;">Versão de Software do Protocolo CAN</td>
<td style="text-align: center;">Sw-version supported</td>
</tr>
<tr>
<td style="text-align: center;">0x1020</td>
<td style="text-align: center;">0xA0</td>
<td style="text-align: center;">Distância percorrida com indicação de
falha</td>
<td style="text-align: center;">Distance travelled while MIL is
activated</td>
</tr>
<tr>
<td style="text-align: center;">0x1021</td>
<td style="text-align: center;">0xA1</td>
<td style="text-align: center;">Tempo de motor ligado com indicação de
falha</td>
<td style="text-align: center;">Minutes run by the engine while MIL
activated</td>
</tr>
<tr>
<td style="text-align: center;">0x1029</td>
<td style="text-align: center;">0xA9</td>
<td style="text-align: center;">Carga da bateria do veículo</td>
<td style="text-align: center;">Vehicle Battery charge</td>
</tr>
</tbody>
</table>

## Descrição das variáveis CAN

Este item apresenta a descrição das variáveis CAN, contendo as seguintes
informações:

- Nome.

- Índice na tabela de variáveis.

- Índice na tabela de informações adicionais.

- Nome correspondente no protocolo FMS/J1939.

- Identificador correspondente no protocolo FMS/J1939.

- Nome correspondente no protocolo OBD/ISO15765.

- Identificador correspondente no protocolo OBD/ISO15765.

- Descrição.

- Formato original no protocolo FMS/J1939.

- Formato original no protocolo OBD/ISO15765.

- Formato usado no protocolo OPEN.

- Conversão do formato do protocolo FMS/J1939 para formato do protocolo
  OPEN.

- Conversão do formato do protocolo OBD/ISO15765 para formato do
  protocolo OPEN.

Caso alguma variável não possua um valor correspondente em um protocolo
CAN específico, os campos para aquele protocolo não serão mostrados.

**Variável CAN: Tipo do Protocolo CAN**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Tipo do Protocolo
CAN</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1000</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x80</td>
</tr>
<tr>
<td>Descrição: esta variável informa qual tipo de protocolo CAN foi
detectado no veículo (a detecção é feita automaticamente pelo
equipamento ligado no veículo). Este é uma informação que não pertence a
nenhum dos protocolos CAN, sendo gerada pelo equipamento a partir da
análise das mensagens que estão fluindo pelo barramento.</td>
</tr>
<tr>
<td><p>Formato usado no protocolo OPEN: inteiro sem sinal de 8 bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Faixa válida: 0 a 255.</p>
<p>0: não existe barramento CAN no veículo.</p>
<p>1: existe barramento CAN, mas o protocolo não pode ser
identificado.</p>
<p>2: FMS / J1939 250kbps.</p>
<p>3: OBD / ISO15765 250kbps 11 bits.</p>
<p>4: J1587/J1708.</p>
<p>5: FMS / J1939 500kbps.</p>
<p>6: OBD / ISO15765 250kbps 29 bits.</p>
<p>7: OBD / ISO15765 500kbps 11 bits.</p>
<p>8: OBD / ISO15765 500kbps 29 bits.</p>
<p>9: FMS / J1939 667kbps.</p>
<p>10 a 255: livres para uso futuro.</p>
<p>Na inicialização do equipamento, esta variável deve ser carregada com
o valor 0.</p></td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Velocidade Medida pelo Tacógrafo**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Velocidade Medida
pelo Tacógrafo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1001</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x81</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Tachograph vehicle
speed</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.132/1624</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: velocidade do veículo medida pelo tacógrafo.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 16
bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 1/256 km/h.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 km/h).</p>
<p>Faixa válida: 0 a 255 km/h.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**Variável CAN: Velocidade Medida por Sensor na Roda**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Velocidade Medida
por Sensor na Roda</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1002</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x82</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Wheel based speed</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.265/84</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Vehicle speed
sensor</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x0D</td>
</tr>
<tr>
<td>Descrição: Velocidade do veículo, medida diretamente por sensor na
roda.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 16
bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 1/256 km/h.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 km/h).</p>
<p>Faixa válida: 0 a 255 km/h.</p></td>
</tr>
<tr>
<td><p>Formato original no protocolo OBD/ISO15765: inteiro sem sinal de
8 bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 1 km/h.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 km/h).</p>
<p>Faixa válida: 0 a 255 km/h.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: multiplicar por 256 (correspondente a mover o byte vindo
do CAN para o byte mais significativo da variável no formato OPEN).</td>
</tr>
</tbody>
</table>

**Variável CAN: Rotação do Motor**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Rotação do
Motor</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1003</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x83</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Engine speed</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
61.444/190</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Engine RPM</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x0C</td>
</tr>
<tr>
<td>Descrição: Valor da rotação do motor.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 16
bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 0,125 rpm.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 rpm).</p>
<p>Faixa válida: 0 a 8031,875 rpm.</p></td>
</tr>
<tr>
<td><p>Formato original no protocolo OBD/ISO15765: inteiro sem sinal de
16 bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 0,25 rpm.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 rpm).</p>
<p>Faixa válida: 0 a 16.383,75 rpm.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
OBD/ISO15765.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: multiplicar por 2.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**Variável CAN:** **Odômetro Total**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Odômetro
Total</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1004</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x84</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: High resolution total
vehicle distance</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.217/917</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: valor do odômetro total do veículo.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 32
bits.</p>
<p>Tamanho total: 4 bytes.</p>
<p>Escala: 1 bit = 5 m.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 m).</p>
<p>Faixa válida: 0 a 21.474.836,475 km.</p></td>
</tr>
<tr>
<td><p>Formato usado no protocolo OPEN: inteiro sem sinal de 32
bits.</p>
<p>Tamanho total: 4 bytes.</p>
<p>Escala: 1 bit = 1 m.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 m).</p>
<p>Faixa válida: 0 a 4.294.967,295 km.</p></td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: dividir por 5.</td>
</tr>
</tbody>
</table>

**Variável CAN: Horímetro Total**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN:</strong>
<strong>Horímetro Total</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1005</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x85</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Engine total hours of
operation</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.253/247</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: tempo acumulado de operação do motor, desde o início de
operação do veículo.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 32
bits.</p>
<p>Tamanho total: 4 bytes.</p>
<p>Escala: 1 bit = 0,05 h.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 h).</p>
<p>Faixa válida: 0 a 210.554.060,75 h.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**Variável CAN: Nível de combustível no tanque**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN:</strong>
<strong>Nível de combustível no tanque</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1006</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x86</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Fuel level 1, 2.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.276/96 (Fuel level 1), 65.276/38 (Fuel level 2).</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Fuel level
input.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x2F</td>
</tr>
<tr>
<td>Descrição: nível de combustível no tanque. No protocolo FMS/J1939,
para veículos com mais de 1 tanque, existe uma informação desta para
cada um dos tanques.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 8
bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 0,4 %.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 %).</p>
<p>Faixa válida: 0 a 100 %.</p></td>
</tr>
<tr>
<td><p>Formato original no protocolo OBD/ISO15765: inteiro sem sinal de
8 bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 100/255 %.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 %).</p>
<p>Faixa válida: 0 a 100 %.</p></td>
</tr>
<tr>
<td><p>Formato usado no protocolo OPEN:</p>
<p>Estrutura = {tlc, nct1, nct2}, onde:</p>
<p>tlc = tipo da leitura de combustível.</p>
<p>nct1 = nível de combustível do tanque 1.</p>
<p>nct2 = nível de combustível do tanque 2.</p>
<p>O formato do tipo de leitura de combustível (tlc) é o seguinte:</p>
<p>Tipo: inteiro sem sinal de 8 bits.</p>
<p>Faixa válida: 0 a 255.</p>
<p>0: valor em porcentagem da quantidade existente de combustível em
relação ao volume total do tanque.</p>
<p>1: valor em litros.</p>
<p>2 a 255: livres para uso futuro.</p>
<p>O formato do valor do nível de combustível (nct1 ou nct2) é o
seguinte:</p>
<p>Tipo: inteiro sem sinal de 8 bits.</p>
<p>Se tlc = 0 (porcentagem): igual ao formato do protocolo
FMS/J1939.</p>
<p>Se tlc = 1 (litros):</p>
<p>Escala: 1 bit = 1 l.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 l).</p>
<p>Faixa válida: 0 a 254 l.</p>
<p>Nos dois casos, o valor 255 significa que o tanque de combustível
correspondente não existe.</p>
<p>Tamanho total = 3 bytes.</p>
<p>Por exemplo, para um veículo com 1 tanque, com nível informado em
porcentagem, 60% de combustível, o valor desta estrutura seria:</p>
<p>{0, 150, 255}.</p></td>
</tr>
<tr>
<td><p>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN:</p>
<p>Montar estrutura contendo:</p>
<p>Primeiro byte: preencher com 0, caso o valor esteja em porcentagem,
ou 1, caso o valor esteja em litros.</p>
<p>Segundo byte: nível de combustível do tanque 1, com cópia direta (sem
necessidade de conversão) do valor lido no protocolo FMS/J1939, se tlc =
0. Se tlc = 1, copiar o valor em l.</p>
<p>Terceiro byte: nível de combustível do tanque 2, com cópia direta
(sem necessidade de conversão) do valor lido no protocolo FMS/J1939, se
tlc = 0. Se tlc = 1, copiar o valor em l. Se o tanque 2 não existir,
preencher com 255.</p></td>
</tr>
<tr>
<td><p>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN:</p>
<p>Montar estrutura contendo:</p>
<p>Primeiro byte: preencher com 0, caso o valor esteja em porcentagem,
ou 1, caso o valor esteja em litros.</p>
<p>Segundo byte: nível de combustível do tanque 1, multiplicar o valor
do protocolo OBD/ISO15765 por (250/255), se tlc = 0. Se tlc = 1, copiar
o valor em l.</p>
<p>Terceiro byte: nível de combustível do tanque 2, multiplicar o valor
do protocolo OBD/ISO15765 por (250/255), se tlc = 0. Se tlc = 1, copiar
o valor em l. Se o tanque 2 não existir, preencher com 255.</p></td>
</tr>
</tbody>
</table>

**Variável CAN: Taxa de Consumo Instantâneo de Combustível**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Taxa de Consumo
Instantâneo de Combustível</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1007</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x87</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Instantaneous fuel
economy.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.266/184</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: taxa de consumo instantâneo de combustível.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 16
bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 1/512 km/l.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 km/l).</p>
<p>Faixa válida: 0 a 125,5 km/l.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**Variável CAN: Quantidade total de combustível consumida**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Quantidade total
de combustível consumida</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1008</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x88</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Engine total fuel
used.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.257/250</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: quantidade total de combustível consumida, desde o início
de operação do veículo.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 32
bits.</p>
<p>Tamanho total: 4 bytes.</p>
<p>Escala: 1 bit = 0,5 l.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 l).</p>
<p>Faixa válida: 0 a 2.105.540.607,5 l.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Taxa de consumo de combustível por tempo**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Taxa de consumo de
combustível por tempo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1009</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x89</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Fuel rate.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.266/183</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Engine Fuel
rate.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x5E</td>
</tr>
<tr>
<td>Descrição: quantidade de combustível consumida pelo motor por
unidade de tempo.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 16
bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 0,05 l/h.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 l/h).</p>
<p>Faixa válida: 0 a 3.212,75 l/h.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OBD/ISO15765: igual ao formato do
protocolo FMS/J1939.</td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
Variável CAN: Temperatura do Líquido de Arrefecimento do Motor**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Temperatura do
Líquido de Arrefecimento do Motor</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x100A</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x8A</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Engine coolant
temperature.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.262/110</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Engine coolant
temperature.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x05</td>
</tr>
<tr>
<td>Descrição: temperatura do líquido de arrefecimento do motor (líquido
do radiador).</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro de 8 bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 1°C.</p>
<p>Offset: -40°C (valor 0 da variável corresponde a -40°C).</p>
<p>Faixa válida: -40°C a 215°C.</p></td>
</tr>
<tr>
<td>Formato original no protocolo OBD/ISO15765: igual ao formato do
protocolo FMS/J1939.</td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Temperatura do Óleo do Motor**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Temperatura do
Óleo do Motor</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x100B</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x8B</td>
</tr>
<tr>
<td>Protocolo FMS/J1939: variável não disponível.</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Engine oil
temperature.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x5C</td>
</tr>
<tr>
<td>Descrição: temperatura do óleo do motor.</td>
</tr>
<tr>
<td><p>Formato original no protocolo OBD/ISO15765: inteiro de 8
bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 1°C.</p>
<p>Offset: -40°C (valor 0 da variável corresponde a -40°C).</p>
<p>Faixa válida: -40°C a 215°C.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
OBD/ISO15765.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Temperatura do Ponto de Entrada de Ar do Motor**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Temperatura do
Ponto de Entrada de Ar do Motor</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x100C</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x8C</td>
</tr>
<tr>
<td>Protocolo FMS/J1939: variável não disponível.</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Intake air
temperature.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):</td>
</tr>
<tr>
<td>Descrição: temperatura medida por sensor no ponto de admissão de ar
do motor.</td>
</tr>
<tr>
<td><p>Formato original no protocolo OBD/ISO15765: inteiro de 8
bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 1°C.</p>
<p>Offset: -40°C (valor 0 da variável corresponde a -40°C).</p>
<p>Faixa válida: -40°C a 215°C.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
OBD/ISO15765.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Temperatura Ambiente**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Temperatura
Ambiente</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x100D</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x8D</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Ambient air
temperature.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.269/171</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Ambient air
temperature.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x46</td>
</tr>
<tr>
<td>Descrição: temperatura do ar ao redor do veículo.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro de 16 bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 0,03125°C.</p>
<p>Offset: -273°C (valor 0 da variável corresponde a -273°C).</p>
<p>Faixa válida: -273°C a 1.774°C.</p></td>
</tr>
<tr>
<td><p>Formato original no protocolo OBD/ISO15765: inteiro de 8
bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 1°C.</p>
<p>Offset: -40°C (valor 0 da variável corresponde a -40°C).</p>
<p>Faixa válida: -40°C a 215°C.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
OBD/ISO15765.</td>
</tr>
<tr>
<td><p>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN:</p>
<ul>
<li><p>Dividir por 32.</p></li>
<li><p>Subtrair 233.</p></li>
<li><p>Truncar para 1 byte (usar o byte menos significativo).</p></li>
</ul></td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Carga percentual do motor na velocidade atual**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Carga percentual
do motor na velocidade atual</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x100E</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x8E</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Engine percent load at
current speed</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
61443/92</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Calculated engine
load value</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x04</td>
</tr>
<tr>
<td>Descrição: valor atual do torque do motor, medido em termos
porcentuais em relação ao máximo torque disponível na velocidade
atual.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 8
bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 1 %.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0%).</p>
<p>Faixa válida: 0 a 125%.</p></td>
</tr>
<tr>
<td><p>Formato original no protocolo OBD/ISO15765: inteiro sem sinal de
8 bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 100/255 %.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0%).</p>
<p>Faixa válida: 0 a 100%.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao usado no protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: dividir por 255.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Torque real do motor**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Torque real do
motor</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x100F</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x8F</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Actual engine percent
torque.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
61.444/513</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Actual engine percent
torque.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x62.</td>
</tr>
<tr>
<td>Descrição: valor atual do torque real do motor, em porcentagem, em
relação ao valor de referência.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro de 8 bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 1 %.</p>
<p>Offset: -125% (valor 0 da variável corresponde a -125%).</p>
<p>Faixa válida: -125 a 125%.</p></td>
</tr>
<tr>
<td>Formato original no protocolo OBD/ISO15765: igual ao formato do
protocolo FMS/J1939.</td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Torque real do freio auxiliar**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Torque real do
freio auxiliar</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1010</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x90</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Actual retarder –
percent torque.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
61.440/520</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: valor real do torque do freio auxiliar (retarder). É
representado como uma porcentagem do valor configurado de referência do
torque do freio auxiliar.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro de 8 bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 1 %.</p>
<p>Offset: -125% (valor 0 da variável corresponde a -125%).</p>
<p>Faixa válida: -125 a 125%.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Modo de freio auxiliar em uso**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Modo de freio
auxiliar em uso</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1011</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x91</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Retarder torque
mode.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
61.440/900.</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: sinal que indica qual modo de freio auxiliar (retarder)
está atualmente gerando, controlando ou limitando o torque.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 8
bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Faixa válida: 0 a 14.</p>
<p>0: desativado (freio auxiliar não está acionado).</p>
<p>1 a 14: há um pedido para acionar algum freio auxiliar, ou então
algum freio auxiliar está acionado.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Posição do pedal do acelerador**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Posição do pedal
do acelerador</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1012</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x92</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Accelerator pedal
position 1.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
61.443/91.</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Relative accelerator
pedal position.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x5A</td>
</tr>
<tr>
<td>Descrição: posição atual do pedal do acelerador, ou alavanca da
válvula reguladora da marcha (throttle lever), medida em termos
porcentuais da posição máxima.</td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN:</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 8
bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 0,4 %.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 %).</p>
<p>Faixa válida: 0 a 100 %.</p></td>
</tr>
<tr>
<td><p>Formato original no protocolo OBD/ISO15765: inteiro sem sinal de
8 bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 100/255 %.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 %).</p>
<p>Faixa válida: 0 a 100 %.</p></td>
</tr>
<tr>
<td>Faixa válida no protocolo OPEN: igual ao formato do protocolo
OBD/ISO15765.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: multiplicar por 255/250.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Pressão do ar nos circuitos dos freios de serviço**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Pressão do ar nos
circuitos dos freios de serviço</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1013</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x93</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Service Brake Air
pressure circuit 1/2.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.198/1087 (circuito 1), 65.198/1088 (circuito 2),</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variáveis não disponíveis.</td>
</tr>
<tr>
<td>Descrição: pressão pneumática nos circuitos ou reservatórios dos
freios de serviço 1 e 2.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: Para cada uma das 2
variáveis:</p>
<p>Tipo: inteiro sem sinal de 8 bits.</p>
<p>Tamanho total: 1 byte cada variável.</p>
<p>Escala: 1 bit = 8 kPa.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 kPa).</p>
<p>Faixa válida: 0 a 2040 kPa.</p></td>
</tr>
<tr>
<td><p>Formato usado no protocolo OPEN: Array com 2 elementos de 1 byte
cada, sendo que cada elemento tem o mesmo formato do protocolo
FMS/J1939. O primeiro elemento corresponde à pressão de ar no circuito
1, e o segundo elemento corresponde à pressão no circuito 2.</p>
<p>Tamanho total: 2 bytes.</p></td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta. O valor da pressão de ar no circuito 1 deve ser
copiado para o primeiro elemento do array, e o valor do circuito 2 deve
ser copiado para o segundo elemento do array.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Nível do tanque do fluído de exaustão do diesel**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Nível do tanque do
fluído de exaustão do diesel</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1014</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x94</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: After treatment 1 Diesel
Exhaust Fluid Tank 1 Level</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.110/1761</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: nível do tanque do fluído de exaustão do diesel.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 8
bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 0,4 %.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 %).</p>
<p>Faixa válida: 0 a 100 %.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: mesmo formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Status do piloto automático, PTO e pedais de embreagem e
freio**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Status do piloto
automático, PTO e pedais de embreagem e freio</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1015</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x95</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Cruise control active,
PTO state, Clutch switch and Brake switch</td>
</tr>
<tr>
<td><p>Identificadores correspondentes no protocolo FMS/J1939
(PGN/SPN):</p>
<p>Cruise control active: 65.265/595</p>
<p>PTO state: 65.265/976</p>
<p>Clutch switch: 65.265/598</p>
<p>Brake switch: 65.265/597</p></td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variáveis não disponíveis.</td>
</tr>
<tr>
<td><p>Descrição: esta variável no protocolo OPEN é uma reunião de
outras variáveis que trazem diversas informações sobre o veículo. Estas
informações são as seguintes:</p>
<p>Cruise control active: indica se o piloto automático (cruise control)
foi ligado.</p>
<p>PTO state: indica o estado atual ou modo de operação do dispositivo
Power Takeoff -PTO.</p>
<p>Clutch switch: sinal de chave (switch) que indica que o motorista
acionou o pedal de embreagem.</p>
<p>Brake switch: sinal de chave (switch) que indica que o motorista
acionou o pedal de freio. O pedal de freio controla o freio de serviço
do veículo (freio total do veículo) e não o freio de estacionamento
(”freio de mão”).</p></td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939:</p>
<p>Cruise control active: 2 bits, sendo os bits 2-1 do byte 4 da
mensagem.</p>
<p>00: piloto automático desligado.</p>
<p>01: piloto automático ligado.</p>
<p>10 e 11: NU.</p>
<p>PTO state: 5 bits, sendo os bits 5-1 do byte 7 da mensagem.</p>
<p>00000: PTO desativado.</p>
<p>00101: PTO ativado.</p>
<p>11111: PTO não disponível.</p>
<p>Demais valores: NU.</p>
<p>Clutch switch: 2 bits, sendo os bits 8-7 do byte 4 da mensagem.</p>
<p>00: pedal de embreagem não acionado.</p>
<p>01: pedal de embreagem acionado.</p>
<p>10 e 11: NU</p>
<p>Brake switch: 2 bits, sendo os bits 6-5 do byte 4 da mensagem.</p>
<p>00: pedal de freio não acionado.</p>
<p>01: pedal de freio acionado.</p>
<p>10 e 11: NU.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: inteiro sem sinal de 16 bits.</td>
</tr>
<tr>
<td><p>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN:</p>
<p>A variável do protocolo OPEN é montada da seguinte forma:</p>
<p>Os bits 2-1 da recebem o valor do Cruise control active (bits 2-1 do
byte 4 da mensagem)</p>
<p>Os bits 6-5 recebem o valor do Brake switch (bits 6-5 do byte 4 da
mensagem).</p>
<p>Os bits 8-7 recebem o valor do Clutch switch (bits 8-7 do byte 4 da
mensagem).</p>
<p>Os bits 13-9 recebem o valor do PTO state (bits 5-1 do byte 7 da
mensagem).</p></td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Indicadores de status (espias)**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Indicadores de
status (espias)</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1016</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x96</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Telltale Status</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN):
64.893</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: Telltale ("denunciador") é um indicador ou sinal que
mostra o status atual de uma situação, mecanismo ou sistema. Neste caso,
é um conjunto de indicadores que apresentam as condições de diversos
sinais no veículo. Cada indicador é representado por um valor de 3
bits.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: Bitmap – 3 bits, para
cada indicador.</p>
<p>000: desligado (condição OK).</p>
<p>001: condição vermelha.</p>
<p>010: condição amarela.</p>
<p>011: condição info.</p>
<p>100 a 110: NU.</p>
<p>111: informação não disponível.</p>
<p>O Identificador de Bloco (Block ID), localizado nos bits 4 a 1 do
Byte 1 da mensagem, informa qual bloco de indicadores está sendo
mostrado. São 15 blocos, sendo 0000 o bloco 1 e 1110 o bloco 15. O valor
1111 não é usado.</p></td>
</tr>
<tr>
<td><p>Formato usado no protocolo OPEN: array de 60 elementos, do tipo
inteiro sem sinal de 8 bits.</p>
<p>Cada elemento pode assumir os seguintes valores:</p>
<p>000: desligado (condição OK).</p>
<p>001: condição vermelha.</p>
<p>010: condição amarela.</p>
<p>011: condição info.</p>
<p>100 a 110: NU.</p>
<p>111: informação não disponível.</p>
<p>A posição dos elementos dentro do array está mostrada na tabela a
seguir.</p></td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: copiar cada indicador para o seu elemento correspondente
do array, zerando os bits não usados.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 38%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr>
<th rowspan="2"
style="text-align: center;"><strong>Elemento</strong></th>
<th colspan="2" style="text-align: center;"><strong>Nome</strong></th>
</tr>
<tr>
<th style="text-align: center;"><strong>Inglês</strong></th>
<th style="text-align: center;"><strong>Português</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">1</td>
<td>Cooling air conditioning</td>
<td>Ar condicionado</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td>High beam, main beam</td>
<td>Farol alto</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td>Low bean, dipped beam</td>
<td>Farol baixo</td>
</tr>
<tr>
<td style="text-align: center;">4</td>
<td>Turn Signals</td>
<td>Luzes de Direção (Setas)</td>
</tr>
<tr>
<td style="text-align: center;">5</td>
<td>Hazard warning</td>
<td>Luzes de Emergência (Pisca Alerta)</td>
</tr>
<tr>
<td style="text-align: center;">6</td>
<td>Provision for the disabled or handicapped persons</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">7</td>
<td>Parking Brake</td>
<td>Freio de estacionamento (Freio de Mão)</td>
</tr>
<tr>
<td style="text-align: center;">8</td>
<td>Brake failure/brake system malfunction</td>
<td>Falha no sistema de freios</td>
</tr>
<tr>
<td style="text-align: center;">9</td>
<td>Hatch open</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">10</td>
<td>Fuel level</td>
<td>Nível de Combustível</td>
</tr>
<tr>
<td style="text-align: center;">11</td>
<td>Engine coolant temperature</td>
<td>Temperatura do líquido de arrefecimento do motor</td>
</tr>
<tr>
<td style="text-align: center;">12</td>
<td>Battery charging condition</td>
<td>Condição de carregamento da bateria</td>
</tr>
<tr>
<td style="text-align: center;">13</td>
<td>Engine oil</td>
<td>Nível de óleo do motor</td>
</tr>
<tr>
<td style="text-align: center;">14</td>
<td>Position lights, side lights</td>
<td>Luzes Laterais</td>
</tr>
<tr>
<td style="text-align: center;">15</td>
<td>Front fog light</td>
<td>Farol de neblina dianteiro</td>
</tr>
<tr>
<td style="text-align: center;">16</td>
<td>Rear fog light</td>
<td>Farol de neblina traseiro</td>
</tr>
<tr>
<td style="text-align: center;">17</td>
<td>Park Heating</td>
<td>Pré-aquecimento (remoto) do motor ou da cabine</td>
</tr>
<tr>
<td style="text-align: center;">18</td>
<td>Engine / Mil indicator</td>
<td>Problema no motor (ou em algum item do conjunto do motor, como
injeção eletrônica, bicos, sensores, etc)</td>
</tr>
<tr>
<td style="text-align: center;">19</td>
<td>Service, call for maintenance</td>
<td>Revisão</td>
</tr>
<tr>
<td style="text-align: center;">20</td>
<td>Transmission fluid temperature</td>
<td>Temperatura do fluído da transmissão</td>
</tr>
<tr>
<td style="text-align: center;">21</td>
<td>Transmission failure/malfunction</td>
<td>Falha na transmissão</td>
</tr>
<tr>
<td style="text-align: center;">22</td>
<td>Anti-lock brake system failure</td>
<td>Falha no ABS</td>
</tr>
<tr>
<td style="text-align: center;">23</td>
<td>Worn brake linings</td>
<td>Pastilhas de freio gastas</td>
</tr>
<tr>
<td style="text-align: center;">24</td>
<td>Windscreen washer fluid/windshield washer fluid</td>
<td>Líquido do limpador de para-brisas</td>
</tr>
<tr>
<td style="text-align: center;">25</td>
<td>Tire failure/malfunction</td>
<td>Falha nos pneus</td>
</tr>
<tr>
<td style="text-align: center;">26</td>
<td>Malfunction/general failure</td>
<td>Falha geral</td>
</tr>
<tr>
<td style="text-align: center;">27</td>
<td>Engine oil temperature</td>
<td>Temperatura do óleo do motor</td>
</tr>
<tr>
<td style="text-align: center;">28</td>
<td>Engine oil level</td>
<td>Nível do óleo do motor</td>
</tr>
<tr>
<td style="text-align: center;">29</td>
<td>Engine coolant level</td>
<td>Nível do líquido de arrefecimento do motor</td>
</tr>
<tr>
<td style="text-align: center;">30</td>
<td>Steering fluid level</td>
<td>Nível do fluído de direção</td>
</tr>
<tr>
<td style="text-align: center;">31</td>
<td>Steering failure</td>
<td>Falha na direção</td>
</tr>
<tr>
<td style="text-align: center;">32</td>
<td>Height Control (Levelling)</td>
<td>Controle de altura</td>
</tr>
<tr>
<td style="text-align: center;">33</td>
<td>Retarder</td>
<td>Freio auxiliar (freio motor)</td>
</tr>
<tr>
<td style="text-align: center;">34</td>
<td>Engine Emission system failure (Mil indicator)</td>
<td>Falha no sistema de emissão do motor</td>
</tr>
<tr>
<td style="text-align: center;">35</td>
<td>ESC indication</td>
<td>Indicador do Controle Eletrônico de Estabilidade</td>
</tr>
<tr>
<td style="text-align: center;">36</td>
<td>Brake lights</td>
<td>Luzes de freio</td>
</tr>
<tr>
<td style="text-align: center;">37</td>
<td>Articulation</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">38</td>
<td>Stop Request</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">39</td>
<td>Pram request</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">40</td>
<td>Bus stop brake</td>
<td>Freio de parada de ônibus</td>
</tr>
<tr>
<td style="text-align: center;">41</td>
<td>AdBlue level</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">42</td>
<td>Raising</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">43</td>
<td>Lowering</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">44</td>
<td>Kneeling</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">45</td>
<td>Engine compartment temperature</td>
<td>Temperatura do compartimento do motor</td>
</tr>
<tr>
<td style="text-align: center;">46</td>
<td>Auxiliary air pressure</td>
<td>Pressão de ar auxiliar</td>
</tr>
<tr>
<td style="text-align: center;">47</td>
<td>Air filter clogged</td>
<td>Filtro de ar entupido</td>
</tr>
<tr>
<td style="text-align: center;">48</td>
<td>Fuel filter differential pressure</td>
<td>Pressão diferencial do filtro de combustível</td>
</tr>
<tr>
<td style="text-align: center;">49</td>
<td>Seat belt</td>
<td>Cinto de Segurança</td>
</tr>
<tr>
<td style="text-align: center;">50</td>
<td>EBS</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">51</td>
<td>Lane departure indication</td>
<td>Aviso de mudança de faixa</td>
</tr>
<tr>
<td style="text-align: center;">52</td>
<td>Advanced emergency braking system</td>
<td>Sistema avançado de freio de emergência</td>
</tr>
<tr>
<td style="text-align: center;">53</td>
<td>ACC</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">54</td>
<td>Trailer connected</td>
<td>Trailer conectado</td>
</tr>
<tr>
<td style="text-align: center;">55</td>
<td>ABS Trailer 1,2</td>
<td>ABS do Trailer 1,2</td>
</tr>
<tr>
<td style="text-align: center;">56</td>
<td>Airbag</td>
<td>Airbag</td>
</tr>
<tr>
<td style="text-align: center;">57</td>
<td>EBS Trailer 1,2</td>
<td> </td>
</tr>
<tr>
<td style="text-align: center;">58</td>
<td>Tachograph indication</td>
<td>Indicação do tacógrafo</td>
</tr>
<tr>
<td style="text-align: center;">59</td>
<td>ESC switched off</td>
<td>Controle Eletrônico de Estabilidade desligado</td>
</tr>
<tr>
<td style="text-align: center;">60</td>
<td>Lane departure warning switched off</td>
<td>Aviso de mudança de faixa desligado</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Peso total do veículo**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Peso total do
veículo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1017</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x97</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Gross Combination
Vehicle Weight.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.136/1760</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: peso total do veículo, incluindo todos os equipamentos
conectados (carretas, trailers, etc).</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 16
bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 10 kg.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 kg).</p>
<p>Faixa válida: 0 a 642.550 kg.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: mesmo do protocolo FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Peso total no eixo**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Peso total no
eixo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1018</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x98</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Axle Weight.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.258/582</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: peso total aplicado pelos pneus no pavimento, no eixo
especificado.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 16
bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 0,5 kg.</p>
<p>Offset: 0 (valor 0 da variável corresponde a 0 kg).</p>
<p>Faixa válida: 0 a 32.767 kg.</p></td>
</tr>
<tr>
<td><p>Formato usado no protocolo OPEN:</p>
<p>Estrutura = {iex, pte}, onde:</p>
<p>iex = indicador do eixo.</p>
<p>pte = peso total no eixo.</p>
<p>O formato do indicador de eixo (pte) é o seguinte:</p>
<p>Tipo: inteiro sem sinal de 8 bits.</p>
<p>Faixa válida: 0 a 255.</p>
<p>O formato do valor do peso total no eixo (pte) é igual ao formato do
protocolo FMS/J1939.</p>
<p>Tamanho total = 3 bytes.</p>
<p>Por exemplo, para um veículo com peso de 500 kg no eixo 1, o valor
desta estrutura seria:</p>
<p>{1, 1.000}.</p></td>
</tr>
<tr>
<td><p>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN:</p>
<p>Montar estrutura contendo:</p>
<p>Primeiro elemento: preencher com o valor do indicador do eixo.</p>
<p>Segundo elemento: copiar o valor do peso total no eixo, com cópia
direta (sem necessidade de conversão) do valor lido no protocolo
FMS/J1939.</p></td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Distância até a próxima revisão**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Distância até a
próxima revisão</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1019</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x99</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Service Distance.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.216/914</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: distância que ainda pode ser percorrida pelo veículo até
a próxima revisão. Um valor negativo significa que a revisão já deveria
ter sido feita.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro de 16 bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 5 km.</p>
<p>Offset: -160.635 km (valor 0 da variável corresponde a -160.635
km).</p>
<p>Faixa válida: -160.635 a 160.635 km.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: mesmo formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Número de identificação do veículo**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Número de
identificação do veículo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x101A</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x9A</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Vehicle identification
Number.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.260/237</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td><p>Descrição: o número de identificação do veículo (VIN – Vehicle
identification Number) é atribuído pelo fabricante do veículo.</p>
<p>1) Se o VIN tem um tamanho de até 8 bytes, ele é transmitido em uma
única mensagem com o PGN 0xFEEC. Bytes não usados são preenchidos com
0xFF.</p>
<p>2) Se o VIN contém mais de 8 bytes, ele é transmitido usando
mensagens TP.CM (PGN 0xEC00) com pelo menos dois TP.DT (PGN 0xEB00).</p>
<p>3) A informação transmitida pode ser somente um sub-conjunto do VIN
completo (por exemplo, podem ser transmitidos somente os últimos 8
bytes).</p></td>
</tr>
<tr>
<td>Formato original no protocolo FMS/J1939: array de caracteres. O
tamanho é variável, com máximo de 200 caracteres. O caracter “*” é
reservado como um delimitador (indica final do campo).</td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: mesmo formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Identificação dos motoristas**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Identificação dos
motoristas</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x101B</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x9B</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Driver 1/2
identification.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.131/1625 (motorista 1), 65.131/1626 (motorista 2)</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variáveis não disponíveis.</td>
</tr>
<tr>
<td>Descrição: identificações dos motoristas, efetuadas pelos cartões
inseridos no tacógrafo.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939:</p>
<p>Este campo é formado pelo Identificador do Motorista 1 + Delimitador
1 (ASCII '*') + Identificador do Motorista 2 + Delimitador 2 (ASCII
'*').</p>
<p>Se apenas o cartão do motorista 1 está presente, então são enviados
somente o parâmetro Identificador do Motorista 1 + dois Delimitadores
(ASCII "*").</p>
<p>Se apenas o cartão do motorista 2 está presente, então são enviados
um Delimitador (ASCII "*") + Identificador do Motorista 2 + um
Delimitador (ASCII "*").</p>
<p>Se nenhum cartão está presente, então são enviados dois Delimitadores
(ASCII "*"), em sequência.</p>
<p>Driver ID = Issuing member state + CardNumber = 3 + 16 Bytes (de
acordo com a ISO 16844).</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: mesmo formato usado no protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Status dos motoristas**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Status dos
motoristas</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x101C</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x9C</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Driver 1/2 working
State, Driver 1/2 card, Driver 1/2 time related states</td>
</tr>
<tr>
<td><p>Identificadores correspondentes no protocolo FMS/J1939
(PGN/SPN):</p>
<p>Driver 1 working State: 65.132/1612</p>
<p>Driver 2 working State: 65.132/1613</p>
<p>Driver 1 card: 65.132/1615</p>
<p>Driver 2 card: 65.132/1616</p>
<p>Driver 1 time related states: 65.132/1617</p>
<p>Driver 2 time related states: 65.132/1618</p></td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variáveis não disponíveis.</td>
</tr>
<tr>
<td><p>Descrição: esta variável no protocolo OPEN é uma reunião de
outras variáveis que trazem informações sobre situações dos motoristas 1
e 2. Estas informações são as seguintes:</p>
<p>Driver 1/2 working State: Estados do trabalho dos motoristas 1/2.</p>
<p>Driver 1/2 card: indicam a presença dos cartões dos motoristas
1/2.</p>
<p>Driver 1/2 time related states: indicam se os motoristas 1/2 estão se
aproximando ou excedendo o tempo limite de trabalho.</p></td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939:</p>
<p>Driver 1/2 working State: 3 bits.</p>
<p>Motorista 1: bits 6 a 4 do byte 1 da mensagem.</p>
<p>Motorista 2: bits 3 a 1 do byte 1 da mensagem.</p>
<p>000: Em descanso.</p>
<p>001: Motorista disponível.</p>
<p>010: Em trabalho.</p>
<p>011: Dirigindo.</p>
<p>100 e 101: NU.</p>
<p>110: Erro.</p>
<p>111: Não disponível.</p>
<p>Driver 1/2 card: 2 bits.</p>
<p>Motorista 1: bits 6-5 do byte 2 da mensagem.</p>
<p>Motorista 2: bits 6-5 do byte 3 da mensagem.</p>
<p>00: cartão ausente.</p>
<p>01: cartão presente.</p>
<p>10 e 11: NU.</p>
<p>Driver 1/2 time related states: 4 bits.</p>
<p>Motorista 1: bits 4 a 1 do byte 2 da mensagem.</p>
<p>Motorista 2: bits 4 a 1 do byte 3 da mensagem.</p>
<p>0000: normal.</p>
<p>0001: 15 minutos antes de 4 horas e meia.</p>
<p>0010: alcançou 4 horas e meia.</p>
<p>0011: 15 minutos antes de 9 horas.</p>
<p>0100: alcançou 9 horas.</p>
<p>0101: 15 minutos antes de 16 horas.</p>
<p>0110: alcançou 16 horas.</p>
<p>0111 a 1101: NU</p>
<p>1110: erro.</p>
<p>1111: não disponível.</p></td>
</tr>
<tr>
<td><p>Formato usado no protocolo OPEN: array de 2 elementos, sendo cada
elemento um inteiro de 16 bits sem sinal.</p>
<p>O primeiro elemento corresponde ao status do motorista 1, e o segundo
ao do motorista 2.</p></td>
</tr>
<tr>
<td><p>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: cada elemento do array é formado da seguinte forma:</p>
<p>Bits 4 a 1: recebem o valor do Driver 1/2 time related states (bits 4
a 1 do byte 2 da mensagem para o motorista 1 e bits 4 a 1 do byte 3 da
mensagem para o motorista 2).</p>
<p>Bits 6 - 5: recebem o valor do Driver 1/2 card (bits 6-5 do byte 2 da
mensagem para o motorista 1 e bits 6-5 do byte 3 da mensagem para o
motorista 2).</p>
<p>Bits 9 a 7: recebem o valor do Driver 1/2 working State (bits 6 a 4
do byte 1 da mensagem para o motorista 1 e bits 3 a 1 do byte 1 da
mensagem para o motorista 2).</p></td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Excesso de velocidade medido pelo tacógrafo**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Excesso de
velocidade medido pelo tacógrafo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x101D</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x9D</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Vehicle overspeed.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
65.132/1614</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: indicador que mostra se o veículo está excedendo o limite
de velocidade configurado no tacógrafo.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: 2 bits, correspondendo
aos bits 8-7 do byte 2 da mensagem.</p>
<p>00: não excedeu limite.</p>
<p>01: excedeu limite.</p>
<p>10 e 11: não usados no momento.</p></td>
</tr>
<tr>
<td><p>Formato usado no protocolo OPEN: inteiro sem sinal de 8 bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Faixa válida: 0,1.</p>
<p>0: não excedeu limite.</p>
<p>1: excedeu limite.</p>
<p>2 a 255: não usados no momento, livres para uso futuro.</p></td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: copiar o valor dos 2 bits da variável do protocolo
FMS/J1939 para os 2 bits menos significativos da variável do protocolo
OPEN, zerando os demais bits.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Evento do tacógrafo**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Evento do
tacógrafo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x101E</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x9E</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: System Event.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: indicador de ocorrência de evento do tacógrafo. Isto pode
incluir situações como interrupção de energia, falha no sensor de
velocidade, dados incorretos no cartão do motorista, dirigindo sem um
cartão de motorista, inserção de um cartão de motorista enquanto o
veículo está sendo dirigido e ajuste de tempo.</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: 2 bits, correspondendo
aos bits 2-1 do byte 4 da mensagem.</p>
<p>00: sem evento.</p>
<p>01: ocorreu um evento.</p>
<p>10 e 11: não usados no momento.</p></td>
</tr>
<tr>
<td><p>Formato usado no protocolo OPEN: inteiro sem sinal de 8 bits.</p>
<p>Tamanho total: 1 byte.</p>
<p>Faixa válida: 0,1.</p>
<p>0: sem evento.</p>
<p>1: ocorreu um evento.</p>
<p>2 a 255: não usados no momento, livres para uso futuro.</p></td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: copiar o valor dos 2 bits da variável do protocolo
FMS/J1939 para os 2 bits menos significativos da variável do protocolo
OPEN, zerando os demais bits.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Versão de Software do Protocolo CAN**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Versão de Software
do Protocolo CAN</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x101F</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0x9F</td>
</tr>
<tr>
<td>Nome correspondente no protocolo FMS/J1939: Sw-version
supported.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo FMS/J1939 (PGN/SPN):
64.977/2806</td>
</tr>
<tr>
<td>Protocolo OBD/ISO15765: variável não disponível.</td>
</tr>
<tr>
<td>Descrição: versão de software do protocolo CAN sob uso (no momento,
esta informação só é disponível no protocolo FMS/J1939).</td>
</tr>
<tr>
<td><p>Formato original no protocolo FMS/J1939: inteiro sem sinal de 32
bits.</p>
<p>Tamanho total: 4 bytes.</p>
<p>Formato “ab.cd”, onde “a” corresponde ao byte 2 da mensagem, “b” ao
byte 3, “c” ao byte 4 e “d” ao byte 5. Os valores “a”, “b”, “c” e “d”
são representados em ASCII.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: mesmo formato do protocolo
FMS/J1939.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo FMS/J1939 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Distância percorrida com indicação de falha**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Distância
percorrida com indicação de falha</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1020</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0xA0</td>
</tr>
<tr>
<td>Protocolo FMS/J1939: variável não disponível.</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Distance travelled
while MIL is activated.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x21.</td>
</tr>
<tr>
<td>Descrição: distância percorrida desde que o indicador MIL
(Malfunction Indicator Lamp – Indicador Genérico de Mau Funcionamento)
foi ativado.</td>
</tr>
<tr>
<td><p>Formato original no protocolo OBD/ISO15765: inteiro sem sinal de
16 bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 1 km.</p>
<p>Offset: 0 km (valor 0 da variável corresponde a 0 km).</p>
<p>Faixa válida: 0 a 65.535 km.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
OBD/ISO15765.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**  
**

**Variável CAN: Tempo de motor ligado com indicação de falha**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Tempo de motor
ligado com indicação de falha</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1021</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0xA1</td>
</tr>
<tr>
<td>Protocolo FMS/J1939: variável não disponível.</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: Minutes run by the
engine while MIL activated.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
0x4D</td>
</tr>
<tr>
<td>Descrição: tempo decorrido com motor ligado com o indicador MIL
(Malfunction Indicator Lamp – Indicador Genérico de Mau Funcionamento)
ativado.</td>
</tr>
<tr>
<td><p>Formato original no protocolo OBD/ISO15765: inteiro sem sinal de
16 bits.</p>
<p>Tamanho total: 2 bytes.</p>
<p>Escala: 1 bit = 1 min.</p>
<p>Offset: 0 min (valor 0 da variável corresponde a 0 min).</p>
<p>Faixa válida: 0 a 65.535 min.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: igual ao formato do protocolo
OBD/ISO15765.</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: direta.</td>
</tr>
</tbody>
</table>

**Variável CAN: Carga da bateria do veículo**

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;"><strong>Variável CAN: Carga da bateria
do veículo</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td>Índice na Tabela de Variáveis: 0x1029</td>
</tr>
<tr>
<td>Índice na Tabela de Informações Adicionais: 0xA9</td>
</tr>
<tr>
<td>Protocolo FMS/J1939: variável não disponível.</td>
</tr>
<tr>
<td>Nome correspondente no protocolo OBD/ISO15765: variável não
disponível.</td>
</tr>
<tr>
<td>Identificador correspondente no protocolo OBD/ISO15765 (PID):
variável não disponível.</td>
</tr>
<tr>
<td>Descrição: Porcentagem da carga da bateria do veículo elétrico</td>
</tr>
<tr>
<td><p>Tamanho total: 1 byte.</p>
<p>Escala: 1 bit = 1 %.</p>
<p>Offset: 0 min (valor 0 da variável corresponde a 0 min).</p>
<p>Faixa válida: 0 a 100%.</p></td>
</tr>
<tr>
<td>Formato usado no protocolo OPEN: -</td>
</tr>
<tr>
<td>Conversão do formato do protocolo OBD/ISO15765 para formato do
protocolo OPEN: -</td>
</tr>
</tbody>
</table>

# Comandos

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 36%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr>
<th colspan="4" style="text-align: center;">Comandos</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">CMT</td>
<td style="text-align: center;">Descrição</td>
<td style="text-align: center;">Dados do Comando (CDT1)</td>
<td style="text-align: center;">Dados do Comando (CDT2)</td>
</tr>
<tr>
<td style="text-align: center;">0x0000</td>
<td style="text-align: center;">Comando PAN</td>
<td style="text-align: center;">PAN Id, PAN Data</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0001</td>
<td style="text-align: center;">Desbloquear veículo</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0002</td>
<td style="text-align: center;">Bloquear veículo (comando simples)</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0003</td>
<td style="text-align: center;">Bloquear veículo (comando específico:
parâmetro 0x0038 será ignorado)</td>
<td style="text-align: center;"><p>0x01 (Ignição desligada e GPS
válido), 0xFF</p>
<p>0x02 (Ignição desligada), 0xFF</p>
<p>0x03 (Progressivo com limite de velocidade), Limite de Velocidade (de
10 a 100 nós)</p>
<p>0x04 (Progressivo sem limite de velocidade), 0xFF</p>
<p>0x05 (Imediato com limite de velocidade), Limite de Velocidade (de 10
a 100 nós)</p>
<p>0x06 (Imediato sem limite de velocidade), 0xFF</p>
<p>0x07 (Alerta + Progressivo com limite de velocidade), Limite de
Velocidade (de 10 a 100 nós)</p>
<p>0x08 (Alerta + Progressivo sem limite de velocidade), 0xFF</p></td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0004</td>
<td style="text-align: center;">Teste de bloqueio</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0005</td>
<td style="text-align: center;">Requisitar Posição</td>
<td style="text-align: center;"><p>0x0001 – Envia Posição por GPRS</p>
<p>0x0002 – Envia Posição por SMS</p>
<p>0x0003 – Envia Posição por 900MHz</p>
<p>0x0004 – Envia Posição por Satélite</p>
<p>0x0005 – Envia Posição com dados de GPS pelo mesmo canal de
recepção</p>
<p>0xFFFF – Envia Posição por GPRS</p></td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0006</td>
<td style="text-align: center;">Limpar memórias externas</td>
<td style="text-align: center;"><p>0x0001 – Limpar as memórias
preservando números de identificação e dados de configuração</p>
<p>0x0002 – Limpar as memórias preservando números de identificação</p>
<p>0x0003 – Limpar as memórias preservando dados de configuração</p>
<p>0x0004 – Limpar as memórias</p></td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0007</td>
<td style="text-align: center;">Limpar dados de configuração (valores
default serão assumidos)</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0008</td>
<td style="text-align: center;">Reset do módulo</td>
<td style="text-align: center;"><p>0x0001 – Hardware Reset</p>
<p>0x0002 – Software Reset</p>
<p>0x0003 – Desligar fonte de alimentação (somente para alguns
modelos)</p>
<p>0x0004 – Modem Reset</p>
<p>0x0005 – Módulo GPS Reset</p></td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0009</td>
<td style="text-align: center;">Desbloquear veículo (acessórios)</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x000A</td>
<td style="text-align: center;">Bloquear veículo (acessórios)</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x000B</td>
<td style="text-align: center;">Desacionar buzzer</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x000C</td>
<td style="text-align: center;">Acionar buzzer</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x000D</td>
<td style="text-align: center;">Desativar dispositivo</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x000E</td>
<td style="text-align: center;">Ativar dispositivo</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0010 ao 0x001F</td>
<td style="text-align: center;">Desativar saídas (Da 01 à 16)</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0020 ao 0x002F</td>
<td style="text-align: center;">Ativar saídas (Da 01 à 16)</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0030</td>
<td style="text-align: center;">Desativar modo de emergência</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0031</td>
<td style="text-align: center;">Ativar modo de emergência</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0032</td>
<td style="text-align: center;">Desativar âncora</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0033</td>
<td style="text-align: center;">Ativar âncora</td>
<td style="text-align: center;">Raio [metros]</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0034</td>
<td style="text-align: center;">Desativar modo alerta de excesso de
velocidade a seco</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0035</td>
<td style="text-align: center;">Ativar modo alerta de excesso de
velocidade a seco</td>
<td style="text-align: center;">Limite de velocidade [nós]</td>
<td style="text-align: center;">Tempo de tolerância [segundos]</td>
</tr>
<tr>
<td style="text-align: center;">0x0036</td>
<td style="text-align: center;">Desativar modo alerta de excesso de
velocidade sob chuva</td>
<td style="text-align: center;">0xFFFF</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0037</td>
<td style="text-align: center;">Ativar modo alerta de excesso de
velocidade sob chuva</td>
<td style="text-align: center;">Limite de velocidade [nós]</td>
<td style="text-align: center;">Tempo de tolerância [segundos]</td>
</tr>
<tr>
<td style="text-align: center;">0x0038</td>
<td style="text-align: center;">Configura odômetro</td>
<td style="text-align: center;">Os dois bytes mais significativos do
odômetro no mesmo formato da variável de odômetro.</td>
<td style="text-align: center;">Os dois bytes menos significativos do
odômetro no mesmo formato da variável de odômetro.</td>
</tr>
<tr>
<td style="text-align: center;">0x0039</td>
<td style="text-align: center;">Limpa arquivos embarcados</td>
<td style="text-align: center;">Número do arquivo???</td>
<td style="text-align: center;">0xFFFF</td>
</tr>
<tr>
<td style="text-align: center;">0x0040 a 0x0047</td>
<td style="text-align: center;">Reservado ELD</td>
<td style="text-align: center;">-</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x0048</td>
<td style="text-align: center;">Reinício Modo Controlado</td>
<td style="text-align: center;"><p>This parameter is used to inhibit a
sensor. The format used is the same of Sensor Status defined in the
document ControlledMode_Password_Spec.</p>
<p>If the more flag is not set in the first group, the second byte will
be ignored.</p></td>
<td style="text-align: center;"><p>This parameter is used to
enable/disable an actuator. The format used is the same of Actuator
Status defined in the document ControlledMode_Password_Spec.</p>
<p>If the more flag is not set in the first group, the second byte will
be ignored.</p></td>
</tr>
<tr>
<td style="text-align: center;">0x0049</td>
<td style="text-align: center;">Desfazer no Modo Controlado</td>
<td style="text-align: center;"><p>This parameter is used to inhibit a
sensor. The format used is the same of Sensor Status defined in the
document ControlledMode_Password_Spec.</p>
<p>If the more flag is not set in the first group, the second byte will
be ignored.</p></td>
<td style="text-align: center;"><p>This parameter is used to
enable/disable an actuator. The format used is the same of Actuator
Status defined in the document ControlledMode_Password_Spec.</p>
<p>If the more flag is not set in the first group, the second byte will
be ignored.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 34%" />
<col style="width: 19%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr>
<th colspan="4">Comandos (PND)</th>
</tr>
</thead>
<tbody>
<tr>
<td>CMT</td>
<td>Descrição</td>
<td>Dados do Comando (CDT1)</td>
<td>Dados do Comando (CDT2)</td>
</tr>
<tr>
<td>0x1001</td>
<td>Ativar Liberação do Bloqueio</td>
<td>0xFFFF</td>
<td>Validade da Liberação (Em Segundos)</td>
</tr>
<tr>
<td>0x1002</td>
<td>Desativar Liberação do Bloqueio</td>
<td>0xFFFF</td>
<td>0xFFFF</td>
</tr>
<tr>
<td>0x1003</td>
<td>Ativar Liberação da Trava de Baú 1</td>
<td>0xFFFF</td>
<td>Validade da Liberação (Em Segundos)</td>
</tr>
<tr>
<td>0x1004</td>
<td>Desativar Liberação da Trava de Baú 1</td>
<td>0xFFFF</td>
<td>0xFFFF</td>
</tr>
<tr>
<td>0x1005</td>
<td>Ativar Liberação da Trava de Baú 2</td>
<td>0xFFFF</td>
<td>Validade da Liberação (Em Segundos)</td>
</tr>
<tr>
<td>0x1006</td>
<td>Desativar Liberação da Trava de Baú 2</td>
<td>0xFFFF</td>
<td>0xFFFF</td>
</tr>
<tr>
<td>0x1007</td>
<td>Enviar Mensagem ao Condutor</td>
<td>Código da Mensagem</td>
<td>Tempo de Duração Opcional (Em Segundos)</td>
</tr>
<tr>
<td>0x1008</td>
<td>Executar POP-UP</td>
<td>Código do POP-UP</td>
<td>Tempo de Duração Opcional (Em Segundos)</td>
</tr>
<tr>
<td>0x1009</td>
<td>Executar Aviso Sonoro</td>
<td>Código do Aviso</td>
<td>Tempo de Duração Opcional (Em Segundos)</td>
</tr>
<tr>
<td>0x100A</td>
<td>Ativar Liberação da Trava de Baú 3</td>
<td>0xFFFF</td>
<td>Validade da Liberação (Em Segundos)</td>
</tr>
<tr>
<td>0x100B</td>
<td>Desativar Liberação da Trava de Baú 3</td>
<td>0xFFFF</td>
<td>0xFFFF</td>
</tr>
<tr>
<td>0x100C</td>
<td>Ativar Liberação da Trava de Quinta Roda</td>
<td>0xFFFF</td>
<td>Validade da Liberação (Em Segundos)</td>
</tr>
<tr>
<td>0x100D</td>
<td>Desativar Liberação da Trava de Quinta Roda</td>
<td>0xFFFF</td>
<td>0xFFFF</td>
</tr>
<tr>
<td>0x100E</td>
<td>Finalizar Modo Controlado</td>
<td>0xFFFF</td>
<td>0xFFFF</td>
</tr>
<tr>
<td>0x100F</td>
<td>Desfazer última alteração de estado do modo controlado</td>
<td>0xFFFF</td>
<td>0xFFFF</td>
</tr>
</tbody>
</table>

# Relatórios

Os relatórios constituem um poderoso recurso do protocolo PST OPEN. Tal
recurso é usado pelo equipamento para enviar as informações que foram
coletadas e resumidas ao longo de um período de tempo. Um bloco
de relatório é composto por três campos, como mostra a tabela abaixo.

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 17%" />
</colgroup>
<tbody>
<tr>
<td colspan="4"
style="text-align: center;"><strong>Relatório</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>RPI</strong></td>
<td style="text-align: center;"><strong>SRD</strong></td>
<td style="text-align: center;"><strong>RPD</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;"><em>SRD</em></td>
</tr>
</tbody>
</table>

- **RPI** é o campo identificador do relatório e tem tamanho de 2 bytes.
  Este campo define o tipo do relatório.

- **SRD** é o tamanho do campo de dados do relatório, com tamanho de 1
  byte. Este campo define o tamanho dos dados do relatório neste bloco.

- **RPD** é o campo de dados do relatório e seu tamanho é definido pelo
  campo ***SRD***.

O equipamento envia os relatórios para outros equipamentos ou para o
servidor por meio da “Mensagem de Lista de Relatórios” (***RPL***) –
veja ***Erro! Fonte de referência não encontrada.***. Os relatórios
podem ser configurados por meio de parâmetro específico – veja
*Parâmetros*.

**Identificadores de Relatórios**

O campo identificador de relatório é utilizado para identificar o tipo
de relatório. Ao analisar esse campo, o receptor pode facilmente
interpretar os blocos de relatório. A tabela abaixo mostra os tipos de
relatórios atualmente disponíveis no sistema. As informações detalhadas
sobre cada tipo de relatório podem ser encontradas nas próximas seções.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 74%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th colspan="3" style="text-align: center;"><strong>Tabela dos tipos de
relatório</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;"><strong>RPI</strong></td>
<td style="text-align: center;"><strong>Relatório</strong></td>
<td style="text-align: center;"><strong>Tamanho do campo de
dados</strong></td>
</tr>
<tr>
<td style="text-align: center;">0x0000</td>
<td style="text-align: center;">Reservado</td>
<td style="text-align: center;">-</td>
</tr>
<tr>
<td style="text-align: center;">0x0001</td>
<td style="text-align: center;">Tempo acumulado de motor parado com
ignição ligada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0002</td>
<td style="text-align: center;">Tempo acumulado de motor em
funcionamento com ignição ligada</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0003</td>
<td style="text-align: center;">Tempo acumulado de motor em
funcionamento abaixo da velocidade mínima</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0004</td>
<td style="text-align: center;">Tempo acumulado de motor em marcha
lenta</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0005</td>
<td style="text-align: center;">Tempo acumulado de motor na faixa ideal
de rotação</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0006</td>
<td style="text-align: center;">Tempo acumulado de motor em excesso de
rotação</td>
<td style="text-align: center;">6</td>
</tr>
<tr>
<td style="text-align: center;">0x0007</td>
<td style="text-align: center;">Tempo acumulado de motor em outras
faixas</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x0008</td>
<td style="text-align: center;">Tempo acumulado de motor com aceleração
em neutro</td>
<td style="text-align: center;">6</td>
</tr>
<tr>
<td style="text-align: center;">0x0009</td>
<td style="text-align: center;">Tempo acumulado de excesso de
velocidade</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x000A</td>
<td style="text-align: center;">Tempo acumulado de banguela</td>
<td style="text-align: center;">5</td>
</tr>
<tr>
<td style="text-align: center;">0x000B</td>
<td style="text-align: center;">Uso do limpador de para-brisa</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x000C</td>
<td style="text-align: center;">Uso do freio motor</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x000D</td>
<td style="text-align: center;">Uso do freio de serviço</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">0x000E</td>
<td style="text-align: center;">Tempo total de velocidade inválida</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Relatório: Tempo acumulado de motor parado com ignição ligada**

Este relatório informa o tempo acumulado de motor parado com a ignição
ligada, dentro de um período de tempo. O campo de dados (***RPD***)
deste relatório é apresentado na tabela abaixo.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 40%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
relatório - Tempo acumulado de motor parado com ignição
ligada</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x0001</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de motor parado com a
ignição ligada</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Relatório: Tempo acumulado do motor em funcionamento com ignição
ligada**

Este relatório informa o tempo acumulado de motor em funcionamento com a
ignição ligada, dentro de um período de tempo. O campo de dados
(***RPD***) deste relatório é apresentado na tabela abaixo.

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD – Dados do
Relatório - Tempo acumulado de motor em funcionamento com ignição
ligada</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x0002</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de motor em
funcionamento com a ignição ligada</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Relatório: Tempo acumulado de motor em funcionamento abaixo da
velocidade mínima**

Este relatório informa o tempo acumulado de motor em funcionamento
abaixo da velocidade mínima (veículo considerado parado), dentro de um
período de tempo. O campo de dados (***RPD***) deste relatório é
apresentado na tabela abaixo.

<table style="width:100%;">
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 20%" />
<col style="width: 12%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
relatório - Tempo acumulado de motor em funcionamento abaixo da
velocidade mínima</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x0003</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de motor em
funcionamento abaixo da velocidade mínima</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Relatório: Tempo acumulado do motor em marcha lenta**

Este relatório informa o tempo acumulado de motor em marcha lenta,
dentro de um período de tempo. O campo de dados (***RPD***) deste
relatório é apresentado na tabela abaixo. Os parâmetros que definem a
condição de repouso podem ser acessados através da tabela de parâmetros
(veja *Parâmetros*).

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
relatório - Tempo acumulado de motor em marcha lenta</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x0004</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de motor em marcha
lenta</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Relatório: Tempo acumulado do motor na faixa ideal de rotação**

Este relatório informa o tempo acumulado de motor na faixa ideal de
rotação, dentro de um período de tempo. O campo de dados (***RPD***)
deste relatório é apresentado na tabela abaixo. Os parâmetros que
definem a faixa ideal de rotação podem ser acessados através da tabela
de parâmetros (veja *Parâmetros*).

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
relatório - Tempo acumulado de motor na faixa ideal de
rotação</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x0005</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de motor na Faixa ideal
de rotação</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Relatório: Tempo acumulado de motor em excesso de rotação**

Este relatório informa o tempo acumulado de motor em condições acima da
faixa ideal de rotação, dentro de um período de tempo. O campo de dados
(***RPD***) deste relatório é apresentado na tabela abaixo. Os
parâmetros que definem a condição acima da faixa ideal de rotação podem
ser acessados através da tabela de parâmetros (veja *Parâmetros*).

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 22%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
Relatório - Tempo acumulado de motor em excesso de rotação</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x0006</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado do motor em excesso de
rotação</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Rotação máxima atingida durante a
condição de excesso de rotação</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">6</td>
</tr>
</tbody>
</table>

**Relatório: Tempo acumulado de motor em outras faixas**

Este relatório informa o tempo acumulado de motor com rotação em outras
faixas, dentro de um período de tempo. O campo de dados (***RPD***)
deste relatório é apresentado na tabela abaixo.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 22%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
relatório - Tempo acumulado de motor em outras faixas</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x0007</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de motor com rotação em
outras faixas</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Relatório: Tempo acumulado de motor com aceleração em neutro**

Este relatório informa o tempo acumulado de veículo parado com a rotação
do motor em condição neutra, dentro de um período de tempo. O campo de
dados (***RPD***) deste relatório é apresentado na tabela abaixo.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 22%" />
<col style="width: 11%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
relatório - Tempo acumulado de motor com aceleração em
neutro</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x0008</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de motor com aceleração
em neutro</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">2</td>
<td style="text-align: center;">Rotação máxima atingida nesta
condição</td>
<td style="text-align: center;">unsigned int 16</td>
<td style="text-align: center;">RPM</td>
<td style="text-align: center;">2</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">6</td>
</tr>
</tbody>
</table>

**Relatório: Tempo acumulado de excesso de velocidade**

Este relatório informa o tempo acumulado em que o veículo esteve com
excesso de velocidade, dentro de um período de tempo. O campo de dados
(***RPD***) deste relatório é apresentado na tabela abaixo. Os
parâmetros que definem o limite de velocidade podem ser acessados
através da tabela de parâmetros (veja *Parâmetros*).

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
Relatório - Tempo acumulado de excesso de velocidade</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x0009</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado do veículo acima do
limite de velocidade</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">Velocidade máxima atingida durante o
excesso de velocidade</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

**Relatório: Tempo acumulado de banguela**

Este relatório informa o tempo acumulado do veículo em alta velocidade
com baixa rotação (banguela), dentro de um período de tempo. O campo de
dados (***RPD***) deste relatório é apresentado na tabela abaixo. Os
parâmetros que definem a banguela podem ser acessados através da tabela
de parâmetros (veja *Parâmetros*).

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 41%" />
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
Relatório - Tempo acumulado de banguela</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x000A</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de veículo em
banguela</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: center;">3</td>
<td style="text-align: center;">A velocidade máxima atingida enquanto
estiver nessa condição (banguela)</td>
<td style="text-align: center;">unsigned int 8</td>
<td style="text-align: center;">nós</td>
<td style="text-align: center;">1</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">5</td>
</tr>
</tbody>
</table>

**Relatório: Uso do limpador de para-brisa**

Este relatório informa o tempo acumulado de uso do limpador de
para-brisa, dentro de um período de tempo. O campo de dados (***RPD***)
deste relatório é apresentado na tabela abaixo.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
Relatório - Uso do limpador de para-brisa</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x000B</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de uso do limpador de
para-brisa</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Relatório: Uso do freio motor**

Este relatório informa o tempo acumulado de uso do freio motor, dentro
de um período de tempo. O campo de dados (***RPD***) deste relatório é
apresentado na tabela abaixo.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
Relatório - Uso do freio motor</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x000C</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de uso do freio
motor</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Relatório: Uso do freio de serviço**

Este relatório informa o tempo acumulado de uso do freio de serviço,
dentro de um período de tempo. O campo de dados (***RPD***) deste
relatório é apresentado na tabela abaixo.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
Relatório - Uso do freio de serviço</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x000D</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo acumulado de uso do freio de
serviço</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Relatório: Tempo total de velocidade inválida**

Este relatório informa o tempo acumulado de uso com velocidade inválida,
dentro de um período de tempo. O campo de dados do relatório (***RPD***)
deste relatório é apresentado na tabela abaixo.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 42%" />
<col style="width: 22%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr>
<th colspan="5" style="text-align: center;"><strong>RPD - Dados do
Relatório - Tempo total de velocidade inválida</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td colspan="5" style="text-align: center;"><strong>Tipo =
0x000E</strong></td>
</tr>
<tr>
<td style="text-align: center;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>Descrição</strong></td>
<td style="text-align: center;"><strong>Tipo de dado</strong></td>
<td style="text-align: center;"><strong>Unidade</strong></td>
<td style="text-align: center;"><strong>Tamanho<br />
[Bytes]</strong></td>
</tr>
<tr>
<td style="text-align: center;">1</td>
<td style="text-align: center;">Tempo total de velocidade inválida</td>
<td style="text-align: center;">unsigned int 32</td>
<td style="text-align: center;">segundos</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td colspan="4" style="text-align: right;">Total</td>
<td style="text-align: center;">4</td>
</tr>
</tbody>
</table>

**Exemplo**

A tabela abaixo mostra um bloco contendo um relatório de "Tempo
acumulado em marcha lenta", considerando que o motor ficou em estado de
repouso durante 30 minutos neste período.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 45%" />
</colgroup>
<tbody>
<tr>
<td colspan="4" style="text-align: center;"><strong>Exemplo – Tempo
acumulado de motor em marcha lenta</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Campo</strong></td>
<td style="text-align: center;"><strong>RPI</strong></td>
<td style="text-align: center;"><strong>SRD</strong></td>
<td style="text-align: center;"><strong>RPD</strong></td>
</tr>
<tr>
<td style="text-align: left;"><strong>Tamanho [Bytes]</strong></td>
<td style="text-align: center;">2</td>
<td style="text-align: center;">1</td>
<td style="text-align: center;">4</td>
</tr>
<tr>
<td style="text-align: left;"><strong>Valor</strong></td>
<td style="text-align: center;">0x0004</td>
<td style="text-align: center;">4</td>
<td style="text-align: center;">0x00000708</td>
</tr>
</tbody>
</table>

# Apêndice A

**<u>Código da Operadora</u>**

<table>
<colgroup>
<col style="width: 68%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Operadora</th>
<th style="text-align: center;">Código</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Reservado</td>
<td style="text-align: center;">0x00</td>
</tr>
<tr>
<td style="text-align: center;">TIM</td>
<td style="text-align: center;">0x01</td>
</tr>
<tr>
<td style="text-align: center;">OI</td>
<td style="text-align: center;">0x02</td>
</tr>
<tr>
<td style="text-align: center;">CLARO</td>
<td style="text-align: center;">0x03</td>
</tr>
<tr>
<td style="text-align: center;">VIVO</td>
<td style="text-align: center;">0x04</td>
</tr>
</tbody>
</table>

**<u>Fabricante/Modelo da antena satelital</u>**

<table>
<colgroup>
<col style="width: 77%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr>
<th style="text-align: center;">Fabricante/Modelo da antena</th>
<th style="text-align: center;">Código</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Não definido</td>
<td style="text-align: center;">0x00</td>
</tr>
<tr>
<td style="text-align: center;">Skywave (DMR-800)</td>
<td style="text-align: center;">0x01</td>
</tr>
<tr>
<td style="text-align: center;">Skywave (IDP-600)</td>
<td style="text-align: center;">0x02</td>
</tr>
</tbody>
</table>

**<u>Tipos de arquivo para transferência entre servidor e módulo</u>**

**<u>Tipo 01</u>: Pontos de controle para Regras de Segurança (14 Bytes
por ponto)**

<u>Estrutura</u>:Ponto_ID / Lat / Long / Raio / Grupo do ponto

<u>Tamanho em Bytes</u>: 2 / 4 / 4 / 2 / 2

**<u>Tipo 02</u>: Cercas eletrônicas para Regras de Segurança (13 Bytes
por vértice)**

<u>Estrutura</u>: Cerca_ID / VTC (1 a n) / Lat / Long / Grupo da cerca

<u>Tamanho em Bytes</u>: 2 / 1 / 4 / 4 / 2

**<u>Tipo 03</u>: Regras de Segurança (9 Bytes por regra)**

<u>Estrutura</u>: Regra_ID / TIPO_CAMPO / PST_ID / PARAM1 / PARAM2

<u>Tamanho em Bytes</u>: 2 / 1 / 2 / 2 / 2

# Apêndice B

## Códigos de Respostas

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr>
<th colspan="2" style="text-align: center;">CÓDIGOS DE RESPOSTAS</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: center;">Valor</td>
<td style="text-align: center;">Significado</td>
</tr>
<tr>
<td style="text-align: center;">0000h</td>
<td style="text-align: center;">Indefinido</td>
</tr>
<tr>
<td style="text-align: center;">0001h</td>
<td style="text-align: center;">Mensagem desconhecida</td>
</tr>
<tr>
<td style="text-align: center;">0002h</td>
<td style="text-align: center;">Índice inválido</td>
</tr>
<tr>
<td style="text-align: center;">0003h</td>
<td style="text-align: center;">Sub-índice inválido</td>
</tr>
<tr>
<td style="text-align: center;">0004h</td>
<td style="text-align: center;">Valor inválido</td>
</tr>
<tr>
<td style="text-align: center;">0005h</td>
<td style="text-align: center;">Falha ao apagar memória</td>
</tr>
<tr>
<td style="text-align: center;">0006h</td>
<td style="text-align: center;">Falha ao escrever na memória</td>
</tr>
<tr>
<td style="text-align: center;">0007h</td>
<td style="text-align: center;">Falha ao ler da memória</td>
</tr>
<tr>
<td style="text-align: center;">0008h</td>
<td style="text-align: center;">Conteúdo de memória inválido</td>
</tr>
<tr>
<td style="text-align: center;">0009h</td>
<td style="text-align: center;">Quantidade de dados pedida é muito
grande (não cabe no buffer de transmissão)</td>
</tr>
<tr>
<td style="text-align: center;">000Ah</td>
<td style="text-align: center;">Download realizado com sucesso</td>
</tr>
<tr>
<td style="text-align: center;">000Bh</td>
<td style="text-align: center;">Falha no download</td>
</tr>
</tbody>
</table>

## Tipo de Veículo

Esta tabela indica o modelo do veículo a ser usado para o monitoramento
de trânsito.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr>
<th colspan="2">Tipo de veículo (VTY)</th>
</tr>
</thead>
<tbody>
<tr>
<td>VTY</td>
<td>Descrição</td>
</tr>
<tr>
<td>0x00</td>
<td>Indefinido</td>
</tr>
<tr>
<td>0x01</td>
<td>Carro de passeio</td>
</tr>
<tr>
<td>0x02</td>
<td>Táxi</td>
</tr>
<tr>
<td>0x03</td>
<td>Ônibus</td>
</tr>
<tr>
<td>0x04</td>
<td>Caminhão leve (pick-up)</td>
</tr>
<tr>
<td>0x05</td>
<td>Caminhão pesado</td>
</tr>
<tr>
<td>0x06</td>
<td>Motocicleta</td>
</tr>
<tr>
<td>0x07</td>
<td>Carro de polícia</td>
</tr>
<tr>
<td>0x08</td>
<td>Ambulância</td>
</tr>
<tr>
<td>0x09</td>
<td>Caminhão de bombeiro</td>
</tr>
</tbody>
</table>

## USO DOS COMANDOS PAN PELOS EQUIPAMENTOS RASTREADORES

Observação: Os comandos PAN destinados ao rastreador possuem
identificador na faixa 60h a 7Fh. É importante notar que esta faixa é
compartilhada com os equipamentos RDLink. Desta forma, qualquer comando
que não seja utilizado pelo rastreador, mesmo dentro desta faixa, deve
ser enviado ao barramento PAN. Além disso, se o rastreador receber
comandos relacionados a bloqueio (bloqueio, desbloqueio ou teste de
bloqueio) na sua faixa, ele deve executar a respectiva ação e gerar um
comando equivalente para o alarme, enviando-o ao barramento (por
exemplo, se o rastreador receber um comando de bloqueio de rastreador,
ele deve executar o bloqueio, gerar um comando de bloqueio para o alarme
e enviá-lo ao barramento). A seguir está uma lista com exemplos de
alguns comandos PAN utilizados no sistema de rastreamento.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 31%" />
<col style="width: 14%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr>
<th colspan="4">Exemplos de comandos PAN</th>
</tr>
</thead>
<tbody>
<tr>
<td>Destino</td>
<td>Descrição</td>
<td>Id PAN</td>
<td>Dado PAN</td>
</tr>
<tr>
<td>Rastreador</td>
<td>Bloqueio</td>
<td style="text-align: center;">7Eh</td>
<td>68h</td>
</tr>
<tr>
<td> </td>
<td>Desbloqueio</td>
<td style="text-align: center;">7Eh</td>
<td>67h</td>
</tr>
<tr>
<td> </td>
<td>Teste de bloqueio</td>
<td style="text-align: center;">7Eh</td>
<td>66h</td>
</tr>
<tr>
<td>Alarme</td>
<td>Bloqueio</td>
<td style="text-align: center;">BEh</td>
<td>A8h</td>
</tr>
<tr>
<td> </td>
<td>Desbloqueio</td>
<td style="text-align: center;">BEh</td>
<td>A7h</td>
</tr>
<tr>
<td> </td>
<td>Teste de bloqueio</td>
<td style="text-align: center;">BEh</td>
<td>A6h</td>
</tr>
<tr>
<td> </td>
<td>Pisca Setas</td>
<td style="text-align: center;">BAh</td>
<td>Número de piscadas</td>
</tr>
<tr>
<td> </td>
<td>Pisca Leds</td>
<td style="text-align: center;">B9h</td>
<td>Número de piscadas</td>
</tr>
<tr>
<td> </td>
<td>Aciona Chirps</td>
<td style="text-align: center;">BBh</td>
<td>Número de chirps</td>
</tr>
</tbody>
</table>

# APÊNDICE C: RESUMO DO PROCEDIMENTO DE DOWNLOAD REMOTO

Esta seção resume o procedimento utilizado para a atualização dos
equipamentos rastreadores com uma nova versão de software. Para executar
o procedimento de download, os seguintes passos devem ser executados no
servidor de rastreamento e no servidor de download:

1.  O servidor de rastreamento deverá enviar uma mensagem de “Iniciar o
    procedimento de download” (SAD) para o equipamento. Após receber a
    mensagem, o equipamento irá enviar um ACK como resposta, e, após 2
    minutos, irá desconectar-se do servidor de rastreamento e
    conectar-se ao servidor de download (o IP e a porta do servidor de
    download são especificados na mensagem).

2.  Após o equipamento conectar-se ao servidor de download, uma mensagem
    “Apagar área de download” (EDA) deverá ser enviada ao equipamento.
    Ao receber esta mensagem, o equipamento irá apagar toda a sua área
    de armazenamento do download. Se não acontecerem problemas ao apagar
    a área de download, o equipamento irá enviar um ACK como resposta.
    Caso contrário, ele responderá com um NACK.

3.  O servidor de download poderá, portanto, iniciar o envio das
    mensagens “Armazenar segmento” (SSG), contidas no arquivo
    executável. Ao receber as mensagens, o equipamento irá armazenar os
    segmentos na área apropriada. Se o segmento for válido e houver sido
    corretamente armazenado, um ACK será enviado pelo equipamento. Caso
    contrário, irá responder com um NACK.

4.  Se uma mensagem “Armazenar segmento” (SSG) não for aceita
    (equipamento responde com um NACK), o servidor de download tentará
    enviá-la novamente. Após algumas tentativas sem sucesso, o
    procedimento deverá ser reiniciado com uma mensagem “Apagar área de
    download” (EDA) (vá para o passo 2).

5.  Após enviar todos os segmentos, o servidor de download deverá enviar
    a mensagem “Verificar código” (CCD). Ao receber esta mensagem, o
    equipamento irá verificar a validade do código recebido. Se o código
    for válido, o equipamento enviará um ACK como resposta. Caso
    contrário, ele responderá com um NACK.

6.  Se a mensagem “Verificar código (CCD)” não for aceita (equipamento
    responde com um NACK), o servidor de download tentará enviá-la
    novamente. Após algumas tentativas sem sucesso, o procedimento deve
    ser reiniciado com uma mensagem “Apagar área de download” (EDA) (vá
    para o passo 2).

7.  Se a mensagem “Verificar código (CCD)” for respondida com sucesso,
    uma mensagem “Atualizar área do programa” (URA) deverá ser enviada.
    O equipamento irá responder com um ACK e pular para a rotina de
    bootloader. O código recebido será verificado novamente, e, se for
    válido, a rotina de bootloader irá atualizar o código da área de
    processamento. Ao final do bootloader, o equipamento irá se
    reinicializar e voltar ao comportamento normal, conectando-se ao
    servidor de rastreamento.

8.  Durante o procedimento de download, se, por alguma razão, for
    desejado abandonar o procedimento, o servidor de download deverá
    enviar uma mensagem “Abandonar o procedimento de download” (SOD) ao
    equipamento. Ao receber esta mensagem, o equipamento enviará um ACK
    como resposta e, após 2 minutos, irá desconectar-se do servidor de
    download e conectar-se ao servidor de rastreamento.

## FORMATO DO ARQUIVO EXECUTÁVEL

O arquivo executável é um arquivo texto ASCII contendo o código a ser
descarregado para o equipamento, contendo também informações para
verificação da validade do código. Este arquivo é formado por linhas,
cada uma representando um registro, no seguinte formato:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">:ssssttdd...cccc</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Onde cada letra representa um dígito hexadecimal.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">:</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

dois pontos, marcando o início de cada registro.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">ssss</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

é o tamanho do registro (número de bytes do registro, excluindo este
campo e os dois pontos).

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">tt</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

é o tipo do registro, que pode ser um dos seguintes valores:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">10</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

– armazenar segmento

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">11</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

– verificar código

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">12</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

– atualizar área de programa

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">dddd</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

é a parte de dados do registro. Esta é a parte que deve ser enviada na
mensagem. Esta parte corresponde ao campo SGC na mensagem “Armazenar
segmento”, ou ao campo CCS nas mensagens “Verificar código” e “Atualizar
área do programa”.

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">cccc</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

é o campo de checksum. O checksum é calculado somando-se os valores de
todos os pares de dígitos hexadecimais no registro.

Exemplo de um arquivo executável:

:000B101123456789ABCDEF00444

:001D1194236741A6519B7E02FE45671738CEAA41EC7A9250910EB52A720B89

:001D1294276741A65B9B7E02FE45681738CEAE41EC7B9C52970EB52A720BB0
