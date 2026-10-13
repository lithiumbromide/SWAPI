---
title: "CreateSplinesByEqnParams2 Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateSplinesByEqnParams2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams2.html"
---

# CreateSplinesByEqnParams2 Method (ISketchManager)

Creates one or more spline segments using the B-curve parameters provided.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSplinesByEqnParams2( _
   ByVal ParamData As SplineParamData _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim ParamData As SplineParamData
Dim value As System.Object

value = instance.CreateSplinesByEqnParams2(ParamData)
```

### C#

```csharp
System.object CreateSplinesByEqnParams2(
   SplineParamData ParamData
)
```

### C++/CLI

```cpp
System.Object^ CreateSplinesByEqnParams2(
   SplineParamData^ ParamData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ParamData`: [ISplineParamData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData.html)

### Return Value

Array of [sketch segments](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchSegment.html) of the newly created spline

## VBA Syntax

See [SketchManager::CreateSplinesByEqnParams2](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateSplinesByEqnParams2.html).

## Examples

[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateSpline2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSpline2.html)
[ISketchManager::CreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineByEqnParams.html)
[ISketchManager::ICreateSpline2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSpline2.html)
[ISketchManager::ICreateSplineByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplineByEqnParams.html)
[ISketchManager::ICreateSplinesByEqnParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~ICreateSplinesByEqnParams.html)
[ISketchManager::CreateSplineParamData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineParamData.html)
[ISketch::GetSplineParams4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams4.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
