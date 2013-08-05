{
  'targets': [
    {
      'target_name': 'hiredis',
      'conditions': [
        ['OS=="win"', {
          'libraries': [
            '-lws2_32.lib'
          ]
        }, {}]
      ],
      'sources': [
          'src/hiredis.cc'
        , 'src/reader.cc'
      ],
      'dependencies': [
        'deps/hiredis.gyp:libhiredis'
      ],
      'defines': [
          '_GNU_SOURCE'
      ],
      'cflags': [
          '-Wall',
          '-O3'
      ]
    }
  ]
}
