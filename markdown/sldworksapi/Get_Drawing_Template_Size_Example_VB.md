---
title: "Get Drawing Template Size Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Drawing_Template_Size_Example_VB.htm"
---

# Get Drawing Template Size Example (VBA)

This example shows how to get the size of the specified drawing template.

```vb
'-------------------------------------
Option Explicit
Public Enum swDwgPaperSizes_e
    swDwgPaperAsize = 0
    swDwgPaperAsizeVertical = 1
    swDwgPaperBsize = 2
    swDwgPaperCsize = 3
    swDwgPaperDsize = 4
    swDwgPaperEsize = 5
    swDwgPaperA4size = 6
    swDwgPaperA4sizeVertical = 7
    swDwgPaperA3size = 8
    swDwgPaperA2size = 9
    swDwgPaperA1size = 10
    swDwgPaperA0size = 11
    swDwgPapersUserDefined = 12
End Enum
Sub main()
    Const sTemplateName As String = "c:Program Files\SOLIDWORKS\data\templates\drawing.drwdot"

    Dim swApp                           As SldWorks.SldWorks
    Dim vTemplateSizes                  As Variant
    Set swApp = CreateObject("SldWorks.Application")
    vTemplateSizes = swApp.GetTemplateSizes(sTemplateName)

    Debug.Print "Template = " & sTemplateName
    Debug.Print "  Paper Size   = " & vTemplateSizes(0)
    Debug.Print "    Width      = " & vTemplateSizes(1) * 1000# & " mm"
    Debug.Print "    Height     = " & vTemplateSizes(2) * 1000# & " mm"
End Sub
'-------------------------------------
```
