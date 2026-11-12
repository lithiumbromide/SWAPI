---
title: "Get Temporary Axis and Its Reference Face Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Temporary_Axis_and_Its_Reference_Face_Example_VB.htm"
---

# Get Temporary Axis and Its Reference Face Example (VBA)

This example shows how to get a temporary axis and its reference face.

```
'---------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\box.sldprt.
' 2. Click View > Hide/Show > Temporary Axes.
' 3. Select the temporary axis.
' 4. Open the Immediate window.
'
' Postconditions:
' 1. Gets whether the selected entity is a temporary
'    axis.
' 2. Gets the reference face of the temporary axis.
' 3. Examine the Immediate window and graphics area.
'
' NOTE: Because the part is used elsewhere, do not save
' changes.
'---------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swFeature As SldWorks.Feature
    Dim swEntity As SldWorks.Entity
    Dim swRefAxis  As SldWorks.RefAxis
    Dim obj As Object
    Dim swFace As SldWorks.Face2
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    'Get selected entity
    Set swSelMgr = swModel.SelectionManager
    Set swFeature = swSelMgr.GetSelectedObject6(1, -1)
    Set swEntity = swFeature
```

```
    If swEntity.GetType = swSelectType_e.swSelDATUMAXES Then
        Set swRefAxis = swFeature.GetSpecificFeature2
        'Get whether selected entity is a temporary axis
        If swRefAxis.IsTempAxis Then
            Debug.Print "Is temporary reference axis"
            'Get reference face of temporary axis
            Set obj = swRefAxis.GetTempAxisReferenceFace
            If Not obj Is Nothing Then
                Debug.Print "  Got reference face of temporary axis"
                Set swFace = obj
                swFace.Highlight (True)
                Debug.Print "  Highlighted reference face of temporary axis; examine the graphics area"
            Else
                Debug.Print "Did not get reference face of temporary axis"
            End If
        Else
            Debug.Print "Not a temporary axis"
        End If
    Else
        Debug.Print "Select a temporary axis and run the macro again"
    End If
```

```
End Sub
```
