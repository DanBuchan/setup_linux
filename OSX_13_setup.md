1. Remove everything from the Dock the I don't use
2. download megasync and log in
  https://mega.io/sync  
3. Install KeepassXC and add to dock
   https://keepassxc.org
4. Log in to Apple ID
   Apple Menu -> System Preferences
5. Log in to github
6. get setuplniux (will ask to install dev tools)
   git clone https://github.com/DanBuchan/setup_linux.git
7. Add git credentials
   git config --global user.name "Daniel Buchan"
   git config --global user.email "clone@myself.com"
8. Configure desktop behaviour
   Apple -> System Settings...
   Desktop & Dock -> Automatically Hide and Show Dock
   Hot Corners -> Top Right -> Mission Control
   Keyboard -> Input Sources -> British PC
   Track Pad -> Tap To Click
   More Gesture -> Mission Control -> Off 
   Finder -> Applications -> List
   Finder -> Add /Users/dbuchan to side bar
   Finder -> /Users/dbuchan -> Show Library folder
   Finder -> settings -> New Finder Window Shows
10. Install Aldente, you will have to turn off optimise battery settings
   https://apphousekitchen.com
11. Install Brew
    https://brew.sh
13. Install middleclick
    https://github.com/artginzburg/MiddleClick-Ventura
14. Install VSCode and sync with github
   https://code.visualstudio.com/Download
15. Install Firefox and login to sync, https://www.mozilla.org/en-GB/firefox/new/
   Log in to web sites mail.com, gmail, firefox, reddit, twitter, feedly
   reload containers from synced settings for each site
   set gb english dictionary, 
16. Install Chrome, https://www.google.com/chrome/
17. Make useful dirs
   mkdir Code
   mkdir Projects
   mkdir Course_dev
18. Install Python3
   brew install python
19. Install virtualenv
   pip3 install virtualenv
   pip3 install virtualenvwrapper
   mkdir ~/virtualenvs

   add to .zshrc
   export WORKON_HOME=$HOME/virtualenvs
   export PROJECT_HOME=$HOME/Code
   export VIRTUALENVWRAPPER_PYTHON=/opt/homebrew/bin/python3
   source virtualenvwrapper.sh
20. Install R
   https://cran.r-project.org/bin/macosx/
21. Install R Studio
   https://www.rstudio.com/products/rstudio/download/#download
22. Install Franz
   https://meetfranz.com/
23. Install OpenVPN for CS
   https://tsg.cs.ucl.ac.uk/working-from-home/#openvpn
   Unzip mac package and install tunnelblic and install the two openvpn configs
24. Add some .zshrc things
   PS1="\[\e[0;32m\]\u\[\e[m\]@\[\e[1;34m\]\h\[\e[m\]:\w\$ ";
   export $PS1;
   alias ls="ls --color=always";
   alias z="ls --color=always -lah";
   alias duall="du -sch .[!.]* * | sort -h";
   alias vi="vim";
   alias sshk="ssh knuckles.cs.ucl.ac.uk"
25. Add VLC
   https://www.videolan.org/
26. Install desktop MS office via Outlook365
27. Install Victor Mono
   https://rubjo.github.io/victor-mono/
   brew tap homebrew/cask-fonts
   brew install --cask font-victor-mono
28. Add jabref
   https://www.jabr/
29. Install Print @ UCL
   https://www.ucl.ac.uk/isd/how-to/connecting-to-printucl-macos
30. Install Be Focussed Pomodoro timer from App store
31. Install Steam
   https://store.steampowered.com/about/
32. Install Traktor
   https://www.native-instruments.com/en/specials/native-access-2/