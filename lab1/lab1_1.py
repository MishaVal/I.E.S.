import matplotlib.pyplot as plt
import signal_generator
import complexity_generator
import statistics_utils

HARMONICS = 8
FREQUENCY = 1100
DISCRETE_CALLS = 256

def calculate_mx(signal_harmonics, start_frequency, number_discrete_calls):
    mx = []
    for n in range(number_discrete_calls):
        signal = signal_generator.generate_signal(signal_harmonics, start_frequency, n)
        mx_n = statistics_utils.math_expectation(signal)
        mx.append(mx_n)
    return mx

signal = signal_generator.generate_signal(
  HARMONICS,
  FREQUENCY,
  DISCRETE_CALLS
)

time = complexity_generator.calculate_time(
  HARMONICS,
  FREQUENCY,
  2500
)

mx = calculate_mx(
  HARMONICS,
  FREQUENCY,
  2500
)

print("Math expectation = " + str(statistics_utils.math_expectation(signal)))
print("Math variance = " + str(statistics_utils.math_variance(signal)))

fig, (ax1, ax2, ax3) = plt.subplots(3)
fig.suptitle('Laboratorka 1.1')
fig.set_size_inches(18.5, 10.5)

ax1.plot(signal)
ax1.set_title('Generated signal')
ax1.set(xlabel='time', ylabel='generated signal')

ax2.plot(time)
ax2.set_title('Complexity of signal generation')
ax2.set(xlabel='number of discrete calls', ylabel='time (seconds)')

ax3.plot(mx)
ax3.set_title('Mx N dependency')
ax3.set(xlabel='N', ylabel='Mx')
fig.savefig('lab1_1.png')

plt.show()
