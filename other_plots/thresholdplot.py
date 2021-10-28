import numpy as np
import matplotlib.pyplot as plt
import pywt

s = np.linspace(-1, 1, 1000)

s_soft = pywt.threshold(s, value=0.5, mode='soft')
s_hard = pywt.threshold(s, value=0.5, mode='hard')
s_garrote = pywt.threshold(s, value=0.5, mode='garrote')
s_firm1 = pywt.threshold_firm(s, value_low=0.5, value_high=1)
s_firm2 = pywt.threshold_firm(s, value_low=0.5, value_high=2)
s_firm3 = pywt.threshold_firm(s, value_low=0.5, value_high=4)

fig, ax = plt.subplots(1, 3, figsize=(18, 6))
ax[0].plot(s, s, label='Original Signal')
ax[0].set_title('Original Signal')
ax[0].set_xlabel('Input value')
ax[0].set_ylabel('Thresholded value')

ax[1].plot(s, s_soft, label='Soft Threshold')
ax[1].set_title('Soft Threshold')
ax[1].set_xlabel('Input value')
ax[1].set_ylabel('Thresholded value')

ax[2].plot(s, s_hard, label='Hard Threshold')
ax[2].set_title('Hard Threshold')
ax[2].set_xlabel('Input value')
ax[2].set_ylabel('Thresholded value')
plt.savefig('threshold.png', dpi=400, bbox_inches="tight")
plt.show()
