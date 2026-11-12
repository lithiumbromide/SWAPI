---
title: "GetSplineParamsCount2 Method (ISketch)"
project: "SOLIDWORKS API Help"
interface: "ISketch"
member: "GetSplineParamsCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParamsCount2.html"
---

# GetSplineParamsCount2 Method (ISketch)

Obsolete. Superseded by [ISketch::GetSplineParamsCount3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSplineParamsCount3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetSplineParamsCount2( _
   ByRef Size As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISketch
Dim Size As System.Integer
Dim value As System.Integer

value = instance.GetSplineParamsCount2(Size)
```

### C#

```csharp
System.int GetSplineParamsCount2(
   out System.int Size
)
```

### C++/CLI

```cpp
System.int GetSplineParamsCount2(
   [Out] System.int Size
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Size`: Size of array required for a call to [ISketch::IGetSplineParams2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~IGetSplineParams2.html)

### Return Value

Number of [splines](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketch~GetSplineParams3.html)

## VBA Syntax

See [Sketch::GetSplineParamsCount2](ms-its:sldworksapivb6.chm::/sldworks~Sketch~GetSplineParamsCount2.html).

## See Also

[ISketch Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch.html)
[ISketch Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch_members.html)
[ISketch::GetSplineCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineCount.html)
[ISketch::GetSplineInterpolateCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineInterpolateCount.html)
[ISketch::GetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplines.html)
[ISketch::GetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplinesInterpolate.html)
[ISketch::IGetSplines Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplines.html)
[ISketch::IGetSplinesInterpolate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~IGetSplinesInterpolate.html)
[ISketch::GetSplineParams2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketch~GetSplineParams2.html)

## Availability

SOLIDWORKS 2000 FCS, Revision Number 8.0
