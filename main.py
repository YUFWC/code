import argparse
import Main_tools

main = """
修改，添加请在Main.py和Main_tools.py里面进行
团队：Thirteen Team
作者：crazy
使用方法：
Windows：python main.py -h
Linux：python main.py -h
工具支持：
url编码/解码,base64编码/解码,十六进制编码/解码,ASCII转码/解码,mad5加密/解密
"""
print(main)
parser = argparse.ArgumentParser(description="可选参数列表")
parser.add_argument("-u", type=str, default=None, help="url编码")  # --
parser.add_argument("-ul", type=str, default=None, help="url解码")  # --
parser.add_argument("-s", type=str, default=None, help="base64编码")  # --
parser.add_argument("-sl", type=str, default=None, help="base64解码")  # --
parser.add_argument("-x", type=str, default=None, help="十六进制编码")  # --
parser.add_argument("-xl", type=str, default=None, help="十六进制解码")  # --
parser.add_argument("-a", type=str, default=None, help="ascii编码")  # --
parser.add_argument("-al", type=str, default=None, help="ascii解码")  # --
parser.add_argument("-t", type=str, default=None, help="md5加密--生成16位，32位")
parser.add_argument("-tl", type=str, default=None, help="md5解密--支持16位，32位")
args = parser.parse_args()
if args.u is not None:
    print("原文   "+args.u)
    Main_tools.u(args.u)
if args.ul is not None:
    print("原文   "+args.ul)
    Main_tools.ul(args.ul)
if args.s is not None:
    print("原文   "+args.s)
    Main_tools.base(args.s)
if args.sl is not None:
    print("原文   "+args.sl)
    Main_tools.Base(args.sl)
if args.x is not None:
    print("原文   "+args.x)
    Main_tools.hex(args.x)
if args.xl is not None:
    print("原文   "+args.xl)
    Main_tools.hex(args.xl)
if args.a is not None:
    print("原文   "+args.a)
    Main_tools.ascii(args.a)
if args.al is not None:
    print("原文   "+args.al)
    Main_tools.Ascii(int(args.al))
if args.t is not None:
    print("原文   "+args.t)
    Main_tools.Time(args.t)
if args.tl is not None:
    print("原文   "+args.tl)
    Main_tools.time(args.tl)
