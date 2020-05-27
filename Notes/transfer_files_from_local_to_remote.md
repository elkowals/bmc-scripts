<html>
<head>Bring-up and test - Transfering files to ast2600 from local windows/linux machine</head>

<body>
<p>You are in need of transfering files from your local machine to your server; if you have access via network to your server
you can try the following:
</p>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight">
<code> scp filename username@ipaddress:/home/root/directory/filename

example:
scp emile.sh root@4.4.4.4:/home/root/emile.sh

You should see the following:

The authenticity of host 'x.x.x.x (x.x.x.x)' can't be established.
RSA key fingerprint is .
Are you sure you want to continue connecting (yes/no)?
Warning: Permanently added 'x.x.x.x' (RSA) to the list of known hosts.
root@x.x.x.x's password:
emile.sh                                                       100%  733     6.3KB/s   00:00


</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight">
<code> 

use AFS pwd
ip -> to GSA

root@rain10bmc:~# scp elkowals@9.3.185.93:/gsa/ausgsa/home/e/l/elkowals/web/public/fan_speed.sh .

Host '9.3.185.93' is not in the trusted hosts file.
(ssh-rsa fingerprint sha1!! 10:ce:89:b8:32:dd:4e:b7:b4:17:4d:bf:cb:0d:3c:ad:3e:5f:f7:d6)
Do you want to continue connecting? (y/n) y
elkowals@9.3.185.93's password:
fan_speed.sh                                  100% 6346     6.2KB/s   00:00


</code></pre></div></div>


<p> you need to have putty installed in windows to have scp available.</p>
</body>
</html>
