---
title: "InsertLocationDimension Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "InsertLocationDimension"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertLocationDimension.html"
---

# InsertLocationDimension Method (IDimXpertPart)

Inserts a linear or angular location dimension between a selected feature and its locating feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertLocationDimension( _
   ByVal Option As DimXpertDimensionOption _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Option As DimXpertDimensionOption
Dim value As System.Boolean

value = instance.InsertLocationDimension(Option)
```

### C#

```csharp
System.bool InsertLocationDimension(
   DimXpertDimensionOption Option
)
```

### C++/CLI

```cpp
System.bool InsertLocationDimension(
   DimXpertDimensionOption^ Option
)
```

### Parameters

- `Option`: [IDimXpertDimensionOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption.html) or Null to dimension the location of the face along an axis normal to the locating feature and to place the dimension text at a default position

### Return Value

True if location dimension is created, false if not

## VBA Syntax

See [DimXpertPart::InsertLocationDimension](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~InsertLocationDimension.html).

## Examples

[Get and Set Location Dimension (C#)](Get_and_Set_Location_Dimension_Example_CSharp.htm)
[Get and Set Location Dimension (VB.NET)](Get_and_Set_Location_Dimension_Example_VBNET.htm)
[Get and Set Location Dimension (VBA)](Get_and_Set_Location_Dimension_Example_VB.htm)

## Remarks

Before calling this method:

1. Call [IDimXpertPart::GetDimOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetDimOption.html) to get an instance of IDimXpertDimensionOption.
2. For distance-between dimensions, set [IDimXpertDimensionOption::TextPosition](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption~TextPosition.html) or [IDimXpertDimensionOption::DimensionPositionOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption~DimensionPositionOption.html) (if both are set, only DimensionPositionOption is in force). For angle-between dimensions, set [IDimXpertDimensionOption::TextPosition](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption~TextPosition.html).
3. Populate Option with the instance of IDimXpertDimensionOption.
4. Multi-select:

  1. Origin Feature
  2. Tolerance (locating) Feature

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)
[IDimXpertPart::AutoDimensionScheme Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~AutoDimensionScheme.html)
[IDimXpertPart::InsertBasicDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)
[IDimXpertPart::InsertDatum Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertDatum.html)
[IDimXpertPart::InsertPattern Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertPattern.html)
[IDimXpertPart::InsertSizeDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertSizeDimension.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
