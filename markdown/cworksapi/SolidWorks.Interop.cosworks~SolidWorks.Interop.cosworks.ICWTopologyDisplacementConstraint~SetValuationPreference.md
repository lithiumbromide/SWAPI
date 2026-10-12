---
title: "SetValuationPreference Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "SetValuationPreference"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetValuationPreference.html"
---

# SetValuationPreference Method (ICWTopologyDisplacementConstraint)

Sets the valuation preference for this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetValuationPreference( _
   ByVal NValuationOption As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
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

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::SetValuationPreference](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~SetValuationPreference.html).

## Examples

See the [ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html) example.

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
