---
title: "CreateConstructionGeometry Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateConstructionGeometry"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateConstructionGeometry.html"
---

# CreateConstructionGeometry Method (IDrawingDoc)

Sets the selected sketch segments to be construction geometry instead of sketch geometry.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CreateConstructionGeometry()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.CreateConstructionGeometry()
```

### C#

```csharp
void CreateConstructionGeometry()
```

### C++/CLI

```cpp
void CreateConstructionGeometry();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::CreateConstructionGeometry](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateConstructionGeometry.html).

## Remarks

This method ignores construction geometry when it generates the solid body.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
[ISketchManager::CreateConstructionGeometry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateConstructionGeometry.html)
