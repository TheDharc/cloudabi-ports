def build(ctx):
    root = ctx.extract('%(name)s-%(version)s.src')
    c_sources = {
        'Unwind-sjlj.c', 'UnwindLevel1-gcc-ext.c', 'UnwindLevel1.c',
        'UnwindRegistersRestore.S', 'UnwindRegistersSave.S',
    }
    cxx_sources = {'Unwind-EHABI.cpp', 'libunwind.cpp'}
    srcdir = root.path('src')
    libunwind = ctx.archive(
        {srcdir.path(f).compile(['-I../include'])
         for f in c_sources} |
        {srcdir.path(f).compile(['-I../include', '-std=c++11'])
         for f in cxx_sources})

    libunwind.install('lib/libunwind.a')

package(
    name='libunwind',
    version='3.7.0',
    homepage='http://libcxx.llvm.org/',
    maintainer='info@nuxi.nl',
    lib_depends={'c-runtime', 'libcxx'},
    build_cmd=build,
)

distfile(
    name='libunwind-3.7.0.src.tar.xz',
    checksum='6a600f30b9f3a54a1faf8c2dfd12522a0c90eb65f1aad63fec540aa27bcaca5b',
    master_sites={'http://llvm.org/releases/3.7.0/'},
)
