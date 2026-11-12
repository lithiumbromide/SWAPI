---
title: "GetAutoDimSchemeOption Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "GetAutoDimSchemeOption"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~GetAutoDimSchemeOption.html"
---

# GetAutoDimSchemeOption Method (IDimXpertPart)

Gets options for creation of an Auto Dimension Scheme.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAutoDimSchemeOption() As DimXpertAutoDimSchemeOption
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim value As DimXpertAutoDimSchemeOption

value = instance.GetAutoDimSchemeOption()
```

### C#

```csharp
DimXpertAutoDimSchemeOption GetAutoDimSchemeOption()
```

### C++/CLI

```cpp
DimXpertAutoDimSchemeOption^ GetAutoDimSchemeOption();
```

### Return Value

[IDimXpertAutoDimSchemeOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAutoDimSchemeOption.html)

## VBA Syntax

See [DimXpertPart::GetAutoDimSchemeOption](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~GetAutoDimSchemeOption.html).

## Examples

[Auto Dimension Scheme (C#)](Auto_Dimension_Scheme_Example_CSharp.htm)
[Auto Dimension Scheme (VB.NET)](Auto_Dimension_Scheme_Example_VBNET.htm)
[Auto Dimension Scheme (VBA)](Auto_Dimension_Scheme_Example_VB.htm)

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)
[IDimXpertPart::AutoDimensionScheme Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~AutoDimensionScheme.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
