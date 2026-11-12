---
title: "Get Loaded Sheets Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loaded_Sheets_Example_VB.htm"
---

# Get Loaded Sheets Example (VBA)

This example shows how to determine which sheets in a drawing document are loaded.

```
'----------------------------------------------
' Preconditions:
' 1. Click File > Open.
' 2. Browse to public_documents\samples\tutorial\advdrawings.
' 3. Select foodprocessor.slddrw.
' 4. Click Select sheets to open > Selected > Sheet1* (Load) > OK > Open.
' 5. Open the Immediate window.
'
' Postconditions:
' 1. Loads Sheet1 only.
' 2. Mouse over the Sheet2, Sheet3, and Sheet4 tabs and
'    examine the Immediate window to verify step 1.
'
' NOTE: Because this drawing is used elsewhere, do not save
' changes.
'----------------------------------------------
```

```vb
Sub main()

    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swDraw                      As SldWorks.DrawingDoc
    Dim vSheetName                  As Variant
    Dim nRetval                     As Long
    Dim i                           As Long
    Dim bRet                        As Boolean

    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swDraw = swModel

    ' Get the sheets in the drawing document
    vSheetName = swDraw.GetSheetNames

    ' Traverse the drawing sheets and determine whether
    ' they're loaded
    For i = 0 To UBound(vSheetName)
        bRet = swDraw.ActivateSheet(vSheetName(i))
        Dim swSheet As Sheet
        Set swSheet = swDraw.GetCurrentSheet
        If (swSheet.IsLoaded) Then
           Debug.Print vSheetName(i) & " is loaded."
        Else
             Debug.Print vSheetName(i) & " is not loaded."
        End If
    Next i
End Sub
```
