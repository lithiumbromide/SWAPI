---
title: "Get Corresponding Objects in Assembly Component Example (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Corresponding_Objects_in_Assembly_Component_Example_VBNET.htm"
---

# Get Corresponding Objects in Assembly Component Example (VB.NET)

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
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System.Runtime.InteropServices
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

    Public Sub main()

        Dim swModel As ModelDoc2
        Dim swAssembly As AssemblyDoc
        Dim swComponent As Component2
        Dim swSketchManager As SketchManager
        Dim swSketchSegment As SketchSegment
        Dim swNote As Note
        Dim swAnnotation As Annotation
        Dim swTextFormat As TextFormat
        Dim swModelDocExt As ModelDocExtension
        Dim swFeature As Feature
        Dim swSketch As Sketch
        Dim swSketchContour As SketchContour = Nothing
        Dim swSelectionMgr As SelectionMgr
        Dim swObject As Object
        Dim sketchSegments() As Object
        Dim sketchContours() As Object
        Dim nbrSketchContours As Integer
        Dim nbrSketchSegments As Integer
        Dim sketchSegmentIDs() As Integer
        Dim sketchSegmentType As Integer
        Dim annotationID As Integer
        Dim annotationType As Integer
        Dim status As Boolean
        Dim errors As Integer
        Dim warnings As Integer
        Dim i As Integer
        Dim j As Integer

        'Create sketch containing a sketch arc,
        'sketch line, and annotation
        swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Part.prtdot", 0, 0, 0)
        swSketchManager = swModel.SketchManager
        swSketchSegment = swSketchManager.CreateArc(-0.0756, 0.0#, 0.0#, -0.020568, 0.0#, 0.0#, -0.130614, 0.001423, 0.0#, 1)
        swSketchSegment = swSketchManager.CreateLine(-0.130614, 0.001423, 0.0#, -0.0756, -0.047042, 0.0#)
        swNote = swModel.InsertNote("This is a sketch segment")
        If Not swNote Is Nothing Then
            swNote.LockPosition = False
            swNote.Angle = 0
            status = swNote.SetBalloon(0, 0)
            swAnnotation = swNote.GetAnnotation()
            If Not swAnnotation Is Nothing Then
                errors = swAnnotation.SetLeader3(swLeaderStyle_e.swUNDERLINED, 0, True, False, False, False)
                status = swAnnotation.SetPosition2(-0.002501468059071, 0.0826874163970699, 0)
                swTextFormat = Nothing
                status = swAnnotation.SetTextFormat(0, True, swTextFormat)
            End If
        End If
        swModel.ClearSelection2(True)
        swModel.WindowRedraw()
        swSketchManager.InsertSketch(True)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SaveAs("C:\test\Part1.SLDPRT", swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)

        'Save part as assembly
        swAssembly = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2016\templates\Assembly.asmdot", 0, 0, 0)
        swComponent = swAssembly.AddComponent5("C:\test\Part1.SLDPRT", swAddComponentConfigOptions_e.swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -0.0000160609059776107, 0, 0.00000847512097834624)
        swModel = swAssembly
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SaveAs("C:\test\Assem1.SLDASM", swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)

        'Get persistent reference IDs of sketch segments in sketch contour in part
        swModel = swApp.ActivateDoc3("Part1.SLDPRT", False, swRebuildOnActivation_e.swRebuildActiveDoc, errors)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Sketch1", "SKETCH", 0.0#, 0.0#, 0.0#, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swFeature = swSelectionMgr.GetSelectedObject6(1, -1)
        swSketch = swFeature.GetSpecificFeature2()
        Debug.Print(swModel.GetPathName)
        Debug.Print("")
        If Not swSketch Is Nothing Then
            sketchContours = swSketch.GetSketchContours()
            nbrSketchContours = UBound(sketchContours) - LBound(sketchContours) + 1
            Debug.Print("  Number of sketch contours in " & swFeature.Name & " = " & nbrSketchContours)
            For i = LBound(sketchContours) To UBound(sketchContours)
                swSketchContour = sketchContours(i)
                If Not swSketchContour Is Nothing Then
                    status = swSketchContour.Select2(False, Nothing)
                End If
                sketchSegments = swSketchContour.GetSketchSegments()
                nbrSketchSegments = UBound(sketchSegments) - LBound(sketchSegments) + 1
                For j = LBound(sketchSegments) To UBound(sketchSegments)
                    swSketchSegment = sketchSegments(j)
                    If Not swSketchSegment Is Nothing Then
                        sketchSegmentIDs = swSketchSegment.GetID
                        sketchSegmentType = swSketchSegment.GetType
                        Debug.Print("  Persistent IDs = [" & sketchSegmentIDs(0) & ", " & sketchSegmentIDs(1) & "] and type = " & sketchSegmentType & " (0 = line; 1 = arc)")
                    End If
                Next
            Next
        End If

        'Get object ID of note annotation in part
        status = swModelDocExt.SelectByID2("DetailItem1@Annotations", "NOTE", -0.00650517330771608, 0.0568327787544409, -0.035178659814812, False, 0, Nothing, 0)
        swNote = swSelectionMgr.GetSelectedObject6(1, -1)
        swAnnotation = swNote.GetAnnotation
        annotationType = swAnnotation.GetType
        annotationID = swModelDocExt.GetObjectId(swAnnotation)
        Debug.Print("")
        Debug.Print("  Annotation ID = " & annotationID & " and type = " & annotationType & " (6 = note)")

        'Activate the assembly
        swModel = swApp.ActivateDoc3("Assem1.SLDASM", False, swRebuildOnActivation_e.swRebuildActiveDoc, errors)
        swModelDocExt = swModel.Extension
        status = swModelDocExt.SelectByID2("Part1-1@Assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
        swSelectionMgr = swModel.SelectionManager
        swComponent = swSelectionMgr.GetSelectedObject6(1, -1)
        Debug.Print("")
        Debug.Print(swModel.GetPathName)
        Debug.Print("")

        'Get corresponding sketch contour and sketch segments
        'and their persistent reference IDs in component
        swObject = swComponent.GetCorresponding(swSketchContour)
        swSketchContour = Nothing
        swSketchContour = swObject
        If Not swSketchContour Is Nothing Then
            status = swSketchContour.Select2(False, Nothing)
        End If
        sketchSegments = swSketchContour.GetSketchSegments()
        Debug.Print("  Number of sketch contours in " & swFeature.Name & " = " & nbrSketchContours)
        nbrSketchSegments = UBound(sketchSegments) - LBound(sketchSegments) + 1
        For j = 0 To UBound(sketchSegments)
            swSketchSegment = sketchSegments(j)
            If Not swSketchSegment Is Nothing Then
                sketchSegmentIDs = swSketchSegment.GetID
                sketchSegmentType = swSketchSegment.GetType
                Debug.Print("  Persistent IDs = [" & sketchSegmentIDs(0) & ", " & sketchSegmentIDs(1) & "] and type = " & sketchSegmentType & " (0 = line; 1 = arc)")
            End If
        Next

        'Get object ID of corresponding note annotation in component
        swObject = swComponent.GetCorresponding(swNote)
        swNote = Nothing
        swNote = swObject
        If Not swNote Is Nothing Then
            swAnnotation = swNote.GetAnnotation
            annotationType = swAnnotation.GetType
            annotationID = swModelDocExt.GetObjectId(swAnnotation)
            Debug.Print("")
            Debug.Print("  Annotation ID = " & annotationID & " and type = " & annotationType & " (6 = note)")
        End If

    End Sub

    ''' <summary>
    ''' The SldWorks swApp variable is pre-assigned for you.
    ''' </summary>
    Public swApp As SldWorks

End Class
```
