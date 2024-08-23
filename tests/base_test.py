from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import ftfy

# 初始化 SparkSession
spark = SparkSession.builder.appName("SimplePySparkExample").getOrCreate()

# 自定义 Python UDF，用于处理特殊字符
def fix_text_udf_func(text):
    return ftfy.fix_text(text).strip() if text else ""

# 注册 UDF，指定返回类型为 StringType()
fix_text_udf = udf(fix_text_udf_func, StringType())

# 使用 range 生成一个 DataFrame
# 创建一个包含整数的 DataFrame
df = spark.range(0, 10).selectExpr("cast(id as string) as value")

# 应用 UDF 处理文本
df = df.withColumn("col_text", fix_text_udf(df.value))

# 过滤掉包含 "hello" 的字符串
filtered_lines = df.filter(df.col_text != "")

# 输出执行计划（用于调试）
filtered_lines.explain(True)

# 计算行数
count = filtered_lines.count()

# 打印结果
print(f"mydebug:Non-empty lines count after fixing: {count}")

# 停止 SparkSession
spark.stop()