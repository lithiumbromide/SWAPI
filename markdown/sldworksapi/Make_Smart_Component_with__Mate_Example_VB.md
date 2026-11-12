---
title: "Make Smart Component with Mate Example (VBA)"
project: ""
interface: ""
member: ""
kind: "example"
source: "sldworksapi/Make_Smart_Component_with__Mate_Example_VB.htm"
---

# Make Smart Component with Mate Example (VBA)

This example shows how to create a Smart Component with a concentric mate reference.

```
'----------------------------------------------------------------
' Preconditions:
' 1. Verify that the specified part and assembly templates exist.
' 2. Verify that C:\temp exists.
' 3. Open the Immediate window.
'
' Postconditions:
' 1. Creates a new part.
' 2. Creates a new assembly using the part as a component.
' 3. Adds two more instances of the part as components.
' 4. Creates a Smart Component with a concentric mate reference.
' 5. Examine the Immediate window and FeatureManager design tree.
'----------------------------------------------------------------
Option Explicit
```

```
Dim swApp As SldWorks.SldWorks
Dim swModel As SldWorks.ModelDoc2
Dim swModelDocExt As SldWorks.ModelDocExtension
Dim swSketchSegment As SldWorks.SketchSegment
Dim swSketchMgr As SldWorks.SketchManager
Dim swFeature As SldWorks.Feature
Dim swFeatureMgr As SldWorks.FeatureManager
Dim swSelectionMgr As SldWorks.SelectionMgr
Dim swAssembly As SldWorks.AssemblyDoc
Dim status As Boolean
Dim errors As Long
Dim warnings As Long
Dim pMateRef As Object
Dim pCompSmart As Object
Dim pComp1 As Object
Dim pComp2 As Object
Dim pFeatArr(0) As Object
Dim pCompArr(1) As Object
Dim relcomp As Variant
Dim relfeat As Variant
Dim boundval As Variant
```

```
Sub main()
```

```
    Set swApp = Application.SldWorks
```

```
    'Create part
    Set swModel = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Part.prtdot", 0, 0, 0)
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SelectByID2("Front Plane", "PLANE", 0, 0, 0, False, 0, Nothing, 0)
    swModel.ActivateSelectedFeature
    swModel.ClearSelection2 True
    Set swSketchMgr = swModel.SketchManager
    swSketchMgr.InsertSketch True
    Set swSketchSegment = swSketchMgr.CreateLine(0#, 0#, 0#, 0#, -0.033793, 0#)
    status = swModelDocExt.SelectByID2("Line1", "SKETCHSEGMENT", 0, 0, 0, False, 16, Nothing, 0)
    Set swFeatureMgr = swModel.FeatureManager
    Set swFeature = swFeatureMgr.FeatureRevolve2(True, True, True, False, False, False, 0, 0, 6.2831853071796, 0, False, False, 0.01, 0.01, 0, 0.01, 0.01, True, True, True)
    status = swModelDocExt.SaveAs("C:\temp\RevolveComponent.SLDPRT", swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)

    'Create assembly
    Set swAssembly = swApp.NewDocument("C:\ProgramData\SolidWorks\SOLIDWORKS 2016\templates\Assembly.asmdot", 0, 0, 0)
    status = swAssembly.AddComponent("C:\temp\RevolveComponent.SLDPRT", 6.25313657656079E-03, 1.63811589345642E-04, -3.41098612290125E-03)
    status = swAssembly.AddComponent("C:\temp\RevolveComponent.SLDPRT", -2.72449827753007E-03, 3.30138755962253E-02, -3.17469704328105E-02)
    status = swAssembly.AddComponent("C:\temp\RevolveComponent.SLDPRT", 0.018507689004764, -4.20309320325032E-02, 1.74126345664263E-02)
    Set swModel = swAssembly
    Set swModelDocExt = swModel.Extension
    status = swModelDocExt.SaveAs("C:\temp\RevolveComponentsAssembly.sldasm", swSaveAsVersion_e.swSaveAsCurrentVersion, swSaveAsOptions_e.swSaveAsOptions_Silent, Nothing, errors, warnings)
```

```
   ' Select component to make smart
    status = swModelDocExt.SelectByID2("RevolveComponent-1@RevolveComponentsAssembly", "COMPONENT", 0, 0, 0, False, 0, Nothing, 0)
```

```
    ' Select components to associate with Smart Component
    status = swModelDocExt.SelectByID2("RevolveComponent-2@RevolveComponentsAssembly", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
    status = swModelDocExt.SelectByID2("RevolveComponent-3@RevolveComponentsAssembly", "COMPONENT", 0, 0, 0, True, 0, Nothing, 0)
```

```
    ' Select an face on a component for the concentric mate reference
    status = swModelDocExt.SelectByID2("", "FACE", 7.12645683466917E-03, 5.00071834983373E-03, 6.55080647294426E-03, True, 0, Nothing, 0)
```

```
    Set swSelectionMgr = swModel.SelectionManager
    Set pCompSmart = swSelectionMgr.GetSelectedObject6(1, 0)
    Set pComp1 = swSelectionMgr.GetSelectedObject6(2, 0)
    Set pComp2 = swSelectionMgr.GetSelectedObject6(3, 0)
    Set pMateRef = swSelectionMgr.GetSelectedObject6(4, 0)
```

```
    Set pCompArr(0) = pComp1
    Set pCompArr(1) = pComp2
```

```
    relcomp = pCompArr
```

```
    swModel.ClearSelection2 True
```

```
    'Create Smart Component with concentric mate reference
    status = swAssembly.CreateSmartComponent(pCompSmart, (relcomp), (relfeat), True, pMateRef, boundval)
    Debug.Print "Smart component created? " & status
```

```
End Sub
```
