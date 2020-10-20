#ezArch
#version 1.0

import os
import time
import configparser

timezoneset = False
install = True


def guidedinstallUEFI():
    print('Enter your timezone')
    print('Example timezones:')
    print('America/Denver')
    print('America/Chicago')
    timezoneset = True
    while timezoneset == True:
        timezone = input('Enter Timezone > ')
        try:
            os.system('timedatectl set-timezone ' + timezone)
            timezoneset = False
        except:
            print('ERROR: Time zone either does not exist or ezArch failed to run command')
    print('Time to set your locale!')
    print('an example of a locale is this en_US.UTF-8 UTF-8')
    print('en_US.UTF-8 UTF-8 is the U.S English locale')
    print('Type your locale (example "> en_US.UTF-8 UTF-8") if you want english just type the U.S locale')
    localetogen = input('> ')
    with open('/etc/locale.conf', 'a') as configfile:
        config.write('\n' + str(localetogen))
    print('Generating Locales')
    os.system('locale-gen')
    print('Now its time to set your computers name!')
    print('Just type in what you want your computers name to be!')
    hostname = input('')
    print('Setting hostname')
    print('Hostname = ' + hostname)
    try:
        os.system('echo ' + str(hostname) + ' > /etc/hostname')
    except:
        print('Failed to set hostname')
        print('You can do it manually!')
        print('Type, "echo (Whatever you want to name your computer) > /etc/host'
              'name"')
    print('Setting up hosts...')
    os.system('touch /etc/hosts')
    with open('/etc/hosts', 'a') as file:
        file.write('127.0.0.1     localhost\n')
        file.write('::1     localhost\n')
        file.write('127.0.1.1     ' + hostname + '\n')
    print('Now its time to set the password!')
    os.system('passwd')
    print('Password Set!')
    print('Initiating grub install')
    os.system('pacman -S grub')
    print('Installing efi boot manager')
    os.system('pacman -S efibootmgr')
    print('Making efi boot directory')
    os.system('mkdir /boot/EFI')
    print('Please enter your EFI partition "/dev/(partition)"')
    efipart = input('')
    print('Initiating EFI mount')
    try:
        os.system('mount ' + efipart + ' /boot/EFI')
    except:
        print('ERROR: Failed to mount! Maybe partition is wrong?')
        exit()
    print('Starting Grub install')
    try:
        os.system('grub-install --target=x86_64-efi --bootloader-id=grub_uefi --recheck')
    except:
        print('failed to install grub')
    print('Installed grub')
    print('Generating grub configuration file!')
    os.system('grub-mkconfig -o /boot/grub/grub.cfg')
    print('Setting up NetworkManager')
    os.system('systemctl enable NetworkManager')
    print('Now, follow these steps carefully (May want to write them down)')
    print('step 1: type "CTRL + C" to exit this program')
    print('step 2: type "umount -R /mnt" to unmount the partitions')
    print('step 3: type "exit"')
    print('step 4: Reboot the system and unplug the installation device')
    print('step 5: Boot into Arch!')

def guidedinstallBIOS():
    print('Enter your timezone')
    print('Example timezones:')
    print('America/Denver')
    print('America/Chicago')
    timezoneset = True
    while timezoneset == True:
        timezone = input('Enter Timezone > ')
        try:
            os.system('timedatectl set-timezone ' + timezone)
            timezoneset = False
        except:
            print('ERROR: Time zone either does not exist or ezArch failed to run command')
    print('Time to set your locale!')
    print('an example of a locale is this en_US.UTF-8 UTF-8')
    print('en_US.UTF-8 UTF-8 is the U.S English locale')
    print('Type your locale (example "> en_US.UTF-8 UTF-8") if you want english just type the U.S locale')
    localetogen = input('> ')
    with open('/etc/locale.conf', 'a') as configfile:
        config.write('\n' + str(localetogen))
    print('Trying locale backups')
    os.system('echo LANG=en_US.UTF-8 > /etc/locale.conf')
    print('Exporting locale backups')
    os.system('export LANG=uen_US.UTF-8')
    print('Generating Locales')
    os.system('locale-gen')
    print('Now its time to set your computers name!')
    print('Just type in what you want your computers name to be!')
    hostname = input('')
    print('Setting hostname')
    print('Hostname = ' + hostname)
    try:
        os.system('echo ' + str(hostname) + ' > /etc/hostname')
    except:
        print('Failed to set hostname')
        print('You can do it manually!')
        print('Type, "echo (Whatever you want to name your computer) > /etc/host'
              'name"')
    print('Setting up hosts...')
    os.system('touch /etc/hosts')
    with open('/etc/hosts', 'a') as file:
        file.write('127.0.0.1     localhost\n')
        file.write('::1     localhost\n')
        file.write('127.0.1.1     ' + hostname + '\n')
    print('Now its time to set the password!')
    os.system('passwd')
    print('Password Set!')
    print('executing mkinitcpio')
    os.system('mkinitcpio -p linux')
    print('Initiating grub package install')
    os.system('pacman -S grub')
    print('Grub package install finished successfully!')
    print('initiating grub system install')
    print('Please enter your device (ex. /dev/sda)')
    devin = input('Input device > ')
    os.system('grub-install ' + devin)
    print('Making grub config')
    os.system('grub-mkconfig -o /boot/grub/grub.cfg')
    print('Enabling NetworkManager')
    os.system('systemctl enable NetworkManager')
    print('Now you are ready to boot! Restart the PC, unplug the flashdrive and boot into Arch!')


print('Welcome to ezArch')
print('type --help for help')

ezArch = input('ezArch > ')

while install == True:
    if ezArch == '--help':
        print('==EZARCH HELP==')
        print('Installation:')
        print('- UEFI')
        print('-- Guided : ezArch install UEFI --guide')
        print('- Legacy/BIOS')
        print('-- Guided : ezArch install BIOS --guide')
        print('Recomendations:')
        print('- Packages')
        print('-- Required')
        print('--- linux')
        print('--- linux-firmware')
        print('--- base')
        print('--- base-devel')
        print('--- python')
        print('-- Non-Required')
        print('--- nano')
        print('--- networkmanager')
        print('-- How to install recomended packages:')
        print('--- pacstrap /mnt base base-devel linux linux-firmware nano networkmanager')
    print('--- pacman -S python')

    if ezArch == 'ezArch install UEFI --guide':
        print('starting ezArch guided arch installation')
        guidedinstallUEFI()
        install = False

    if ezArch == 'ezArch install BIOS --guide':
        print('starting ezArch guided arch installation')
        guidedinstallBIOS()
        install = False