---
title: "GetLineFontName Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "GetLineFontName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~GetLineFontName.html"
---

# GetLineFontName Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::GetLineFontName2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~GetLineFontName2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetLineFontName( _
   ByVal Index As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Index As System.Integer
Dim value As System.String

value = instance.GetLineFontName(Index)
```

### C#

```csharp
System.string GetLineFontName(
   System.int Index
)
```

### C++/CLI

```cpp
System.String^ GetLineFontName(
   System.int Index
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Index`:

## VBA Syntax

See [DrawingDoc::GetLineFontName](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~GetLineFontName.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
