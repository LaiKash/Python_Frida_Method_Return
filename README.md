# Python-Frida-Method-Return
A simple Python script that use Frida to print the returned value from an Android static method.

Read the -h option first.

This script will read from the file "arguments.txt" in the same directory and pass each line as an argument to the Java method of the class and package specified. Then it will print the returned values.

This is usefull when trying to deobfuscate some strings that have custom deobfuscation methods. Just do something like:

`cat > arguments.txt`

And paste+enter the obfuscated strings (without ""). At the end, ctrl+c and execute the script. Dirty but easy.

It just works with static methods.
