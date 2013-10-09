
import pyfits
import matplotlib.pyplot as plt
import numpy as np

def main():
#read in and plot the spectra   
file='lbgu17qnq_x1d.fits'
fits=pyfits.open(file)
cos=fits[1].data
wavec=cos['wavelength']
fluxc=cos['flux']

wavec=wavec.flatten()
fluxc=fluxc.flatten()


file='o8k401010_x1d.fits'
fits=pyfits.open(file)
stis=fits[1].data
waves=stis['wavelength']
fluxs=stis['flux']

waves=waves.flatten()
fluxs=fluxs.flatten()


print 'plotting COS'
plt.figure(1)
plt.clf()
plt.cla()
plt.plot(wavec,fluxc,'k-')

print 'plotting STIS'
plt.figure(2)
plt.clf()
plt.cla()
plt.plot(waves,fluxs,'k-')

#find signal to noise 
#get the indecies of the regions I want for noise level
zc=np.where((wavec>1150) & (wavec<1200))
zs=np.where((waves>1150) & (waves<1200))

#I'm not sure if the max in the cos data is real so choose a different segment
zmc=np.where(wavec>1225)
zms=np.where(waves>1225)

noisec=fluxc[zc]
noises=fluxs[zs]
signalc=fluxc[zmc]
signals=fluxs[zms]

print 'Signal to noise for COS:'
print '  ',signalc.max()/noisec.mean()

print 'Signal to noise for STIS:'
print '  ',signals.max()/noises.mean()


#interpolate things
newcos=np.interp(waves,wavec,fluxc)
plt.figure(3)
plt.cla()
plt.clf()
plt.plot(waves,newcos,'g-')
plt.plot(waves,fluxs,'r-')


if __name__ == '__main__':
    main()
