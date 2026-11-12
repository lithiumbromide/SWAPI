---
title: "CreateConstructionGeometry Method (ISketchManager)"
project: "SOLIDWORKS API Help"
interface: "ISketchManager"
member: "CreateConstructionGeometry"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager~CreateConstructionGeometry.html"
---

# CreateConstructionGeometry Method (ISketchManager)

Sets selected sketch segments to be construction geometry instead of sketch geometry.

## Syntax

### Visual Basic (Declaration)

```vb
Sub CreateConstructionGeometry()
```

### Visual Basic (Usage)

```vb
Dim instance As ISketchManager

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

See [SketchManager::CreateConstructionGeometry](ms-its:sldworksapivb6.chm::/Sldworks~SketchManager~CreateConstructionGeometry.html).

## Remarks

This method supports all document types, unlike [IDrawingDoc::CreateConstructionGeometry](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateConstructionGeometry.html), which only supports drawing documents. Both methods perform the same functionality.

## See Also

[ISketchManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager.html)
[ISketchManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISketchManager_members.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
