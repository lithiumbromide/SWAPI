---
title: "SetVirtualEdges Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "SetVirtualEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.html"
---

# SetVirtualEdges Method (IWeldmentBeadFeatureData)

Sets the edges to which to apply this weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetVirtualEdges( _
   ByVal Side As System.Integer, _
   ByVal EdgesIn As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim EdgesIn As System.Object

instance.SetVirtualEdges(Side, EdgesIn)
```

### C#

```csharp
void SetVirtualEdges(
   System.int Side,
   System.object EdgesIn
)
```

### C++/CLI

```cpp
void SetVirtualEdges(
   System.int Side,
   System.Object^ EdgesIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)
- `EdgesIn`: Array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) to which to apply this weld bead

## VBA Syntax

See [WeldmentBeadFeatureData::SetVirtualEdges](ms-its:sldworksapivb6.chm::/sldworks~WeldmentBeadFeatureData~SetVirtualEdges.html).

## Remarks

After using [IWeldmentBeadFeatureData::SetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html), use [IWeldmentBeadFeatureData::GetVirtualEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.html) to get the new intersections. Then use IWeldmentBeadFeatureData::SetVirtualEdges to specify the edges to which you want the weld bead applied. By default, IWeldmentBeadFeatureData::SetFaces creates the bead on all virtual edges. IWeldmentBeadFeatureData::SetVirtualEdges lets you exclude any of these edges.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::ISetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges.html)
[IWeldmentBeadFeatureData::ISetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.html)
[IWeldmentBeadFeatureData::IGetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.html)
[IWeldmentBeadFeatureData::GetVirtualEdgesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdgesCount.html)
[IWeldmentBeadFeatureData::GetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~GetVirtualEdges.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
