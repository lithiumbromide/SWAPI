---
title: "GetTemplateSizes Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "GetTemplateSizes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetTemplateSizes.html"
---

# GetTemplateSizes Method (ISldWorks)

Gets the sheet properties from a template document.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTemplateSizes( _
   ByVal FileName As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim FileName As System.String
Dim value As System.Object

value = instance.GetTemplateSizes(FileName)
```

### C#

```csharp
System.object GetTemplateSizes(
   System.string FileName
)
```

### C++/CLI

```cpp
System.Object^ GetTemplateSizes(
   System.String^ FileName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FileName`: Name of template with full directory path

### Return Value

Array of 3 doubles containing the paper size, width, and height

## VBA Syntax

See [SldWorks::GetTemplateSizes](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~GetTemplateSizes.html).

## Examples

[Get Drawing Template Size (VBA)](Get_Drawing_Template_Size_Example_VB.htm)

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::IGetTemplateSizes Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~IGetTemplateSizes.html)
[ISldWorks::GetDocumentTemplate Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetDocumentTemplate.html)
[ISldWorks::PreSelectDwgTemplateSize Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PreSelectDwgTemplateSize.html)

## Availability

SOLIDWORKS 2001 FCS, Revision Number 9.0
