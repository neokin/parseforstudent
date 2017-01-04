import sys
import os
A = [( 125 ,129 ),
( 130 ,132 ),
( 132 , 137),
( 137 , 141),
( 141 , 144),
( 144 , 146),
( 154 , 159),
( 160 , 161),
( 162 , 164),
( 166 , 169),
( 170 , 188),
( 190 , 194),
( 194 , 197),
( 198 , 202),
( 202 , 207),
( 218 , 221),
( 221 , 230),
( 240 , 244),
( 244 , 245),
( 245 , 249),
( 250 , 253),
( 260 , 262),
( 262 , 271),
( 272 , 276),
( 278 , 280),
( 280 , 285),
( 285 , 288),
( 289 , 291),
( 291 , 295)]
counter = 30
for i in A:
	begp = i[0]-124
	endp = i[1]-124
	cmd1 = "pdfseparate -f " + str(begp) + " -l " + str(endp) + " mcha_6.pdf answer1-%d.pdf"
	c = str(counter)+"_"
	cmd2 ="pdfunite a*.pdf " + c +".pdf && rm a*.pdf"
	
	cmd3 = "mv " + c + " " + str(counter) + ".*"
	os.system(cmd1)
	os.system(cmd2)
	os.system(cmd3)
	counter = counter + 1
print(counter)
	
