---
title: "GetSplineCount Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetSplineCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineCount.html"
---

# GetSplineCount Method (ISketchBlockDefinition)

Gets the number of splines in this block definition.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineCount( _
   ByRef PointCount As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim PointCount As System.Integer
Dim value As System.Integer

value = instance.GetSplineCount(PointCount)
```

### C#

```csharp
System.int GetSplineCount(
   out System.int PointCount
)
```

### C++/CLI

```cpp
System.int GetSplineCount(
   [Out] System.int PointCount
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PointCount`: Number of points (see **Remarks**)

### Return Value

Number of splines in the block definition

## VBA Syntax

See [SketchBlockDefinition::GetSplineCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetSplineCount.html).

## Remarks

Call this method before calling [ISketchBlockDefiniton::IGetSplines2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.html). PointCount is the value use to determine the size of the array for this method.

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[GetSplines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.html)
[ISketchBlockDefinition::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineInterpolateCount.html)
[ISketchBlockDefinition::GetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParams.html)
[ISketchBlockDefinition::GetSplineParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParamsCount.html)
[ISketchBlockDefinition::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate.html)
[ISketchBlockDefinition::IGetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplineParams.html)
[ISketchBlockDefinition::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
