---
title: "Get Mass Properties of Assembly Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_of_Assembly_Component_Example_VB.htm"
---

# Get Mass Properties of Assembly Component Example (VBA)

An assembly component (part or sub-assembly) can contain assembly-level features, typically cuts. These features affect the mass properties, but the features are not present in the part or sub-assembly.

This example shows to get the mass properties of an assembly component.

```
'----------------------------------------------------
' Preconditions:
' 1. Open an assembly document.
' 2. Select a component,
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Gets the mass properties of the selected component
' 2. Examine the Immediate window.
'
' NOTE: The mass property values are returned relative to
' the component origin, not the assembly origin.
'----------------------------------------------------
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp As SldWorks.Component2
    Dim swCompModel As SldWorks.ModelDoc2
    Dim swCompBody As SldWorks.Body2
    Dim vMassProps As Variant
    Dim nDensity As Double
    Dim bRet As Boolean
```

```
    Set swApp = Application.SldWorks
    Set swModel = swApp.ActiveDoc
    Set swSelMgr = swModel.SelectionManager
    Set swComp = swSelMgr.GetSelectedObjectsComponent3(1, 0)
```

```
    Set swCompBody = swComp.GetBody
    Set swCompModel = swComp.GetModelDoc
```

```
    ' Calculate component material density
    nDensity = swCompModel.GetUserPreferenceDoubleValue(swMaterialPropertyDensity)
```

```
    ' Use this method to get component mass properties
    vMassProps = swCompBody.GetMassProperties(nDensity)
```

```
    Debug.Print "File = " & swModel.GetPathName
    Debug.Print "  Comp     = " & swComp.Name2
    Debug.Print "  Config   = " & swComp.ReferencedConfiguration
    Debug.Print "  Density  = " & nDensity & " kg/m^3"
    Debug.Print ""
    Debug.Print "  CenterOfMass = (" & vMassProps(0) * 1000# & ", " & vMassProps(1) * 1000# & ", " & vMassProps(2) * 1000# & ") mm"
    Debug.Print "  Volume       = " & vMassProps(3) * 1000000000# & " mm^3"
    Debug.Print "  Area         = " & vMassProps(4) * 1000000# & " mm^2"
    Debug.Print "  Mass         = " & vMassProps(5) & " kg"
    Debug.Print "  MomXX        = " & vMassProps(6) & " kg*m^2"
    Debug.Print "  MomYY        = " & vMassProps(7) & " kg*m^2"
    Debug.Print "  MomZZ        = " & vMassProps(8) & " kg*m^2"
    Debug.Print "  MomXY        = " & vMassProps(9) & " kg*m^2"
    Debug.Print "  MomZX        = " & vMassProps(10) & " kg*m^2"
    Debug.Print "  MomYZ        = " & vMassProps(11) & " kg*m^2"
```

```
End Sub
```
