---
title: "GetDirections Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "GetDirections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetDirections.html"
---

# GetDirections Method (ICWDynamicInitialCondition)

Obsolete. Superseded by [ICWDynamicInitialCondition::GetDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetDirections2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetDirections( _
   ByRef BDir1 As System.Integer, _
   ByRef BDir2 As System.Integer, _
   ByRef BDir3 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim BDir1 As System.Integer
Dim BDir2 As System.Integer
Dim BDir3 As System.Integer

instance.GetDirections(BDir1, BDir2, BDir3)
```

### C#

```csharp
void GetDirections(
   out System.int BDir1,
   out System.int BDir2,
   out System.int BDir3
)
```

### C++/CLI

```cpp
void GetDirections(
   [Out] System.int BDir1,
   [Out] System.int BDir2,
   [Out] System.int BDir3
)
```

### Parameters

- `BDir1`: 1 if initial condition is applied along direction 1 (if direction reference is a plane or face) or in a radial direction (if direction reference is a cylindrical face or axis), 0 if not (see **Remarks**)
- `BDir2`: 1 if initial condition is applied along direction 2 (if direction reference is a plane or face) or in a circumferential direction (if direction reference is a cylindrical face or axis), 0 if not (see **Remarks**)
- `BDir3`: 1 if initial condition is applied along the normal (if direction reference is a plane or face), or in an axial direction (if direction reference is a cylindrical face or axis), or along an edge (if direction reference is an edge); 0 if not (see **Remarks**)

## VBA Syntax

See [CWDynamicInitialCondition::GetDirections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicInitialCondition~GetDirections.html).

## Remarks

Call [ICWDynamicInitialCondition::SetDirectionEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirectionEntity.html) to set the direction reference for this initial condition.

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)
[ICWDynamicInitialCondition::SetDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirections.html)
[ICWDynamicInitialCondition::GetReverseDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetReverseDirections.html)
[ICWDynamicInitialCondition::GetValues Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetValues.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
