---
title: "FeatureSelectorOptions Property (IDimXpertDimensionOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDimensionOption"
member: "FeatureSelectorOptions"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption~FeatureSelectorOptions.html"
---

# FeatureSelectorOptions Property (IDimXpertDimensionOption)

Gets and sets the type of feature to dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Property FeatureSelectorOptions As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDimensionOption
Dim value As System.Object

instance.FeatureSelectorOptions = value

value = instance.FeatureSelectorOptions
```

### C#

```csharp
System.object FeatureSelectorOptions {get; set;}
```

### C++/CLI

```cpp
property System.Object^ FeatureSelectorOptions {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

Array of long values as defined in [swDimXpertFeatureSelectorOption_e](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertFeatureSelectorOption_e.html); however, only the first element in the array is used; all of the other elements, if any, in the array are ignored

## VBA Syntax

See [DimXpertDimensionOption::FeatureSelectorOptions](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDimensionOption~FeatureSelectorOptions.html).

## Examples

[Get and Set Pattern Example (C#)](Get_and_Set_Pattern_Example_CSharp.htm)
[Get and Set Pattern Example (VB.NET)](Get_and_Set_Pattern_Example_VBNET.htm)
[Get and Set Pattern Example (VBA)](Get_and_Set_Pattern_Example_VB.htm)

## Remarks

Use this property to set the type of feature to dimension. For example, if you select a hole face and you want that face to be dimensioned as a cylinder, then make [swDimXpertFeatureSelectorOption_e.swDimXpertFeatureSelectorOption_Cylinder](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.swDimXpertFeatureSelectorOption_e.html) the first element in the FeatureSelectorOptions array.

## See Also

[IDimXpertDimensionOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption.html)
[IDimXpertDimensionOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption_members.html)
[IDimXpertPart::InsertDatum Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertDatum.html)
[IDimXpertPart::InsertSizeDimension Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertSizeDimension.html)
[IDimXpertPart::InsertPattern Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertPattern.html)
[IDimXpertPart::InsertBasicDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
