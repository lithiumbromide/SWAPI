---
title: "IsFreeState Method (IDimXpertAnnotation)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation"
member: "IsFreeState"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation~IsFreeState.html"
---

# IsFreeState Method (IDimXpertAnnotation)

Gets whether this annotation is in a free state.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsFreeState() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAnnotation
Dim value As System.Boolean

value = instance.IsFreeState()
```

### C#

```csharp
System.bool IsFreeState()
```

### C++/CLI

```cpp
System.bool IsFreeState();
```

### Return Value

True if the tolerance is in a free state; false otherwise

## VBA Syntax

See [DimXpertAnnotation::IsFreeState](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAnnotation~IsFreeState.html).

## Remarks

This tolerance modifier is set by clicking the F option at the top of the Geometric Tolerance Properties dialog (invoked from the Geometric Tolerance icon on the DimXpert tool bar).

## See Also

[IDimXpertAnnotation Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)
[IDimXpertAnnotation Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
