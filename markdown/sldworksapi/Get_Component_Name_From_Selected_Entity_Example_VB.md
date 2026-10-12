---
title: "Get Component Name From Selected Entity Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Component_Name_From_Selected_Entity_Example_VB.htm"
---

# Get Component Name From Selected Entity Example (VBA)

This example shows how to get the name of a component to possibly use with a future call to [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html), when selectively opening the assembly document and specific components using [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.html) and [IDocumentSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.html), etc. This example also shows how to set and get a component reference.

```
'--------------------------------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Select an entity (face, edge, vertex, or loop) on any
'    component in the graphics area.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Adds a component reference to the component to which the
'    entity belongs.
' 2. Examine the Immediate window.
' 3. Locate the component to which the component reference was added
'    in the FeatureManager design tree. If necessary, use the scrollbar
'    at the bottom of the FeatureManager design tree to see the component
'    reference.
'--------------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swEntity As SldWorks.Entity
Dim swComponent As SldWorks.Component2
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
```

```
    ' Get the selected entity (i.e., face, edge, vertex, or loop)
    ' and get the name of its component
    Set swSelectionMgr = swModel.SelectionManager
    Set swEntity = swSelectionMgr.GetSelectedObject6(1, -1)
    Set swComponent = swEntity.GetComponent
```

```
    ' Print the name of the component to which the
    ' the selected entity belongs
    Debug.Print "Name of component to which the selected entity belongs: " & swComponent.GetSelectByIDString
```

```
    ' Set a component reference to this component
    swComponent.ComponentReference = "TestComponentReference"
    Debug.Print "Component reference added to the component to which the selected entity belongs: " & swComponent.ComponentReference
```

```
    ' Rebuild the assembly to see the component reference
    ' beside the name of the component in the FeatureManager design
    ' tree
    swModel.ForceRebuild3 True
```

```
End Sub
```
