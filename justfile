default:
  just -l

install-bashrc:
  pwd
  cp dot_bashrc_extras ~/.bashrc_extras
  just append-if-missing ~/.bashrc "source .bashrc_extras # Install bashrc"

append-if-missing FILE LINE:
  #!/usr/bin/python3
  with open("{{FILE}}", "r+") as file:
    for line in file:
      if "{{LINE}}" == line.strip():
        break
    else: # not found, we are at the eof
      file.write("{{LINE}}\n") # append missing data
