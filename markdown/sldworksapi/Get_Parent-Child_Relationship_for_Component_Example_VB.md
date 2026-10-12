---
title: "Get Parent-Child Relationship for Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Parent-Child_Relationship_for_Component_Example_VB.htm"
---

# Get Parent-Child Relationship for Component Example (VBA)

This example shows how to get the parent-child relationship for an assembly component.

```
'------------------------------------------------------------
' Preconditions:
' 1. Open an assembly.
' 2. Select a component that is not in a subassembly.
'    NOTE: This example does not support selections in
'    subassemblies, because the selected component in
'    a subassembly is not a feature in the top-level assembly.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the parent-child relationship for the selected
'    component.
' 2. Examine the Immediate window.
'------------------------------------------------------------
Option Explicit
```

```
Sub ProcessFeature(swApp As SldWorks.SldWorks, swModel As SldWorks.ModelDoc2, swFeat As SldWorks.Feature)
```

```
    Dim vParentArr As Variant
    Dim vParent As Variant
    Dim swParentFeat As SldWorks.Feature
    Dim vChildArr As Variant
    Dim vChild As Variant
    Dim swChildFeat As SldWorks.Feature
    Dim i As Long
```

```
    vParentArr = swFeat.GetParents
    vChildArr = swFeat.GetChildren
```

```
    Debug.Print "  Feature name = " + swFeat.Name + " [" + swFeat.GetTypeName + "]"
```

```
    If Not IsEmpty(vParentArr) Then
        Debug.Print "    Parents:"
        For Each vParent In vParentArr
        Set swParentFeat = vParent
            Debug.Print "      " + swParentFeat.Name + " [" + swParentFeat.GetTypeName + "]"
        Next vParent
    End If
```

```
    If Not IsEmpty(vChildArr) Then
        Debug.Print "    Children:"
        For Each vChild In vChildArr
            Set swChildFeat = vChild
            Debug.Print "      " + swChildFeat.Name + " [" + swChildFeat.GetTypeName + "]"
        Next vChild
    End If
```

```
End Sub
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssy As SldWorks.AssemblyDoc
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp As SldWorks.Component2
    Dim swFeat As SldWorks.Feature
    Dim i As Long
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swAssy = swModel
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
    Set swFeat = swAssy.FeatureByName(swComp.Name2): Debug.Assert Not swFeat Is Nothing
```

```
    Debug.Print "File = " & swModel.GetPathName
```

```
    ProcessFeature swApp, swModel, swFeat
```

```
End Sub
```
