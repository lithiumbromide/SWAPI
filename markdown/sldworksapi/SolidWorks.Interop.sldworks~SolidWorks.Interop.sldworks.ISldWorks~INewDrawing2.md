---
title: "INewDrawing2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "INewDrawing2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDrawing2.html"
---

# INewDrawing2 Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::NewDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~NewDocument.html) and [ISldWorks::INewDocument2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~INewDocument2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function INewDrawing2( _
   ByVal TemplateToUse As System.Integer, _
   ByVal TemplateName As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As DrawingDoc
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim TemplateToUse As System.Integer
Dim TemplateName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As DrawingDoc

value = instance.INewDrawing2(TemplateToUse, TemplateName, PaperSize, Width, Height)
```

### C#

```csharp
DrawingDoc INewDrawing2(
   System.int TemplateToUse,
   System.string TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

### C++/CLI

```cpp
DrawingDoc^ INewDrawing2(
   System.int TemplateToUse,
   System.String^ TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TemplateToUse`:
- `TemplateName`:
- `PaperSize`:
- `Width`:
- `Height`:

## VBA Syntax

See [SldWorks::INewDrawing2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~INewDrawing2.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
