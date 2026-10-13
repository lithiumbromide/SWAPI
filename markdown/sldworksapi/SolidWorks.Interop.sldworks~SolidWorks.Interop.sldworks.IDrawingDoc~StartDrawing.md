---
title: "StartDrawing Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "StartDrawing"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~StartDrawing.html"
---

# StartDrawing Method (IDrawingDoc)

Provides faster creation of entities within a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub StartDrawing()
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc

instance.StartDrawing()
```

### C#

```csharp
void StartDrawing()
```

### C++/CLI

```cpp
void StartDrawing();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [DrawingDoc::StartDrawing](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~StartDrawing.html).

## Remarks

This method automatically disables inferencing to provide faster geometry creation. Use this method and [IDrawingDoc::EndDrawing](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~EndDrawing.html) to bound your entity creation statements.

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
