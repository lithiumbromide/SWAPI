---
title: "GetDimOption Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "GetDimOption"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~GetDimOption.html"
---

# GetDimOption Method (IDimXpertPart)

Gets options for insertion of datums, patterns, and dimensions.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDimOption() As DimXpertDimensionOption
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim value As DimXpertDimensionOption

value = instance.GetDimOption()
```

### C#

```csharp
DimXpertDimensionOption GetDimOption()
```

### C++/CLI

```cpp
DimXpertDimensionOption^ GetDimOption();
```

### Return Value

[IDimXpertDimensionOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption.html)

## VBA Syntax

See [DimXpertPart::GetDimOption](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~GetDimOption.html).

## Examples

[Get and Set Pattern (C#)](Get_and_Set_Pattern_Example_CSharp.htm)
[Get and Set Pattern (VB.NET)](Get_and_Set_Pattern_Example_VBNET.htm)
[Get and Set Pattern (VBA)](Get_and_Set_Pattern_Example_VB.htm)

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)
[IDimXpertPart::InsertDatum Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertDatum.html)
[IDimXpertPart::InsertLocationDimension Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertLocationDimension.html)
[IDimXpertPart::InsertPattern Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertPattern.html)
[IDimXpertPart::InsertSizeDimension Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertSizeDimension.html)
[IDimXpertPart::InsertBasicDimension Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
