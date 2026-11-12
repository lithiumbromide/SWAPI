---
title: "AutoDimensionScheme Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "AutoDimensionScheme"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~AutoDimensionScheme.html"
---

# AutoDimensionScheme Method (IDimXpertPart)

Creates an Auto Dimension Scheme.

## Syntax

### Visual Basic (Declaration)

```vb
Function AutoDimensionScheme( _
   ByVal Option As DimXpertAutoDimSchemeOption _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Option As DimXpertAutoDimSchemeOption
Dim value As System.Boolean

value = instance.AutoDimensionScheme(Option)
```

### C#

```csharp
System.bool AutoDimensionScheme(
   DimXpertAutoDimSchemeOption Option
)
```

### C++/CLI

```cpp
System.bool AutoDimensionScheme(
   DimXpertAutoDimSchemeOption^ Option
)
```

### Parameters

- `Option`: [IDimXpertAutoDimSchemeOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAutoDimSchemeOption.html)

### Return Value

True if Auto Dimension Scheme is created, false if not

## VBA Syntax

See [DimXpertPart::AutoDimensionScheme](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~AutoDimensionScheme.html).

## Examples

[Auto Dimension Scheme (C#)](Auto_Dimension_Scheme_Example_CSharp.htm)
[Auto Dimension Scheme (VB.NET)](Auto_Dimension_Scheme_Example_VBNET.htm)
[Auto Dimension Scheme (VBA)](Auto_Dimension_Scheme_Example_VB.htm)

## Remarks

Before calling this method, call [IDimXpertPart::GetAutoDimSchemeOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetAutoDimSchemeOption.html) to populate the Option parameter.

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)
[IDimXpertPart::InsertBasicDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)
[IDimXpertPart::InsertDatum Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertDatum.html)
[IDimXpertPart::InsertLocationDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertLocationDimension.html)
[IDimXpertPart::InsertPattern Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertPattern.html)
[IDimXpertPart::InsertSizeDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertSizeDimension.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
