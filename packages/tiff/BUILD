def build(ctx):
    build = ctx.extract().autoconf()
    build.make(['bin_PROGRAMS=', 'noinst_PROGRAMS='])
    build.make_install(
        ['bin_PROGRAMS=', 'noinst_PROGRAMS=', 'install']).install()

package(
    name='tiff',
    version='4.0.5',
    homepage='http://www.remotesensing.org/libtiff/',
    maintainer='info@nuxi.nl',
    lib_depends={'c++-runtime'},
    build_cmd=build,
)

distfile(
    name='tiff-4.0.5.tar.gz',
    checksum='e25eaa83ed7fab43ddd278b9b14d91a406a4b674cedc776adb95535f897f309c',
    master_sites={
        'ftp://ftp.remotesensing.org/pub/libtiff/',
        'http://download.osgeo.org/libtiff/'},
    patches={
        'no-strcpy',
        'no-sprintf',
        'no-TIFFOpen',
    },
)
