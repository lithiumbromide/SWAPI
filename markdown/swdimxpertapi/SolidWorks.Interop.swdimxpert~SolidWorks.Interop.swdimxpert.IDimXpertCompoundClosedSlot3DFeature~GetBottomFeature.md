---
title: "GetBottomFeature Method (IDimXpertCompoundClosedSlot3DFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundClosedSlot3DFeature"
member: "GetBottomFeature"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature~GetBottomFeature.html"
---

# GetBottomFeature Method (IDimXpertCompoundClosedSlot3DFeature)

Gets the bottom DimXpert feature for this DimXpert compound closed slot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetBottomFeature() As DimXpertFeature
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundClosedSlot3DFeature
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

See [DimXpertCompoundClosedSlot3DFeature::GetBottomFeature](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundClosedSlot3DFeature~GetBottomFeature.html).

## Remarks

Only blind slots have bottom features. The bottom feature of a blind slot is a DimXpert plane feature in which the plane is perpendicular to the slot axis.

## See Also

[IDimXpertCompoundClosedSlot3DFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature.html)
[IDimXpertCompoundClosedSlot3DFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
