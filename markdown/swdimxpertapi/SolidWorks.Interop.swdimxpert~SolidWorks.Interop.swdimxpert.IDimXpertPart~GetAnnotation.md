---
title: "GetAnnotation Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "GetAnnotation"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~GetAnnotation.html"
---

# GetAnnotation Method (IDimXpertPart)

Gets a DimXpert annotation by name for the given model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotation( _
   ByVal Name As System.String _
) As DimXpertAnnotation
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim Name As System.String
Dim value As DimXpertAnnotation

value = instance.GetAnnotation(Name)
```

### C#

```csharp
DimXpertAnnotation GetAnnotation(
   System.string Name
)
```

### C++/CLI

```cpp
DimXpertAnnotation^ GetAnnotation(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the annotation

### Return Value

[IDimXpertAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation.html)

## VBA Syntax

See [DimXpertPart::GetAnnotation](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~GetAnnotation.html).

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
