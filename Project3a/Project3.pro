TEMPLATE = app
CONFIG += console c++11
CONFIG -= app_bundle
CONFIG -= qt

SOURCES += main.cpp \
    sun_earth.cpp

HEADERS += \
    sun_earth.hpp

INCLUDEPATH += /usr/local/include
LIBS += -L/usr/local/lib
LIBS += -larmadillo -llapack -lblas
