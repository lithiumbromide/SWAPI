---
title: "InsertSizeDimension Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "InsertSizeDimension"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertSizeDimension.html"
---

# InsertSizeDimension Method (IDimXpertPart)

Inserts a size dimension for the selected face or edge.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertSizeDimension( _
   ByVal Option As DimXpertDimensionOption _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Option As DimXpertDimensionOption
Dim value As System.Boolean

value = instance.InsertSizeDimension(Option)
```

### C#

```csharp
System.bool InsertSizeDimension(
   DimXpertDimensionOption Option
)
```

### C++/CLI

```cpp
System.bool InsertSizeDimension(
   DimXpertDimensionOption^ Option
)
```

### Parameters

- `Option`: [IDimXpertDimensionOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption.html)

### Return Value

True if size dimension is created, false if not

## VBA Syntax

See [DimXpertPart::InsertSizeDimension](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~InsertSizeDimension.html).

## Examples

[Get and Set Size Dimension (C#)](Get_and_Set_Size_Dimension_Example_CSharp.htm)
[Get and Set Size Dimension (VB.NET)](Get_and_Set_Size_Dimension_Example_VBNET.htm)
[Get and Set Size Dimension (VBA)](Get_and_Set_Size_Dimension_Example_VB.htm)

## Remarks

Before calling this method:

1. Call [IDimXpertPart::GetDimOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetDimOption.html) to get an instance of IDimXpertDimensionOption.
2. Set [IDimXpertDimensionOption::TextPosition](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption~TextPosition.html) and/or [IDimXpertDimensionOption::FeatureSelectorOptions](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption~FeatureSelectorOptions.html).
3. Populate Option with the instance of IDimXpertDimensionOption.
4. Select a face or edge.

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)
[IDimXpertPart::AutoDimensionScheme Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~AutoDimensionScheme.html)
[IDimXpertPart::InsertBasicDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)
[IDimXpertPart::InsertDatum Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertDatum.html)
[IDimXpertPart::InsertLocationDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertLocationDimension.html)
[IDimXpertPart::InsertPattern Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertPattern.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
