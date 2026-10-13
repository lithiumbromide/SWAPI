---
title: "InsertDatum Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "InsertDatum"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertDatum.html"
---

# InsertDatum Method (IDimXpertPart)

Inserts a datum for the selected face.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertDatum( _
   ByVal Option As DimXpertDimensionOption _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Option As DimXpertDimensionOption
Dim value As System.Boolean

value = instance.InsertDatum(Option)
```

### C#

```csharp
System.bool InsertDatum(
   DimXpertDimensionOption Option
)
```

### C++/CLI

```cpp
System.bool InsertDatum(
   DimXpertDimensionOption^ Option
)
```

### Parameters

- `Option`: [IDimXpertDimensionOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption.html)

### Return Value

True if datum is created, false if not

## VBA Syntax

See [DimXpertPart::InsertDatum](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~InsertDatum.html).

## Examples

[Get and Set Datum (C#)](Get_and_Set_Datum_Example_CSharp.htm)
[Get and Set Datum (VB.NET)](Get_and_Set_Datum_Example_VBNET.htm)
[Get and Set Datum (VBA)](Get_and_Set_Datum_Example_VB.htm)

## Remarks

Before calling this method:

1. Call [IDimXpertPart::GetDimOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPart~GetDimOption.html) to get an instance of IDimXpertDimensionOption.
2. Set [IDimXpertDimensionOption::FeatureSelectorOptions](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption~FeatureSelectorOptions.html).
3. Populate Option with the instance of IDimXpertDimensionOption.
4. Select a face to which to attach the datum.

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)
[IDimXpertPart::AutoDimensionScheme Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~AutoDimensionScheme.html)
[IDimXpertPart::InsertBasicDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)
[IDimXpertPart::InsertLocationDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertLocationDimension.html)
[IDimXpertPart::InsertPattern Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertPattern.html)
[IDimXpertPart::InsertSizeDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertSizeDimension.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
