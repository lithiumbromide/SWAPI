---
title: "AutoBalloon Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "AutoBalloon"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~AutoBalloon.html"
---

# AutoBalloon Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::AutoBalloon3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~AutoBalloon3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AutoBalloon( _
   ByVal Layout As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Layout As System.Integer
Dim value As System.Object

value = instance.AutoBalloon(Layout)
```

### C#

```csharp
System.object AutoBalloon(
   System.int Layout
)
```

### C++/CLI

```cpp
System.Object^ AutoBalloon(
   System.int Layout
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Layout`:

## VBA Syntax

See [DrawingDoc::AutoBalloon](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~AutoBalloon.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
