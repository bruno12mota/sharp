{
  'targets': [{
    'target_name': 'sharp',
    'variables': {
      'runtime_link%':'shared', 
    },
    'sources': [
      'src/common.cc',
      'src/metadata.cc',
      'src/operations.cc',
      'src/pipeline.cc',
      'src/sharp.cc',
      'src/utilities.cc'
    ],
    'conditions': [
        ['OS=="win"', {
            'library_dirs': [
                '$(VIPS_HOME)/lib'
            ],
            'libraries': [
                'libvips.lib',
                'libglib-2.0.lib',
                'libgobject-2.0.lib'
            ],
            'include_dirs': [
                '$(VIPS_HOME)/include',
                '$(VIPS_HOME)/include/glib-2.0',
                '$(VIPS_HOME)/lib/glib-2.0/include',
                '<!(node -e "require(\'nan\')")'
            ]
        }, {
            'variables': {
                'PKG_CONFIG_PATH': '<!(which brew >/dev/null 2>&1 && eval $(brew --env) && echo $PKG_CONFIG_LIBDIR || true):$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig:/usr/lib/pkgconfig'
            },
            'libraries': [
                '<!(PKG_CONFIG_PATH="<(PKG_CONFIG_PATH)" pkg-config --libs vips)'
            ],
            'include_dirs': [
                '<!(PKG_CONFIG_PATH="<(PKG_CONFIG_PATH)" pkg-config --cflags vips glib-2.0)',
                '<!(node -e "require(\'nan\')")'
            ],
            'conditions': [
                ['runtime_link == "static"', {
                  'libraries': ['<!(PKG_CONFIG_PATH="<(PKG_CONFIG_PATH)" pkg-config --libs vips --static)']
                }]
            ]
        }]
    ],
    'cflags_cc': [
      '-std=c++0x',
      '-fexceptions',
      '-Wall',
      '-O3'
    ],
    'xcode_settings': {
      'OTHER_CPLUSPLUSFLAGS': [
        '-std=c++11',
        '-stdlib=libc++',
        '-fexceptions',
        '-Wall',
        '-O3'
      ],
      'MACOSX_DEPLOYMENT_TARGET': '10.7'
    },
    'msvs_settings': {
      'VCCLCompilerTool': {
        'ExceptionHandling': 1 # /EHsc
      }
    },
    'configurations': {
      'Release': {
        'msvs_settings': {
          'VCCLCompilerTool': {
            'ExceptionHandling': 1,
          }
        }
      }
    },
  }]
}
