import XMonad

myTerm = "alacritty"
myModMask = mod1Mask
myBorderWidth = 2

main = xmonad $ def
    { borderWidth = 2
    , terminal = myTerm
    , ModMask = myModMask
    , borderWidth = myBorderWidth
    , normalBorderColor = "#cccccc"
    , focusedBorderColor = "#cd8b00" }

