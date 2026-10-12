---
title: "Replace Sketch Relation Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Replace_Sketch_Relation_Example_VB.htm"
---

# Replace Sketch Relation Example (VBA)

This example shows how to reassign a sketch relation from one sketch line to another.

```
'--------------------------------------
' Preconditions:
' 1. Verify that the specified part document template
'    exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new part document and inserts a sketch.
' 2. Gets the number of relations, each relation type and
'    number of entities associated with the relation in the
'    sketch.
' 3. Reassigns horizontal constraints.
' 4. Changes the suppression states of all of the relations
'    in the sketch.
' 5. Examine the Immediate window.
'--------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swModelDocExt As SldWorks.ModelDocExtension
    Dim swSketchMgr As SldWorks.SketchManager
    Dim swSketchSegment As SldWorks.SketchSegment
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeat As SldWorks.Feature
    Dim swSketch As SldWorks.Sketch
    Dim swSkRelMgr As SldWorks.SketchRelationManager
    Dim swSkRel As SldWorks.SketchRelation
    Dim vSkRelArr As Variant
    Dim vSkRel As Variant
    Dim i As Long
    Dim boolstatus As Boolean
    Dim result As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2014\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
    swSketchMgr.InsertSketch True
    boolstatus = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    Set swSketchSegment = swSketchMgr.CreateLine(-0.040395, 0.028613, 0#, 0.031793, 0.028613, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(-0.040395, -0.033476, 0#, 0.031793, -0.033476, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(-0.040395, 0.028613, 0#, -0.040395, -0.033476, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(0.031793, 0.028613, 0#, 0.031793, -0.033476, 0#)
    Set swSketchSegment = swSketchMgr.CreateLine(-0.040395, 0.055823, 0#, 0.031793, 0.055823, 0#)
    Set swSketchMgr = swModel.SketchManager
```

```
    swModel.ClearSelection2 True
```

```
    boolstatus = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0, 0, 0, False, 0, Nothing, 0)
    boolstatus = swModelDocExt.SelectByID2("Line1@Sketch1", "EXTSKETCHSEGMENT", -7.85461847389557E-03, 2.86132530120482E-02, 0, True, 0, Nothing, 1)
```

```
    Set swSelMgr = swModel.SelectionManager
    Set swFeat = swSelMgr.GetSelectedObject6(1, -1)
    Set swSketch = swFeat.GetSpecificFeature2
    Set swSkRelMgr = swSketch.RelationManager
    Dim newEntity As Object
    Set newEntity = swSelMgr.GetSelectedObject6(2, -1)
```

```
    Debug.Print "  Feature = " & swFeat.Name
```

```
    vSkRelArr = swSkRelMgr.GetRelations(swAll)
    Dim RelationsCount As Long
    RelationsCount = swSkRelMgr.GetRelationsCount(swAll)
    Debug.Print "  Number of relations = " & RelationsCount
    For Each vSkRel In vSkRelArr
        Set swSkRel = vSkRel
        Debug.Print "    Sketch relation(" & i & ")"
        Debug.Print "      Type = " & swSkRel.GetRelationType
        Dim EntitiesCount As Long
        Dim vEntities As Variant
        EntitiesCount = swSkRel.GetEntitiesCount
        Debug.Print "      Entities count = " & EntitiesCount
```

```
        If (swSkRel.GetRelationType = swConstraintType_e.swConstraintType_HORIZONTAL) Then
            vEntities = swSkRel.GetEntities
            swModel.ClearSelection2 True
            Dim Entity As SldWorks.Entity
            Dim oldEntity As Object
            Dim SketchSeg As SldWorks.SketchSegment
            Dim SketchPt As SldWorks.SketchPoint
            Set Entity = Nothing
            Set SketchSeg = Nothing
            Set SketchPt = Nothing
            On Error Resume Next
            Set oldEntity = vEntities(0)
            result = swSkRel.ReplaceEntity(oldEntity, newEntity)
            Debug.Print "      Sketch entity replaced? " & result
        End If
```

```
        result = swSkRel.Suppressed
        Debug.Print "      Suppressed = " & result
        If (result) Then
            swSkRel.Suppressed = False
        Else
            swSkRel.Suppressed = True
        End If
        Debug.Print "      Suppressed  = " & swSkRel.Suppressed
        i = i + 1
    Next
```

```
End Sub
```
