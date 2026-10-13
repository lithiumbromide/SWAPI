---
title: "GetGravitationalAcclerationValues Method (ICWGravity)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWGravity"
member: "GetGravitationalAcclerationValues"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~GetGravitationalAcclerationValues.html"
---

# GetGravitationalAcclerationValues Method (ICWGravity)

Gets the gravitational acceleration values.

## Syntax

### Visual Basic (Declaration)

```vb
Sub GetGravitationalAcclerationValues( _
   ByRef DVal1 As System.Double, _
   ByRef DVal2 As System.Double, _
   ByRef DVal3 As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWGravity
Dim DVal1 As System.Double
Dim DVal2 As System.Double
Dim DVal3 As System.Double

instance.GetGravitationalAcclerationValues(DVal1, DVal2, DVal3)
```

### C#

```csharp
void GetGravitationalAcclerationValues(
   out System.double DVal1,
   out System.double DVal2,
   out System.double DVal3
)
```

### C++/CLI

```cpp
void GetGravitationalAcclerationValues(
   [Out] System.double DVal1,
   [Out] System.double DVal2,
   [Out] System.double DVal3
)
```

### Parameters

- `DVal1`: Acceleration of gravity in plane direction 1
- `DVal2`: Acceleration of gravity in plane direction 2
- `DVal3`: Acceleration of gravity in the direction normal to the plane

## VBA Syntax

See [CWGravity::GetGravitationalAcclerationValues](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWGravity~GetGravitationalAcclerationValues.html).

## Examples

See the [ICWGravity](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html) examples.

## See Also

[ICWGravity Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity.html)
[ICWGravity Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity_members.html)
[ICWGravity::SetGravitationalAcclerationValues Method](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWGravity~SetGravitationalAcclerationValues.html)

## Availability

SOLIDWORKS Simulation API 2008 SP1.0
