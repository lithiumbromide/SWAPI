---
title: "Get Active PropertyManager Page Name Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Active_PropertyManager_Page_Name_Example_VBNET.htm"
---

# Get Active PropertyManager Page Name Example (VB.NET)

This example shows how to get the name of the active PropertyManager page.

```vb
'--------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\fillets\knob.sldprt.
 ' 2. In SOLIDWORKS Design, click Insert > Features > Fillet/Round.
 ' 3. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Gets the name of the active PropertyManager page.
 ' 2. Examine the Immediate window.
 ' 3. In the SOLIDWORKS Design user-interface:
 '    a. Close the PropertyManager page.
 '    b. Close the part document.
 '
 ' NOTE: Because the part is used elsewhere, do not
 ' save changes.
 '----------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System
 Imports System.Diagnostics

 Partial  Class SolidWorksMacro

     Public  Sub Main()

         Dim swModel  As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim pageName  As  String

         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension

         ' Print the name of the active PropertyManager page in the Immediate window
         pageName = swModelDocExt.GetActivePropertyManagerPage
         Debug.Print("Name of active PropertyManager page: " & pageName)

     End  Sub

     '''  <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     '''  </summary>
     Public swApp As SldWorks

 End  Class
```
