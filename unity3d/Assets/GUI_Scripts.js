private var textFieldString = "Socket string data";

private var myTCP; 

var s : GameObject;
s = GameObject.Find("Sphere_l_1");

public var intc : int = 1;

function Awake() {
 		myTCP = gameObject.AddComponent('s_TCP');
}

function OnGUI () {
 	if(myTCP.socketReady==false) {
  		if (GUI.Button (Rect (20,10,80,20),"Connect")) {
   			myTCP.setupSocket();
  		}
 	} else {
  		myTCP.maintainConnection();

  	if (GUI.Button (Rect (20,40,80,20), "change")) {
   		myTCP.writeSocket(" The is from Level 1 Button");
   		textFieldString=myTCP.readSocket();
   		intc = intc - parseInt(textFieldString); 
   		s.transform.localScale = Vector3(10,10,10);  
   		//intc = parseInt(textFieldString);
   		}
   		
  if (GUI.Button (Rect (20,70,80,20), "get data")) {
   		myTCP.writeSocket(" The is from Level 2 Button");
   		textFieldString=myTCP.readSocket();
  }
  
  textFieldString = GUI.TextField (Rect (25, 100, 300, 30), textFieldString);
  
  if (GUI.Button (Rect (20,140,80,20),"Disconnect")) {
   		myTCP.closeSocket();
   		textFieldString = "Socket Disconnected...";
  }
 }
}

