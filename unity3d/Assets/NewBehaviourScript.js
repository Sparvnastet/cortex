#pragma strict

var ct : int = 2; 
public var countdown : float = 1f;
public var r : float = 1f;
public var temp : float = 1f;

function Update () {
	countdown -= Time.deltaTime;
    if(countdown <= 0.5f) {
		ct++;
		r = Random.Range(1.0, 2.0);
		temp = ct - r;
	    transform.localScale = Vector3(temp,temp,temp);
	if (ct == 5) {
			ct = 4;	
		}
		countdown = 2f;
	}
}