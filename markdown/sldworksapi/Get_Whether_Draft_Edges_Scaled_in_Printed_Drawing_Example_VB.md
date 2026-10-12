---
title: "Get Whether Draft Edges Scaled in Printed Drawing Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Whether_Draft_Edges_Scaled_in_Printed_Drawing_Example_VB.htm"
---

# Get Whether Draft Edges Scaled in Printed Drawing Example (VBA)

This example shows how to get whether draft edges are scaled when printing a drawing in high quality.

```
'------------------------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified drawing exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the drawing.
' 2. Examine the Immediate window.
'------------------------------------------------------------------------------
Dim swApp As SldWorks.SldWorks
Dim swDrawing As SldWorks.DrawingDoc
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swPageSetup As SldWorks.PageSetup
Dim fileName As String
Dim errors As Long
Dim warnings As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\advdrawings\foodprocessor.slddrw"
    Set swDrawing = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocDRAWING, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModel = swDrawing
    Set swModelDocExt = swModel.Extension
    Set swPageSetup = swModelDocExt.AppPageSetup
    If swPageSetup.HighQuality Then
        Debug.Print "Drawing set to print in high quality. Are draft edges scaled? " & swPageSetup.ScaleDraftEdges
    Else
        Debug.Print "Drawing not set to print in high quality. Can only scale draft edges when drawing set to print in high quality."
    End If
```

```
End Sub
```
