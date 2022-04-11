var cl;
var meth;
var line;
var strArg = []
recv('cls', function onMessage(cls) { 
    cl = cls.class;
    meth = cls.meth;
    strArg = cls.line;
});

var f = new File("/sdcard/log.txt", "w");
var result
Java.perform(function(){
    for (let i = 0; i < strArg.length; i++) {
        strArg[i] = strArg[i].replace(/(\r\n|\n|\r)/gm, "");
	console.log("\x1b[31m"+strArg[i]+"\x1b[0m")
    
    f.write("\x1b[31m"+strArg[i]+"\x1b[0m\n");
    result = Java.use(cl)[meth](strArg[i])
    f.write(result + "\n");

	send(
        result
                
        );
        }
        f.flush();
        f.close();
});
