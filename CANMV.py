### 实验名称：数字识别
### 实验平台：01Studio CanMV K210

# 导入相关模块
import sensor, image, time, lcd
from maix import KPU
import gc

# 初始化LCD
lcd.init(freq=15000000)

# 初始化传感器
sensor.reset()
sensor.set_vflip(1)
sensor.set_hmirror(1)
# 将摄像头设置成后置方式（所见即所得）
# GC0328摄像头（如果使用ov2640摄像头，注释此行。）

sensor.set_pixformat(sensor.RGB565)
sensor.set_framesize(sensor.QVGA)
sensor.set_windowing((224, 224))
sensor.skip_frames(time=1000)

# 创建时钟对象跟踪FPS
clock = time.clock()

# 构建KPU对象
kpu = KPU()

# 加载KPU模型，放在SD卡根目录
kpu.load_kmodel("/sd/uint8_mnist_cnn_model.kmodel")

try:
    while True:
        gc.collect()
        
        # 采集图像
        img = sensor.snapshot()
        
        # 图像预处理
        img_mnist1 = img.to_grayscale(1)  # 转换为灰度图
        img_mnist2 = img_mnist1.resize(112, 112)
        img_mnist2.invert()  # 反转图像（MNIST数据集需要）
        img_mnist2.strech_char(1)  # 图片预处理，消除暗角
        img_mnist2.pix_to_ai()  # 转换为KPU可处理格式
        
        # 将摄像头采集图片输送到KPU运算
        out = kpu.run_with_output(img_mnist2, getlist=True)
        max_mnist = max(out)
        index_mnist = out.index(max_mnist)  # 计算识别的数字
        score = KPU.sigmoid(max_mnist)  # 可信度分数，最大值为1
        
        # 显示字符串
        display_str = "num:{}".format(index_mnist)
        
        # 打印识别的数字和可信度分数
        print(display_str)
        print("Score:", score)
        
        # LCD显示识别的数字和可信度分数
        img.draw_string(4, 3, display_str, color=(255, 0, 0), scale=2)
        img.draw_string(4, 25, 'Score:' + str(score), color=(255, 0, 0), scale=2)
        lcd.display(img)
        
        # 计算并显示FPS（可选）
        clock.tick()
        # print("FPS:", clock.fps())

finally:
    # 确保程序退出时释放KPU资源
    kpu.deinit()