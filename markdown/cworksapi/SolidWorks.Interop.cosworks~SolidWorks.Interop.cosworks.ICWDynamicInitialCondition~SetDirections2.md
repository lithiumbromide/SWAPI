---
title: "SetDirections2 Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "SetDirections2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirections2.html"
---

# SetDirections2 Method (ICWDynamicInitialCondition)

Sets the directions in which this initial condition is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDirections2( _
   ByVal BDir1 As System.Boolean, _
   ByVal BDir2 As System.Boolean, _
   ByVal BDir3 As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim BDir1 As System.Boolean
Dim BDir2 As System.Boolean
Dim BDir3 As System.Boolean

instance.SetDirections2(BDir1, BDir2, BDir3)
```

### C#

```csharp
void SetDirections2(
   System.bool BDir1,
   System.bool BDir2,
   System.bool BDir3
)
```

### C++/CLI

```cpp
void SetDirections2(
   System.bool BDir1,
   System.bool BDir2,
   System.bool BDir3
)
```

### Parameters

- `BDir1`: -1 or true to set this initial condition along direction 1 (if direction reference is a plane or face) or in a radial direction (if direction reference is a cylindrical face or axis), 0 or false to not (see **Remarks**)
- `BDir2`: -1 or true to set this initial condition along direction 2 (if direction reference is a plane or face) or in a circumferential direction (if direction reference is a cylindrical face or axis), 0 or false to not (see **Remarks**)
- `BDir3`: -1 or true to set this initial condition along the normal (if direction reference is a plane or face), or in an axial direction (if direction reference is a cylindrical face or axis), or along an edge (if direction reference is an edge); 0 or false to not (see **Remarks**)

## Remarks

Call [ICWDynamicInitialCondition::SetDirectionEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirectionEntity.html) to set the direction reference for this initial condition.

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
