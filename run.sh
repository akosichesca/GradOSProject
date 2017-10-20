#!/bin/bash

pi="pi2"
encryptSchemes="aes rsa"
files="echo_client.py echo_server.py"

outDir="results"

# Ensure directory exists
mkdir $outDir

getName() {
	echo $1-$2-$(basename "${3%.*}")-$4.dat
}

for scheme in $encryptSchemes; do
	for file in $files; do
		echo "Encrypting $file using $scheme on $pi"
		./mon ./encrypt.py $file | tee $outDir/$(getName $pi $scheme $file "encrypt")
		sync # Clear out buffered IO
		
		echo "Decrypting $file using $scheme on $pi"
		./mon ./decrypt.py output | tee $outDir/$(getName $pi $scheme $file "decrypt")
		sync # Clear out buffered IO
	done
done
