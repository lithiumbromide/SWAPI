---
title: "Get Corresponding Objects in Assembly Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corresponding_Objects_in_Assembly_Component_Example_VB.htm"
---

# Get Corresponding Objects in Assembly Component Example (VBA)

This example shows how to get the corresponding sketch contour, sketch segments, and annotation for a component in the context of the assembly.

```
'------------------------------------------------------------------
' Preconditions:
' 1. Verify that:
'    * specified part and assembly templates
'    * C:\test
'    exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens a new part and creates a sketch containing
'    a sketch arc, sketch line, and a note.
' 2. Saves the part as C:\test\part1.sldprt.
' 3. Makes an assembly using the part document and saves
'    the assembly as C:\test\assem1.sldasm.
' 4. Activates the part.
'    a. Gets the persistent reference IDs of the sketch segments
'       in the sketch contour.
'    b. Gets the object ID of the note annotation.
' 5. Activates the assembly.
'    a. Gets the persistent reference IDs of the sketch
'       segments in the sketch contour in the context
'       of the assembly.
'    b. Gets the object ID of the note annotation in the context
'       of the assembly.
' 6. Examine the Immediate window.
'------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swAssembly As SldWorks.AssemblyDoc
Dim swComponent As SldWorks.Component2
Dim swSketchManager As SldWorks.SketchManager
Dim swSketchSegment As SldWorks.SketchSegment
Dim swNote As SldWorks.Note
Dim swAnnotation As SldWorks.Annotation
Dim swTextFormat As SldWorks.TextFormat
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swFeature As SldWorks.Feature
Dim swSketch As SldWorks.Sketch
Dim swSketchContour As SldWorks.SketchContour
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swObject As Object
Dim sketchSegments As Variant
Dim sketchContours As Variant
Dim nbrSketchContours As Long
Dim nbrSketchSegments As Long
Dim sketchSegmentIDs As Variant
Dim sketchSegmentType As Long
Dim annotationID As Long
Dim annotationType As Long
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim i As Long
Dim j As Long
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Create sketch containing a sketch arc,
    'sketch line, and annotation
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Part.prtdot", 0, 0, 0)
    Set swSketchManager = swModel.SketchManager
    Set swSketchSegment = swSketchManager.CreateArc(-0.0756, 0#, 0#, -0.020568, 0#, 0#, -0.130614, 0.001423, 0#, 1)
    Set swSketchSegment = swSketchManager.CreateLine(-0.130614, 0.001423, 0#, -0.0756, -0.047042, 0#)
    Set swNote = swModel.InsertNote("This is a sketch segment")
    If Not swNote Is Nothing Then
       swNote.LockPosition = False
       swNote.Angle = 0
       status = swNote.SetBalloon(0, 0)
       Set swAnnotation = swNote.GetAnnotation()
       If Not swAnnotation Is Nothing Then
          errors = swAnnotation.SetLeader3(swLeaderStyle_e.swUNDERLINED, 0, True, False, False, False)
          status = swAnnotation.SetPosition2(-0.002501468059071, 8.26874163970699E-02, 0)
          status = swAnnotation.SetTextFormat(0, True, swTextFormat)
       End If
    End If
    swModel.ClearSelection2 True
    swModel.WindowRedraw
    swSketchManager.InsertSketch True
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SaveAs("C:\test\Part1.SLDPRT", swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)
```

```
    'Save part as assembly
    Set swAssembly = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Assembly.asmdot", 0, 0, 0)
    Set swComponent = swAssembly.AddComponent5("C:\test\Part1.SLDPRT", swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -1.60609059776107E-05, 0, 8.47512097834624E-06)
    Set swModel = swAssembly
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SaveAs("C:\test\Assem1.SLDASM", swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)
```

```
    'Get persistent reference IDs of sketch segments in sketch contour in part
    Set swModel = swApp.ActivateDoc3("Part1.SLDPRT", False, swRebuildOnActivation_e.swRebuildActiveDoc, errors)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0#, 0#, 0#, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swSketch = swFeature.GetSpecificFeature2()
    Debug.Print swModel.GetPathName
    Debug.Print ""
    If Not swSketch Is Nothing Then
        sketchContours = swSketch.GetSketchContours()
        nbrSketchContours = UBound(sketchContours) - LBound(sketchContours) + 1
        Debug.Print "  Number of sketch contours in " & swFeature.Name & " = " & nbrSketchContours
        For i = LBound(sketchContours) To UBound(sketchContours)
            Set swSketchContour = sketchContours(i)
            If Not swSketchContour Is Nothing Then
                status = swSketchContour.Select2(False, Nothing)
            End If
            sketchSegments = swSketchContour.GetSketchSegments()
            nbrSketchSegments = UBound(sketchSegments) - LBound(sketchSegments) + 1
                For j = LBound(sketchSegments) To UBound(sketchSegments)
                    Set swSketchSegment = sketchSegments(j)
                    If Not swSketchSegment Is Nothing Then
                        sketchSegmentIDs = swSketchSegment.GetID
                        sketchSegmentType = swSketchSegment.GetType
                        Debug.Print "  Persistent IDs = [" & sketchSegmentIDs(0) & ", " & sketchSegmentIDs(1) & "] and type = " & sketchSegmentType & " (0 = line; 1 = arc)"
                    End If
                Next
         Next
    End If
```

```
    'Get object ID of note annotation in part
    status = swModelDocExt.SelectByID2("DetailItem1@Annotations", "NOTE", -6.50517330771608E-03, 5.68327787544409E-02, -0.035178659814812, False, 0, Nothing, 0)
    Set swNote = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swAnnotation = swNote.GetAnnotation
    annotationType = swAnnotation.GetType
    annotationID = swModelDocExt.GetObjectId(swAnnotation)
    Debug.Print ""
    Debug.Print "  Annotation ID = " & annotationID & " and type = " & annotationType & " (6 = note)"
```

```
    'Activate the assembly
    Set swModel = swApp.ActivateDoc3("Assem1.SLDASM", False, swRebuildOnActivation_e.swRebuildActiveDoc, errors)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Part1-1@Assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swSelectionMgr = swModel.SelectionManager
    Set swComponent = swSelectionMgr.GetSelectedObject6(1, -1)
    Debug.Print ""
    Debug.Print swModel.GetPathName
    Debug.Print ""
    'Get corresponding sketch contour and sketch segments
    'and their persistent reference IDs in component
    Set swObject = swComponent.GetCorresponding(swSketchContour)
    Set swSketchContour = Nothing
    Set swSketchContour = swObject
    If Not swSketchContour Is Nothing Then
        status = swSketchContour.Select2(False, Nothing)
    End If
    sketchSegments = swSketchContour.GetSketchSegments()
    Debug.Print "  Number of sketch contours in " & swFeature.Name & " = " & nbrSketchContours
    nbrSketchSegments = UBound(sketchSegments) - LBound(sketchSegments) + 1
    For j = 0 To UBound(sketchSegments)
        Set swSketchSegment = sketchSegments(j)
        If Not swSketchSegment Is Nothing Then
            sketchSegmentIDs = swSketchSegment.GetID
            sketchSegmentType = swSketchSegment.GetType
            Debug.Print "  Persistent IDs = [" & sketchSegmentIDs(0) & ", " & sketchSegmentIDs(1) & "] and type = " & sketchSegmentType & " (0 = line; 1 = arc)"
        End If
    Next
```

```
    'Get object ID of corresponding note annotation in component
    Set swObject = swComponent.GetCorresponding(swNote)
    Set swNote = Nothing
    Set swNote = swObject
    If Not swNote Is Nothing Then
        Set swAnnotation = swNote.GetAnnotation
        annotationType = swAnnotation.GetType
        annotationID = swModelDocExt.GetObjectId(swAnnotation)
        Debug.Print ""
        Debug.Print "  Annotation ID = " & annotationID & " and type = " & annotationType & " (6 = note)"
    End If

End Sub
```
