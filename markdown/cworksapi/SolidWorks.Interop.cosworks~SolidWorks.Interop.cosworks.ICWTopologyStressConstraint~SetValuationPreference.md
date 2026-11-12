---
title: "SetValuationPreference Method (ICWTopologyStressConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStressConstraint"
member: "SetValuationPreference"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint~SetValuationPreference.html"
---

# SetValuationPreference Method (ICWTopologyStressConstraint)

Sets the valuation preference for this topology study stress constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetValuationPreference( _
   ByVal NValuationOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStressConstraint
Dim NValuationOption As System.Integer
Dim value As System.Integer

value = instance.SetValuationPreference(NValuationOption)
```

### C#

```csharp
System.int SetValuationPreference(
   System.int NValuationOption
)
```

### C++/CLI

```cpp
System.int SetValuationPreference(
   System.int NValuationOption
)
```

### Parameters

- `NValuationOption`: Valuation preference as defined in [swsTopologyStudyConstraintValuationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyConstraintValuationOption_e.html)

### Return Value

Result code as defined in [swsTopologyStudy_StressConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_StressConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyStressConstraint::SetValuationPreference](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStressConstraint~SetValuationPreference.html).

## Examples

See the [ICWTopologyStressConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html) example.

## See Also

[ICWTopologyStressConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint.html)
[ICWTopologyStressConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStressConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
