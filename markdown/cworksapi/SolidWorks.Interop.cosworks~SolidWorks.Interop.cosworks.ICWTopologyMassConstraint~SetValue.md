---
title: "SetValue Method (ICWTopologyMassConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMassConstraint"
member: "SetValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~SetValue.html"
---

# SetValue Method (ICWTopologyMassConstraint)

Sets the reduce-mass-by value of this topology study mass constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetValue( _
   ByVal DValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMassConstraint
Dim DValue As System.Double
Dim value As System.Integer

value = instance.SetValue(DValue)
```

### C#

```csharp
System.int SetValue(
   System.double DValue
)
```

### C++/CLI

```cpp
System.int SetValue(
   System.double DValue
)
```

### Parameters

- `DValue`: Reduce-mass-by value of the mass constraint

### Return Value

Result code as defined in [swsTopologyStudy_MassConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MassConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyMassConstraint::SetValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMassConstraint~SetValue.html).

## Examples

See the [ICWTopologyMassConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html) example.

## Remarks

DValue depends on the reduce-mass-by preference specified with [ICWTopologyMassConstriant::SetMassPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~SetMassPreference.html).

## See Also

[ICWTopologyMassConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html)
[ICWTopologyMassConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint_members.html)
[ICWTopologyMassConstraint::SetUnit Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~SetUnit.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
