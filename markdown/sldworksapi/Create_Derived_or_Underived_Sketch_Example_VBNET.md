---
title: "Create Derived or Underived Sketch Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_Derived_or_Underived_Sketch_Example_VBNET.htm"
---

# Create Derived or Underived Sketch Example (VB.NET)

This example shows how to create a derived or underived sketch.

```
'--------------------------------------------------------------
' Preconditions:
' 1. Open a part that contains at least one sketch.
' 2. Select a sketch.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. If the selected sketch is not derived, then a
'    derived sketch is created.
'    - or -
'    If the selected sketch is derived, then the
'    sketch is changed to underived.
' 2. Examine the FeatureManager design tree and Immediate
'    window.
'--------------------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Diagnostics
Imports System
Imports System.Runtime.InteropServices

Partial Class SolidWorksMacro
```

```vb
     Public Sub main()

         Dim swModel As ModelDoc2
         Dim swSelMgr As SelectionMgr
         Dim swFeat As Feature
         Dim swSketch As Sketch

         swModel = swApp.ActiveDoc

         ' Interactively select a sketch
         swSelMgr = swModel.SelectionManager
         swFeat = swSelMgr.GetSelectedObject6(1, -1)
         swSketch = swFeat.GetSpecificFeature2

         Debug.Print("Is the selected sketch derived? " & swSketch.IsDerived)

          ' If the selected sketch is a derived sketch,
         ' then create a derived sketch; else, underive the
         ' selected sketch
         If swSketch.IsDerived Then
             swModel.UnderiveSketch
             Debug.Print ("  Selected sketch was derived; sketch is now underived.")
         Else
             swModel.DeriveSketch
             Debug.Print ("  Selected sketch was not derived; a derived sketch has been created.")
         End If

         swModel.ForceRebuild3(False)

     End Sub
    ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
