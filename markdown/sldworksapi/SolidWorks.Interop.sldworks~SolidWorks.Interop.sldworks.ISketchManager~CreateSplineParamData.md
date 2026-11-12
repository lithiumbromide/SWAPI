---
title: "CreateSplineParamData Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateSplineParamData"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplineParamData.html"
---

# CreateSplineParamData Method (ISketchManager)

Creates an empty spline parameter data object.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSplineParamData() As SplineParamData
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager
Dim value As SplineParamData

value = instance.CreateSplineParamData()
```

### C#

```csharp
SplineParamData CreateSplineParamData()
```

### C++/CLI

```cpp
SplineParamData^ CreateSplineParamData();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ISplineParamData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISplineParamData.html)

## VBA Syntax

See [SketchManager::CreateSplineParamData](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateSplineParamData.html).

## Examples

[Get Spline's Parameters (C#)](Get_Spline's_Parameters_Example_CSharp.htm)
[Get Spline's Parameters (VB.NET)](Get_Spline's_Parameters_Example_VBNET.htm)
[Get Spline's Parameters (VBA)](Get_Spline's_Parameters_Example_VB.htm)

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)
[ISketchManager::CreateSplinesByEqnParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateSplinesByEqnParams2.html)
[ISketch::GetSplineParams4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams4.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
