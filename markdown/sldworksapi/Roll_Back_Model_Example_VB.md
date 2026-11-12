---
title: "Roll Back Model Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Roll_Back_Model_Example_VB.htm"
---

# Roll Back Model Example (VBA)

This example shows how to step through the FeatureManager design tree of a model by rolling back to each feature in reverse sequence. Running an example like this can provide insight into the design intent of the user.

```
'-----------------------------------
' Preconditions:
' 1. Open a part or assembly document.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Observe the FeatureManager design tree
'    while the macro executes.
' 2. Examine the Immediate window to see the
'    names of the features rolled back and forward.
'
' NOTE: The delay between steps is set to 1 second.
'-----------------------------------
```

```
Option Explicit
```

```
Sub Main()
```

```
    ' Delay in seconds
    Const DELAY                     As Single = 1#
```

```
    Dim swApp                       As SldWorks.SldWorks
    Dim swModel                     As SldWorks.ModelDoc2
    Dim swModelView                 As SldWorks.ModelView
    Dim swPart                      As SldWorks.PartDoc
    Dim swAssy                      As SldWorks.AssemblyDoc
    Dim swFeatMgr                   As SldWorks.FeatureManager
    Dim swFeat                      As SldWorks.Feature
    Dim featFace                    As Variant
    Dim swFace                      As SldWorks.Face2
    Dim rect                        As Variant
    Dim featName()                  As String
    Dim timeNow                     As Single
    Dim docType                     As Long
    Dim i                           As Long
    Dim j                           As Long
    Dim status                      As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelView = swModel.ActiveView
    Set rect = Nothing
    Set swFeatMgr = swModel.FeatureManager
    Set swFeat = swModel.FirstFeature
```

```
    docType = swModel.GetType
    Select Case docType
        Case swDocPART
            Set swPart = swModel
        Case swDocASSEMBLY
            Set swAssy = swModel
        Case Else
            Debug.Print "Open a part or assembly document, then rerun this macro."
            Exit Sub
    End Select
```

```
    ReDim featName(0)
```

```
    Do While Not swFeat Is Nothing
        featName(UBound(featName)) = swFeat.Name
        ReDim Preserve featName(UBound(featName) + 1)
        Set swFeat = swFeat.GetNextFeature
    Loop
```

```
    ' Loop over-allocates array by 1, so remove last (empty) entry
    ReDim Preserve featName(UBound(featName) - 1)
```

```
    ' Playback each feature in the FeatureManager design tree
    For i = 0 To UBound(featName)
        Debug.Print featName(i)
        status = swFeatMgr.EditRollback(swMoveRollbackBarToAfterFeature, featName(i))
```

```
        ' Do not assert because you may be trying to roll back or roll forward
        ' to a feature that cannot be rolled back or forward to; for example,
        ' the Lighting or Annotations folder
```

```
        'Debug.Assert status
```

```
        ' Remove any previous highlights
        swModelView.GraphicsRedraw (rect)
```

```
        ' Highlight feature if it has any geometry
        Select Case docType
            Case swDocPART
                Set swFeat = swPart.FeatureByName(featName(i))
            Case swDocASSEMBLY
                Set swFeat = swAssy.FeatureByName(featName(i))
        End Select
```

```
        featFace = swFeat.GetFaces
        If Not IsEmpty(featFace) Then
            For j = 0 To UBound(featFace)
                Set swFace = featFace(j)
                swFace.Highlight True
            Next j
        End If
```

```
        ' Only pause if rollback is successful
        If status Then
            timeNow = Timer
            While timeNow + DELAY > Timer
                ' Allow SOLIDWORKS Design to refresh screen
                DoEvents
            Wend
        End If
    Next i
```

```
    ' Remove highlight from last feature
    swModelView.GraphicsRedraw (rect)
```

```
End Sub
```
