---
title: "Get and Set Model View HLR Quality Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_and_Set_Model_View_HLR_Quality_Example_VBNET.htm"
---

# Get and Set Model View HLR Quality Example (VB.NET)

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

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Sub main()

         Dim swModel As ModelDoc2
         Dim swModView As ModelView

         swModel = swApp.ActiveDoc
         swModView = swModel.ActiveView

         ' Set HLR quality to a fast redraw and lower image quality of model edges
         swModView.HlrQuality = swHlrQuality_e.swFastHlr

         Debug.Print("File = " & swModel.GetPathName)
         Debug.Print("  Hidden-line removal quality as defined in swHlrQuality_e (1 = swHlrQuality_e.swFastHlr) = " & swModView.HlrQuality)

     End Sub

     Public swApp As SldWorks

 End  Class
```
