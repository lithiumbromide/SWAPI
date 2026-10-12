---
title: "SetDirections Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "SetDirections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirections.html"
---

# SetDirections Method (ICWDynamicInitialCondition)

Obsolete. Superseded by [ICWDynamicInitialCondition::SetDirections2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirections2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDirections( _
   ByVal BDir1 As System.Integer, _
   ByVal BDir2 As System.Integer, _
   ByVal BDir3 As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim BDir1 As System.Integer
Dim BDir2 As System.Integer
Dim BDir3 As System.Integer

instance.SetDirections(BDir1, BDir2, BDir3)
```

### C#

```csharp
void SetDirections(
   System.int BDir1,
   System.int BDir2,
   System.int BDir3
)
```

### C++/CLI

```cpp
void SetDirections(
   System.int BDir1,
   System.int BDir2,
   System.int BDir3
)
```

### Parameters

- `BDir1`: 1 to set this initial condition along direction 1 (if direction reference is a plane or face) or in a radial direction (if direction reference is a cylindrical face or axis), 0 to not (see **Remarks**)
- `BDir2`: 1 to set this initial condition along direction 2 (if direction reference is a plane or face) or in a circumferential direction (if direction reference is a cylindrical face or axis), 0 to not (see **Remarks**)
- `BDir3`: 1 to set this initial condition along the normal (if direction reference is a plane or face), or in an axial direction (if direction reference is a cylindrical face or axis), or along an edge (if direction reference is an edge); 0 to not (see **Remarks**)

## VBA Syntax

See [CWDynamicInitialCondition::SetDirections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicInitialCondition~SetDirections.html).

## Remarks

Call [ICWDynamicInitialCondition::SetDirectionEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirectionEntity.html) to set the direction reference for this initial condition.

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)
[ICWDynamicInitialCondition::GetDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetDirections.html)
[ICWDynamicInitialCondition::SetReverseDirections Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetReverseDirections.html)
[ICWDynamicInitialCondition::SetValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetValues.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
