---
title: "SetValue Method (ICWTopologyStressConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStressConstraint"
member: "SetValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint~SetValue.html"
---

# SetValue Method (ICWTopologyStressConstraint)

Sets the value in the stress component equation of this topology study stress constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetValue( _
   ByVal DValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStressConstraint
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

- `DValue`: > Minimum model stress

### Return Value

Result code as defined in [swsTopologyStudy_StressConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_StressConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyStressConstraint::SetValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStressConstraint~SetValue.html).

## Examples

See the [ICWTopologyStressConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html) example.

## Remarks

DValue:

- must be greater than the minimum stress for the model. Run a static analysis with the same loads and fixtures used in the topology study to estimate the minimum model stress.
- depends on the [ICWTopologyStressConstraint::SetValuationPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint~SetValuationPreference.html) setting.

This stress constraint equation:

```
stress_component comparator DValue
```

## See Also

[ICWTopologyStressConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html)
[ICWTopologyStressConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
