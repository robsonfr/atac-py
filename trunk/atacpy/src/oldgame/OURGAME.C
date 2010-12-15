#include <io.h>
#include <conio.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <graphics.h>

enum MENS_IDX {
	MN_WAIT, MN_READY, MN_ETELG, MN_30ANOS, MN_CRED1, 
	MN_CRED2, MN_CRED3, MN_CRED4, MN_TITLE,
	MN_COPYR1, MN_COPYR2, MN_COPYR3, MN_PRES,
	MN_PERSTIT, MN_SUANV, MN_OINIMG, MN_POWER,
	MN_VIDAEX, MN_BONUS, MN_PRESQT,
};

char *mensagens[] = {
      "\nAguarge o carregamento dos desenhos...",
	  "\nCarregamento concluido\nAperte qualquer tecla para iniciar",
	  "ETE LAURO GOMES",
	  "30 anos",
	  "Robson dos Santos Franca",
	  "Ricardo S. Silva",
	  "e Roger Alvarenga",
	  "APRESENTAM ...",
	  "ATAC-C",
	  "ATAC-C(C) Todos os direitos reservados.",
	  "... a turna 2o. O da area de PD e",
	  "a ETE LAURO GOMES pelos seus 30 anos",
	  "Pressione uma tecla para seguir...",
	  "Personagens e valores :",
	  "Sua Nave",
	  "O Inimigo: 100 pontos",
	  "Power Up: 50 pontos + poder de fogo",
	  "Vida Extra: Mais uma vida",
	  "Bonus: 1000 pontos",
	  "Pressione qualquer tecla...",
	  "Selecione a velocidade",
	  "1. Lento",
	  "2. Medio",
	  "3. Rapido",
	  "Escolha a Dificuldade",
	  "1. Facil",
	  "2. Dificil"
};

char *arquivo_sprites = "ATAC-C.BMP";

char sprites[350];
char bufferELG[5500];
char buffer30A[19825];

#define SPR_NAVE &sprites[0]
#define SPR_INIM &sprites[70]

int grDriver = CGA;
int grMode = CGAC0;

void espera_tecla() {
	int t;
	do {
		t = getch();
	} while (t == 0);
	if (t == 3) {
		closegraph();
		exit(0);
	}
}

void intro_screen() {
	int c,i,j;
	cleardevice();
	settextstyle(TRIPLEX_FONT,HORIZ_DIR,3);
	outtextxy(40,10,mensagens[MN_ETELG]);
	for(i=0;i<220;i++) {
		for(j=0;j<25;j++) {
			bufferELG[i*25+j] = getpixel(i+40,j+10);
		}
	}
	cleardevice();
	setcolor(CGA_LIGHTRED);
	settextstyle(GOTHIC_FONT,HORIZ_DIR,8);
	outtextxy(20,105,mensagens[MN_30ANOS]);
	for(i=0;i<305;i++) {
		for(j=0;j<65;j++) {
			c = getpixel(i+10,j+120);
			buffer30A[i*65+j] = c;
			putpixel(i+10,j+120,3-c);
		}
	}
	cleardevice();
}

#define DIR_UP -1
#define DIR_DOWN 1

int powerup;
int left;

void zap() {
	sound((rand() % 500) + 300);
	delay(1);
	nosound();
}

int draw_laser(int x, int y1, int y2, int dir,int sfx) {
	int hit = 0;
	int j;
	int i;
	for(i=y1+8;sgn(dir,i,y2);i+=dir) {
		for(j=0;j<2;j++) {
			if (powerup) {
				if (getpixel(left+3,i) !=0 || getpixel(left+12,i) !=0)
					hit = 1;
				putpixel(left+3,i,rand() % 4);
				putpixel(left+12,i,rand() % 4);
			}
			if (sgn(-dir,i,y1)) {
				if (getpixel(x+j,i) != 0) {
					hit = 1;
				}
				putpixel(x+j,i,rand() % 4);
			}
			if (sfx) {
				zap();
			}
		}
	}
	i=getcolor();
	setcolor(BLACK);
	line(x,y1,x,y2);
	line(x+1,y1,x+1,y2);
	if (powerup) {
		line(x,y1,x,y2);
		line(x+1,y1,x+1,y2);
	}
	setcolor(i);
	return hit;
}

void draw_explosion(int x, int y) {
	

}

void outtextcenter(char *str, int y, int font, int charsize) {
	int w;	
	settextstyle(font,HORIZ_DIR,charsize);
	w=textwidth(str);
	outtextxy((getmaxx()-w)>>1,y,str);	
}

void intro_anim() {
	int i,j,k,left,y;
	cleardevice();
	for(i=0;i<220;i++) {
		if (i > 0)
			putimage(i+39,40,SPR_NAVE,XOR_PUT);
		putimage(i+40,40,SPR_NAVE,XOR_PUT);
		setcolor(CGA_YELLOW);
		draw_laser(i+47,35,11,-1,1);
		for(j=25;j>0;j--) {
			for(left=0;left<2;left++) {
				for(k=0;k<2;k++) {
					putpixel(i+k+47,j+10,rand() % 4);
				}
				for(k=0;k<2;k++) {
					putpixel(i+k+47,j+10,bufferELG[i*25+j]);
				}
			}			
		}
	}
	putimage(259,40,SPR_NAVE,XOR_PUT);
	for(left=258;left>=152;left--) {
		if (left < 258) {
			putimage(left+1,40,SPR_NAVE,XOR_PUT);
			putimage(left+1,60,SPR_INIM,XOR_PUT);
		}
		putimage(left,40,SPR_NAVE,XOR_PUT);
		putimage(left,60,SPR_INIM,XOR_PUT);
	}
	/*draw_laser(160,58,39,-1,1);
	draw_explosion(160,48);*/
	putimage(152,40,SPR_NAVE,XOR_PUT);
	putimage(152,60,SPR_INIM,XOR_PUT);
	for(j=0;j<305;j++) {
		if (j > 0) {
			putimage(j+2,100,SPR_INIM,XOR_PUT);		
		}
		putimage(j+3,100,SPR_INIM,XOR_PUT);
		for(i=64;i>=0;i--) {
			for(left=0;left<5;left++) {
				putpixel(j+10,i+120,(rand() % 3) + 1);
				zap();
			}
			putpixel(j+10,i+120,buffer30A[j*65+i]);
		}
	}
	putimage(306,100,SPR_INIM,XOR_PUT);
	setcolor(CGA_YELLOW);
	espera_tecla();
	setcolor(BLACK);
	line(0,100,319,100);
	for(y=0;y<100;y++) {
		line(0,y,319,y);
		line(0,200-y,319,200-y);	
	}
	setcolor(CGA_YELLOW);
	
}

int draw_background() {
	cleardevice();
	setfillstyle(SOLID_FILL,CGA_LIGHTRED);
	bar(0,0,319,199);
	setfillstyle(SOLID_FILL,BLACK);
	bar(10,10,240,160);
}

int sgn(int a, int b, int c) {
	if (a < 0) {
		if (b > c) {
			return 1;
		} else return 0;
	} else {
		if (b <= c) {
			return 1;
		} else return 0;
	}
}

int main(int argc, char **argv) 
{
	int handle;
	printf(mensagens[MN_WAIT]);
	handle = open(arquivo_sprites,O_RDONLY);
	read(handle,sprites,350);
	close(handle);
	if ((argc == 1) && (stricmp(argv[1],"-D"))) 
	{
		printf(mensagens[MN_READY]);
		espera_tecla();
	}
	initgraph(&grDriver, &grMode, "");
	intro_screen();
	intro_anim();
	cleardevice();
	exit(0);
}