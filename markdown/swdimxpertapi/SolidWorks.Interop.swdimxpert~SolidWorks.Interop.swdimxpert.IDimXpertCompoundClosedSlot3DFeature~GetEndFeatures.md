---
title: "GetEndFeatures Method (IDimXpertCompoundClosedSlot3DFeature)"
project: "SOLIDWORKS DimXpert API Help"
interface: "IDimXpertCompoundClosedSlot3DFeature"
member: "GetEndFeatures"
kind: "method"
source: "swdimxpertapi/SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature~GetEndFeatures.html"
---

# GetEndFeatures Method (IDimXpertCompoundClosedSlot3DFeature)

Gets the closed end features of this DimXpert compound closed slot.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetEndFeatures( _
   ByRef End1 As DimXpertFeature, _
   ByRef End2 As DimXpertFeature _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDimXpertCompoundClosedSlot3DFeature
Dim End1 As DimXpertFeature
Dim End2 As DimXpertFeature
Dim value As System.Boolean

value = instance.GetEndFeatures(End1, End2)
```

### C#

```csharp
System.bool GetEndFeatures(
   out DimXpertFeature End1,
   out DimXpertFeature End2
)
```

### C++/CLI

```cpp
System.bool GetEndFeatures(
   [Out] DimXpertFeature^ End1,
   [Out] DimXpertFeature^ End2
)
```

### Parameters

- `End1`: [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)
- `End2`: [IDimXpertFeature](SOLIDWORKS.Interop.swdimxpert~SOLIDWORKS.Interop.swdimxpert.IDimXpertFeature.html)

### Return Value

True if method call is successful; false otherwise

## VBA Syntax

See [DimXpertCompoundClosedSlot3DFeature::GetEndFeatures](ms-its:swdimxpertapivb6.chm::/swdimxpert~DimXpertCompoundClosedSlot3DFeature~GetEndFeatures.html).

## See Also

[IDimXpertCompoundClosedSlot3DFeature Interface](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature.html)
[IDimXpertCompoundClosedSlot3DFeature Members](SolidWorks.Interop.swdimxpert~SolidWorks.Interop.swdimxpert.IDimXpertCompoundClosedSlot3DFeature_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
