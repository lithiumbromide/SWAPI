---
title: "GetFeature Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "GetFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~GetFeature.html"
---

# GetFeature Method (IDimXpertPart)

Gets a DimXpert feature by name for the given model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature( _
   ByVal Name As System.String _
) As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Name As System.String
Dim value As DimXpertFeature

value = instance.GetFeature(Name)
```

### C#

```csharp
DimXpertFeature GetFeature(
   System.string Name
)
```

### C++/CLI

```cpp
DimXpertFeature^ GetFeature(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of a DimXpert feature

### Return Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertPart::GetFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~GetFeature.html).

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
