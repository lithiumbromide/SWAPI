---
title: "Open Advanced Dialog on Document Open Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Advanced_Dialog_On_Open_Example_VBNET.htm"
---

# Open Advanced Dialog on Document Open Example (VB.NET)

This example shows how to open an advanced dialog box before opening a document.

'----------------------------------------------------------------------
' Preconditions: Verify that the specified model document to open exists.
'
' Postconditions:
' 1. Displays the Configure Document dialog box before the model
' document opens.
' 2. Click **OK** to close the dialog box.
' 3. Close the document without saving.
'---------------------------------------------------------------------------

```vb
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

     Sub main()

        Dim myDoc As ModelDoc2
        Dim openDocParams As DocumentSpecification
        openDocParams = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve_cam.sldasm")
        openDocParams.DocumentType = swDocumentTypes_e.swDocASSEMBLY
        openDocParams.InteractiveAdvancedOpen = True
        myDoc = swApp.OpenDoc7(openDocParams)

    End Sub

    Public swApp As SldWorks

End Class
```
