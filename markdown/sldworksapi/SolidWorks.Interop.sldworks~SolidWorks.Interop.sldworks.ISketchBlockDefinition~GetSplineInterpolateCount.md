---
title: "GetSplineInterpolateCount Method (ISketchBlockDefinition)"
project: "SOLIDWORKS API Help"
interface: "ISketchBlockDefinition"
member: "GetSplineInterpolateCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineInterpolateCount.html"
---

# GetSplineInterpolateCount Method (ISketchBlockDefinition)

Gets the number of splines in the sketch block definition and the size of array required to hold the data for the interpolation of these splines.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineInterpolateCount( _
   ByRef ArraySize As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchBlockDefinition
Dim ArraySize As System.Integer
Dim value As System.Integer

value = instance.GetSplineInterpolateCount(ArraySize)
```

### C#

```csharp
System.int GetSplineInterpolateCount(
   out System.int ArraySize
)
```

### C++/CLI

```cpp
System.int GetSplineInterpolateCount(
   [Out] System.int ArraySize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ArraySize`: Size of the array needed to hold the spline interpolation data information

### Return Value

Number of splines in this sketch block definition

## VBA Syntax

See [SketchBlockDefinition::GetSplineInterpolateCount](ms-its:sldworksapivb6.chm::/sldworks~SketchBlockDefinition~GetSplineInterpolateCount.html).

## Remarks

The ArraySize value is intended to be used as the input ArraySize argument to [ISketchBlockDefinition::IGetSplinesInterpolate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchBlockDefinition~IGetSplinesInterpolate.html).

## See Also

[ISketchBlockDefinition Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition.html)
[ISketchBlockDefinition Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition_members.html)
[ISketchBlockDefinition::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineCount.html)
[ISketchBlockDefinition::GetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParams.html)
[ISketchBlockDefinition::GetSplineParamsCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplineParamsCount.html)
[ISketchBlockDefinition::GetSplines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplines2.html)
[ISketchBlockDefinition::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~GetSplinesInterpolate.html)
[ISketchBlockDefinition::IGetSplineParams Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplineParams.html)
[ISketchBlockDefinition::IGetSplines2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchBlockDefinition~IGetSplines2.html)

## Availability

SOLIDWORKS 2007 SP2, Revision Number 15.2
