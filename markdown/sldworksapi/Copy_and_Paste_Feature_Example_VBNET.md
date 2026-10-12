---
title: "Copy and Paste Feature Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Copy_and_Paste_Feature_Example_VBNET.htm"
---

# Copy and Paste Feature Example (VB.NET)

This example shows how to copy and paste a feature in a part document.

```
'----------------------------------------------------------------
' Preconditions: Verify that the specified part document to
' open exists.
'
' Postconditions:
' 1. Displays the Copy Confirmation dialog after calling
'    IModelDoc2::Paste.
' 2. Click Delete.
' 3. Pastes the copied feature on the selected face.
'
' NOTE: Because this part is used elsewhere, do not save changes.
'----------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System

Partial Class SolidWorksMacro

    Dim swModel As ModelDoc2
    Dim swModelDocExt As ModelDocExtension
    Dim fileName As String
    Dim status As Boolean
    Dim errors As Integer, warnings As Integer

    Sub main()

        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\testpart1.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        ' Select the feature to copy
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swModel.EditCopy()

        swModel.ClearSelection2(True)

        ' Select the face where to paste the copied feature
        status = swModelDocExt.SelectByID2("", "FACE", 0.0297472797980731, 0.0564587562103043, 0.00676585125080464, False, 0, Nothing, 0)

        ' Paste the copied feature on the selected face
        swModel.Paste()

        ' Displays the Copy Confirmation dialog
        ' Click Delete
        ' Pastes on the copied feature on the selected face
```

' Zoom to selection, then zoom to fit
swModel.**ViewZoomToSelection**()
swModel.**ViewZoomtofit2**()

End Sub

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks

End Class
