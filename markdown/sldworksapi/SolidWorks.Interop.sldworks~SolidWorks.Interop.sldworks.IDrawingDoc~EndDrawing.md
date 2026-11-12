---
title: "EndDrawing Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "EndDrawing"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~EndDrawing.html"
---

# EndDrawing Method (IDrawingDoc)

Provides faster creation of entities in a drawing when used with [IDrawingDoc::StartDrawing](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~StartDrawing.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub EndDrawing()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.EndDrawing()
```

### C#

```csharp
void EndDrawing()
```

### C++/CLI

```cpp
void EndDrawing();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::EndDrawing](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~EndDrawing.html).

## Remarks

Use [IDrawingDoc::StartDrawing](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~StartDrawing.html) and this method to bound your entity creation statements.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
