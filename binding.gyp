{
  "targets": [
    {
      "target_name": "hello",
      "sources": ["hello.cpp"],
      "include_dirs": [
        "./node_modules/node-addon-api"
      ],
      "defines": [
        "NODE_ADDON_API_DISABLE_CPP_EXCEPTIONS"
      ]
    },
    {
        "target_name": "test_runner",
        "type": "executable",
        "sources": [
            "test_hello.cpp",
            "third_party/googletest/googletest/src/gtest-all.cc"
        ],
        "include_dirs": [
          "./third_party/googletest/googletest/include",
          "./third_party/googletest/googletest"
        ],
        "defines": ["GTEST_HAS_PTHREAD=0"]
    }
  ]
}