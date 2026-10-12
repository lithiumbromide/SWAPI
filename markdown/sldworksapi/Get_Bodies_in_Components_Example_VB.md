---
title: "Get Bodies in Components Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Bodies_in_Components_Example_VB.htm"
---

# Get Bodies in Components Example (VBA)

This example shows how to get the number of normal and user bodies in the components in an assembly.

```
'-----------------------------------------------------
' Preconditions:
' 1. Verify that the specified assembly document
'    to open exists.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Gets and prints each component's name, number of
'    solid bodies, body names, and body types
'    to the Immediate window.
' 2. Right-click filterholder<1> in the FeatureManager
'    design tree and click the Open Part button.
'    Notice that there are no screw holes in the part.
' 3. Close the part and examine the filterholder<1>
'    component, which is the orange, flat, circular
'    component located on the front of the assembly
'    in the graphics area. There are screw
'    holes in the component.
' 4. Examine the filterholder<1>'s information in the
'    Immediate window. Because the component was
'    modified in the assembly, its body is identified
'    as a user body.
'
' NOTE: Because this assembly document is used by
' elsewhere, do not save changes.
'-----------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As ModelDoc2
Dim swAssembly As SldWorks.AssemblyDoc
Dim vComponents As Variant
Dim oneComponent As Component2
Dim vBodies As Variant
Dim vBodyInfo As Variant
Dim errors As Long, warnings As Long
Dim i As Long, j As Long
```

```
Sub main()
```

```
Set swApp = Application.SldWorks
```

```
    ' Open the assembly
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\toolbox\lens_mount.sldasm", swDocASSEMBLY, swOpenDocOptions_Silent, "", errors, warnings)
    Set swAssembly = swModel
```

```
    ' Get the components in the assembly
    vComponents = swAssembly.GetComponents(True)
    For i = 0 To UBound(vComponents)
        Set oneComponent = vComponents(i)
        Debug.Print " "
            Debug.Print "Component name: " & oneComponent.Name2
        ' Get the solid bodies in the component
        vBodies = oneComponent.GetBodies3(SwConst.swBodyType_e.swSolidBody, vBodyInfo)
        Debug.Print "  Number of solid bodies: " & (UBound(vBodies) + 1)
        For j = 0 To UBound(vBodies)
            Debug.Print "  Body number: " & (j + 1)
            Debug.Print "  Body name: " & vBodies(j).Name
            ' Print the type of body
                Select Case vBodyInfo(j)
                Case 0
                  Debug.Print "  Body type: user"
                Case 1
                  Debug.Print "  Body type: normal"
            End Select
        Next
    Next
```

```
End Sub
```
