---
title: "SetGravitationalAcclerationValues Method (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "SetGravitationalAcclerationValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~SetGravitationalAcclerationValues.html"
---

# SetGravitationalAcclerationValues Method (ICWGravity)

Sets the gravitational acceleration values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetGravitationalAcclerationValues( _
   ByVal DVal1 As System.Double, _
   ByVal DVal2 As System.Double, _
   ByVal DVal3 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity
Dim DVal1 As System.Double
Dim DVal2 As System.Double
Dim DVal3 As System.Double

instance.SetGravitationalAcclerationValues(DVal1, DVal2, DVal3)
```

### C#

```csharp
void SetGravitationalAcclerationValues(
   System.double DVal1,
   System.double DVal2,
   System.double DVal3
)
```

### C++/CLI

```cpp
void SetGravitationalAcclerationValues(
   System.double DVal1,
   System.double DVal2,
   System.double DVal3
)
```

### Parameters

- `DVal1`: Acceleration of gravity in plane direction 1
- `DVal2`: Acceleration of gravity in plane direction 2
- `DVal3`: Acceleration of gravity in a direction normal to the plane

## VBA Syntax

See [CWGravity::SetGravitationalAcclerationValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGravity~SetGravitationalAcclerationValues.html).

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)
[ICWGravity::GetGravitationalAcclerationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~GetGravitationalAcclerationValues.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
