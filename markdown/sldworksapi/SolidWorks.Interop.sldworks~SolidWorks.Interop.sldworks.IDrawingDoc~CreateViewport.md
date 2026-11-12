---
title: "CreateViewport Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateViewport"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport.html"
---

# CreateViewport Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateViewport3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateViewport3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateViewport( _
   ByVal LowerLeftX As System.Double, _
   ByVal LowerLeftY As System.Double, _
   ByVal UpperRightX As System.Double, _
   ByVal UpperRightY As System.Double, _
   ByVal SketchSize As System.Short _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim LowerLeftX As System.Double
Dim LowerLeftY As System.Double
Dim UpperRightX As System.Double
Dim UpperRightY As System.Double
Dim SketchSize As System.Short
Dim value As System.String

value = instance.CreateViewport(LowerLeftX, LowerLeftY, UpperRightX, UpperRightY, SketchSize)
```

### C#

```csharp
System.string CreateViewport(
   System.double LowerLeftX,
   System.double LowerLeftY,
   System.double UpperRightX,
   System.double UpperRightY,
   System.short SketchSize
)
```

### C++/CLI

```cpp
System.String^ CreateViewport(
   System.double LowerLeftX,
   System.double LowerLeftY,
   System.double UpperRightX,
   System.double UpperRightY,
   System.short SketchSize
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LowerLeftX`:
- `LowerLeftY`:
- `UpperRightX`:
- `UpperRightY`:
- `SketchSize`:

## VBA Syntax

See [DrawingDoc::CreateViewport](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateViewport.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
