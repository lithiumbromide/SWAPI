---
title: "Get and Set Model View HLR Quality Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Model_View_HLR_Quality_Example_VB.htm"
---

# Get and Set Model View HLR Quality Example (VBA)

This example shows how to get and set the hidden-line removal quality of model edges.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Open a part or assembly document.
 '
 ' Postconditions:
 ' 1. Sets the hidden-line removal quality to
 '    swHlrQuality_e.swFastHlr for a fast redraw and lower
 '    image quality of model edges.
 ' 2. Examine the Immediate window.
 '----------------------------------------------------------------------------
Option Explicit
Sub main()
    Dim swApp                       As SldWorks.SldWorks
     Dim swModel                     As SldWorks.ModelDoc2
     Dim swModView                   As SldWorks.ModelView
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swModView = swModel.ActiveView
    ' Set HLR quality to a fast redraw and lower image quality of model edges
     swModView.HlrQuality = swFastHlr
    Debug.Print "File = " & swModel.GetPathName
     Debug.Print "  Hidden-line removal quality as defined in swHlrQuality_e (1 = swHlrQaulity_e.swFastHlr)= " & swModView.HlrQuality
End Sub
```
