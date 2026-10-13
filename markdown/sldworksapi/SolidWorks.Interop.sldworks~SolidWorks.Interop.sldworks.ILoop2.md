---
title: "ILoop2 Interface"
project: "SOLIDWORKS API Help"
interface: "ILoop2"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.html"
---

# ILoop2 Interface

Allows access to the owning face and to the list of edges and coedges contained in the loop.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ILoop2
```

### Visual Basic (Usage)

```vb
Dim instance As ILoop2
```

### C#

```csharp
public interface ILoop2
```

### C++/CLI

```cpp
public interface class ILoop2
```

## VBA Syntax

See [Loop2](ms-its:sldworksapivb6.chm::/sldworks~Loop2.html).

## Examples

[Get Sketch Regions (VBA)](Get_Sketch_Regions_Example_VB.htm)
[Get Sketch Regions (VB.NET)](Get_Sketch_Regions_Example_VBNET.htm)
[Get Sketch Regions (C#)](Get_Sketch_Regions_Example_CSharp.htm)

## Accessors

[ICoEdge::GetLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~GetLoop.html)

[ICoEdge::IGetLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICoEdge~IGetLoop2.html)

[IEnumLoops2::Next](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IEnumLoops2~Next.html)

[IFace2::GetFirstLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetFirstLoop.html) and [IFace2::IGetFirstLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IGetFirstLoop.html)

[ILoop2::GetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~GetNext.html) and [ILoop2::IGetNext](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ILoop2~IGetNext.html)

[ISelectionMgr::GetSelectedObjectLoop2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISelectionMgr~GetSelectedObjectLoop2.html)

[ISimpleFilletFeatureData2::IGetLoops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~IGetLoops.html)

[ISimpleFilletFeatureData2::Loops](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISimpleFilletFeatureData2~Loops.html)

[ISketchRegion::GetFirstLoop](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISketchRegion~GetFirstLoop.html)

## Access Diagram

[Loop2](SWObjectModel.pdf#Loop2)

## See Also

[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
[IEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.html)
[ICoEdge Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoEdge.html)
[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[DAssemblyDocEvents_FlipLoopNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FlipLoopNotifyEventHandler.html)
[DPartDocEvents_FlipLoopNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FlipLoopNotifyEventHandler.html)
