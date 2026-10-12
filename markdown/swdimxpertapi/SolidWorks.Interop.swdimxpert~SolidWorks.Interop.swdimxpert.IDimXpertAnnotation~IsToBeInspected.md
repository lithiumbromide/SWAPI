---
title: "IsToBeInspected Method (IDimXpertAnnotation)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertAnnotation"
member: "IsToBeInspected"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation~IsToBeInspected.html"
---

# IsToBeInspected Method (IDimXpertAnnotation)

Gets whether this annotation is to be inspected.

## Syntax

### Visual Basic (Declaration)

```vb
Function IsToBeInspected() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertAnnotation
Dim value As System.Boolean

value = instance.IsToBeInspected()
```

### C#

```csharp
System.bool IsToBeInspected()
```

### C++/CLI

```cpp
System.bool IsToBeInspected();
```

### Return Value

True if to be inspected; false otherwise

## VBA Syntax

See [DimXpertAnnotation::IsToBeInspected](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertAnnotation~IsToBeInspected.html).

## Remarks

This tolerance modifier is set by clicking the second option from the right on the Dimension Text section of the DimXpert Properties manager.

## See Also

[IDimXpertAnnotation Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation.html)
[IDimXpertAnnotation Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertAnnotation_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
