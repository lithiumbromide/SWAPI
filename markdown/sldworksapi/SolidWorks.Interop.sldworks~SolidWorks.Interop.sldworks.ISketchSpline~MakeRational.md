---
title: "MakeRational Method (ISketchSpline)"
project: "SOLIDWORKS API Help"
interface: "ISketchSpline"
member: "MakeRational"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~MakeRational.html"
---

# MakeRational Method (ISketchSpline)

Sets whether this spline is rational or non-rational.

## Syntax

### Visual Basic (Declaration)

```vb
Function MakeRational( _
   ByVal Val As System.Boolean _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchSpline
Dim Val As System.Boolean
Dim value As System.Boolean

value = instance.MakeRational(Val)
```

### C#

```csharp
System.bool MakeRational(
   System.bool Val
)
```

### C++/CLI

```cpp
System.bool MakeRational(
   System.bool Val
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`: True to make rational, false to make non-rational

### Return Value

True if successfully set, false if not

## VBA Syntax

See [SketchSpline::MakeRational](ms-its:sldworksapivb6.chm::/sldworks~SketchSpline~MakeRational.html).

## See Also

[ISketchSpline Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline.html)
[ISketchSpline Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline_members.html)
[ISketchSpline::IsRationalCurve Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchSpline~IsRationalCurve.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
