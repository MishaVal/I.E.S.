import matplotlib.pyplot as plt
import signal_generator
import fft

HARMONICS = 8
FREQUENCY = 1100
DISCRETE_CALLS = 256

def calculate_time(signal_harmonics, start_frequency, number_discrete_calls):
    time = []
    for n in range(number_discrete_calls):
    	signal = signal_generator.generate_signal(signal_harmonics, start_frequency, n)
        start_time = t.time()
        fft.fast_fourier_transform(signal)
        end_time = t.time()
        time.append(end_time - start_time)
    return time

signal = signal_generator.generate_signal(
  HARMONICS,
  FREQUENCY,
  DISCRETE_CALLS
)
spectrum_fft = fft.fast_fourier_transform(signal)
print(spectrum_fft)

time = complexity_generator.calculate_time(
  HARMONICS,
  FREQUENCY,
  2500
)

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Laboratorka 2.2')
fig.set_size_inches(18.5, 10.5)

ax1.plot(signal)
ax1.set_title('Generated signal')
ax1.set(xlabel='time', ylabel='generated signal')

ax2.plot(spectrum_fft)
ax2.set_title('Fast Fourier transform of generated signal')
ax2.set(xlabel='time', ylabel='fft')
fig.savefig('lab2_2.png')

ax2.plot(time)
ax2.set_title('FFT time dependency')
ax2.set(xlabel='N', ylabel='time')
fig.savefig('lab2_2.png')
plt.show()
