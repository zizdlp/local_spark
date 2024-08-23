from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import ftfy

# 初始化 SparkSession
spark = SparkSession.builder.appName("SimplePySparkExample").getOrCreate()

# 自定义 Python UDF，用于处理特殊字符
def fix_text(text):
    return ftfy.fix_text(text).strip() if text else ""

# 注册 UDF，指定返回类型为 StringType()
fix_text_udf = udf(fix_text, StringType())

# 读取本地文本文件
text_file = spark.read.text("/app/data/example.txt")

# 应用 UDF 处理文本
processed_lines = text_file.withColumn("fixed_text", fix_text_udf(text_file.value))

# 过滤掉空字符串
filtered_lines = processed_lines.filter(processed_lines.fixed_text != "hello")

# 输出执行计划（用于调试）
filtered_lines.explain(True)

# 计算行数
count = filtered_lines.count()

# 打印结果
print(f"mydebug:Non-empty lines count after fixing: {count}")

# 停止 SparkSession
spark.stop()