genrule(
    name = "day0",
    srcs = ["day0.pptx"],
    outs = ["output/day0.pptx"],
    cmd = "cp $< $@",
)

genrule(
    name = "day1",
    srcs = ["day1.md"],
    outs =  ["output/day1.pptx"],
    cmd = "CHROME_PATH='/Applications/Google Chrome.app/Contents/MacOS/Google Chrome' marp $(execpath day1.md) -o $@ --allow-local-files --pptx",
)