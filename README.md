# Desafio b2bflow

Projeto desenvolvido em Python para ler contatos cadastrados no Supabase e enviar mensagens personalizadas via WhatsApp utilizando a Z-API.

## Mensagem enviada

```text
Olá, <nomecontato> tudo bem com você?
```

## Estrutura da tabela (Supabase)

Tabela: `contatos`

| Campo | Tipo |
|-------|------|
| id | int8 (Identity) |
| nome | text |
| telefone | text |

Exemplo:

| id | nome | telefone |
|----|------|-----------|
| 1 | Contato 1 | 5511999999999 |
| 2 | Contato 2 | 5511888888888 |

## Variáveis de ambiente

Criar um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
```

## Instalação

```bash
pip install -r requirements.txt
```

## Execução

```bash
python main.py
```

## Fluxo da aplicação

Supabase → Python → Z-API → WhatsApp