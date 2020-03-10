define INIT_MESSAGE
You are about to install all the dependencies to make all of the test scripts work.
If you encounter a missing import, please add it to either:
setup/requirements.txt  -  pip3 installs
setup/install_apps.sh  -  apt-get installs

--------------------------------------------------------------------------------

endef

export INIT_MESSAGE

init:
	@echo "$$INIT_MESSAGE"
	sudo pip3 install -r setup/requirements.txt
	sudo ./setup/install_apps.sh

# ----------- THIS IS KEPT IN HERE AS AN EXAMPLE TO EXPAND MAKEFILE ------------
# define PROJECTOR_INSTALL
# sudo pip3 install -r setup/requirements_explorer.txt
# sudo ./setup/install_apps_explorer.sh
# endef

# projector:
# 	$(call PROJECTOR_INSTALL)
# 	./setup/create_db_projector.py

# projector_db:
# 	./setup/create_db_projector.py
