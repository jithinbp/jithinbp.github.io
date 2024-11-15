
# CAEN Digitizer data collection and viewing on Ubuntu

DT5743 is what i have, but the instructions will work for a wide range

## Setup toolchain
---


!!! info "Install Packages from CAEN"
	+ [CAENVMELib-v4.0.2](https://www.caen.it/?downloadfile=8633){:target=_blank}
	+ [CAENComm-v1.7.0](https://www.caen.it/?downloadfile=8292){:target=_blank}
	+ [CAENDigitizer-v2.17.3](https://www.caen.it/?downloadfile=7354){:target=_blank}
	+ [CAENUSBdrvB-v1.6.0](https://www.caen.it/?downloadfile=10084){:target=_blank} : Get specific drivers for your device from [CAEN](https://www.caen.it/download/?filter=CAENComm%20Library){:target=_blank}
	+ [caenwavedemo_x743-1.2.1](https://www.caen.it/?downloadfile=9675){:target=_blank}

### Installing
---

Dependencies : glibc and libusb are required. along with the build tools like make.

!!! tip "you can check glibc version"
	<pre><font color="#26A269"><b>jithin@jithin-Victus</b></font>:<font color="#12488B"><b>~</b></font>$ ldd --version | head -n1
	ldd (Ubuntu GLIBC 2.35-0ubuntu3.8) 2.35
	</pre>

	minimum version 2.11 is asked by CAEN.


The first 4 packages are simply `sudo ./install_x64` , except the USBdrv where you make need to do `make` followed by `sudo make install` if you do not want to use DKMS.


There are some sample programs inside CAENDigitizer which you can try to compile using `make`


### Wavedemo
---

gnuplot is needed. you can get it from synaptic.

There seems to be a redefinition bug in `include/Wavedemo.h` for which [Cursor](https://downloader.cursor.sh/linux/appImage/x64){:target="blank_"} easily suggested a fix. Change the enum definitions in that file to what's shown below to avoid redefinition errors.

```c
typedef enum {
	WPLOT_MODE_1BD,		//plots only output waveforms of one board at a time without any processing
	WPLOT_MODE_1CH,		//plots analogue and digital waveforms of one channel at a time
	WPLOT_MODE_STD,		//plots analogue and digital waveforms of events

	WPLOT_MODE_DUMMY_LAST
} WPLOT_MODE_t;

typedef enum {
	HPLOT_DISABLED,
	HPLOT_TIME,
	HPLOT_ENERGY,

	HPLOT_TYPE_DUMMY_LAST
} HPLOT_TYPE_t;
```


MAKE and INSTALLATION

```sh
./configure CFLAGS=-O2
make
sudo make install
```

### Execute Wavedemo. [User Manual](file:///home/jithin/Downloads/UM8789_WaveDemo_x743_UserManual_rev1.pdf){:target="blank_"}
---

![](images/CAEN/wavedemo_histogram.png)


```
WaveDemo_x743 WaveDemoConfig.ini
```

The config file contains all info. I have attached my config file below.
Notice that I have set all SAVE_DATA options to NO because it fills up a few gigs within minutes, and
I only have like 2GB of space left :(

??? tip "WaveDemoConfig.ini : I am only using CH0 on board 1"
	```java

	--8<-- "assets/WaveDemoConfig.ini"

	```

Tweak the config file, and run it. Good luck!

This is a terminal utility, but shows spectra with Gnuplot. There are shortcut keys which you can check by pressing `?` .
Some useful ones

+ `h`: Enable histogram (Counts, Time) . Press again to make Counts, Channels.
+ `qy`: Quit, yes.



