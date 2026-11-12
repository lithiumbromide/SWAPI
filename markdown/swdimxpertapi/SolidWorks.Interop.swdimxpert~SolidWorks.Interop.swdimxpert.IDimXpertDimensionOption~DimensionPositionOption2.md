---
title: "DimensionPositionOption2 Property (IDimXpertDimensionOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDimensionOption"
member: "DimensionPositionOption2"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption~DimensionPositionOption2.html"
---

# DimensionPositionOption2 Property (IDimXpertDimensionOption)

Gets and sets the reference axis with which to dimension the location of a face with respect to another locating feature.

## Syntax

### Visual Basic (Declaration)

```vb
Property DimensionPositionOption2 As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDimensionOption
Dim value As System.Integer

instance.DimensionPositionOption2 = value

value = instance.DimensionPositionOption2
```

### C#

```csharp
System.int DimensionPositionOption2 {get; set;}
```

### C++/CLI

```cpp
property System.int DimensionPositionOption2 {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Reference axis as defined in [swDimXpertDimensionPositionOption_e](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.swDimXpertDimensionPositionOption_e.html)

## VBA Syntax

See [DimXpertDimensionOption::DimensionPositionOption2](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDimensionOption~DimensionPositionOption2.html).

## Examples

[Get and Set Location Dimension (VBA)](Get_and_Set_Location_Dimension_Example_VB.htm)
[Get and Set Location Dimension (VB.NET)](Get_and_Set_Location_Dimension_Example_VBNET.htm)
[Get and Set Location Dimension (C#)](Get_and_Set_Location_Dimension_Example_CSharp.htm)

## See Also

[IDimXpertDimensionOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption.html)
[IDimXpertDimensionOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption_members.html)
[IDimXpertPart::InsertLocationDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertLocationDimension.html)
[IDimXpertPart::InsertBasicDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
