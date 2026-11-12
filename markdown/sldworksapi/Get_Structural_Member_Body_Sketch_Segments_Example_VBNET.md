---
title: "Get Structural Member Body Sketch Segments Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Structural_Member_Body_Sketch_Segments_Example_VBNET.htm"
---

# Get Structural Member Body Sketch Segments Example (VB.NET)

This example shows how to get the sketch segments that define the path of a body in a structural member.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions:
 ' 1. Open public_documents\samples\tutorial\api\weldment_box3.sldprt.
 ' 2. Open the Immediate window.
 '
 ' Postconditions:
 ' 1. Gets the feature definition of Structural Member1.
 ' 2. Selects body, Structural Member1[1].
 ' 3. Gets the number of sketch segments that define the path of the
 '    selected body.
 ' 4. Examine the Immediate window.
 '
 ' NOTE: Because the part is used elsewhere, do not save changes.
 ' ---------------------------------------------------------------------------
 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System
 Imports System.Diagnostics

 Partial Class SolidWorksMacro

     Dim Part As ModelDoc2
     Dim boolstatus As Boolean

     Dim swFeat As Feature
     Dim featData As StructuralMemberFeatureData
     Dim selMan As SelectionMgr
     Dim swBody As Body2
     Dim vSeg As Object

     Sub main()

         Part = swApp.ActiveDoc
         boolstatus = Part.Extension.SelectByID2("Structural Member1",  "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
         selMan = Part.SelectionManager
         swFeat = selMan.GetSelectedObject6(1, -1)
         featData = swFeat.GetDefinition

         Part.ClearSelection2(True)

         ' Select a body in Structural Member1
         boolstatus = Part.Extension.SelectByID2("Structural Member1[1]",  "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
         swBody = selMan.GetSelectedObject6(1, -1)

         ' Get the sketch segments that define the path of the selected body
         vSeg = featData.GetSketchSegments(swBody)
         Debug.Print(" Number of sketch segments: " & UBound(vSeg) + 1)

     End Sub

     Public swApp As SldWorks

 End  Class
```
