---
title: "Change Visibility of Sketch Block Instances (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Visibility_of_Sketch_Block_Instances_Example_VB.htm"
---

# Change Visibility of Sketch Block Instances (VBA)

This example shows how to hide and show sketch block instances in a drawing document.

```
'-------------------------------------------------
' Preconditions:
' 1. Drawing document containing a sketch
'    block with one or more sketch block instances is open.
' 2. The sketch block is selected in the FeatureManager design tree.
'
' Postconditions: All sketch block instances are hidden if visible, or
' shown if hidden.
'-------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModelDoc As SldWorks.ModelDoc2
Dim swSelMgr As SldWorks.SelectionMgr
Dim swFeature As SldWorks.Feature
Dim swBlockDefinition As SldWorks.SketchBlockDefinition
Dim blocks As Variant
Dim i As Long
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
Set swModelDoc = swApp.ActiveDoc
Set swSelMgr = swModelDoc.SelectionManager
```

```
' Select block is selected in FeatureManager design tree
Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
If swFeature Is Nothing Then
    MsgBox ("Select a sketch block in the FeatureManager design tree, then rerun the macro.")
Else
    Set swBlockDefinition = swFeature.GetSpecificFeature2
    Debug.Print "Feature type : " & swFeature.GetTypeName2
    If Not (swBlockDefinition Is Nothing) Then
        blocks = swBlockDefinition.GetInstances
        For i = LBound(blocks) To UBound(blocks)
```

```
            Dim swBlockInstance As SldWorks.SketchBlockInstance
            Set swBlockInstance = blocks(i)
            Debug.Print "Sketch block instance: " & (i + 1)
            Debug.Print "  Angle : " & swBlockInstance.Angle
            Debug.Print "  Scale : " & swBlockInstance.Scale2
```

```
            ' Hide or show the sketch block instance
            Dim status As Long
            status = swBlockInstance.Visible
            Select Case status
                Case swAnnotationHidden
                    swBlockInstance.Visible = swAnnotationVisible
                    Debug.Print "  Was hidden, now visible."
                Case swAnnotationVisible
                    swBlockInstance.Visible = swAnnotationHidden
                    Debug.Print "  Was visible, now hidden."
                Case swAnnotationHalfHidden
                    MsgBox ("This block is half hidden.")
                Case swAnnotationVisibilityUnknown
                    MsgBox ("Failed to determine visibility of this block.")
            End Select
```

```
        Next i
    End If
```

```
    blocks = Empty
```

```
End If
```

```
End Sub
```
