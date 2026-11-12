---
title: "Change Visibility of Sketch Block Instances (VB.NET)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Visibility_of_Sketch_Block_Instances_Example_VBNET.htm"
---

# Change Visibility of Sketch Block Instances (VB.NET)

This example shows how to hide and show sketch block instances in a drawing document.

'-------------------------------------------------
' Preconditions:
' 1. Drawing document containing a sketch
' block with one or more sketch block instances is open.
' 2. The sketch block is selected in the FeatureManager design tree.
'
' Postconditions: All sketch block instances are hidden if visible, or
' shown if hidden.
'-------------------------------------------------
Imports SolidWorks.Interop.sldworks
Imports SolidWorks.Interop.swconst
Imports System
Imports System.Diagnostics

Partial Class SolidWorksMacro

Sub Main()

Dim swModelDoc As ModelDoc2
Dim swSelMgr As SelectionMgr
Dim swFeature As Feature
Dim swBlockDefinition As SketchBlockDefinition
Dim blocks As Object
Dim i As Integer

swModelDoc = swApp.**ActiveDoc**
swSelMgr = swModelDoc.**SelectionManager**

' Select block is selected in FeatureManager design tree
swFeature = swSelMgr.**GetSelectedObject6**(1, -1)
If swFeature Is Nothing Then
MsgBox("Select a sketch block in the FeatureManager design tree, then rerun the macro.")
Else
swBlockDefinition = swFeature.**GetSpecificFeature2**
Debug.Print("Feature type : " & swFeature.**GetTypeName2**)
If Not (swBlockDefinition Is Nothing) Then
blocks = swBlockDefinition.**GetInstances**
For i = LBound(blocks) To UBound(blocks)

Dim swBlockInstance As SketchBlockInstance
swBlockInstance = blocks(i)
Debug.Print("Sketch block instance: " & (i + 1))
Debug.Print(" Angle : " & swBlockInstance.**Angle**)
Debug.Print(" Scale : " & swBlockInstance.**Scale2**)

' Hide or show the sketch block instance
Dim status As Long
status = swBlockInstance.**Visible**
Select Case status
Case swAnnotationVisibilityState_e.swAnnotationHidden
swBlockInstance.**Visible** = swAnnotationVisibilityState_e.swAnnotationVisible
Debug.Print(" Was hidden, now visible.")
Case swAnnotationVisibilityState_e.swAnnotationVisible
swBlockInstance.**Visible** = swAnnotationVisibilityState_e.swAnnotationHidden
Debug.Print(" Was visible, now hidden.")
Case swAnnotationVisibilityState_e.swAnnotationHalfHidden
MsgBox("This block is half hidden.")
Case swAnnotationVisibilityState_e.swAnnotationVisibilityUnknown
MsgBox("Failed to determine visibility of this block.")
End Select

Next i
End If

blocks = Nothing

End If

End Sub

''' <summary>
''' The SldWorks swApp variable is pre-assigned for you.
''' </summary>
Public swApp As SldWorks

End Class
