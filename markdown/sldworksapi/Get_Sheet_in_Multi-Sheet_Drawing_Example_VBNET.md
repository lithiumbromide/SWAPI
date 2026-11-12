---
title: "Get Sheet in Multi-Sheet Drawing Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Sheet_in_Multi-Sheet_Drawing_Example_VBNET.htm"
---

# Get Sheet in Multi-Sheet Drawing Example (VB.NET)

This example shows how to get each sheet in a multi-sheet drawing regardless whether the sheet is loaded.

```
'----------------------------------------------------------------------
' Preconditions:
' 1. Click File > Open.
' 2. Open public_documents\samples\tutorial\advdrawings\foodprocessor.sldrw.
' 3. Click Select sheets to open > Selected > Sheet1* (load) > OK  >Open.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Loads Sheet1 only.
' 2. Mouse over Sheet2, Sheet3, and Sheet4 tabs and examine the
'    Immediate window.
'
' NOTE: Because this drawing is used elsewhere, do not save changes.
'---------------------------------------------------------------------
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
            swSheet = swDraw.Sheet(vSheetName(i))
            'swSheet = swDraw.GetCurrentSheet
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
