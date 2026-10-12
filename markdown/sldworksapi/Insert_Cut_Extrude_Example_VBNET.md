---
title: "Insert Cut Extrude Feature (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Cut_Extrude_Example_VBNET.htm"
---

# Insert Cut Extrude Feature (VB.NET)

## Insert Cut Extrude Example (VB.NET)

This example shows how to insert a cut extrude feature.

```
'-------------------------------------------------------------
' Preconditions: Verify that the specified file to open exists.
'
' Postconditions:
' 1. Inserts a cut extrude feature in the model.
' 2. Examine the graphics area.
'
' NOTE: Because the part document is used elsewhere, do not save
' changes.
'--------------------------------------------------------------
```

```vb
Imports SolidWorks.Interop.sldworks
 Imports SolidWorks.Interop.swconst
 Imports System

 Partial Class SolidWorksMacro

     Public Sub Main()

         Dim swModel As ModelDoc2
         Dim swModelDocExt As ModelDocExtension
         Dim swSketchManager As SketchManager
         Dim swSketchSegment As SketchSegment
         Dim swFeatureManager As FeatureManager
         Dim swFeature As Feature
         Dim boolstatus As Boolean
         Dim fileerror As Long, filewarning As Long

         ' Open part document
         swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\plate.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", fileerror, filewarning)
         swModel = swApp.ActiveDoc
         swModelDocExt = swModel.Extension

         ' Select the face where to sketch a circle
         boolstatus = swModelDocExt.SelectByID2("", "FACE", -0.02031412853728, 0.006977746007294, -0.008053400767039, False, 0, Nothing, 0)
         swSketchManager = swModel.SketchManager
         swSketchManager.InsertSketch(True)
         swModel.ClearSelection2(True)

         ' Sketch a circle
         swSketchSegment = swSketchManager.CreateCircle(0.0#, 0.0#, 0.0#, 0.01708, -0.030458, 0.0#)
         boolstatus = swModelDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
         swModel.ClearSelection2(True)

         ' Create a cut-extrude feature using the circle
         swFeatureManager = swModel.FeatureManager
         swFeature = swFeatureManager.FeatureCut3(True, False, False, swEndConditions_e.swEndCondThroughAll, swEndConditions_e.swEndCondBlind, 0.01, 0.01, False, False, False, False, 0.01745329251994, 0.01745329251994, False, False, False, False, False, True, True, False, False, False, swStartConditions_e.swStartSketchPlane, 0, False)

     End Sub

     ''' <summary>
     ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
     Public swApp As SldWorks

 End Class
```
