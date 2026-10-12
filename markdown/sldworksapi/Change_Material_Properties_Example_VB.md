---
title: "Change Material Properties Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Change_Material_Properties_Example_VB.htm"
---

# Change Material Properties Example (VBA)

This example shows how to change the color of the selected assembly component.

```
'----------------------------------------------------
' Preconditions:
' 1. Open public_documents\samples\tutorial\api\landing_gear.sldasm.
' 2. Click oleostrut<1> in the FeatureManager design tree.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Changes the color of the selected component to blue.
' 2. Examine the component in the graphics area and
'    the Immediate window.
'
' NOTE: Because this assembly is used elsewhere, do not save
' changes.
'----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swCompModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp As SldWorks.Component2
    Dim vMatProp As Variant
    Dim bRet As Boolean
```

```
    Set swApp = CreateObject("SldWorks.Application")
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent2(1)
```

```
    vMatProp = swComp.MaterialPropertyValues
    If IsEmpty(vMatProp) Then
        ' Empty if no component-level colors specified,
        ' so get from underlying model
        Set swCompModel = swComp.GetModelDoc
        If swCompModel Is Nothing Then
            ' Component is lightweight
            Debug.Print "Selected component is lightweight; exiting macro."
            Exit Sub
        End If
        vMatProp = swCompModel.MaterialPropertyValues
    End If
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Component = " & swComp.Name2 & " (" & swComp.ReferencedConfiguration & ")"
    Debug.Print "    State = " & swComp.GetSuppression
    Debug.Print "    Suppressed = " & swComp.IsSuppressed
    Debug.Print "    Hidden = " & swComp.IsHidden(False)
    Debug.Print "    RGB = [" & vMatProp(0) * 255# & ", " & vMatProp(1) * 255# & ", " & vMatProp(2) * 255# & "]"
    Debug.Print "    Ambient = " & vMatProp(3)
    Debug.Print "    Diffuse = " & vMatProp(4)
    Debug.Print "    Specular = " & vMatProp(5)
    Debug.Print "    Shininess = " & vMatProp(6)
    Debug.Print "    Transparency = " & vMatProp(7)
    Debug.Print "    Emission = " & vMatProp(8)
```

```
    ' Force component color to blue
    vMatProp(0) = 0#
    vMatProp(1) = 0#
    vMatProp(2) = 1#
    swComp.MaterialPropertyValues = vMatProp
```

```
    ' Deselect component to see new color
    swModel.ClearSelection2 True
```

```
End Sub
```
