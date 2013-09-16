var net = require('net');
var server = net.createServer(function(c) { //'connection' listener
  console.log('server connected');
  c.on('end', function() {
    console.log('server disconnected');
  });
	x=1; 
	setInterval(function(){
	r = Math.floor((Math.random()*100)+1);
		x++;
		c.write(''+r+'');
	}, 1000);

  c.pipe(c);
});
server.listen(8124, function() { //'listening' listener
  console.log('server bound');
});

