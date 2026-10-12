---
title: "NewDrawing Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "NewDrawing"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~NewDrawing.html"
---

# NewDrawing Method (ISldWorks)

Obsolete. Superseded by [ISldWorks::NewDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~NewDocument.html) and [ISldWorks::INewDocument2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~INewDocument2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function NewDrawing( _
   ByVal TemplateToUse As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim TemplateToUse As System.Integer
Dim value As System.Object

value = instance.NewDrawing(TemplateToUse)
```

### C#

```csharp
System.object NewDrawing(
   System.int TemplateToUse
)
```

### C++/CLI

```cpp
System.Object^ NewDrawing(
   System.int TemplateToUse
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TemplateToUse`:

## VBA Syntax

See [SldWorks::NewDrawing](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~NewDrawing.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
