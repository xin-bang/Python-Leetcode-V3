## 说明：

基本需求就是：根据序列ID进行序列的索引，输出结果包括“序列ID	序列长度	序列”


```
#输入文件：
1：fish fasta:序列总文件，例如：example.fasta
2：bait file:包含需要提取序列的ID，例如：index.txt

#使用：
python operation.py -f1 example.fasta -f2 index.txt

#输出结果：fish.txt
##Fasta_id	Fasta_len	Fasta_seq
```
