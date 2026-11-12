---
title: "GetValues Method (ICWDynamicInitialCondition)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWDynamicInitialCondition"
member: "GetValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~GetValues.html"
---

# GetValues Method (ICWDynamicInitialCondition)

Gets the values of this initial condition by direction.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetValues( _
   ByRef DVal1 As System.Double, _
   ByRef DVal2 As System.Double, _
   ByRef DVal3 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWDynamicInitialCondition
Dim DVal1 As System.Double
Dim DVal2 As System.Double
Dim DVal3 As System.Double

instance.GetValues(DVal1, DVal2, DVal3)
```

### C#

```csharp
void GetValues(
   out System.double DVal1,
   out System.double DVal2,
   out System.double DVal3
)
```

### C++/CLI

```cpp
void GetValues(
   [Out] System.double DVal1,
   [Out] System.double DVal2,
   [Out] System.double DVal3
)
```

### Parameters

- `DVal1`: Value along direction 1 (if direction reference is a face or plane) or along a radial direction (if direction reference is a cylindrical face or axis); valid only if BDir1 = 1 in [ICWDynamicInitialCondition::GetDirections](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWDynamicInitialCondition~GetDirections.html)
- `DVal2`: Value along direction 2 (if direction reference is a face or plane) or along a circumferential direction (if direction reference is a cylindrical face or axis); valid only if BDir2 = 1 in ICWDynamicInitialCondition::GetDirections
- `DVal3`: Value along the normal to the plane (if direction reference is a face or plane), or along an axial direction (if direction reference is a cylindrical face or axis), or along an edge (if direction reference is an edge); valid only if BDir3 = 1 in ICWDynamicInitialCondition::GetDirections

## VBA Syntax

See [CWDynamicInitialCondition::GetValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWDynamicInitialCondition~GetValues.html).

## Examples

See the [ICWDynamicInitialCondition](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html) examples.

## Remarks

Call [ICWDynamicInitialCondition::SetDirectionEntity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetDirectionEntity.html) to set the direction reference for this initial condition.

## See Also

[ICWDynamicInitialCondition Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition.html)
[ICWDynamicInitialCondition Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition_members.html)
[ICWDynamicInitialCondition::SetValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWDynamicInitialCondition~SetValues.html)

## Availability

SOLIDWORKS Simulation API 2012 SP0
