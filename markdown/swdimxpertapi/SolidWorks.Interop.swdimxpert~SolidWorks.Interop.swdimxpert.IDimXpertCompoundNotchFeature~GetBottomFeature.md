---
title: "GetBottomFeature Method (IDimXpertCompoundNotchFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundNotchFeature"
member: "GetBottomFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundNotchFeature~GetBottomFeature.html"
---

# GetBottomFeature Method (IDimXpertCompoundNotchFeature)

Gets the bottom DimXpert feature for this DimXpert compound notch.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBottomFeature() As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundNotchFeature
Dim value As DimXpertFeature

value = instance.GetBottomFeature()
```

### C#

```csharp
DimXpertFeature GetBottomFeature()
```

### C++/CLI

```cpp
DimXpertFeature^ GetBottomFeature();
```

### Return Value

[IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

## VBA Syntax

See [DimXpertCompoundNotchFeature::GetBottomFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundNotchFeature~GetBottomFeature.html).

## Remarks

Only blind notches have bottom features. The bottom feature of a blind notch is a [DimXpert plane feature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertPlaneFeature.html) in which the plane is perpendicular to the notch axis.

## See Also

[IDimXpertCompoundNotchFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundNotchFeature.html)
[IDimXpertCompoundNotchFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundNotchFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
