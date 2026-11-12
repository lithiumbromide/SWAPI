---
title: "GetAnnotations Method (IDimXpertPart)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertPart"
member: "GetAnnotations"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart~GetAnnotations.html"
---

# GetAnnotations Method (IDimXpertPart)

Gets all of the DimXpert annotations in the model.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertPart
Dim value As System.Object

value = instance.GetAnnotations()
```

### C#

```csharp
System.object GetAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetAnnotations();
```

### Return Value

Array of [IDimXpertAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation.html)s

## VBA Syntax

See [DimXpertPart::GetAnnotations](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertPart~GetAnnotations.html).

## See Also

[IDimXpertPart Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart.html)
[IDimXpertPart Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertPart_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
