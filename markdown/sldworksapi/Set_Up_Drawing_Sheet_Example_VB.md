---
title: "Change Setup of Drawing Sheet Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Set_Up_Drawing_Sheet_Example_VB.htm"
---

# Change Setup of Drawing Sheet Example (VBA)

This example shows how to change the setup of a drawing sheet by changing its paper size and template.

```
'--------------------------------------------------------
' Preconditions:
' 1. Verify that the specified sheet format template exists.
' 2. Open public_documents\samples\tutorial\api\2012-sm.slddrw.
'
' Postconditions:
' 1. Changes the sheet format's paper size and template.
' 2. Examine the drawing.
'
' NOTE: Because the drawing is used elsewhere, do not save
' changes.
'--------------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Const sTemplatePath As String = "C:\ProgramData\SolidWorks\SOLIDWORKS 2016\lang\english\sheetformat\b-landscape.slddrt"
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSheet As SldWorks.Sheet
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
    Set swSheet = swDraw.GetCurrentSheet
```

```
    bRet = swDraw.SetupSheet4(swSheet.GetName, swDwgPaperBsize, swDwgTemplateBsize, 1#, 1#, False, "", 0#, 0#, "")
```

```
    swModel.ForceRebuild3 (False)
```

```
End Sub
```
