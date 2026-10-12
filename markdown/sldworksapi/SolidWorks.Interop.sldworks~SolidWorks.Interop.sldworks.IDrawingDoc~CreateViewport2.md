---
title: "CreateViewport2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "CreateViewport2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~CreateViewport2.html"
---

# CreateViewport2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::CreateViewport3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~CreateViewport3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateViewport2( _
   ByVal LowerLeftX As System.Double, _
   ByVal LowerLeftY As System.Double, _
   ByVal UpperRightX As System.Double, _
   ByVal UpperRightY As System.Double, _
   ByVal SketchSize As System.Short, _
   ByVal Scale As System.Double _
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
Dim Scale As System.Double
Dim value As System.String

value = instance.CreateViewport2(LowerLeftX, LowerLeftY, UpperRightX, UpperRightY, SketchSize, Scale)
```

### C#

```csharp
System.string CreateViewport2(
   System.double LowerLeftX,
   System.double LowerLeftY,
   System.double UpperRightX,
   System.double UpperRightY,
   System.short SketchSize,
   System.double Scale
)
```

### C++/CLI

```cpp
System.String^ CreateViewport2(
   System.double LowerLeftX,
   System.double LowerLeftY,
   System.double UpperRightX,
   System.double UpperRightY,
   System.short SketchSize,
   System.double Scale
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `LowerLeftX`:
- `LowerLeftY`:
- `UpperRightX`:
- `UpperRightY`:
- `SketchSize`:
- `Scale`:

## VBA Syntax

See [DrawingDoc::CreateViewport2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~CreateViewport2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
