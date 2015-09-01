def libcxxabi_build(ctx):
  ctx.insert_sources(0, '.')
  ctx.insert_sources(1, 'libunwind')
  sources = {
      'abort_message.cpp', 'cxa_aux_runtime.cpp',
      'cxa_default_handlers.cpp', 'cxa_demangle.cpp',
      'cxa_exception.cpp', 'cxa_exception_storage.cpp', 'cxa_guard.cpp',
      'cxa_handlers.cpp', 'cxa_new_delete.cpp', 'cxa_personality.cpp',
      'cxa_thread_atexit.cpp', 'cxa_unexpected.cpp', 'cxa_vector.cpp',
      'cxa_virtual.cpp', 'exception.cpp', 'private_typeinfo.cpp',
      'stdexcept.cpp', 'typeinfo.cpp',
  }
  libcxxabi = ctx.link_library(
      ctx.compile(
          os.path.join('src', f),
          ['-Iinclude', '-Ilibunwind/include', '-std=c++11'])
      for f in sources)

  ctx.install(libcxxabi, 'lib/libc++abi.a')
  for f in {'cxxabi.h', '__cxxabi_config.h'}:
    ctx.install(os.path.join('include', f), os.path.join('include/c++/v1', f))

package(
    name = 'libcxxabi',
    version = '3.7.0-rc3',
    homepage = 'http://libcxxabi.llvm.org/',
    maintainer = 'info@nuxi.nl',
    lib_depends = {'c-runtime', 'libcxx'},
    distfiles = ['libcxxabi-3.7.0rc3.src.tar.xz',
                 'libunwind-3.7.0rc3.src.tar.xz'],
    build_cmd = libcxxabi_build,
)

distfile(
    name = 'libcxxabi-3.7.0rc3.src.tar.xz',
    checksum = 'd56e11a0d6799f54568d29b8e4c92595afc63c067404e97429ede23a0a7df661',
    master_sites = {'http://llvm.org/pre-releases/3.7.0/rc3/'},
)