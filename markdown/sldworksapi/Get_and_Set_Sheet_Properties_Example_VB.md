---
title: "Get and Set Sheet Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Sheet_Properties_Example_VB.htm"
---

# Get and Set Sheet Properties Example (VBA)

This example shows how to get the sheet properties and how to switch projection.

```
'----------------------------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\block1.sldprt and make
'    a drawing with front, side, and top views.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Switches projection to third angle from first angle or vice versa.
' 2. Examine the graphics area and Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'----------------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSheet As SldWorks.Sheet
    Dim vSheetProps As Variant
    Dim bFirstAng As Boolean
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swDraw = swApp.ActiveDoc
    Set swSheet = swDraw.GetCurrentSheet
```

```
    ' Get current sheet properties
    vSheetProps = swSheet.GetProperties
```

```
    ' Current sheet properties
    Debug.Print "Name = " + swSheet.GetName
    Debug.Print "  TemplateName              = " & swSheet.GetTemplateName
    Debug.Print "  PaperSize                 = " & vSheetProps(0)
    Debug.Print "  TemplateIn                = " & vSheetProps(1)
    Debug.Print "  Scale1                    = " & vSheetProps(2)
    Debug.Print "  scale2                    = " & vSheetProps(3)
    Debug.Print "  FirstAngle                = " & vSheetProps(4)
    Debug.Print "  Width                     = " & vSheetProps(5)
    Debug.Print "  Height                    = " & vSheetProps(6)
```

```
    ' Switch projection property
    bFirstAng = vSheetProps(4)
    vSheetProps(4) = Not bFirstAng
```

```
    ' Apply updated sheet properties
    swSheet.SetProperties vSheetProps(0), vSheetProps(1), vSheetProps(2), vSheetProps(3), vSheetProps(4), vSheetProps(5), vSheetProps(6)
```

```
    ' Current projection property
    Debug.Print " "
    Debug.Print "  New FirstAngle setting    = " & vSheetProps(4)
```

```
    swDraw.EditRebuild
```

```
End Sub
```
