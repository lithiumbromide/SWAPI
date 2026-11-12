---
title: "GetAppliedAnnotations Method (IDimXpertAnnotation)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation"
member: "GetAppliedAnnotations"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation~GetAppliedAnnotations.html"
---

# GetAppliedAnnotations Method (IDimXpertAnnotation)

Gets all of the annotations that reference this DimXpert annotation (datum).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetAppliedAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAnnotation
Dim value As System.Object

value = instance.GetAppliedAnnotations()
```

### C#

```csharp
System.object GetAppliedAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetAppliedAnnotations();
```

### Return Value

Array of [IDimXpertAnnotation](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertAnnotation.html)s

## VBA Syntax

See [DimXpertAnnotation::GetAppliedAnnotations](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAnnotation~GetAppliedAnnotations.html).

## Remarks

Currently, this method works only for annotations of type [IDimXpertDatum](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertDatum.html).

## See Also

[IDimXpertAnnotation Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)
[IDimXpertAnnotation Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
