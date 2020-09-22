# DatabaseDesign
This is for SCUT Database Course Design




文件构成：

./CourseDesign/templates 存放html文件

./CourseDesign/Ability 特定Ability功能（如Login）

./CourseDesign/CourseDesign 项目汇总设置


Table design:

User: id/name/password/birthday/isMale/college/address/QQ/tel/email
Teacher: id/name/password/isMale
Commodity: name/price/description/owner/status(True表示在售/False表示已经被出售，作为交易相关的商品信息的存储)
Transaction: buyer/seller/commodity(ForeignKey)/status/comment
