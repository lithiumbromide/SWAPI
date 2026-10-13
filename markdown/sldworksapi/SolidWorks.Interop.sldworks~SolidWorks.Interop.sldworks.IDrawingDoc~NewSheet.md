---
title: "NewSheet Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "NewSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet.html"
---

# NewSheet Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::NewSheet3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~NewSheet3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub NewSheet( _
   ByVal Name As System.String, _
   ByVal PaperSize As System.Short, _
   ByVal TemplateIn As System.Short, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Name As System.String
Dim PaperSize As System.Short
Dim TemplateIn As System.Short
Dim Scale1 As System.Double
Dim Scale2 As System.Double

instance.NewSheet(Name, PaperSize, TemplateIn, Scale1, Scale2)
```

### C#

```csharp
void NewSheet(
   System.string Name,
   System.short PaperSize,
   System.short TemplateIn,
   System.double Scale1,
   System.double Scale2
)
```

### C++/CLI

```cpp
void NewSheet(
   System.String^ Name,
   System.short PaperSize,
   System.short TemplateIn,
   System.double Scale1,
   System.double Scale2
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `PaperSize`:
- `TemplateIn`:
- `Scale1`:
- `Scale2`:

## VBA Syntax

See [DrawingDoc::NewSheet](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~NewSheet.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
