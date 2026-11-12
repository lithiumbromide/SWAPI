---
title: "DimensionPositionOption Property (IDimXpertDimensionOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDimensionOption"
member: "DimensionPositionOption"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption~DimensionPositionOption.html"
---

# DimensionPositionOption Property (IDimXpertDimensionOption)

Obsolete. Superseded by [IDimXpertDimensionOption::DimensionPositionOption2](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption~DimensionPositionOption2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Property DimensionPositionOption As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDimensionOption
Dim value As System.Integer

instance.DimensionPositionOption = value

value = instance.DimensionPositionOption
```

### C#

```csharp
System.int DimensionPositionOption {get; set;}
```

### C++/CLI

```cpp
property System.int DimensionPositionOption {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

0, 1, or 2 (see **Remarks**)

## VBA Syntax

See [DimXpertDimensionOption::DimensionPositionOption](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDimensionOption~DimensionPositionOption.html).

## Remarks

This property sets or returns:

- 0 to use a normal axis to dimension the location of a face with respect to its locating feature.
- 1 to use the horizontal axis to dimension the location of a face with respect to its locating feature.
- 2 to use the vertical axis to dimension the location of a face with respect to its locating feature.

## See Also

[IDimXpertDimensionOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption.html)
[IDimXpertDimensionOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption_members.html)
[IDimXpertPart::InsertLocationDimension Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertLocationDimension.html)
[IDimXpertPart::InsertBasicDimension Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
