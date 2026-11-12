---
title: "Open Advanced Dialog on Document Open Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Open_Advanced_Dialog_On_Open_Example_VB.htm"
---

# Open Advanced Dialog on Document Open Example (VBA)

This example shows how to open an advanced dialog box before opening a document.

```vb
'----------------------------------------------------------------------
 ' Preconditions: Verify that the specified model document to open exists.
 '
 ' Postconditions:
 ' 1. Displays the Configure Document dialog box before the model
 '    document opens.
 ' 2. Click OK to close the dialog box.
 ' 3. Close the document without saving.
 '---------------------------------------------------------------------------
Option Explicit

Sub main()

    Dim swApp As SldWorks.SldWorks
    Dim myDoc As SldWorks.ModelDoc2
    Dim openDocParams As SldWorks.DocumentSpecification

    Set swApp = Application.SldWorks
    Set openDocParams = swApp.GetOpenDocSpec("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\motionstudies\valve_cam.sldasm")
    openDocParams.DocumentType = SwConst.swDocASSEMBLY
    openDocParams.InteractiveAdvancedOpen = True

    Set myDoc = swApp.OpenDoc7(openDocParams)
End Sub
```
