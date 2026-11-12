---
title: "GetDocumentTemplate Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetDocumentTemplate"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate.html"
---

# GetDocumentTemplate Method (ISldWorks)

Gets the name of document template that can be used in [ISldWorks::NewDocument](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~NewDocument.html) or [ISldWorks::INewDocument2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~INewDocument2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDocumentTemplate( _
   ByVal Mode As System.Integer, _
   ByVal TemplateName As System.String, _
   ByVal PaperSize As System.Integer, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Mode As System.Integer
Dim TemplateName As System.String
Dim PaperSize As System.Integer
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.String

value = instance.GetDocumentTemplate(Mode, TemplateName, PaperSize, Width, Height)
```

### C#

```csharp
System.string GetDocumentTemplate(
   System.int Mode,
   System.string TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

### C++/CLI

```cpp
System.String^ GetDocumentTemplate(
   System.int Mode,
   System.String^ TemplateName,
   System.int PaperSize,
   System.double Width,
   System.double Height
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Mode`: Document type as defined in [swDocumentTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDocumentTypes_e.html) (see Remarks)
- `TemplateName`: Name of custom template including full directory path
- `PaperSize`: Size of paper as defined in [swDwgPaperSizes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgPaperSizes_e.html)
- `Width`: Width of paper; used only when paperSize is swDwgPapersUserDefined
- `Height`: Height of paper; used only when paperSize is swDwgPapersUserDefined

### Return Value

Name of the selected document template

## VBA Syntax

See [SldWorks::GetDocumentTemplate](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetDocumentTemplate.html).

## Examples

[Get Locations and Names of Document Templates (VBA)](Get_Locations_and_Names_of_Document_Templates_Example_VB.htm)

## Remarks

| If type is... | Then... |
| --- | --- |
| swDocPART or swDocASSEMBLY | Remaining arguments are not used. |
| swDocDRAWING | Remaining arguments are used to determine which drawing template to use. |

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetTemplateSizes.html)
[ISldWorks::IGetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetTemplateSizes.html)
[ISldWorks::PreSelectDwgTemplateSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreSelectDwgTemplateSize.html)

## Availability

SOLIDWORKS 2001Plus SP4, Revision Number 10.4
