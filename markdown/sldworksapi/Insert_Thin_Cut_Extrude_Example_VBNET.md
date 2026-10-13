---
title: "Insert Thin Cut Extrude Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Thin_Cut_Extrude_Example_VBNET.htm"
---

# Insert Thin Cut Extrude Example (VB.NET)

This example shows how to insert a thin cut extrude feature.

```
'------------------------------------------------------
' Preconditions: Verify that the specified part exists.
'
' Postconditions:
' 1. Opens the part.
' 2. Inserts a thin cut extrude feature in the part.
' 3. Examine the FeatureManager design tree and
'    graphics area.
'
' NOTE: Because this part document is used elsewhere,
' do not save changes.
'-----------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System

Partial Class SolidWorksMacro

    Public
 Sub main()
```

```vb
         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swSketchManager As SketchManager
         Dim swSketchSegment As SketchSegment
         Dim swFeatureManager As FeatureManager
         Dim swFeature As Feature
         Dim boolstatus As Boolean
         Dim longstatus As Integer, longwarnings As Integer

         ' Open part
         swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\water.sldprt", 1, 0, "", longstatus,
 longwarnings)
         swModel = swApp.ActiveDoc

         ' Select face on which to sketch a circle
         swModelDocExt = swModel.Extension
         boolstatus = swModelDocExt.SelectByID2("", "FACE", 0.0001655362220845, -0.0477671348753, 0.072, False, 0, Nothing, 0)
         swModel.ShowNamedView2("*Normal To", swStandardViews_e.swBackView)
         swModel.ClearSelection2(True)

         ' Sketch a circle
         swSketchManager = swModel.SketchManager
         swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.030255, -0.042492, 0.0#)
         swModel.ClearSelection2(True)

         ' Create the thin cut extrude
         boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
         swFeatureManager = swModel.FeatureManager
         swFeature = swFeatureManager.FeatureCutThin2(True, False, False, swEndConditions_e.swEndCondBlind,
 swEndConditions_e.swEndCondBlind, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False,
 False, False, 0.01, 0.01, 0.01, 0, 0, False, 0.005, True, True, swStartConditions_e.swStartSketchPlane, 0, False)
         swModel.ShowNamedView2("*Isometric", swStandardViews_e.swIsometricView)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
     ''' </summary>
     Public swApp As SldWorks

 End Class
```
