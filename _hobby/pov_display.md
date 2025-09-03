---
layout: project
title: 'POV Display Atmega32'
date: 20 Jan 2011
image:  
  path: /assets/img/hobby/pov_cover.jpg
links:
  - title: Youtube
    url: https://www.youtube.com/watch?v=
caption: Persistence of vision . light and wind show for Science Day at IISER
description: >
    The Indian Institute of Science Education and Research (IISER), Mohali organizes an annual event , during the course of which, its doors are thrown open to school kids in the hope that they will be inspired to take up scientific research.
accent_color: '#4fb1ba'
accent_image:
  background: 'linear-gradient(to bottom,#40182a 0%,#3d1d3c 30%,#e700ff 50%,#9900e9 70%,#008729 100%)'
  overlay:    true
---

* this list will be replaced by the toc
{:toc .large-only}

<iframe width="560" height="315" src="https://www.youtube.com/embed/1QtpcMzg6HE?si=qLRljMF__tJFgpvg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

## PERSISTENCE OF VISION DISPLAY

<iframe width="560" height="315" src="https://www.youtube.com/embed/BRIWQPskKdc?si=lll0wGV4VYFrlCOA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>


### Several Demos are set up by students of IISER that explain simple concepts as well as attract and enthrall.

One of the demos I set up was a persistence of vision display.  It consists of a linear row of Light Emitting Diodes controlled by a microcontroller. This rig is then taped to a rotating  platform such as a table fan, and the microcontroller is coded to blink the LEDs at precise intervals in order to generate patterns/text in mid air.  The viewer is unable to distinguish the flickering nature of the LEDs due to his/her eyes’ slow frame rate, and instead sees a complete pattern.  The stationary red LED is used to trigger the electronics and ensure that the text formed by each rotation overlaps perfectly with the rest in the viewer’s frame of reference.

## How it works

![](/assets/img/hobby/pov1.jpg)

Displaying a character, say A.

‘A’ on an 8×8 grid looks like
```c	
 	1 	2 	3 	4 	5 	6 	7 	8
1 				X 	X 			
2 			X 			X 		
4 			X 			X 		
8 		X 	X 			X 	X 	
16 		X 	X 	X 	X 	X 	X 	
32 		X 	X 			X 	X 	
64 	X 	X 					X 	X
128 	X 							X
```

the first column lists the bit values that represent each LED. The marked LEDs in each column need to be lighted rapidly one column

the first column lists the bit values that represent each LED. The marked LEDs in each column need to be lighted rapidly one column

after the other in order to make an A appear as you wave the entire LED column in the air.

WHEN PORTB=128+64, the bottom two LEDS glow , next, PORTB=64+32+16+8, LEDS 4,5,6,7 glow and so on

so if i were to store the values for A in an array it would look like

uint8_t ca[]={128+64,64+32+16+8,32+16+8+4+2,17,17,32+16+8+4+2,8+16+32+64,128+64};

and a loop execution of the elements of this array in quick succession,

```c
uint8_t x;
for(x=0;x<8;x++>
  {
  PORTB=ca[x];
  delay(340);
  }
PORTB=0;
delay(1000);
}
```

### Technical details:

All code was written in C, and downloaded onto an Atmega32 processor. The microHOPE dev board was used to save time.
A few automatic RGB LEDs were added to include a pleasing effect.

In order to figure out the blinking sequence for each character, a 8×7 grid was drawn and relevant pixel coordinates converted to binary.

### A handheld POV display  ( Made a few years prior )

A Display using a row of 8 LEDS that rapidly change patterns as you wave it through the air giving the

impression of an display with 8xX resolution .. X depends on how far you wave it , usually around 50 or so.

![](/assets/img/hobby/pov2.jpg)

The program in this instance merely repeats the characters T & A in a loop and, waving the board around shows you TATATA….

no switch was used in order to synchronise their appearance.



```c
void showchar(uint8_t c[]){
  uint8_t x;
  for(x=0;x<8;x++)
   {
   PORTB=c[x];
   delay(340);
   }
  PORTB=0;
  delay(1000);
}
 

main(){
  uint8_t ca[]={128+64,64+32+16,16+8+4,19,19,16+8+4,16+32+64,128+64};
  uint8_t ct[]={1,1,1,255,255,1,1,1};
  uint8_t cj[]={128+64+1,128+1,128+1,128+1,255,1,1,1};
  uint8_t ci[]={0,0,129,255,255,129,0,0};
  uint8_t ch[]={255,255,24,24,24,24,255,255};
  uint8_t cn[]={255,3,14,24,16+32,64+32,64+128,255};
  uint8_t cv[]={1+2,2+4+8,16+8+4,19,19,16+8+4,2+4+8,1+64};

  uint8_t x;
  
  DDRB=255;
  DDRD=0;
  PORTD=255;
 
  for(;;){
    if(PIND!=255){
        delay(2000);
        showchar(cj);
        showchar(ci);
        showchar(ct);
        showchar(ch);
        showchar(ci);
        showchar(cn);
        delay(8000);
    }
  }
}
```


### Alternative Arrangement


An alternative arrangement would be to have a rotating mirror and keep the LED row in front of it.. the mirror must have an input trigger

and you can easily view your text in the mirror… this is better since the angular velocity of the mirror can be kept fairly

constant thus giving you a maintained aspect ratio.

![](/assets/img/hobby/pov3.jpg)

![](/assets/img/hobby/pov4.jpg)
