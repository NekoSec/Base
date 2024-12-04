Base64：
包含大写字母（A-Z）,小写字母（a-z），数字（0-9）以及+/;

Base32:
而Base32中只有大写字母（A-Z）和数字234567；

Base16:
而Base16就是16进制，他的范围是数字(0-9)，字母（ABCDEF）；

顺便说一句，当ASCll用Base加密达不到所对应的位数的时候用=号补齐；

在这里附带由三种Base加密的:I love you！

Base64:SSBsb3ZlIHlvde+8gQ==

Base32:JEQGY33WMUQHS33V566IC===

Base16:49206c6f766520796f75efbc81


用于解密可能经过Base64、Base32或Base16编码的字符串，最多尝试3次解密，并输出所有可能的结果：

![image](https://github.com/user-attachments/assets/dd36fa49-8f12-4cdf-9df6-b6a2cf76209b)
