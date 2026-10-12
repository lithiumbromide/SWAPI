---
title: "IsStatistical Method (IDimXpertAnnotation)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation"
member: "IsStatistical"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation~IsStatistical.html"
---

# IsStatistical Method (IDimXpertAnnotation)

Gets whether this annotation is statistical.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsStatistical() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAnnotation
Dim value As System.Boolean

value = instance.IsStatistical()
```

### C#

```csharp
System.bool IsStatistical()
```

### C++/CLI

```cpp
System.bool IsStatistical();
```

### Return Value

True if the tolerance is statistical; false otherwise

## VBA Syntax

See [DimXpertAnnotation::IsStatistical](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAnnotation~IsStatistical.html).

## Remarks

This tolerance modifier is set by clicking the ST option at the top of the Geometric Tolerance Properties dialog (invoked from the Geometric Tolerance icon on the DimXpert tool bar).

## See Also

[IDimXpertAnnotation Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)
[IDimXpertAnnotation Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
