---
title: "SetupSheet Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "SetupSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~SetupSheet.html"
---

# SetupSheet Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::SetupSheet4](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~SetupSheet4.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetupSheet( _
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

instance.SetupSheet(Name, PaperSize, TemplateIn, Scale1, Scale2)
```

### C#

```csharp
void SetupSheet(
   System.string Name,
   System.short PaperSize,
   System.short TemplateIn,
   System.double Scale1,
   System.double Scale2
)
```

### C++/CLI

```cpp
void SetupSheet(
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

See [DrawingDoc::SetupSheet](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~SetupSheet.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
