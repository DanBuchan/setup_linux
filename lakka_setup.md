1. Configuring Audio for the different HDMI outputs

The underlying issue is that regardless of which HDMI port you're using on your pi400 the default audio device Lakka configures is always the HDMI0 audio device. The solution is to look up the actual name of the HDMI1 audio device and enter that in the audio settings, here's what I did to solve that;

You can find out the actual names of the audio devices by booting lakka in command line mode. First mount your Lakka SD card on some machine so you can edit cmdline.txt to switch on command line booting, as described here:

https://www.lakka.tv/doc/Accessing-Lakka-command-line-interface/

With that edit done put the SD card back in your pi400 and boot to the command line (don't forget to also run the command systemctl start retroarch.target when you get to the prompt):. From there you can list all the possible audio devices with the command aplay -L, as described here:

https://www.lakka.tv/doc/Audio-settings/

Now, look through the list returned for the hdmi entries. IIRC The hdmi audio devices for HDMI0 and HDMI1 should be hdmi:CARD=vc4hdmi0,DEV=0 and hdmi:CARD=vc4hdmi1,DEV=0 respectively. I don't think they should be different on different pi400s but worth double checking. Write those down and turn off the pi400.

Once again edit cmdline.txt so that your lakka install no longer boots to the command line interface. Put the Lakka SD card back in your pi400 and boot as normal. Then use the menus to go to Settings->Audio->Output->Device and enter the device name your wrote down (no spaces).

If you entered hdmi:CARD=vc4hdmi1,DEV=0 hopefully you should now have sound over HDMI1. I'd guess a similar process should also address some missing audio issues for pi4 users but I can't confirm that.
