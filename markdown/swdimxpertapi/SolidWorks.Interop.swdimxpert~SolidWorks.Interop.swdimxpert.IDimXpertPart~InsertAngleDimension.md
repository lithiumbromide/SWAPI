---
title: "InsertAngleDimension Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "InsertAngleDimension"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertAngleDimension.html"
---

# InsertAngleDimension Method (IDimXpertPart)

Inserts an angle dimension.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertAngleDimension( _
   ByVal Option As DimXpertDimensionOption _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Option As DimXpertDimensionOption
Dim value As System.Boolean

value = instance.InsertAngleDimension(Option)
```

### C#

```csharp
System.bool InsertAngleDimension(
   DimXpertDimensionOption Option
)
```

### C++/CLI

```cpp
System.bool InsertAngleDimension(
   DimXpertDimensionOption^ Option
)
```

### Parameters

- `Option`: [IDimXpertDimensionOption](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDimensionOption.html)

### Return Value

True if the angle dimension is created, false if not

## VBA Syntax

See [DimXpertPart::InsertAngleDimension](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~InsertAngleDimension.html).

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)
[IDimXpertPart::InsertBasicDimension Method ()](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertBasicDimension.html)

## Availability

SOLIDWORKS 2026 SP02, Revision Number 34.2
