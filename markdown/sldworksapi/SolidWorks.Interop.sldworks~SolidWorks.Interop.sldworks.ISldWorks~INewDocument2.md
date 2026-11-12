---
title: "INewDocument2 Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "INewDocument2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~INewDocument2.html"
---

# INewDocument2 Method (ISldWorks)

Creates a new document based on the specified template.

## Syntax

### Visual Basic (Declaration)

```vb
Function INewDocument2( _
   ByVal TemplateName As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim TemplateName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As ModelDoc2

value = instance.INewDocument2(TemplateName, PaperSize, Width, Height)
```

### C#

```csharp
ModelDoc2 INewDocument2(
   System.string TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

### C++/CLI

```cpp
ModelDoc2^ INewDocument2(
   System.String^ TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TemplateName`: Name of the template to use for creating the new document
- `PaperSize`: Size of paper as defined in [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)
- `Width`: Width of paper; used only when PaperSize is swDwgPapersUserDefined
- `Height`: Height of paper; used only when PaperSize is swDwgPapersUserDefined

### Return Value

Newly created [document](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html) or NULL if the operation fails

## VBA Syntax

See [SldWorks::INewDocument2](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~INewDocument2.html).

## Examples

[Access Assembly (C++)](Access_Assembly_Example_CPlusPlus_COM.htm)

## Remarks

To get the default template filename, use [ISldWorks::GetUserPreferenceStringValue](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~GetUserPreferenceStringValue.html):

- for parts: swDefaultTemplatePart
- for assemblies: swDefaultTemplateAssembly
- for drawings: swDefaultTemplateDrawing

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetDocumentTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate.html)
[ISldWorks::NewDocument Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~NewDocument.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
