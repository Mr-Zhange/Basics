"""

                一般字符

 字符             含  义

  .         匹配任意单个字符（不包括换行符\n）
  \         转义字符（把有特殊含义的字符转换成字面意思）
[...]       字符集。对应字符集中的任意字符

"."     字符为匹配任意单个字符，例如，a.b可以的匹配结果为abd、aic、a&c等，但不包含换行符
"\"     字符为转义字符,可以把字符改变为原来的意思。例如"."字符，是匹配任意单个字符，但有时不需要这个功能，只想让它代表一个点，，这时
        就可以使用"\."，就能匹配为"."了
"[...]" 为字符集，相当于在中括号中任选一个。例如a[bcd],匹配的结果为ab、ac、ad。


               预定义字符

字符          含  义
 \d      匹配一个数字字符。等价于[0-9]
 \D      匹配一个非数字字符。等价于[^0-9]
 \s      匹配任何空白字符，包括空格、制表符、换页符等。等价于[\f\n\r\t\v]
 \S      匹配任何非空白字符。等价于[^\f\n\r\t\v]
 \w      匹配包括下划线的任何单词字符。等价于[A-Za-z0-9_]
 \W      匹配任何非单词字符。等价于[^A-Za-z0-9_]


            数量词

数量词            含  义
   *        匹配前一个字符0或无限次
   +        匹配前一个字符1或无限次
   ?        匹配前一个字符0或1次
  {m}       匹配前一个字符m次
{m, n}      匹配前一个字符m至n次

"*"     数量词匹配前一个字符0或无限次，例如，ab*c匹配ac、abc、abbc 和 abbbc 等。
"+"     "+" 与 "*" 很类似，只是至少匹配前一个字符一次。例如，ab+c匹配abc、abbc 和 abbbc 等。
"?"     数量词匹配前一个字符0或1次。例如，ab?c匹配ac 和 abc。
{m}     数量词匹配前一个字符m次。例如，ab{3}匹配abbbc。
{m, n}  数量词匹配前一个字符m至n次。例如，ab{1,3}匹配abc、abbc、abbbc。


    边界匹配

边界匹配      含  义
  ^       匹配字符串开头
  $       匹配字符串结尾
  \A      仅匹配字符串开头
  \Z      仅匹配字符串结尾

"^"     匹配字符串的开头，例如，^abc匹配abc开头的字符串
"$"     匹配字符串的结尾，例如，abc$匹配abc结尾的字符串
"\A"    仅匹配字符串的开头，例如，\Aabc
"\Z"    仅匹配字符串的结尾，例如，abc\Z

"""

import re

a = "ssIssfddfgssLovessfdfdsfedsfssPythonss"

infos = re.findall("ss(.*?)ss", a)

print(infos)

"""

search() 匹配并提取第一个符合规律的内容，返回一个正则表达式对象

re.match(pattern, string, flags=0)

pattern     为匹配的正则表达式
string      为要匹配的字符串
flags       为标志符，用于控制正则表达式的匹配方式，如是否区分大小写，多行匹配等

"""
a = "one1two2three3"

infos = re.match("\d+", a)

print(infos)

infos = re.search("\d+", a)

print(infos)

print(infos.group())

"""

sub() 用于替换字符串中的匹配项

re.sub(pattern, repl, string, count=0, flags=0)

pattern     为匹配的正则表达式
repl        为替换的字符串
string      为要被查找替换的原始字符串
counts      为模式匹配后替换的最大次数，默认 0 表示替换所有的匹配
flags       为标志符，用于控制正则表达式的匹配方式，如是否区分大小写，多行匹配等

"""

phone = "123-1234-5678"

new_phone = re.sub("\D", "", phone)

print(new_phone)

"""

findall() 匹配所有符合规律的内容，并以列表的形式返回结果

"""

a = "one1two2three3"

infos = re.findall("\d+", a)

print(infos)

"""

    re模块修饰符
    
修饰符      描  述
re.I    使匹配对大小写不敏感
re.L    做本地化识别(locale-aware)匹配
re.M    多行匹配，影响 ^ 和 $
re.S    使匹配包括换行在内的所有字符
re.U    根据Unicode字符集解析字符。这个标志影响\w \W \b \B
re.X    该标志通过给予更灵活的格式，以便将正则表达式写的更易理解

"""

a = '<div>指数</div>'

word = re.findall('<div>(.*?)</div>', a)

print(word)

a = '''<div>指数
</div>'''

word = re.findall('<div>(.*?)</div>', a, re.S)

print(word)

print(word[0].strip())  # 使用strip() 方法去除换行
