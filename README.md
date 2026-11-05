# OldWeb.today / Netcapsule

Ambiente experimental para revisitar páginas arquivadas em seus contextos históricos, com seleção de navegador, URL e data/hora.

## Estado desta implementação

Esta primeira entrega prepara a interface e a infraestrutura de replay. O replay de páginas é feito pelo pywb (CDX/Wayback). A interface oferece perfis visuais de navegadores históricos; **ela ainda não inicia contêineres com sistemas operacionais/navegadores antigos nem fornece isolamento VNC por sessão**. Isso exige imagens de navegador específicas e uma camada de orquestração, que será uma etapa posterior.

## Executar com Docker

Requisitos: Docker Engine e Docker Compose v2.

```bash
git clone https://github.com/William9079/netcapsule.git
cd netcapsule
docker compose up --build
```

Abra http://localhost:9020. O pywb fica disponível em http://localhost:8080.

## Usar

1. Escolha um navegador/perfil.
2. Informe uma URL completa (por exemplo, `https://example.com/`).
3. Informe uma data/hora. Aceita `YYYYMMDDhhmmss` ou `YYYY-MM`.
4. Clique em **Navegar no arquivo**. A página será aberta pelo replay do pywb.

## Fonte de arquivo

O pywb usa por padrão o arquivo público do Internet Archive Wayback. Para usar uma coleção CDX própria, configure `pywb/config.yaml` e monte os índices/warcs em `./archives`. Consulte a documentação do [pywb](https://pywb.readthedocs.io/).

## Estrutura

- `app/`: interface web responsiva.
- `pywb/`: configuração da coleção e armazenamento de arquivos.
- `docker-compose.yml`: serviços web e replay.
- `.env.example`: portas e opções básicas.

## Próximas etapas para emulação real

- Criar imagens Docker independentes para Mosaic, Netscape, IE/Wine, Safari/Wine e Firefox/Chrome antigos.
- Adicionar sessões descartáveis com VNC/noVNC e proxy HTTP/S por sessão.
- Conectar eventos de navegação e heartbeat para encerrar sessões inativas.
- Adicionar linha do tempo de capturas consultando CDX/Memento.

## Licença

A implementação deste repositório é distribuída conforme a licença definida pelo mantenedor. O projeto histórico Netcapsule e seus componentes mantêm suas respectivas licenças e avisos de copyright.
