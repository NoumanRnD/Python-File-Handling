from numpy import sin, linspace, pi
from pylab import plot, show, title, xlabel, ylabel, subplot , savefig
from scipy import fft, arange

def plotSpectrum(y,Fs):
 
 n = len(y) # length of the signal
 k = arange(n)
 T = n/Fs
 frq = k/T  
 frq = frq[range(n/2)] # one side frequency range

 Y = fft(y)/n 
 Y = Y[range(n/2)]
 
 plot(frq,abs(Y),'r') # plotting the spectrum
 xlabel('Freq (Hz)')
 ylabel('|Y(freq)|')

Fs = 50.0;  # sampling rate
Ts = 2.0/Fs; # sampling interval
t = arange(0,1,Ts) # time vector

ff = 50;   # frequency of the signal
y = sin(2*pi*ff*t)

subplot(2,1,1)
plot(t,y)
xlabel('Time')
ylabel('Amplitude')
subplot(2,1,2)
plotSpectrum(y,Fs)
savefig("output/_sine_wave.png")
show()

