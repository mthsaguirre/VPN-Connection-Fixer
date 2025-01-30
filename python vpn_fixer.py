import subprocess
import time

def check_vpn_status():
    """Verifica se a VPN está ativa antes de executar os comandos."""
    result = subprocess.run('netsh interface show interface "VPN"', shell=True, capture_output=True, text=True)
    return "Connected" in result.stdout

def reset_network():
    """Executa comandos para resetar a conexão de forma segura."""
    commands = [
        ('ipconfig /release', '✅ IP liberado!'), 
        ('ipconfig /flushdns', '✅ Cache DNS limpo!'),
        ('ipconfig /renew', '✅ IP renovado!'),
        ('netsh interface ipv4 set dns name="Wi-Fi" static 8.8.8.8', '✅ DNS configurado (Google)!'),
        ('netsh winsock reset', '✅ Winsock resetado!')
    ]
    
    for cmd, msg in commands:
        try:
            subprocess.run(cmd, shell=True, check=True, timeout=10)
            print(msg)
        except subprocess.CalledProcessError as e:
            print(f'❌ Falha em "{cmd.split()[0]}": {e}')
        time.sleep(1)

if not check_vpn_status():
    print("⚠️ VPN desconectada! Iniciando reparo...")
    reset_network()
    print("\n🎉 Rede resetada! Conecte-se à VPN novamente.")
    # Opcional: Iniciar VPN automaticamente (ex: 'rasdial "MinhaVPN" usuario senha')
else:
    print("🔒 VPN já está conectada. Nenhuma ação necessária!")
