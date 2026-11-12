---
title: "IGetTemplateSizes Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "IGetTemplateSizes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetTemplateSizes.html"
---

# IGetTemplateSizes Method (ISldWorks)

Gets the sheet properties from a template document.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTemplateSizes( _
   ByVal FileName As System.String, _
   ByRef PaperSize As System.Integer, _
   ByRef Width As System.Double, _
   ByRef Height As System.Double _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Boolean

value = instance.IGetTemplateSizes(FileName, PaperSize, Width, Height)
```

### C#

```csharp
System.bool IGetTemplateSizes(
   System.string FileName,
   out System.int PaperSize,
   out System.double Width,
   out System.double Height
)
```

### C++/CLI

```cpp
System.bool IGetTemplateSizes(
   System.String^ FileName,
   [Out] System.int PaperSize,
   [Out] System.double Width,
   [Out] System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of template with full directory path
- `PaperSize`: Paper size as defined in [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)
- `Width`: Custom paper width if PaperSize is set to swDwgPapersUserDefined
- `Height`: Custom paper height if PaperSize is set to swDwgPapersUserDefined

### Return Value

True if the operation is successful, false if not

## VBA Syntax

See [SldWorks::IGetTemplateSizes](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~IGetTemplateSizes.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetTemplateSizes.html)
[ISldWorks::GetDocumentTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate.html)
[ISldWorks::PreSelectDwgTemplateSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreSelectDwgTemplateSize.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
