---
title: "Get Bounding Box Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Bounding_Box_Example_VBNET.htm"
---

# Get Bounding Box Example (VB.NET)

This example shows how to get the bounding boxes for the selected feature and face. This example also shows how to draw 3D sketches depicting the bounding boxes.

```
'----------------------------------------------
' Preconditions:
' 1. Verify that the part to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Selects the Sweep1 feature.
' 2. Creates a 3D sketch of the bounding box of
'    the selected Sweep1 feature.
' 3. Selects the top face.
' 4. Creates a 3D sketch of the bounding box of
'    the selected face.
' 5. Examine the graphics area and the Immediate
'    window.
'
' NOTE: Because this part is used elsewhere,
' do not save changes.
'----------------------------------------------

Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub Main()

        Dim swModel As ModelDoc2
        Dim swModelDocExt As ModelDocExtension
        Dim swSelMgr As SelectionMgr
        Dim swFeat As Feature
        Dim swFace As Face2
        Dim BoxFeatureArray(6) As Double
        Dim BoxFaceArray(6) As Double
        Dim swSketchMgr As SketchManager
        Dim swSketchPt(8) As SketchPoint
        Dim swSketchSeg(12) As SketchSegment
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim fileName As String

        ' Open part document
        fileName = "C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\api\cstick.sldprt"
        swModel = swApp.OpenDoc6(fileName, swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)

        ' Select feature
        swModelDocExt = swModel.Extension
        swSelMgr = swModel.SelectionManager
        status = swModelDocExt.SelectByID2("Sweep1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
        swFeat = swSelMgr.GetSelectedObject6(1, -1)

        ' Get selected feature's bounding box
        Debug.Print("Feature:")
        status = swFeat.GetBox(BoxFeatureArray) : Debug.Assert(status)
        Debug.Print("  Pt1 = " & _
                "(" & _
                BoxFeatureArray(0) * 1000.0# & ", " & _
                BoxFeatureArray(1) * 1000.0# & ", " & _
                BoxFeatureArray(2) * 1000.0# & _
                ") mm")
        Debug.Print("  Pt2 = " & _
                "(" & _
                BoxFeatureArray(3) * 1000.0# & ", " & _
                BoxFeatureArray(4) * 1000.0# & ", " & _
                BoxFeatureArray(5) * 1000.0# & _
                ") mm")

        swModel.Insert3DSketch2(True)
        swModel.SetAddToDB(True)
        swModel.SetDisplayWhenAdded(False)

        swSketchMgr = swModel.SketchManager

        ' Draw points at each corner of bounding box
        swSketchPt(0) = swSketchMgr.CreatePoint(BoxFeatureArray(3), BoxFeatureArray(1), BoxFeatureArray(5))
        swSketchPt(1) = swSketchMgr.CreatePoint(BoxFeatureArray(0), BoxFeatureArray(1), BoxFeatureArray(5))
        swSketchPt(2) = swSketchMgr.CreatePoint(BoxFeatureArray(0), BoxFeatureArray(1), BoxFeatureArray(2))
        swSketchPt(3) = swSketchMgr.CreatePoint(BoxFeatureArray(3), BoxFeatureArray(1), BoxFeatureArray(2))
        swSketchPt(4) = swSketchMgr.CreatePoint(BoxFeatureArray(3), BoxFeatureArray(4), BoxFeatureArray(5))
        swSketchPt(5) = swSketchMgr.CreatePoint(BoxFeatureArray(0), BoxFeatureArray(4), BoxFeatureArray(5))
        swSketchPt(6) = swSketchMgr.CreatePoint(BoxFeatureArray(0), BoxFeatureArray(4), BoxFeatureArray(2))
        swSketchPt(7) = swSketchMgr.CreatePoint(BoxFeatureArray(3), BoxFeatureArray(4), BoxFeatureArray(2))

        ' Now draw bounding box
        swSketchSeg(0) = swSketchMgr.CreateLine(swSketchPt(0).X, swSketchPt(0).Y, swSketchPt(0).Z, swSketchPt(1).X, swSketchPt(1).Y, swSketchPt(1).Z)
        swSketchSeg(1) = swSketchMgr.CreateLine(swSketchPt(1).X, swSketchPt(1).Y, swSketchPt(1).Z, swSketchPt(2).X, swSketchPt(2).Y, swSketchPt(2).Z)
        swSketchSeg(2) = swSketchMgr.CreateLine(swSketchPt(2).X, swSketchPt(2).Y, swSketchPt(2).Z, swSketchPt(3).X, swSketchPt(3).Y, swSketchPt(3).Z)
        swSketchSeg(3) = swSketchMgr.CreateLine(swSketchPt(3).X, swSketchPt(3).Y, swSketchPt(3).Z, swSketchPt(0).X, swSketchPt(0).Y, swSketchPt(0).Z)
        swSketchSeg(4) = swSketchMgr.CreateLine(swSketchPt(0).X, swSketchPt(0).Y, swSketchPt(0).Z, swSketchPt(4).X, swSketchPt(4).Y, swSketchPt(4).Z)
        swSketchSeg(5) = swSketchMgr.CreateLine(swSketchPt(1).X, swSketchPt(1).Y, swSketchPt(1).Z, swSketchPt(5).X, swSketchPt(5).Y, swSketchPt(5).Z)
        swSketchSeg(6) = swSketchMgr.CreateLine(swSketchPt(2).X, swSketchPt(2).Y, swSketchPt(2).Z, swSketchPt(6).X, swSketchPt(6).Y, swSketchPt(6).Z)
        swSketchSeg(7) = swSketchMgr.CreateLine(swSketchPt(3).X, swSketchPt(3).Y, swSketchPt(3).Z, swSketchPt(7).X, swSketchPt(7).Y, swSketchPt(7).Z)
        swSketchSeg(8) = swSketchMgr.CreateLine(swSketchPt(4).X, swSketchPt(4).Y, swSketchPt(4).Z, swSketchPt(5).X, swSketchPt(5).Y, swSketchPt(5).Z)
        swSketchSeg(9) = swSketchMgr.CreateLine(swSketchPt(5).X, swSketchPt(5).Y, swSketchPt(5).Z, swSketchPt(6).X, swSketchPt(6).Y, swSketchPt(6).Z)
        swSketchSeg(10) = swSketchMgr.CreateLine(swSketchPt(6).X, swSketchPt(6).Y, swSketchPt(6).Z, swSketchPt(7).X, swSketchPt(7).Y, swSketchPt(7).Z)
        swSketchSeg(11) = swSketchMgr.CreateLine(swSketchPt(7).X, swSketchPt(7).Y, swSketchPt(7).Z, swSketchPt(4).X, swSketchPt(4).Y, swSketchPt(4).Z)
```

```
        swModel.SetDisplayWhenAdded(True)
        swModel.SetAddToDB(False)
        swModel.Insert3DSketch2(True)

        swModel.ClearSelection2(True)

        ' Get selected face's bounding box
        status = swModelDocExt.SelectByID2("", "FACE", -0.0000762173696102764, 0.219999999999857, 0.00945327855254163, False, 0, Nothing, 0)
        swFace = swSelMgr.GetSelectedObject6(1, -1)

        ' Get selected face's bounding box
        Debug.Print("Face =")
        BoxFaceArray = swFace.GetBox
        Debug.Print("  Pt1 = " & _
                "(" & _
                BoxFaceArray(0) * 1000.0# & ", " & _
                BoxFaceArray(1) * 1000.0# & ", " & _
                BoxFaceArray(2) * 1000.0# & _
                ") mm")
        Debug.Print("  Pt2 = " & _
                "(" & _
                BoxFaceArray(3) * 1000.0# & ", " & _
                BoxFaceArray(4) * 1000.0# & ", " & _
                BoxFaceArray(5) * 1000.0# & _
                ") mm")

        swModel.Insert3DSketch2(True)
        swModel.SetAddToDB(True)
        swModel.SetDisplayWhenAdded(False)

        ' Draw points at each corner of bounding box
        swSketchPt(0) = swSketchMgr.CreatePoint(BoxFaceArray(3), BoxFaceArray(1), BoxFaceArray(5))
        swSketchPt(1) = swSketchMgr.CreatePoint(BoxFaceArray(0), BoxFaceArray(1), BoxFaceArray(5))
        swSketchPt(2) = swSketchMgr.CreatePoint(BoxFaceArray(0), BoxFaceArray(1), BoxFaceArray(2))
        swSketchPt(3) = swSketchMgr.CreatePoint(BoxFaceArray(3), BoxFaceArray(1), BoxFaceArray(2))
        swSketchPt(4) = swSketchMgr.CreatePoint(BoxFaceArray(3), BoxFaceArray(4), BoxFaceArray(5))
        swSketchPt(5) = swSketchMgr.CreatePoint(BoxFaceArray(0), BoxFaceArray(4), BoxFaceArray(5))
        swSketchPt(6) = swSketchMgr.CreatePoint(BoxFaceArray(0), BoxFaceArray(4), BoxFaceArray(2))
        swSketchPt(7) = swSketchMgr.CreatePoint(BoxFaceArray(3), BoxFaceArray(4), BoxFaceArray(2))

        ' Now draw bounding box
        swSketchSeg(0) = swSketchMgr.CreateLine(swSketchPt(0).X, swSketchPt(0).Y, swSketchPt(0).Z, swSketchPt(1).X, swSketchPt(1).Y, swSketchPt(1).Z)
        swSketchSeg(1) = swSketchMgr.CreateLine(swSketchPt(1).X, swSketchPt(1).Y, swSketchPt(1).Z, swSketchPt(2).X, swSketchPt(2).Y, swSketchPt(2).Z)
        swSketchSeg(2) = swSketchMgr.CreateLine(swSketchPt(2).X, swSketchPt(2).Y, swSketchPt(2).Z, swSketchPt(3).X, swSketchPt(3).Y, swSketchPt(3).Z)
        swSketchSeg(3) = swSketchMgr.CreateLine(swSketchPt(3).X, swSketchPt(3).Y, swSketchPt(3).Z, swSketchPt(0).X, swSketchPt(0).Y, swSketchPt(0).Z)
        swSketchSeg(4) = swSketchMgr.CreateLine(swSketchPt(0).X, swSketchPt(0).Y, swSketchPt(0).Z, swSketchPt(4).X, swSketchPt(4).Y, swSketchPt(4).Z)
        swSketchSeg(5) = swSketchMgr.CreateLine(swSketchPt(1).X, swSketchPt(1).Y, swSketchPt(1).Z, swSketchPt(5).X, swSketchPt(5).Y, swSketchPt(5).Z)
        swSketchSeg(6) = swSketchMgr.CreateLine(swSketchPt(2).X, swSketchPt(2).Y, swSketchPt(2).Z, swSketchPt(6).X, swSketchPt(6).Y, swSketchPt(6).Z)
        swSketchSeg(7) = swSketchMgr.CreateLine(swSketchPt(3).X, swSketchPt(3).Y, swSketchPt(3).Z, swSketchPt(7).X, swSketchPt(7).Y, swSketchPt(7).Z)
        swSketchSeg(8) = swSketchMgr.CreateLine(swSketchPt(4).X, swSketchPt(4).Y, swSketchPt(4).Z, swSketchPt(5).X, swSketchPt(5).Y, swSketchPt(5).Z)
        swSketchSeg(9) = swSketchMgr.CreateLine(swSketchPt(5).X, swSketchPt(5).Y, swSketchPt(5).Z, swSketchPt(6).X, swSketchPt(6).Y, swSketchPt(6).Z)
        swSketchSeg(10) = swSketchMgr.CreateLine(swSketchPt(6).X, swSketchPt(6).Y, swSketchPt(6).Z, swSketchPt(7).X, swSketchPt(7).Y, swSketchPt(7).Z)
        swSketchSeg(11) = swSketchMgr.CreateLine(swSketchPt(7).X, swSketchPt(7).Y, swSketchPt(7).Z, swSketchPt(4).X, swSketchPt(4).Y, swSketchPt(4).Z)

        swModel.SetDisplayWhenAdded(True)
        swModel.SetAddToDB(False)
        swModel.Insert3DSketch2(True)

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
