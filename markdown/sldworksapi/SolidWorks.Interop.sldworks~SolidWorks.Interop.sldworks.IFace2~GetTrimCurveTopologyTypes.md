---
title: "GetTrimCurveTopologyTypes Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetTrimCurveTopologyTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyTypes.html"
---

# GetTrimCurveTopologyTypes Method (IFace2)

Gets the types of elements in the trim curve topology for this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrimCurveTopologyTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetTrimCurveTopologyTypes()
```

### C#

```csharp
System.object GetTrimCurveTopologyTypes()
```

### C++/CLI

```cpp
System.Object^ GetTrimCurveTopologyTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of longs or integers (see [Long vs. Integer](sldworksapiprogguide.chm::/overview/Long_vs_Integer.htm)) indicating topology types as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [Face2::GetTrimCurveTopologyTypes](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetTrimCurveTopologyTypes.html).

## Remarks

Use [IFace2::GetTrimCurveTopology](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTrimCurveTopology.html) or [IFace2::IGetTrimCurveTopology](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTrimCurveTopology.html) to get the trim curve topology for this face.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetTrimCurves2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.html)
[IFace2::GetTrimCurveTopologyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyCount.html)
[IFace2::IGetTrimCurveSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize2.html)
[IFace2::IGetTrimCurveTopologyTypes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopologyTypes.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
