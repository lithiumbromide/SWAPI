---
title: "ISetVirtualEdges Method (IWeldmentBeadFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IWeldmentBeadFeatureData"
member: "ISetVirtualEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~ISetVirtualEdges.html"
---

# ISetVirtualEdges Method (IWeldmentBeadFeatureData)

Sets the edges to which to apply this weld bead.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetVirtualEdges( _
   ByVal Side As System.Integer, _
   ByVal Count As System.Integer, _
   ByRef EdgesIn As Edge _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IWeldmentBeadFeatureData
Dim Side As System.Integer
Dim Count As System.Integer
Dim EdgesIn As Edge

instance.ISetVirtualEdges(Side, Count, EdgesIn)
```

### C#

```csharp
void ISetVirtualEdges(
   System.int Side,
   System.int Count,
   ref Edge EdgesIn
)
```

### C++/CLI

```cpp
void ISetVirtualEdges(
   System.int Side,
   System.int Count,
   Edge^% EdgesIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Side`: Side as defined in [swWeldBeadSide_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swWeldBeadSide_e.html)
- `Count`: Number of edges to which to apply this weld bead
- `EdgesIn`: - in-process, unmanaged C++: Pointer to an array of [edges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEdge.html) to which to apply this weld bead

  VBA, VB.NET, C#, and C++/CLI: Not supported

  See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## Remarks

After using [IWeldmentBeadFeatureData::ISetFaces](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~ISetFaces.html), use [IWeldmentBeadFeatureData::IGetVirtualEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.html) to get the new intersections. Then use IWeldmentBeadFeatureData::ISetVirtualEdges to specify the edges to which you want the weld bead applied. By default, IWeldmentBeadFeatureData::ISetFaces creates the bead on all virtual edges. IWeldmentBeadFeatureData::ISetVirtualEdges lets you exclude any of these edges.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details.

## See Also

[IWeldmentBeadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData.html)
[IWeldmentBeadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData_members.html)
[IWeldmentBeadFeatureData::SetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetVirtualEdges.html)
[IWeldmentBeadFeatureData::SetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~SetFaces.html)
[IWeldmentBeadFeatureData::IGetVirtualEdges Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWeldmentBeadFeatureData~IGetVirtualEdges.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
