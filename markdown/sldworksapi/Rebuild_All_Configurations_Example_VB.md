---
title: "Rebuild All Configurations Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Rebuild_All_Configurations_Example_VB.htm"
---

# Rebuild All Configurations Example (VBA)

To rebuild all of the configurations in a part, assembly, or drawing document, see:

- [Forcibly Rebuild All Configurations Example (VBA)](Forcibly_Rebuild_All_Configurations_Example_VB.htm)
- [Get Active Document Dependents Example (VBA)](Get_Active_Document_Dependents_Example_VB.htm)

Also, because each drawing view on each sheet can contain a different model and each in a different configuration, first you must find the parts or assemblies associated with the drawing. You can then rebuild them in the usual manner. Next, you must activate each drawing sheet and rebuild that sheet. The following example shows how to activate each sheet in a drawing document.

```
'---------------------------------------------
' Preconditions:
' 1. Open a drawing document that has multiple
'    sheets.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets the names of each drawing sheet and
'    activates that sheet.
' 2. Examine the Immediate window.
'----------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swDraw As SldWorks.DrawingDoc
    Dim swSheet As SldWorks.Sheet
    Dim vSheetNameArr As Variant
    Dim vSheetName As Variant
    Dim bRet As Boolean
    Dim i As Long
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel
```

```
    Set swSheet = swDraw.GetCurrentSheet
    Debug.Print "FileName = " & swModel.GetPathName
    Debug.Print "  Current sheet = " & swSheet.GetName
    Debug.Print ""
```

```
    vSheetNameArr = swDraw.GetSheetNames
    For Each vSheetName In vSheetNameArr
        Debug.Print "  SheetName[" & i & "] = " & vSheetName
        bRet = swDraw.ActivateSheet(vSheetName): Debug.Assert bRet
    Next vSheetName
```

```
End Sub
```
