---
title: "Insert Coordinate System Feature at Center of Mass Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Insert_Coordinate_System_Feature_at_Center_of_Mass_Example_VB.htm"
---

# Insert Coordinate System Feature at Center of Mass Example (VBA)

This example shows how to insert a coordinate system feature on the center of mass.

'-------------------------------------------------------
' Preconditions:
' 1. Open a part or assembly.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Inserts a 3D sketch at the center of mass.
' 2. Inserts a coordinate system at center of mass.
' 3. Examine the graphics area and the Immediate window.
'-------------------------------------------------------
Option Explicit

Sub main()

```vb
    Dim swApp As SldWorks.SldWorks
     Dim swModel As SldWorks.ModelDoc2
     Dim swFeatMgr As SldWorks.FeatureManager
     Dim swModDocExt As SldWorks.ModelDocExtension
     Dim swMass As SldWorks.MassProperty
     Dim vCofG As Variant
     Dim vXaxis As Variant
     Dim vYAxis As Variant
     Dim vZAxis As Variant
     Dim swSkCofG As SldWorks.SketchPoint
     Dim swSkXaxis As SldWorks.SketchLine
     Dim swSkYaxis As SldWorks.SketchLine
     Dim swSkSegXaxis As SldWorks.SketchSegment
     Dim swSkSegYaxis As SldWorks.SketchSegment
     Dim swSelMgr As SldWorks.SelectionMgr
     Dim swSelData As SldWorks.SelectData
     Dim swFeat As SldWorks.Feature
     Dim swCoordSys As SldWorks.CoordinateSystemFeatureData
     Dim swComp As SldWorks.Component2
     Dim bRet As Boolean
    Set swApp = Application.SldWorks
     Set swModel = swApp.ActiveDoc
     Set swSelMgr = swModel.SelectionManager
     Set swSelData = swSelMgr.CreateSelectData
     Set swModDocExt = swModel.Extension

     Set swMass = swModDocExt.CreateMassProperty
     vCofG = swMass.CenterOfMass
     vXaxis = swMass.PrincipleAxesOfInertia(0)
     vYAxis = swMass.PrincipleAxesOfInertia(1)
     vZAxis = swMass.PrincipleAxesOfInertia(2)
     swModel.Insert3DSketch2 False
     swModel.SetAddToDB True
     Set swSkCofG = swModel.CreatePoint2(vCofG(0), vCofG(1), vCofG(2))
     Set swSkXaxis = swModel.CreateLine2(vCofG(0), vCofG(1), vCofG(2),  vCofG(0) + vXaxis(0), vCofG(1) + vXaxis(1), vCofG(2) + vXaxis(2))
     Set swSkYaxis = swModel.CreateLine2(  vCofG(0), vCofG(1), vCofG(2), vCofG(0) + vYAxis(0), vCofG(1) + vYAxis(1), vCofG(2) + vYAxis(2))
     Set swSkSegXaxis = swSkXaxis
     Set swSkSegYaxis = swSkYaxis
     swModel.SetAddToDB False
     swModel.Insert3DSketch2 True
     swModel.ClearSelection2 True
     swSelData.Mark = 1
     bRet = swSkCofG.Select4(True, swSelData): Debug.Assert bRet
     swSelData.Mark = 2
     bRet = swSkSegXaxis.Select4(True, swSelData): Debug.Assert bRet
     swSelData.Mark = 4
     bRet = swSkSegYaxis.Select4(True, swSelData): Debug.Assert bRet

     ' Insert the coordinate system feature, get the feature, and modify it, using the feature data
     Set swFeatMgr = swModel.FeatureManager
     Set swFeat = swFeatMgr.InsertCoordinateSystem(False, False, False)
     If swFeat Is Nothing Then
         Debug.Print "Did not get coordinate system feature."
     Else
         Set swCoordSys = swFeat.GetDefinition
         bRet = swCoordSys.AccessSelections(swModel, swComp)
         Debug.Print "XFlipped? " & swCoordSys.XFlipped
         swCoordSys.XFlipped = True
        ' Get the origin entity
         Dim gvx As Variant
         Dim vxCount As Long
         Dim i As Long

        ' Get the origin entity
         Dim entType As Long
         Dim geo  As Object
         Dim oent As SldWorks.Entity
         Dim skpnt As SldWorks.SketchPoint
         Set geo = swCoordSys.OriginEntity

         ' Is it an entity?
         If TypeOf geo Is Entity Then
             Set oent = geo
             entType = geo.GetType
             Debug.Print "Entity type: " & entType
         Else
             Debug.Print "Is sketch point."
             Set skpnt = geo
             If Not skpnt Is Nothing Then
                 Debug.Print "Got sketch point."
             End If
         End If

        Dim xEnt As Object
         vxCount = swCoordSys.GetXAxisEntitiesCount
         gvx = swCoordSys.XAxisEntities

        ' Find out about the x axis entities
         Dim skent As SldWorks.SketchSegment
         For i = 0 To UBound(gvx)
             Set xEnt = gvx(i)
             If TypeOf xEnt Is SketchSegment Then
                 Set skent = xEnt
                 entType = skent.GetType
                 Debug.Print "Entity type: " & entType
             End If
         Next i
        bRet = swFeat.ModifyDefinition(swCoordSys, swModel, Nothing)

        swCoordSys.ReleaseSelectionAccess

    End If
End Sub
```
