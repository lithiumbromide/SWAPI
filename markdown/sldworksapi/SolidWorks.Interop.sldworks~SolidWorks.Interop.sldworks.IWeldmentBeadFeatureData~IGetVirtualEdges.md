---
title: "IGetVirtualEdges Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "IGetVirtualEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.html"
---

# IGetVirtualEdges Method (IWeldmentBeadFeatureData)

Gets the edges to which the weld bead is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetVirtualEdges( _
   ByVal FromFeature As System.Boolean, _
   ByVal Side As System.Integer, _
   ByVal Count As System.Integer _
) As Edge
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim FromFeature As System.Boolean
Dim Side As System.Integer
Dim Count As System.Integer
Dim value As Edge

value = instance.IGetVirtualEdges(FromFeature, Side, Count)
```

### C#

```csharp
Edge IGetVirtualEdges(
   System.bool FromFeature,
   System.int Side,
   System.int Count
)
```

### C++/CLI

```cpp
Edge^ IGetVirtualEdges(
   System.bool FromFeature,
   System.int Side,
   System.int Count
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FromFeature`: True gets the virtual edges used by the feature, false gets all of the virtual edges
- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)
- `Count`: Number of edges to which weld bead applied

### Return Value

- in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html)

VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

Do not perform any operations on the returned edges as they are only temporary to help you decide which edges to keep for this weld bead.

Call [IWeldmentBeadFeatureData::GetVirutalEdgesCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdgesCount.html) to get the number of edges.

After using [IWeldmentBeadFeatureData::ISetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.html), use IWeldmentBeadFeatureData::IGetVirtualEdges to get the new intersections. Then use [IWeldmentBeadFeatureData::ISetVirtualEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges.html) to specify the edges to which you want the weld bead applied. By default, IWeldmentBeadFeatureData::ISetFaces creates the bead on all virtual edges; IWeldmentBeadFeatureData::ISetVirtualEdges lets you exclude any of these edges.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::GetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.html)
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html)
[IWeldmentBeadFeatureData::SetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
