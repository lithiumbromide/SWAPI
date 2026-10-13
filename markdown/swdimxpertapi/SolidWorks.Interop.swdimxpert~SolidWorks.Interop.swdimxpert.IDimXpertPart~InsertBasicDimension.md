---
title: "InsertBasicDimension Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "InsertBasicDimension"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html"
---

# InsertBasicDimension Method (IDimXpertPart)

Inserts a basic dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertBasicDimension( _
   ByVal Option As DimXpertDimensionOption _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Option As DimXpertDimensionOption
Dim value As System.Boolean

value = instance.InsertBasicDimension(Option)
```

### C#

```csharp
System.bool InsertBasicDimension(
   DimXpertDimensionOption Option
)
```

### C++/CLI

```cpp
System.bool InsertBasicDimension(
   DimXpertDimensionOption^ Option
)
```

### Parameters

- `Option`: [IDimXpertDimensionOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption.html)

### Return Value

True if the basic dimension is created, false if not

## VBA Syntax

See [DimXpertPart::InsertBasicDimension](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~InsertBasicDimension.html).

## Examples

[Insert Basic Dimension (VBA)](Get_and_Set_Basic_Dimension_Example_VB.htm)
[Insert Basic Dimension (VB.NET)](Get_and_Set_Basic_Dimension_Example_VBNET.htm)
[Insert Basic Dimension (C#)](Get_and_Set_Basic_Dimension_Example_CSharp.htm)

## Remarks

A DimXpert basic dimension is the distance or angle between selected reference features.

Before calling this method:

1. Call [IDimXpertPart::GetDimOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetDimOption.html) to get an instance of IDimXpertDimensionOption.
2. Set:

  - IDimXpertDimensionOption::TextPosition or [IDimXpertDimensionOption::DimensionPositionOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption~DimensionPositionOption.html) (if both are set, only DimensionPositionOption is in force) for distance-between dimensions.
  - [IDimXpertDimensionOption::TextPosition](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption~TextPosition.html) for angle-between dimensions.
3. Populate Option with the instance of IDimXpertDimensionOption.
4. Multi-select reference features using [IModelDocExtension::SelectByID2](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html):

  1. Origin feature (Append = false)
  2. Tolerance feature (Append = true)

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)
[IDimXpertPart::InsertDatum Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertDatum.html)
[IDimXpertPart::InsertLocationDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertLocationDimension.html)
[IDimXpertPart::InsertPattern Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertPattern.html)
[IDimXpertPart::InsertSizeDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertSizeDimension.html)
[IDimXpertPart::AutoDimensionScheme Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~AutoDimensionScheme.html)
[IDimXpertPart::InsertAngleDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertAngleDimension.html)

## Availability

SOLIDWORKS 2016 FCS, Revision Number 24.0
