---
title: "DatumLength Property (IDimXpertDimensionOption)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertDimensionOption"
member: "DatumLength"
kind: "property"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption~DatumLength.html"
---

# DatumLength Property (IDimXpertDimensionOption)

Gets and sets the leader length of the datum.

## Syntax

### Visual Basic (Declaration)

```vb
Property DatumLength As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertDimensionOption
Dim value As System.Double

instance.DatumLength = value

value = instance.DatumLength
```

### C#

```csharp
System.double DatumLength {get; set;}
```

### C++/CLI

```cpp
property System.double DatumLength {
   System.double get();
   void set (    System.double value);
}
```

### Property Value

Length of datum leader in meters.

## VBA Syntax

See [DimXpertDimensionOption::DatumLength](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertDimensionOption~DatumLength.html).

## Examples

[Get and Set Datum Example (C#)](Get_and_Set_Datum_Example_CSharp.htm)
[Get and Set Datum Example (VB.NET)](Get_and_Set_Datum_Example_VBNET.htm)
[Get and Set Datum Example (VBA)](Get_and_Set_Datum_Example_VB.htm)

## See Also

[IDimXpertDimensionOption Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption.html)
[IDimXpertDimensionOption Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertDimensionOption_members.html)
[IDimXpertPart::InsertDatum Method](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertDatum.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
