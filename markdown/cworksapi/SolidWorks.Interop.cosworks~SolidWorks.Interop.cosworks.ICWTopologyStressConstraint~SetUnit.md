---
title: "SetUnit Method (ICWTopologyStressConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStressConstraint"
member: "SetUnit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint~SetUnit.html"
---

# SetUnit Method (ICWTopologyStressConstraint)

Sets the units of this topology study stress constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUnit( _
   ByVal NUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStressConstraint
Dim NUnit As System.Integer
Dim value As System.Integer

value = instance.SetUnit(NUnit)
```

### C#

```csharp
System.int SetUnit(
   System.int NUnit
)
```

### C++/CLI

```cpp
System.int SetUnit(
   System.int NUnit
)
```

### Parameters

- `NUnit`: Units as defined in [swsStrengthUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsStrengthUnit_e.html)

### Return Value

Result code as defined in [swsTopologyStudy_StressConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_StressConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyStressConstraint::SetUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStressConstraint~SetUnit.html).

## Examples

See the [ICWTopologyStressConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html) example.

## See Also

[ICWTopologyStressConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html)
[ICWTopologyStressConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint_members.html)
[ICWTopologyStressConstraint::SetValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint~SetValue.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
