var cl;
var meth;
var line;
var strArg = []
recv('cls', function onMessage(cls) { 
    cl = cls.class;
    meth = cls.meth;
    strArg = cls.line;
});


Java.perform(function(){
    strArg[i] = strArg[i].replace(/(\r\n|\n|\r)/gm, "");
    console.log("\x1b[31m"+strArg[i]+"\x1b[0m")
    for (let i = 0; i < strArg.length; i++) {
        send(
                Java.use(cl)[meth](strArg[i])
        );
        }
});
