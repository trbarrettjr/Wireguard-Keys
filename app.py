from flask import Flask, jsonify, request, render_template, Response
import nacl.public
import nacl.utils
import base64

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")

@app.route("/man")
@app.route("/wg")
def man_wg():
    return render_template("wg.html")

@app.route("/wg-quick")
def man_wg_quick():
    return render_template("wg-quick.html")

@app.route("/<int:count>")
def genkeys(count):
    keys = list()
    for i in range(count):
        pkey = nacl.public.PrivateKey.generate()
        pub_key = pkey.public_key
        psk = nacl.utils.random(32)
        pkey_b64 = pkey.encode(nacl.encoding.Base64Encoder).decode('utf-8')
        pub_key_b64 = pub_key.encode(nacl.encoding.Base64Encoder).decode('utf-8')
        psk_b64 = base64.b64encode(psk).decode('utf-8')
        keys.append(dict(privkey=pkey_b64, pubkey=pub_key_b64, psk=psk_b64))
    return jsonify(keys)

@app.route("/csv/<int:count>")
def genkeys_csv(count):
    keys = list()
    for i in range(count):
        pkey = nacl.public.PrivateKey.generate()
        pub_key = pkey.public_key
        psk = nacl.utils.random(32)
        pkey_b64 = pkey.encode(nacl.encoding.Base64Encoder).decode('utf-8')
        pub_key_b64 = pub_key.encode(nacl.encoding.Base64Encoder).decode('utf-8')
        psk_b64 = base64.b64encode(psk).decode('utf-8')
        keys.append(dict(privkey=pkey_b64, pubkey=pub_key_b64, psk=psk_b64))

    csv_out = "Private Key,Public Key,Preshared Key\n"
    for item in keys:
        csv_out += item['privkey'] + ',' + item['pubkey'] + ',' + item['psk'] + '\n'

    response = Response(csv_out, mimetype='text/csv')

    return(response)

if __name__ == "__main__":
    app.run(debug = False)
