---
title: "Set User-defined Route Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "routingapi/Set_User-defined_Route_Example_VB.htm"
---

# Set User-defined Route Example (VBA)

This example shows how to:

- set the type of route of the active component to user defined.
- get and set the name and cross-section type of the user-defined route of an active component.

```
'-----------------------------------------------------------------------------
' Preconditions:
' 1. Add SOLIDWORKS Routing as an add-in
'    (in SOLIDWORKS click Tools > Add-Ins > SOLIDWORKS Routing).
' 2. Add the SOLIDWORKS <version> Routing Type Library as a reference
'    (in the IDE select Tools > References).
' 3. In Tools > Options > System Options > Routing > Routing File Locations,
'    add the locations of your SOLIDWORKS Routing files.
' 4. Open an assembly containing a route that has rectangular sections.
' 5. Open an Immediate Window.
'
' Postconditions:
' 1. Sets the active component's route to user defined.
' 2. Gets and sets the active component's user-defined route's
'    name and cross-section type.
' 3. Examine the Immediate window.
'---------------------------------------------------------------------------
```

```
Sub main()
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swRtCompMgr As SWRoutingLib.RoutingComponentManager
Dim crossSectionCompType As Long
Dim compUserDefinedRouteName As String
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swModelDocExt = swModel.Extension
```

```
    Set swRtCompMgr = swModelDocExt.GetRoutingComponentManager
    If swRtCompMgr Is Nothing Then Exit Sub

    'Set the active component's route type to user defined
    swRtCompMgr.SetComponentRouteTypeToCustomProperty (swComponentRouteType_e.swUserDefinedType)
```

```
    ' Get and set the name the user-defined route
    Debug.Print "Name of user-defined route for the active component: "
    compUserDefinedRouteName = swRtCompMgr.GetComponentUserDefinedRouteTypeName
    Debug.Print "  Current: " & crossSectionCompType
    compUserDefinedRouteName = "HVAC"
    swRtCompMgr.SetComponentUserDefinedRouteTypeName (compUserDefinedRouteName)
    Debug.Print "  Modified: " & compUserDefinedRouteName
```

```
    Debug.Print ""
```

```
    ' Get and set the cross-section type for a user-defined route
    Debug.Print "Type of cross section for the user-defined route for the active component: "
    crossSectionCompType = swRtCompMgr.GetComponentCrossSectionType
    Debug.Print "  Current: " & crossSectionCompType
    crossSectionCompType = swComponentCrossSectionType_e.swRectangularCrossSection
    swRtCompMgr.SetComponentCrossSectionType (crossSectionCompType)
    Debug.Print "  Modified: " & crossSectionCompType
```

```
End Sub
```
