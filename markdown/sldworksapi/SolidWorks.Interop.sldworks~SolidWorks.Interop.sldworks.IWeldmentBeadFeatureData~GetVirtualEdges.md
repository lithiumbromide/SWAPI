---
title: "GetVirtualEdges Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "GetVirtualEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.html"
---

# GetVirtualEdges Method (IWeldmentBeadFeatureData)

Gets the edges to which the weld bead is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetVirtualEdges( _
   ByVal FromFeature As System.Boolean, _
   ByVal Side As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim FromFeature As System.Boolean
Dim Side As System.Integer
Dim value As System.Object

value = instance.GetVirtualEdges(FromFeature, Side)
```

### C#

```csharp
System.object GetVirtualEdges(
   System.bool FromFeature,
   System.int Side
)
```

### C++/CLI

```cpp
System.Object^ GetVirtualEdges(
   System.bool FromFeature,
   System.int Side
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromFeature`: True gets the virtual edges used by the feature, false gets all of the virtual edges
- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)

### Return Value

Array of the [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

## VBA Syntax

See [WeldmentBeadFeatureData::GetVirtualEdges](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~GetVirtualEdges.html).

## Examples

See the [IWeldmentBeadFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html) examples.

## Remarks

Do not perform any operations on the returned edges as they are only temporary to help you decide which edges to keep for this weld bead.

After using [IWeldmentBeadFeatureData::SetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html), use IWeldmentBeadFeatureData::GetVirtualEdges to get the new intersections. Then use [IWeldmentBeadFeatureData::SetVirtualEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.html) to specify the edges to which you want the weld bead applied. By default, IWeldmentBeadFeatureData::SetFaces creates the bead on all virtual edges; IWeldmentBeadFeatureData::SetVirtualEdges lets you exclude any of these edges.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::GetVirtualEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdgesCount.html)
[IWeldmentBeadFeatureData::IGetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.html)
[IWeldmentBeadFeatureData::ISetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges.html)
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
