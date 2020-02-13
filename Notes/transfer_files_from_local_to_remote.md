<html>
<head><title>Bring-up and test - Transfering files to ast2600 from local windows/linux machine</title></head>

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

<p> you need to have putty installed in windows to have scp available.</p>
</body>
</html>
