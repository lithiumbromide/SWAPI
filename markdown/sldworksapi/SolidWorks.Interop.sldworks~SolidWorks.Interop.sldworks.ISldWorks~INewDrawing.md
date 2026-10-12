---
title: "INewDrawing Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "INewDrawing"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDrawing.html"
---

# INewDrawing Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::NewDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~NewDocument.html) and [ISldWorks::INewDocument2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~INewDocument2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function INewDrawing( _
   ByVal TemplateToUse As System.Integer _
) As DrawingDoc
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim TemplateToUse As System.Integer
Dim value As DrawingDoc

value = instance.INewDrawing(TemplateToUse)
```

### C#

```csharp
DrawingDoc INewDrawing(
   System.int TemplateToUse
)
```

### C++/CLI

```cpp
DrawingDoc^ INewDrawing(
   System.int TemplateToUse
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TemplateToUse`:

## VBA Syntax

See [SldWorks::INewDrawing](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~INewDrawing.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
