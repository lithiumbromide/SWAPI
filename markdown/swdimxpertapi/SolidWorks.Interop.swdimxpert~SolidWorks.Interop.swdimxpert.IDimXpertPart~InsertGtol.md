---
title: "InsertGtol Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "InsertGtol"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~InsertGtol.html"
---

# InsertGtol Method (IDimXpertPart)

Inserts the specified Gtol annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function InsertGtol( _
   ByVal Type As System.Integer _
) As DimXpertAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Type As System.Integer
Dim value As DimXpertAnnotation

value = instance.InsertGtol(Type)
```

### C#

```csharp
DimXpertAnnotation InsertGtol(
   System.int Type
)
```

### C++/CLI

```cpp
DimXpertAnnotation^ InsertGtol(
   System.int Type
)
```

### Parameters

- `Type`: Type of Gtol to insert as defined in [swDimXpertGtolType_e](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.swDimXpertGtolType_e.html)

### Return Value

[IDimXpertAnnotation](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)

## VBA Syntax

See [DimXpertPart::InsertGtol](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~InsertGtol.html).

## Remarks

Before calling this method, select the leader attachment points.

This method creates an empty Gtol symbol with a default value of 0.02 for Tolerance 1. To fill in the text and symbols, get the underlying SOLIDWORKS Gtol object and use [IGtol::SetFrameSymbols2](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.html) and [IGtol::SetFrameValues2](ms-its:sldworksapi.chm::/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues2.html) to change frame symbols and values.

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
