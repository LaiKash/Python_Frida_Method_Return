var cl;
var meth;
var line;
var strArg;
recv('cls', function onMessage(cls) { 
    cl = cls.class;
    meth = cls.meth;
    strArg = cls.line;
});


Java.perform(function(){
    
    send(
        Java.use(cl)[meth](strArg)
    );
        
});
