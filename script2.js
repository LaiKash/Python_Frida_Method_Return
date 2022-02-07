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
    var context = Java.use('android.app.ActivityThread').currentApplication().getApplicationContext();
    var decoderClass = Java.use(cl);
    var decoderInstance = decoderClass.$new(context);
    for (let i = 0; i < strArg.length; i++) {
        strArg[i] = strArg[i].replace(/(\r\n|\n|\r)/gm, "");
        console.log("\x1b[31m"+strArg[i]+"\x1b[0m")
        send(
            eval('decoderInstance.'+meth+'(\''+strArg[i]+'\')')
                
        );
        }
});
