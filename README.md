# VPN Connection Fixer

Um script Python que resolve quedas repentinas de VPN/Wi-Fi ao automatizar comandos essenciais de rede. Ideal para quem precisa restaurar a conectividade rapidamente sem esforço manual.

## Funcionalidades
- Verifica se a VPN está desconectada antes de agir.
- Executa uma sequência de comandos para:
  - Liberar e renovar o endereço IP.
  - Limpar o cache DNS.
  - Configurar um servidor DNS estático (Google 8.8.8.8 por padrão).
  - Resetar o Winsock (resolve conflitos de conexão).
- Fornece feedback claro em cada etapa.

## Como Usar
1. Clone o repositório:
   ```bash
   git clone https://github.com/mthsaguirre/VPN-Connection-Fixer.git

2. Execute o script quando a VPN falhar:
```bash
cd VPN-Connection-Fixer
python vpn_fixer.py
