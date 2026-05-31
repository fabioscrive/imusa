# I-Musa — File di configurazione

## Struttura repo consigliata

### Repo 1: imusa-config (pubblico)
- token.json          ← token GitHub criptato
- mod_msg.json        ← messaggio di moderazione (opzionale)

### Repo 2: imusa (pubblico)
- imusa-write.html    ← app per utenti
- admin.html          ← pannello admin
- books.json          ← libreria (creato automaticamente)

## Istruzioni

1. Carica token.json su github.com/fabioscrive/imusa-config
2. Carica imusa-write.html e admin.html su github.com/fabioscrive/imusa
3. Apri imusa-write.html dal tuo hosting (GitHub Pages)
4. Apri admin.html per moderare

## Aggiornare il token

Se il token scade o viene compromesso:
1. Genera nuovo token su GitHub
2. Esegui: python generate_token.py ghp_nuovo_token
3. Sostituisci token.json su imusa-config

## Messaggio di moderazione

Crea mod_msg.json su imusa-config:
{
  "msg": "Il tuo messaggio di moderazione qui..."
}

Se assente, usa il messaggio di default.
