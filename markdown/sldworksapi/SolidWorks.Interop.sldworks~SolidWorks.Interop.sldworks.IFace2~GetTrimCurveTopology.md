---
title: "GetTrimCurveTopology Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetTrimCurveTopology"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopology.html"
---

# GetTrimCurveTopology Method (IFace2)

Gets the trim curve topology for this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTrimCurveTopology() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Object

value = instance.GetTrimCurveTopology()
```

### C#

```csharp
System.object GetTrimCurveTopology()
```

### C++/CLI

```cpp
System.Object^ GetTrimCurveTopology();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of coedges, vertices, and NULLs (see **Remarks**)

## VBA Syntax

See [Face2::GetTrimCurveTopology](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetTrimCurveTopology.html).

## Remarks

This method returns a list of coedges, vertices, and NULLs. You must call [IFace2::GetTrimCurves2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTrimCurves2.html) or [IFace2::IGetTrimCurves2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTrimCurveSize2.html) before calling this method.

This method returns a list of proper edges corresponding to the list of SP curves from IFace2::GetTrimCurves2 or IFace2::IGetTrimCurves2. Otherwise, this method prompts the user for the list of edges that the software thinks are on the face. These two lists differ in order and content.

Use [IFace2::GetTrimCurveTopologyTypes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetTrimCurveTopology.html) or [IFace2::IGetTrimCurveTopologyTypes](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetTrimCurveTopology.html) to get an array of types corresponding to the returned objects.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IFace2::IGetTrimCurveTopology Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetTrimCurveTopology.html)
[IFace2::GetTrimCurveTopologyCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetTrimCurveTopologyCount.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
