---
title: "IGetTrimCurveSize2 Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetTrimCurveSize2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize2.html"
---

# IGetTrimCurveSize2 Method (IFace2)

Gets the size of the array required for [IFace2::GetTrimCurves2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTrimCurves2.html)

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTrimCurveSize2( _
   ByVal WantCubic As System.Integer, _
   ByVal WantNRational As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim WantCubic As System.Integer
Dim WantNRational As System.Integer
Dim value As System.Integer

value = instance.IGetTrimCurveSize2(WantCubic, WantNRational)
```

### C#

```csharp
System.int IGetTrimCurveSize2(
   System.int WantCubic,
   System.int WantNRational
)
```

### C++/CLI

```cpp
System.int IGetTrimCurveSize2(
   System.int WantCubic,
   System.int WantNRational
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `WantCubic`: True if the trim curves are to be cubic, false if not
- `WantNRational`: True if the trim curves are to be non-rational, false if not

### Return Value

Size of the array required for IFace2::GetTrimCurves2

## VBA Syntax

See [Face2::IGetTrimCurveSize2](ms-its:sldworksapivb6.chm::/sldworks~Face2~IGetTrimCurveSize2.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetTrimCurveTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopology.html)
[IFace2::GetTrimCurveTopologyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyCount.html)
[IFace2::GetTrimCurveTopologyTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyTypes.html)
[IFace2::IGetTrimCurveTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopology.html)
[IFace2::IGetTrimCurveTopologyTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopologyTypes.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
