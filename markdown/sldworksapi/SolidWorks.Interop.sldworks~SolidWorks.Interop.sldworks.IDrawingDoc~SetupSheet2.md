---
title: "SetupSheet2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SetupSheet2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet2.html"
---

# SetupSheet2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::SetupSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~SetupSheet4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetupSheet2( _
   ByVal Name As System.String, _
   ByVal PaperSize As System.Short, _
   ByVal TemplateIn As System.Short, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal SkPointsFlag As System.Integer _
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
Dim SkPointsFlag As System.Integer

instance.SetupSheet2(Name, PaperSize, TemplateIn, Scale1, Scale2, SkPointsFlag)
```

### C#

```csharp
void SetupSheet2(
   System.string Name,
   System.short PaperSize,
   System.short TemplateIn,
   System.double Scale1,
   System.double Scale2,
   System.int SkPointsFlag
)
```

### C++/CLI

```cpp
void SetupSheet2(
   System.String^ Name,
   System.short PaperSize,
   System.short TemplateIn,
   System.double Scale1,
   System.double Scale2,
   System.int SkPointsFlag
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `PaperSize`:
- `TemplateIn`:
- `Scale1`:
- `Scale2`:
- `SkPointsFlag`:

## VBA Syntax

See [DrawingDoc::SetupSheet2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SetupSheet2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
