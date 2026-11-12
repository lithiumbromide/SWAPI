---
title: "PreSelectDwgTemplateSize Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "PreSelectDwgTemplateSize"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreSelectDwgTemplateSize.html"
---

# PreSelectDwgTemplateSize Method (ISldWorks)

Establishes which template to use when creating a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
Sub PreSelectDwgTemplateSize( _
   ByVal TemplateToUse As System.Integer, _
   ByVal TemplateName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim TemplateToUse As System.Integer
Dim TemplateName As System.String

instance.PreSelectDwgTemplateSize(TemplateToUse, TemplateName)
```

### C#

```csharp
void PreSelectDwgTemplateSize(
   System.int TemplateToUse,
   System.string TemplateName
)
```

### C++/CLI

```cpp
void PreSelectDwgTemplateSize(
   System.int TemplateToUse,
   System.String^ TemplateName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `TemplateToUse`: Type of template to use as defined in [swDwgTemplates_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDwgTemplates_e.html)
- `TemplateName`: Reserved for future use; use NULL

## VBA Syntax

See [SldWorks::PreSelectDwgTemplateSize](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~PreSelectDwgTemplateSize.html).

## Remarks

By calling this method and specifying a template size, no dialog appears when the end-user interactively selects File, New, Drawing.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetDocumentTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate.html)
[ISldWorks::GetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetTemplateSizes.html)
[ISldWorks::IGetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetTemplateSizes.html)
