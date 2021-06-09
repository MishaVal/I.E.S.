import matplotlib.pyplot as plt
import signal_generator
import dft

HARMONICS = 8
FREQUENCY = 1100
DISCRETE_CALLS = 256

def calculate_time(signal_harmonics, start_frequency, number_discrete_calls):
    time = []
    for n in range(number_discrete_calls):
    	signal = signal_generator.generate_signal(signal_harmonics, start_frequency, n)
        start_time = t.time()
        dft.discrete_fourier_transform(signal)
        end_time = t.time()
        time.append(end_time - start_time)
    return time

signal = signal_generator.generate_signal(
  HARMONICS,
  FREQUENCY,
  DISCRETE_CALLS
)
spectrum_dft = dft.discrete_fourier_transform(signal)

time = complexity_generator.calculate_time(
  HARMONICS,
  FREQUENCY,
  2500
)

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Laboratorka 2.1')
fig.set_size_inches(18.5, 10.5)

ax1.plot(signal)
ax1.set_title('Generated signal')
ax1.set(xlabel='time', ylabel='generated signal')

ax2.plot(spectrum_dft)
ax2.set_title('Discrete Fourier transform of generated signal')
ax2.set(xlabel='time', ylabel='dft')


ax3.plot(time)
ax3.set_title('DFT time dependency')
ax3.set(xlabel='N', ylabel='time')
fig.savefig('lab2_1.png')

plt.show()
