---
title: "Create and Convert non-manifold Bodies Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Create_and_Convert_Non-manifold_Bodies_Example_VB.htm"
---

# Create and Convert non-manifold Bodies Example (VBA)

## Create and Convert Non-manifold Bodies Example (VBA)

This example shows how to create non-manifold bodies, which by default are not allowed in SOLIDWORKS Design, and then convert the non-manifold bodies to manifold bodies.

```
'-----------------------------------------------------
' Preconditions: Verify that the specified part document
' template exists.
'
' Postconditions:
' 1. Click Debug > Step Into in the IDE.
' 2. Step through the rest of the macro by pressing F8
'    while observing the graphics area.
' 3. Creates and tessellates non-manifold bodies
'    and coverts them to manifold bodies.
'----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModeler As SldWorks.Modeler
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchManager As SldWorks.SketchManager
Dim swFeature As SldWorks.Feature
Dim swSelMgr As SldWorks.SelectionMgr
Dim swSketchSegment As SldWorks.SketchSegment
Dim swFeatureManager As SldWorks.FeatureManager
Dim tess As SldWorks.Tessellation
Dim tool As SldWorks.Body2
Dim tgt1 As SldWorks.Body2
Dim tgt0 As SldWorks.Body2
Dim sketchLines As Variant
Dim resVar As Variant
Dim resvar2 As Variant
Dim manifVar As Variant
Dim vFacetId As Variant
Dim vFinId As Variant
Dim vVertexId As Variant
Dim vVertex1 As Variant
Dim vVertex2 As Variant
Dim f As Object
Dim boolstatus As Boolean
Dim i As Long
Dim j As Long
Dim clr(0 To 1) As Long
```

```
Sub DisplayBody(ByVal b As Object, col As Long)
    Call b.Display2(swModel, col, swTempBodySelectOptions_e.swTempBodySelectable)
End Sub
```

```
Sub HideBody(ByVal b As Object)
    Call b.Hide(swModel)
End Sub
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks

    Set swModeler = swApp.GetModeler
    'SOLIDWORKS requires this option to be
    'false, so make sure it is set to false
    swModeler.GeneralTopology = False
```

```
    'Create part having a tool and target bodies
    Set swModel = swApp.NewDocument("C:\ProgramData\SOLIDWORKS\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    boolstatus = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstToRectEntity, swUserPreferenceOption_e.swDetailingNoOptionSpecified, False)
    boolstatus = swModelDocExt.SetUserPreferenceToggle(swUserPreferenceToggle_e.swSketchAddConstLineDiagonalType, swUserPreferenceOption_e.swDetailingNoOptionSpecified, True)
    Set swSketchManager = swModel.SketchManager
    sketchLines = swSketchManager.CreateCornerRectangle(0, 0, 0, 0.13786334229408, 0.069192775961991, 0)
    boolstatus = swModelDocExt.SelectByID2("Line2", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Line4", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Line3", "SKETCHSEGMENT", 0, 0, 0, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 0, 0, 0, False, 4, Nothing, 0)
    Set swFeatureManager = swModel.FeatureManager
    Set swFeature = swFeatureManager.FeatureExtrusion2(True, False, False, swEndConditions_e.swEndCondBlind, 0, 0.01524, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, True, True, True, swStartConditions_e.swStartSketchPlane, 0, False)
    Set swSelMgr = swModel.SelectionManager
    swSelMgr.EnableContourSelection = False
    swModel.ClearSelection2 True
    swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, True, 0, Nothing, 0)
    swSketchManager.InsertSketch (True)
    Set swSketchSegment = swSketchManager.CreateLine(0#, 0.034596, 0#, 0.137863, 0.034596, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0.068932, 0.069193, 0#, 0.068932, 0#, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0#, 0#, 0#, 0.137863, 0#, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0.137863, 0#, 0#, 0.137863, 0.069193, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0.137863, 0.069193, 0#, 0#, 0.069193, 0#)
    Set swSketchSegment = swSketchManager.CreateLine(0#, 0.069193, 0#, 0#, 0#, 0#)
    boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCHREGION", 2.95651111315002E-02, 5.62122082077101E-02, 7.61999999999985E-03, True, 4, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCHREGION", 8.12426680973543E-02, 1.81340083381333E-02, 7.62000000000011E-03, True, 4, Nothing, 0)
    swModel.ClearSelection2 True
    boolstatus = swModelDocExt.SelectByID2("Line9", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCH", 2.95651111315002E-02, 5.62122082077101E-02, 7.61999999999985E-03, True, 4, Nothing, 0)
    swSelMgr.EnableContourSelection = True
    boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCHREGION", 2.95651111315002E-02, 5.62122082077101E-02, 7.61999999999985E-03, True, 4, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Sketch2", "SKETCHREGION", 8.12426680973543E-02, 1.81340083381333E-02, 7.62000000000011E-03, True, 4, Nothing, 0)
    Set swFeature = swFeatureManager.FeatureExtrusion2(True, False, False, swEndConditions_e.swEndCondBlind, 0, 0.01524, 0.01524, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, True, True, swStartConditions_e.swStartSketchPlane, 0, False)
    swSelMgr.EnableContourSelection = False
```

```
    'Hide the boss-extrude and sketch features
    boolstatus = swModelDocExt.SelectByID2("Boss-Extrude1", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    swFeatureManager.HideBodies
    boolstatus = swModelDocExt.SelectByID2("Boss-Extrude2", "BODYFEATURE", 0, 0, 0, False, 0, Nothing, 0)
    swFeatureManager.HideBodies
```

```
    'Make selections of tool and target bodies;
    'Boss-Extrude1 is larger cube, whereas Boss-Extrude2[1]
    'and Boss-Extrude2[2] are 1/4 the size of Boss-Extrude1,
    'so (Boss-Extrude - Boss-Extrude2[1])-Boss-Extrude2[2])
    'results in non-manifold bodies; under normal conditions,
    'i.e., when non-manifold bodies are not allowed,
    'such an operation results in two bodies;
    'when creation of non-manifold bodies is allowed,
    'then one general body is the result
    boolstatus = swModelDocExt.SelectByID2("Boss-Extrude1", "SOLIDBODY", 0, 0, 0, False, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Boss-Extrude2[1]", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Boss-Extrude2[2]", "SOLIDBODY", 0, 0, 0, True, 0, Nothing, 0)
```

```
    Set tool = swSelMgr.GetSelectedObject6(1, -1)
    Set tgt0 = swSelMgr.GetSelectedObject6(2, -1)
    Set tgt1 = swSelMgr.GetSelectedObject6(3, -1)
```

```
    'Create temporary bodies
    Set tool = tool.Copy
    Set tgt0 = tgt0.Copy
    Set tgt1 = tgt1.Copy
```

```
    swModel.ClearSelection2 True
```

```
    'First cut operation : Boss-Extrude1 - Boss-Extrude2[1]
    Dim errCode As Long
    resVar = tool.Operations2(swBodyOperationType_e.SWBODYCUT, tgt0, errCode)
```

```
    'SOLIDWORKS requires this option
    'to be false; thus, switch it back to false
    'as soon as your intended operations complete
    swModeler.GeneralTopology = True

    'Second cut operation: (Boss-Extrude1 - Boss-Extrude2[1])- Boss-Extrude2[2])
    resvar2 = resVar(0).Operations2(swBodyOperationType_e.SWBODYCUT, tgt1, errCode)
```

```
    'Reset the option back to false
    swModeler.GeneralTopology = False
```

```
    clr(0) = RGB(0, 0, 255)
    clr(1) = RGB(255, 0, 0)
    For i = LBound(resvar2) To UBound(resvar2)
        Call DisplayBody(resvar2(i), clr(i))
    Next i
```

```
    'Hide the displayed bodies
    For i = LBound(resvar2) To UBound(resvar2)
        HideBody (resvar2(i))
    Next i
```

```
    'Try tessellation
```

```
    'Add sketch for this face
    swModel.Insert3DSketch2 False
```

```
    'Add lines directly to sketch to increase performance
    swModel.SetAddToDB True
    Set tess = resvar2(0).GetTessellation(Empty)
    tess.NeedFaceFacetMap = True
    tess.MatchType = swTesselationMatchFacetGeometry
    boolstatus = tess.Tessellate
    Set f = resvar2(0).GetFirstFace
    While Not f Is Nothing
        vFacetId = tess.GetFaceFacets(f)
            For i = 0 To UBound(vFacetId)
                vFinId = tess.GetFacetFins(vFacetId(i))
                For j = 0 To 2
                    'Should always be three fins per facet
                    vVertexId = tess.GetFinVertices(vFinId(j))
                    'Should always be two vertices per fin
                    vVertex1 = tess.GetVertexPoint(vVertexId(0))
                    vVertex2 = tess.GetVertexPoint(vVertexId(1))
                    Call swModel.CreateLine2(vVertex1(0), vVertex1(1), vVertex1(2), vVertex2(0), vVertex2(1), vVertex2(2))
                Next j
            Next i
            Set f = f.GetNextFace
    Wend
```

```
    'Convert non-manifold bodies to manifold bodies
    manifVar = swModeler.MakeManifoldBodies(resvar2(0))
    For i = LBound(manifVar) To UBound(manifVar)
        Call DisplayBody(manifVar(i), RGB(0, 255, 0))
    Next i
```

```
    swModel.ClearSelection2 True
```

```
    For i = LBound(manifVar) To UBound(manifVar)
            HideBody (manifVar(i))
    Next i
```

```
End Sub
```
