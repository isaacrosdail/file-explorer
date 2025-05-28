#include "gtest/gtest.h" // not the full path

// Simple test to verify everything works
TEST(BasicTest, TrueIsTrue){ 
    EXPECT_TRUE(true);
}

int main(int argc, char **argv) {
    ::testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}