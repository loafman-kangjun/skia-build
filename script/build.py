#! /usr/bin/env python3

import common, os, subprocess, sys

def main():
  os.chdir(os.path.join(os.path.dirname(__file__), os.pardir, 'skia'))

  build_type = common.build_type()
  machine = common.machine()
  system = common.system()
  ndk = common.ndk()  

  if build_type == 'Debug':
    args = ['is_debug=true']
  else:
    args = ['is_official_build=true']

  args += [
    'target_cpu="' + machine + '"',
    'skia_use_system_expat=false',
    'skia_use_system_libjpeg_turbo=false',
    'skia_use_system_libpng=false',
    'skia_use_system_libwebp=false',
    'skia_use_system_zlib=false',
    'skia_use_freetype=true',
    'skia_use_system_harfbuzz=false',
    'skia_pdf_subset_harfbuzz=true',
    'skia_use_system_icu=false',
    'skia_enable_skottie=true'
  ]


  args += [
     'skia_use_system_freetype2=false',
     'skia_use_direct3d=true',
     'extra_cflags=["-DSK_FONT_HOST_USE_SYSTEM_SETTINGS"]',
  ]

  out = os.path.join('out', build_type + '-' + machine)
  gn = 'gn.exe'
  subprocess.check_call([os.path.join('bin', gn), 'gen', out, '--args=' + ' '.join(args)])
  ninja = 'ninja.exe'
  subprocess.check_call([os.path.join('..', 'depot_tools', ninja), '-C', out, 'skia', 'modules'])

  return 0

if __name__ == '__main__':
  sys.exit(main())
