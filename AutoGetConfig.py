from subprocess import call

call('sudo mv /srv/tftp/sw1_running_config /home/pi/switchconfigs/', shell=True)
call('sudo mv /srv/tftp/hp_switch_configuration /home/pi/switchconfigs/hpConfigs/', shell=True)


