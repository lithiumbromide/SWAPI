---
title: "NewSheet2 Method (IDrawingDoc)"
project: "SOLIDWORKS API Help"
interface: "IDrawingDoc"
member: "NewSheet2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc~NewSheet2.html"
---

# NewSheet2 Method (IDrawingDoc)

Obsolete. Superseded by [IDrawingDoc::NewSheet3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IDrawingDoc~NewSheet3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function NewSheet2( _
   ByVal Name As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal TemplateIn As System.Integer, _
   ByVal Scale1 As System.Double, _
   ByVal Scale2 As System.Double, _
   ByVal FirstAngle As System.Boolean, _
   ByVal TemplateName As System.String, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDrawingDoc
Dim Name As System.String
Dim PaperSize As System.Integer
Dim TemplateIn As System.Integer
Dim Scale1 As System.Double
Dim Scale2 As System.Double
Dim FirstAngle As System.Boolean
Dim TemplateName As System.String
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Boolean

value = instance.NewSheet2(Name, PaperSize, TemplateIn, Scale1, Scale2, FirstAngle, TemplateName, Width, Height)
```

### C#

```csharp
System.bool NewSheet2(
   System.string Name,
   System.int PaperSize,
   System.int TemplateIn,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.string TemplateName,
   System.double Width,
   System.double Height
)
```

### C++/CLI

```cpp
System.bool NewSheet2(
   System.String^ Name,
   System.int PaperSize,
   System.int TemplateIn,
   System.double Scale1,
   System.double Scale2,
   System.bool FirstAngle,
   System.String^ TemplateName,
   System.double Width,
   System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`:
- `PaperSize`:
- `TemplateIn`:
- `Scale1`:
- `Scale2`:
- `FirstAngle`:
- `TemplateName`:
- `Width`:
- `Height`:

## VBA Syntax

See [DrawingDoc::NewSheet2](ms-its:sldworksapivb6.chm::/sldworks~DrawingDoc~NewSheet2.html).

## See Also

[IDrawingDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc.html)
[IDrawingDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDrawingDoc_members.html)
