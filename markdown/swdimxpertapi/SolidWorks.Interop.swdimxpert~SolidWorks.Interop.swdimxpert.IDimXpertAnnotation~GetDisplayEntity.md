---
title: "GetDisplayEntity Method (IDimXpertAnnotation)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation"
member: "GetDisplayEntity"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation~GetDisplayEntity.html"
---

# GetDisplayEntity Method (IDimXpertAnnotation)

Gets the SOLIDWORKS annotation representing this DimXpert annotation.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetDisplayEntity() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAnnotation
Dim value As System.Object

value = instance.GetDisplayEntity()
```

### C#

```csharp
System.object GetDisplayEntity()
```

### C++/CLI

```cpp
System.Object^ GetDisplayEntity();
```

### Return Value

[IAnnotation](ms-its:sldworksapi.chm::/Solidworks.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAnnotation.html)

## VBA Syntax

See [DimXpertAnnotation::GetDisplayEntity](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAnnotation~GetDisplayEntity.html).

## Examples

[Get DimXpert Tolerance Example (VBA)](Get_DimXpert_Tolerance_Example_VB.htm)
[Get DimXpert Tolerance Example (VB.NET)](Get_DimXpert_Tolerance_Example_VBNET.htm)

## See Also

[IDimXpertAnnotation Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)
[IDimXpertAnnotation Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
