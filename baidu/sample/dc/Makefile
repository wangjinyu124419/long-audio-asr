## asr Makefile ##
CC=g++
#AR=ar

#FILE_NAME=$(src)
INC_PATH= -I/home/xqw/py3env/include/python3.5m

SRC_PATH=./src
OBJ_PATH=.
TARGET=_bds.so
LIB_PATH=../../lib
EXTERN_PATH=../../extern/lib
TARGET_PATH=./

CPPFLAGS1=-Wall -O0 -fPIC -shared -g -D__LINUX__ -Wno-unknown-pragmas -D_GLIBCXX_USE_CXX11_ABI=0  -std=c++11
CPPFLAGS= $(CPPFLAGS1) $(LIB_PATH)/libBDSpeechSDK.a $(EXTERN_PATH)/libcurl.a $(EXTERN_PATH)/libiconv.a $(EXTERN_PATH)/libz.a $(EXTERN_PATH)/libssl.a $(EXTERN_PATH)/libcrypto.a $(EXTERN_PATH)/libuuid.a -lrt -ldl -lpthread -lpython3.5m
SRC=bds_wrap.cxx  BaiduSpeechAPI.cpp

$(TARGET):
	swig -python -c++  bds.i
	$(CC) -o $(TARGET)  $(SRC) $(INC_PATH) $(CPPFLAGS)

clean:
	-rm -f $(OBJ)
	-rm -f $(TARGET)
	-rm -f bds.py
	-rm -f bds_wrap.cxx

cleanall:
	-rm -f $(OBJ)
	-rm -f $(TARGET)
	-rm -f bds.py
	-rm -f bds_wrap.cxx


