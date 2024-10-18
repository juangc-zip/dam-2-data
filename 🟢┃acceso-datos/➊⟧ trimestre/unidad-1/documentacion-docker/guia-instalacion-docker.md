##  ACCDAT | DOCKER | GUIA DE INSTALACION
————————————————————————————————————————————————————————————————————————————————————————————————
###   INSTALACION DOCKER | WINDOWS
####    1. DESCARGAR UBUNTU 18.04 LTS
Descargar desde la Store de Microsoft e instalar Ubuntu 18.04 LTS. Para instalar Ubuntu, debes entrar en él e introducir el usuario y contraseña que te pide (apúntalas para que no se te olviden).
- __Link de Instalacion:__ https://apps.microsoft.com/detail/9pnksf5zn4sw?hl=en-us&gl=US
————————————————————————————————————————————————————————————————————————
####    2. INSTALACION DESDE POWERSHELL
Instalar desde un PowerShell(PowerShell hay que descargarlo desde la tienda de Microsoft) WSL:
- __Comando:__ wsl --install (Posteriormente reiniciar)
Si no deja, actualizar a través del enlace:
- __Link de Instalacion:__ https://docs.microsoft.com/es-es/windows/wsl/install-manual#step-4---download-the-linux-kernel-update-package
————————————————————————————————————————————————————————————————————————
####    3. INSTALAR DOCKER DESKTOP
- __Link de Instalacion:__ https://www.docker.com/products/docker-desktop/
————————————————————————————————————————————————————————————————————————
####    4. ACTUALIZACION DE WSL A WSL2
Actualizar WSL a WSL 2: Desde cmd ejecutar:
- __Comando:__ wsl --list  
- __Comando:__ wsl --set-version nombre_que_aparezca_en_list 2
Si este paso da error, verificar en Docker Desktop que se ha habilitado WSL. En caso afirmativo, podemos seguir.
————————————————————————————————————————————————————————————————————————
####    5. HABILITAR DOCKER DESKTOP
Habilitar en Docker Desktop WSL2
————————————————————————————————————————————————————————————————————————
####    6. AÑADIR USUARIOS A WINDOWS
Añadir en Windows cada usuario que queramos que utilice Docker Desktop al grupo de usuarios: docker-users
————————————————————————————————————————————————————————————————————————
####    7. IMPORTANTE | INSTALAR DOCKER DESKTOP
Limitar los recursos de toma Vmmem. Para ello, crear el archivo .wslconfig en la carpeta C:\Users\<yourUserName>\ con el siguiente contenido:
```json
[wsl2]  
memory=4GB  
swap=0  
processors=2  
localhostForwarding=true
```
————————————————————————————————————————————————————————————————————————
####    8. FINALIZAR INSTALACION
Reiniciamos el equipo
————————————————————————————————————————————————————————————————————————————————————
###   INSTALACION DOCKER | LINUX
####    1. VERIFICAR REQUISITOS DEL SISTEMA
- CPU de 64 bits con soporte para virtualización
- Al menos 4 GB de RAM
- Kernel KVM habilitado
————————————————————————————————————————————————————————————————————————
####    2. INSTALAR DOCKER ENGINE
```bash
sudo apt-get update
sudo apt-get install ca-certificates curl gnupg lsb-release
sudo mkdir -m 0755 -p /etc/apt/keyrings curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
```
————————————————————————————————————————————————————————————————————————
####    3. DESCARGAR DOCKER DESKTOP
```bash
wget https://desktop.docker.com/linux/main/amd64/docker-desktop-<version>-amd64.deb
```
 - Reemplaza `<version>` con la versión más reciente disponible.
————————————————————————————————————————————————————————————————————————
####    4. INSTALAR DOCKER DESKTOP
```bash
sudo apt update
sudo apt install ./docker-desktop-<version>-amd64.deb
```
————————————————————————————————————————————————————————————————————————
####    5. INICIAR DOCKER DESKTOP
- Busca "Docker Desktop" en el menú de aplicaciones y ejecútalo, o
- Desde la terminal: `systemctl --user start docker-desktop`
————————————————————————————————————————————————————————————————————————
####    6. CONFIGURACION POST-INSTALACION
- Acepta los términos de servicio cuando se te solicite
- Añade tu usuario al grupo docker:
```bash
sudo usermod -aG docker $USER
```
- Cierra sesión y vuelve a iniciarla para que los cambios surtan efecto
————————————————————————————————————————————————————————————————————————
####    7. VERIFICAR LA INSTALACION
```bash
docker --version
docker-compose --version
```
————————————————————————————————————————————————————————————————————————
####    8. USAR DOCKER DESKTOP
- Docker Desktop crea y usa un contexto Docker personalizado llamado `desktop-linux`
- Para cambiar entre contextos:
```bash
docker context use desktop-linux
docker context use default
```
————————————————————————————————————————————————————————————————————————————————————————————————

