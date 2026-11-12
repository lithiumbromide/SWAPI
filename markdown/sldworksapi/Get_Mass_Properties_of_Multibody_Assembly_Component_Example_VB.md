---
title: "Get Mass Properties of Multibody Assembly Component Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Get_Mass_Properties_of_Multibody_Assembly_Component_Example_VB.htm"
---

# Get Mass Properties of Multibody Assembly Component Example (VBA)

This example shows how to get the mass properties of a multibody assembly component in which an assembly cut-extrude feature is created.

**NOTES:**

-

  ```vb
  An assembly component, i.e., a part or subassembly, can contain  one or more assembly-level features. Some types of assembly features, e.g., cut extrude, can affect the mass properties. Assembly features are not present in the part or subassembly.
  ```
-

  ```vb
  Mass property values returned are relative to the component origin, not the assembly origin.
  ```

```
'---------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified multibody part document
'    and assembly document template exist.
' 2. Open the Immediate window.
'
' Postconditions:
' 1. Opens the specified multibody part document.
' 2. Creates an assembly using the specified multibody
'    part document.
' 3. Creates an assembly cut-extrude feature.
' 4. Selects the multibody component.
' 5. Gets the mass property values of the multibody
'    component.
' 6. Examine the Immediate window.
'
' NOTE: Because the part is used elsewhere, do not save changes.
'---------------------------------------------------------------
```

```
Option Explicit
```

```
Sub main()
```

```
    Dim swApp As SldWorks.SldWorks
    Dim swModel As SldWorks.ModelDoc2
    Dim swAssembly As SldWorks.AssemblyDoc
    Dim swDocExt As SldWorks.ModelDocExtension
    Dim swMass As SldWorks.MassProperty
    Dim swSelMgr As SldWorks.SelectionMgr
    Dim swComp As SldWorks.Component2
    Dim swSketchMgr As SldWorks.SketchManager
    Dim swSketchSegment As SldWorks.SketchSegment
    Dim swFeatMgr As SldWorks.FeatureManager
    Dim swFeat As SldWorks.Feature
    Dim vBodyArr As Variant
    Dim vBodyInfo as Variant
    Dim vCoM As Variant
    Dim vMoI As Variant
    Dim vPrinAoIx As Variant
    Dim vPrinAoIy As Variant
    Dim vPrinAoIz As Variant
    Dim vPrinMoI As Variant
    Dim bRet As Boolean
    Dim errors As Long
    Dim warnings As Long
```

```
    Set swApp = Application.SldWorks
```

```
    'Open multibody part document and create an assembly
    Set swModel = swApp.OpenDoc6("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt", swDocumentTypes_e.swDocPART, swOpenDocOptions_e.swOpenDocOptions_Silent, "", errors, warnings)
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SolidWorks 2017\templates\Assembly.asmdot", 0, 0, 0)
    Set swAssembly = swModel
    Set swComp = swAssembly.AddComponent5("C:\Users\Public\Documents\SOLIDWORKS\SOLIDWORKS 2018\samples\tutorial\multibody\multi_inter.sldprt", swAddComponentConfigOptions_CurrentSelectedConfig, "", False, "", -9.26777909171506E-05, 0, 4.8904806817518E-05)
```

```
    'Create an assembly cut-extrude feature
    Set swDocExt = swModel.Extension
    Set swSketchMgr = swModel.SketchManager
    Set swFeatMgr = swModel.FeatureManager
    bRet = swDocExt.SelectByID2("", "FACE", -1.95381300573558E-02, 4.49999999998454E-02, -3.03401890568011E-03, False, 0, Nothing, 0)
    swModel.ClearSelection2 True
    Set swSketchSegment = swSketchMgr.CreateCircle(0#, 0#, 0#, 0.002956, -0.004701, 0#)
    swModel.ClearSelection2 True
    bRet = swDocExt.SelectByID2("Arc1", "SKETCHSEGMENT", 0, 0, 0, False, 0, Nothing, 0)
    Set swFeat = swFeatMgr.FeatureCut3(True, False, False, 0, 0, 0.5, 0.00254, False, False, False, False, 1.74532925199433E-02, 1.74532925199433E-02, False, False, False, False, False, True, True, True, True, False, 0, 0, False)
    Set swSelMgr = swModel.SelectionManager
    swSelMgr.EnableContourSelection = False
```

```
    'Select multibody component
    bRet = swDocExt.SelectByID2("multi_inter-1@Assem1", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)

    Set swMass = swDocExt.CreateMassProperty
    Set swComp = swSelMgr.GetSelectedObjectsComponent4(1, -1)
```

```
    vBodyArr = swComp.GetBodies3(swSolidBody, vBodyInfo)
    bRet = swMass.AddBodies((vBodyArr))
```

```
    'Get mass properties of selected component's bodies
    vCoM = swMass.CenterOfMass
    vMoI = swMass.GetMomentOfInertia(swMassPropertyMomentAboutCenterOfMass)
    vPrinAoIx = swMass.PrincipleAxesOfInertia(0)
    vPrinAoIy = swMass.PrincipleAxesOfInertia(1)
    vPrinAoIz = swMass.PrincipleAxesOfInertia(2)
    vPrinMoI = swMass.PrincipleMomentsOfInertia
    Debug.Print "Component = " & swComp.Name2
    Debug.Print "Configuration = " & swComp.ReferencedConfiguration
    Debug.Print "Density = " & swMass.Density & " kg/m^3"
    Debug.Print ""
    Debug.Print "Center of mass = (" & vCoM(0) * 1000# & ", " & vCoM(1) * 1000# & ", " & vCoM(2) * 1000# & ") mm"
    Debug.Print "Volume = " & swMass.Volume * 1000000000# & " mm^3"
    Debug.Print "Area = " & swMass.SurfaceArea * 1000000# & " mm^2"
    Debug.Print "Mass = " & swMass.Mass & " kg"
    Debug.Print "Principle axes of inertia "
    Debug.Print "  Ix = (" & vPrinAoIx(0) & ", " & vPrinAoIx(1) & ", " & vPrinAoIx(2) & ")"
    Debug.Print "  Iy = (" & vPrinAoIy(0) & ", " & vPrinAoIy(1) & ", " & vPrinAoIy(2) & ")"
    Debug.Print "  Iz = (" & vPrinAoIz(0) & ", " & vPrinAoIz(1) & ", " & vPrinAoIz(2) & ")"
    Debug.Print "Principle moments of inertia"
    Debug.Print "  Px = " & vPrinMoI(0) & " kg*m^2"
    Debug.Print "  Py = " & vPrinMoI(1) & " kg*m^2"
    Debug.Print "  Pz = " & vPrinMoI(2) & " kg*m^2"
    Debug.Print "Products of inerita"
    Debug.Print "  Lxx = " & vMoI(0) & " kg*m^2"
    Debug.Print "  Lxy = " & vMoI(1) & " kg*m^2"
    Debug.Print "  Lxz = " & vMoI(2) & " kg*m^2"
    Debug.Print "  Lyx = " & vMoI(3) & " kg*m^2"
    Debug.Print "  Lyy = " & vMoI(4) & " kg*m^2"
    Debug.Print "  Lyz = " & vMoI(5) & " kg*m^2"
    Debug.Print "  Lzx = " & vMoI(6) & " kg*m^2"
    Debug.Print "  Lzy = " & vMoI(7) & " kg*m^2"
    Debug.Print "  Lzz = " & vMoI(8) & " kg*m^2"
```

```
End Sub
```
