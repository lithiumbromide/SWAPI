---
title: "ICoEdge Interface"
project: "SOLIDWORKS API Help"
interface: "ICoEdge"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html"
---

# ICoEdge Interface

Allows access to the underlying edge and loop as well as various coedge data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICoEdge
```

### Visual Basic (Usage)

```vb
Dim instance As ICoEdge
```

### C#

```csharp
public interface ICoEdge
```

### C++/CLI

```cpp
public interface class ICoEdge
```

## VBA Syntax

See [CoEdge](ms-its:sldworksapivb6.chm::/sldworks~CoEdge.html).

## Examples

[Select Edges of All Holes on Face (VBA)](Select_Edges_of_All_Holes_on_Face_Example_VB.htm)
[Select Edges of All Holes on Face (C#)](Select_Edges_of_All_Holes_on_Face_Example_CSharp.htm)
[Select Edges of All Holes on Face (VB.NET)](Select_Edges_of_All_Holes_on_Face_Example_VBNET.htm)

## Accessors

[ICoEdge::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~GetNext.html) and [ICoEdge::IGetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~IGetNext.html)

[ICoEdge::GetPartner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~GetPartner.html) and [ICoEdge::IGetPartner](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~IGetPartner.html)

[IDiagnoseResult::GetCoEdgesAtGap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult~GetCoEdgesAtGap.html) and [IDiagnoseResult::IGetCoEdgesAtGap](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDiagnoseResult~IGetCoEdgesAtGap.html)

[IEnumCoEdges::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumCoEdges~Next.html)

[ILoop2::GetCoEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~GetCoEdges.html) and [ILoop2::IGetCoEdges](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IGetCoEdges.html)

[ILoop2::GetFirstCoEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~GetFirstCoEdge.html) and [ILoop2::IGetFirstCoEdge](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IGetFirstCoEdge.html)

[ISMGussetFeatureData::ReferenceLine](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMGussetFeatureData~ReferenceLine.html)

## Access Diagram

[CoEdge](SWObjectModel.pdf#CoEdge)

## See Also

[ICoEdge Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IEnumCoEdgeClass Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEnumCoEdges.html)
[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html)
