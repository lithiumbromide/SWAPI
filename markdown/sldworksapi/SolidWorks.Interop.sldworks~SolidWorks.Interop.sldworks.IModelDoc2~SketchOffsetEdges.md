---
title: "SketchOffsetEdges Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "SketchOffsetEdges"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEdges.html"
---

# SketchOffsetEdges Method (IModelDoc2)

Offsets the edges of the selected entities.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SketchOffsetEdges( _
   ByVal Val As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Val As System.Double

instance.SketchOffsetEdges(Val)
```

### C#

```csharp
void SketchOffsetEdges(
   System.double Val
)
```

### C++/CLI

```cpp
void SketchOffsetEdges(
   System.double Val
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`: Offset value in meters

## VBA Syntax

See [ModelDoc2::SketchOffsetEdges](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~SketchOffsetEdges.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::SketchOffset2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffset2.html)
[IModelDoc2::SketchOffsetEntities2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~SketchOffsetEntities2.html)
[IModelDocExtension::SketchOffsetOnSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SketchOffsetOnSurface.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
