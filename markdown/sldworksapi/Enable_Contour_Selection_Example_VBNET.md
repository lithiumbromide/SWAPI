---
title: "Enable Contour Selection Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Enable_Contour_Selection_Example_VBNET.htm"
---

# Enable Contour Selection Example (VB.NET)

This example shows how to select the contour of a sketch region and extrude the selected region.

```vb
 '----------------------------------------------------------------------------
 ' Preconditions: Ensure that the specified document template exists.
 '
 ' Postconditions: The selected sketch region is extruded.
 ' ---------------------------------------------------------------------------

 Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System.Runtime.InteropServices
 Imports System

 Partial Class SolidWorksMacro

     Dim swModel As ModelDoc2
     Dim vSkLines As Object
     Dim boolstatus As Boolean

     Sub main()

         swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2014\templates\Part.prtdot", 0, 0, 0)
         swModel = swApp.ActiveDoc
         boolstatus = swModel.SetUserPreferenceToggle(swUserPreferenceToggle_e.swDisplayOrigins, True)
         swModel.ClearSelection2(True)

         vSkLines = swModel.SketchManager.CreateCornerRectangle(-0.0390769010920735, 0.0405984975017191, 0, 0.0129020232818107, -0.0166534302871355, 0)
         swModel.ClearSelection2(True)
         vSkLines = swModel.SketchManager.CreateCornerRectangle(-0.00751826843645631, 0.0156092594749566, 0, 0.0487922329685375, -0.041704950991857, 0)
         swModel.ClearSelection2(True)
         swModel.SketchManager.InsertSketch(True)

         ' Enable contour selection
         swModel.SelectionManager.EnableContourSelection = True
         ' Select a contour to extrude
         swModel.Extension.SelectByID2("Sketch1", "SKETCHREGION", 0, 0.01, 0, True, 4, Nothing, 0)
         swModel.FeatureManager.FeatureExtrusion3(True, False, False, 0, 0, 0.01, 0.01, False, False, False, False, 0, 0, False, False, False, False, True, True, True, 0, 0, False)
         ' Disable contour selection
         swModel.SelectionManager.EnableContourSelection = False
         swModel.ClearSelection2(True)

     End Sub

     Public swApp As SldWorks

 End  Class
```
