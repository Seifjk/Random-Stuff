fft = np.fft.rfft(dfum.value, norm="ortho")
def abs2(x):
    return x.real**2 + x.imag**2
selfconvol = np.fft.irfft(abs2(fft), norm="ortho")
fs = 1
f, Pxx_den = signal.periodogram(dfum.value, fs)
plt.semilogy(f, Pxx_den)
plt.ylim([1e-7, 1e2])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()