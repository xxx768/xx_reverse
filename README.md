# xx_reverse
A linear and mini-mulit reverse shell.
It functions just like many otherss out there. It is built ontop of python socket library,subprocess, and os library.<br>

<h1>Disclaimer</h1>
  <b>
  I am not reponsible for your use of this script.
  Use only on devices you're given permission
  </b>
 

<h1>Features </h1>
<ul>
  <li>Handles more than one client. well this is possible when you disconnect(by typing <b>"exit"</b>)it automatically connects to the next available client</li>
  <li>Client retry connection if it can't connect to server</li>
  <li>Server waits for connections if all clients are disconnected using <b>exit</li>
  <li>Excludes directory from windows defender scanning</li>
</ul>
<h1>To do</h1>
<ul>
  <li> Add features to send current client to background and connect the next</li>
  <li>Copeis itself to general startup directory(This requires admin rights though)</li>
</ul>
<h1>Bonus</h1>
<p>Before converting to exe using pyinstaller do well to obfuscate the script using obfuscating services like <a href ="https://pyobfuscate.com">https://pyobfuscate.com</a><br>
as this help evade Av. From my last test it wasn't detected as malicious by windows defender.<br>
You could host the script online using <a href = "https://pythonanywhere.com//">https://pythonanywhere.com/</a>, <a href = "https://playit.gg">https://playit.gg</a><br> could be used to obtained a static public IP.</p>
