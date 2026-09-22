import streamlit as st
from ciphers.substitution.caesar import CaesarCipher
from ciphers.substitution.atbash import AtbashCipher
from ciphers.substitution.affine import AffineCipher
from ciphers.substitution.monoalphabetic import MonoalphabeticCipher
from ciphers.substitution.homophonic import HomophonicCipher
from ciphers.polyalphabetic.vigenere import VigenereCipher
from ciphers.polyalphabetic.beaufort import BeaufortCipher
from ciphers.polyalphabetic.variant_beaufort import VariantBeaufortCipher
from ciphers.transposition.rail_fence import RailFenceCipher
from ciphers.transposition.columnar import ColumnarTranspositionCipher
from ciphers.transposition.route import RouteCipher
from ciphers.polygraphic.playfair import PlayfairCipher
from ciphers.polygraphic.hill import HillCipher
from ciphers.polygraphic.bifid import BifidCipher
from ciphers.polygraphic.trifid import TrifidCipher
from cryptanalysis.breaker import analyze_cipher

st.set_page_config(page_title="Classical Cipher Lab",page_icon="🔐",layout="centered")
st.title("🔐 Classical Cipher Lab")
st.caption("15 classical ciphers • encryption • decryption • frequency analysis • cryptanalysis")
families={"Substitution":["Caesar","Atbash","Affine","Monoalphabetic Substitution","Homophonic Substitution"],"Polyalphabetic":["Vigenère","Beaufort","Variant Beaufort"],"Transposition":["Rail Fence","Columnar Transposition","Route Cipher"],"Polygraphic":["Playfair","Hill","Bifid","Trifid"]}
family=st.selectbox("Cipher Family",list(families));name=st.selectbox("Cipher",families[family]);operation=st.selectbox("Operation",["Encrypt","Decrypt","Analyze / Break"]);text=st.text_area("Input Text",height=160)
key=None
if operation!="Analyze / Break":
    if name=="Caesar":key=st.number_input("Shift",0,25,3)
    elif name in ["Vigenère","Beaufort","Variant Beaufort","Playfair","Bifid","Trifid","Columnar Transposition"]:key=st.text_input("Keyword")
    elif name=="Affine":
        raw=st.text_input("Affine key (a,b)","5,8")
        try:key=tuple(int(x.strip()) for x in raw.split(","))
        except:key=(5,8)
    elif name=="Monoalphabetic Substitution":key=st.text_input("26-letter substitution alphabet","QWERTYUIOPASDFGHJKLZXCVBNM")
    elif name=="Rail Fence":key=st.number_input("Rails",2,50,3)
    elif name=="Route Cipher":
        raw=st.text_input("Rows,Columns","3,4")
        try:key=tuple(int(x.strip()) for x in raw.split(","))
        except:key=(3,4)
    elif name=="Hill":
        raw=st.text_input("2x2 matrix a,b;c,d","3,3;2,5")
        try:key=[[int(x) for x in r.split(",")] for r in raw.split(";")]
        except:key=[[3,3],[2,5]]
    else:st.info("Built-in homophonic mapping is used.")
classes={"Caesar":CaesarCipher,"Atbash":AtbashCipher,"Affine":AffineCipher,"Monoalphabetic Substitution":MonoalphabeticCipher,"Homophonic Substitution":HomophonicCipher,"Vigenère":VigenereCipher,"Beaufort":BeaufortCipher,"Variant Beaufort":VariantBeaufortCipher,"Rail Fence":RailFenceCipher,"Columnar Transposition":ColumnarTranspositionCipher,"Route Cipher":RouteCipher,"Playfair":PlayfairCipher,"Hill":HillCipher,"Bifid":BifidCipher,"Trifid":TrifidCipher}
if st.button("Run",type="primary"):
    if not text.strip():st.warning("Enter input text.")
    else:
        try:
            if operation=="Analyze / Break":
                result=analyze_cipher(name,text);basic=result.get("analysis",{});st.subheader("🔎 Cryptanalysis Results")
                a,b,c=st.columns(3);a.metric("Length",basic.get("length",0));b.metric("IoC",f"{basic.get('ioc',0):.4f}");c.metric("N-Gram Score",f"{basic.get('ngram_score',0):.2f}")
                if basic.get("frequency"):st.subheader("📊 Frequency Analysis");st.bar_chart(basic["frequency"])
                br=result.get("break")
                if br:
                    if br.get("best"):st.subheader("🔓 Best Candidate");st.write("Key:",br["best"].get("key","Known mapping"));st.code(br["best"].get("plaintext",br.get("plaintext","")))
                    if br.get("candidates"):st.subheader("Candidate Solutions");st.dataframe(br["candidates"])
                if "key_length_candidates" in result:
                    kd=result["key_length_candidates"];st.subheader("🔑 Key-Length Analysis");st.write("Friedman estimate:",result.get("friedman_estimate"));st.dataframe(kd.get("ioc_results",[])[:10]);
                    if kd.get("kasiski",{}).get("key_length_candidates"):st.write("Kasiski candidates");st.dataframe(kd["kasiski"]["key_length_candidates"][:10])
                st.caption("Cryptanalysis is statistical/heuristic and is not guaranteed to recover the original key.")
            else:
                result=getattr(classes[name](),operation.lower())(text,key);st.subheader("Result");st.text_area("Output",result,height=180);st.subheader("📘 How It Was Done");st.write(f"**Algorithm:** {name}");st.write(f"**Operation:** {operation}");st.write(f"**Key / Parameters:** `{key}`")
                if name=="Caesar":st.code("Encrypt: C=(P+K) mod 26\nDecrypt: P=(C-K) mod 26")
                elif name=="Affine":st.code("Encrypt: C=(aP+b) mod 26\nDecrypt: P=a⁻¹(C-b) mod 26")
                elif name=="Atbash":st.code("A↔Z, B↔Y, ..., M↔N")
                elif name in ["Vigenère","Beaufort","Variant Beaufort"]:st.code("A=0,...,Z=25; keyword values are applied cyclically to alphabetic characters.")
                elif name=="Playfair":st.code("I/J are combined; digraphs use same-row, same-column, or rectangle rules.")
                elif name=="Hill":st.code("Blocks are multiplied by the key matrix modulo 26.")
                else:st.code("The selected classical cipher transforms the input according to its algorithm and key.")
        except Exception as e:st.error(f"Error: {e}")
