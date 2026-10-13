---
title: "GetModelFeature Method (IDimXpertAnnotation)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation"
member: "GetModelFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation~GetModelFeature.html"
---

# GetModelFeature Method (IDimXpertAnnotation)

Gets the underlying DimXpert model feature that corresponds to this geometric, dimensioning, and tolerancing annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelFeature() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAnnotation
Dim value As System.Object

value = instance.GetModelFeature()
```

### C#

```csharp
System.object GetModelFeature()
```

### C++/CLI

```cpp
System.Object^ GetModelFeature();
```

### Return Value

[IFeature](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)

## VBA Syntax

See [DimXpertAnnotation::GetModelFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAnnotation~GetModelFeature.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertAnnotation Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)
[IDimXpertAnnotation Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
