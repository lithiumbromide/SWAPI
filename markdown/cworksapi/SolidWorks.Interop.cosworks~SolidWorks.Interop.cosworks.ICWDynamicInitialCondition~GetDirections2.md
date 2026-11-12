---
title: "GetDirections2 Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "GetDirections2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetDirections2.html"
---

# GetDirections2 Method (ICWDynamicInitialCondition)

Gets the directions in which this initial condition is applied.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetDirections2( _
   ByRef BDir1 As System.Boolean, _
   ByRef BDir2 As System.Boolean, _
   ByRef BDir3 As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim BDir1 As System.Boolean
Dim BDir2 As System.Boolean
Dim BDir3 As System.Boolean

instance.GetDirections2(BDir1, BDir2, BDir3)
```

### C#

```csharp
void GetDirections2(
   out System.bool BDir1,
   out System.bool BDir2,
   out System.bool BDir3
)
```

### C++/CLI

```cpp
void GetDirections2(
   [Out] System.bool BDir1,
   [Out] System.bool BDir2,
   [Out] System.bool BDir3
)
```

### Parameters

- `BDir1`: -1 or true if initial condition is applied along direction 1 (if direction reference is a plane or face) or in a radial direction (if direction reference is a cylindrical face or axis), 0 or false if not (see **Remarks**)
- `BDir2`: -1 or true if initial condition is applied along direction 2 (if direction reference is a plane or face) or in a circumferential direction (if direction reference is a cylindrical face or axis), 0 or false if not (see **Remarks**)
- `BDir3`: -1 or true if initial condition is applied along the normal (if direction reference is a plane or face), or in an axial direction (if direction reference is a cylindrical face or axis), or along an edge (if direction reference is an edge); 0 or false if not (see **Remarks**)

## Examples

See the [ICWDynamicInitialCondition](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html) examples.

## Remarks

Call [ICWDynamicInitialCondition::SetDirectionEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirectionEntity.html) to set the direction reference for this initial condition.

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
