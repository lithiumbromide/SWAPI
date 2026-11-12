---
title: "INewDocument Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "INewDocument"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDocument.html"
---

# INewDocument Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::INewDocument2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~INewDocument2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function INewDocument( _
   ByVal TemplateName As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As ModelDoc
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim TemplateName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As ModelDoc

value = instance.INewDocument(TemplateName, PaperSize, Width, Height)
```

### C#

```csharp
ModelDoc INewDocument(
   System.string TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

### C++/CLI

```cpp
ModelDoc^ INewDocument(
   System.String^ TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TemplateName`:
- `PaperSize`:
- `Width`:
- `Height`:

## VBA Syntax

See [SldWorks::INewDocument](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~INewDocument.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
