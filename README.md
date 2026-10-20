Bu paket, rastgele sıcaklık verileri yayınlayan bir sensör düğümü ve bu verileri izleyip eşik değer aşıldığında uyarı veren bir izleyici düğüm içerir.

## Çalıştırma Adımları

1. **Paketi Derleme:**
   ```bash
   cd ~/ros2_ws
   colcon build --packages-select sicaklik_izleyici_py
   source install/setup.bash

    Sensör Düğümünü Çalıştırma:
    Bash

ros2 run sicaklik_izleyici_py sensor

İzleyici Düğümünü Çalıştırma:
Bash

ros2 run sicaklik_izleyici_py izleyici

Grafik Ekranını Görme:
Bash

    rqt_graph

