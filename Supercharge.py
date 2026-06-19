import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# 1. Definisikan fungsi ODE
def metabolic_system(y, t):
    A, B, P = y
    
    # Persamaan fluks parameter soal
    v1 = (5.0 * 10) / ((2.0 + 10) * (1 + (P / 3.0)))
    v2 = 1.0 * A
    v3 = 0.8 * B
    v4 = 0.3 * A
    
    # Laju perubahan d[A]/dt, d[B]/dt, d[P]/dt
    dAdt = v1 - v2 - v4
    dBdt = v2 - v3
    dPdt = v3
    
    return [dAdt, dBdt, dPdt]

# 2. Kondisi awal (asumsi awal konsentrasi metabolit di dalam sel adalah 0)
y0 = [0.0, 0.0, 0.0]

# 3. Rentang waktu simulasi (0 sampai 50 satuan waktu)
t = np.linspace(0, 50, 500)

# 4. Selesaikan ODE
sol = odeint(metabolic_system, y0, t)

# 5. Plot Hasil Simulasi
plt.plot(t, sol[:, 0], label='[A]')
plt.plot(t, sol[:, 1], label='[B]')
plt.plot(t, sol[:, 2], label='[P]')
plt.legend()
plt.xlabel('Waktu')
plt.ylabel('Konsentrasi')
plt.title('Simulasi Kinetik Model dengan Inhibisi Allosterik')
plt.show()