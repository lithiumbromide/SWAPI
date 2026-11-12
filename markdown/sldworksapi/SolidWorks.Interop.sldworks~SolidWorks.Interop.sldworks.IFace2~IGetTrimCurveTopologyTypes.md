---
title: "IGetTrimCurveTopologyTypes Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IGetTrimCurveTopologyTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopologyTypes.html"
---

# IGetTrimCurveTopologyTypes Method (IFace2)

Gets the trim curve topology type array for this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTrimCurveTopologyTypes() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Integer

value = instance.IGetTrimCurveTopologyTypes()
```

### C#

```csharp
System.int IGetTrimCurveTopologyTypes()
```

### C++/CLI

```cpp
System.int IGetTrimCurveTopologyTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

- in-process, unmanaged C++: Pointer to an array of longs indicating the topology types as defined in [swSelectType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectType_e.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Use [IFace2::GetTrimCurveTopology](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTrimCurveTopology.html) or [IFace2::IGetTrimCurveTopology](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTrimCurveTopology.html) to get the trim curve topology for this face.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetTrimCurves2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurves2.html)
[IFace2::GetTrimCurveTopologyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyCount.html)
[IFace2::IGetTrimCurveSize2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveSize2.html)
[IFace2::GetTrimCurveTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopology.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
