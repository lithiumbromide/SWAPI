---
title: "GetVirtualEdgesCount Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "GetVirtualEdgesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdgesCount.html"
---

# GetVirtualEdgesCount Method (IWeldmentBeadFeatureData)

Gets the number of edges to which the weld bead is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVirtualEdgesCount( _
   ByVal FromFeature As System.Boolean, _
   ByVal Side As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim FromFeature As System.Boolean
Dim Side As System.Integer
Dim value As System.Integer

value = instance.GetVirtualEdgesCount(FromFeature, Side)
```

### C#

```csharp
System.int GetVirtualEdgesCount(
   System.bool FromFeature,
   System.int Side
)
```

### C++/CLI

```cpp
System.int GetVirtualEdgesCount(
   System.bool FromFeature,
   System.int Side
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromFeature`: True gets the virtual edges used by the feature, false gets all of the virtual edges
- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

### Return Value

Number of edges

## VBA Syntax

See [WeldmentBeadFeatureData::GetVirtualEdgesCount](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~GetVirtualEdgesCount.html).

## Remarks

Call this method before calling [IWeldmentBeadFeatureData::GetVirtualEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.html).

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::GetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.html)
[IWeldmentBeadFeatureData::ISetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges.html)
[IWeldmentBeadFeatureData::SetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.html)
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.html)
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
