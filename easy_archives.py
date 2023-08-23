from shutil import make_archive

make_archive("ANSWERS", 'zip')   # ANSWERS.zip

make_archive("c:/SPAM", 'zip', "ANSWERS")   # SPAM.zip

make_archive("ANSWERS", "gztar")  # ANSWERS.tar.gz