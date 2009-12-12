package {
	import flash.display.Sprite;
	import flash.events.*
	import flash.net.Socket;
	//import flash.display.Stage;
	import flash.external.ExternalInterface;

	public class BrowserSocket extends Sprite {      
		public var socket:Socket;
		//public var isConnected:Number;

		public function BrowserSocket() {
			socket = new Socket();
			//stage.frameRate = 60;
			
			ExternalInterface.addCallback("first_connection",function(ip:String,port:int):void{
				var socket_policy:Socket = new Socket(ip,port);
			})
			
			ExternalInterface.addCallback("connect",function(ip:String,port:int):void{
				socket.connect(ip,port);
			})
				
			ExternalInterface.addCallback("send",function(what:String):void{
				socket.writeUTFBytes(what);
				socket.flush();
			})
				
			socket.addEventListener(flash.events.SecurityErrorEvent.SECURITY_ERROR,function(e:flash.events.SecurityErrorEvent):void{
				ExternalInterface.call("browserSocket_securityError",e.text);
			})

			socket.addEventListener( flash.events.IOErrorEvent.IO_ERROR,function(e:flash.events.IOErrorEvent):void{
				ExternalInterface.call("browserSocket_ioError",e.text);
			})
			 
			socket.addEventListener(flash.events.ProgressEvent.SOCKET_DATA,function(e:flash.events.ProgressEvent):void{
				ExternalInterface.call("browsersocket_ondata",socket.readMultiByte(socket.bytesAvailable, "iso-8859-1"));
			})			 
			 
			/*
			socket.addEventListener(flash.events.Event.CONNECT,function(e:Event):void{alert("connected") 
				//isConnected = 1;
				//this keeps fireing every frame?
			})
			*/
				
			ExternalInterface.call("browserSocket_ready");
			
		} //end BrowserSocket Constructor
	} //end BrowserSocket Class
} //end package