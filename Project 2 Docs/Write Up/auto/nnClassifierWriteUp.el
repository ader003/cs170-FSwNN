(TeX-add-style-hook
 "nnClassifierWriteUp"
 (lambda ()
   (TeX-add-to-alist 'LaTeX-provided-package-options
                     '(("geometry" "margin=1in")))
   (TeX-run-style-hooks
    "latex2e"
    "article"
    "art10"
    "geometry"
    "ragged2e"
    "enumerate"
    "graphicx"
    "rotating"
    "float"
    "listings"
    "color"))
 :latex)

