#!/bin/bash

pi="pi2"
os="raspbian"
encryptSchemes="AES DES3 ARC4"
files="echo_client.py echo_server.py"

outDir="results"

# Ensure directory exists
mkdir $outDir

getName() {
	echo $1-$2-$3-$(basename "${4%.*}")-$5.dat
}

for scheme in $encryptSchemes; do
	for file in $files; do
		echo "Encrypting $file using $scheme on $pi running $os"
		./mon ./encrypt.py $file $scheme | tee $outDir/$(getName $pi $os $scheme $file "encrypt")
		sync # Clear out buffered IO
		
		echo "Decrypting $file using $scheme on $pi running $os"
		./mon ./decrypt.py output $scheme | tee $outDir/$(getName $pi $os $scheme $file "decrypt")
		sync # Clear out buffered IO
	done
done
