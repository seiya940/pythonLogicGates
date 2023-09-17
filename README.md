This is a library that adds multiple logic gates to Python. Note
I will explain the types.
NAND gate: This is a gate that combines AND and NOT. Originally, in AND, the place of True becomes False.
NOR Gate: This is a logic gate that combines OR and NOT. Originally, in OR, True becomes False.
HNAND: This is a logic gate that I made myself. Abbreviation for HirfNotAND gate. One input is inverted. In other words, only True|False returns True. ---When mode is set to 1, it becomes a logic gate that returns True only when False|True is the opposite.---
XOR: This returns True only if only one is True. Both True and both False are not allowed.
HNXOR: This is the XOR version of HNAND that I explained earlier. There is nothing further to explain.
XNOR: This is a gate that combines XOR and NOT. Just use XOR to return True and set it to False.

これはPythonに複数の論理ゲートを追加するライブラリです。
種類を説明します
NANDゲート：ANDとNOTを融合させた論理ゲートです。本来ANDではTrueになるところがFalseになります。
NORゲート：ORとNOTを融合させた論理ゲートです。本来ORではTrueになるところがFalseになります。
HNAND：これは私が作った論理ゲートです。HirfNotANDゲートの省略です。片方の入力が反転されたANDゲートです。つまりTrue|Falseの場合のみがTrueを返します。---modeを1にするとFalse|TrueのみTrueを返すようになります。---
XORゲート：1つだけがTrueの場合にのみTrueを返します。両方Trueまたは両方FalseならFalseになります。
HNXOR：これは前に説明したHNANDのXOR版です。これ以上説明することはありません。
XNOR：XORとNOTを組み合わせたゲートです。本来XORではTrueになるところがFalseになります。
