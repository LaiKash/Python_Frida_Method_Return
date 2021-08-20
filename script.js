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
    for (let i = 0; i < strArg.length; i++) {
        send(
                Java.use(cl)[meth](strArg[i])
        );
        }
});
