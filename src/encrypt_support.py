

import hashlib
import gnupg




class encrypt_support():


   def calc_sha1_for_file(self, file_name):
      """Accepts a file name and return ths SHA1 code."""

      fh_hash = open(file_name)
      hashlib_obj = hashlib.sha1()
      hashlib_obj.update(fh_hash.read())
      hash = hashlib_obj.hexdigest()
      fh_hash.close()

      return( hash )


   def gpg_encrypt_file(self, file_name_in, file_name_encrypted, gpg_email, gnupg_home):
      """Accepts a file name and a gpg email address for encrytion.  The
      incoming file is gpg encrypted and then written to a second file
      with '.gpg' extension added."""

      gpg = gnupg.GPG(gnupghome=gnupg_home)

      fh_00 = open(file_name_in, "rb")
      encrypted_ascii_data = gpg.encrypt_file(fh_00, gpg_email, always_trust=True, output=file_name_encrypted)
      fh_00.close()
