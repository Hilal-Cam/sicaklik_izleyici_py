# ROS 2 Sıcaklık İzleyici Paketi (sicaklik_izleyici_py)
Bu paket, bir sıcaklık sensörü simülasyonu yapan ve eşik değer aşıldığında uyarı veren iki ROS 2 düğümünden oluşur.

## Çalıştırma Adımları

1. **Paketi Derleme:**
```bash
cd ~/ros2_ws
colcon build --packages-select sicaklik_izleyici_py
source install/setup.bash
```

2. **Sensör Düğümünü Çalıştırma (1. Terminal):**
```bash
ros2 run sicaklik_izleyici_py sensor
```

3. **Izleyici Düğümünü Çalıştırma (2. Terminal):**
```bash
ros2 run sicaklik_izleyici_py izleyici
```

4. **Düğüm Grafiğini Görüntüleme (3. Terminal):**
```bash
rqt_graph
```
