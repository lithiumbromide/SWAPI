---
title: "Get Loaded Sheets Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Loaded_Sheets_Example_VBNET.htm"
---

# Get Loaded Sheets Example (VB.NET)

This example shows how to determine if the sheets in a drawing are loaded.

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swDraw As DrawingDoc
        Dim vSheetName As Object
        Dim i As Integer
        Dim bRet As Boolean

        swModel = swApp.ActiveDoc
        swDraw = swModel

        ' Get the sheets in the drawing document
        vSheetName = swDraw.GetSheetNames

        ' Traverse the drawing sheets and determine whether
        ' they're loaded
        For i = 0 To UBound(vSheetName)
            bRet = swDraw.ActivateSheet(vSheetName(i))
            Dim swSheet As Sheet
            swSheet = swDraw.GetCurrentSheet
            If (swSheet.IsLoaded) Then
                Debug.Print(vSheetName(i) & " is loaded.")
            Else
                Debug.Print(vSheetName(i) & " is not loaded.")
            End If
        Next i
    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
