---
title: "SetUnit Method (ICWTopologyDisplacementConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDisplacementConstraint"
member: "SetUnit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetUnit.html"
---

# SetUnit Method (ICWTopologyDisplacementConstraint)

Sets the units of this topology study displacement constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUnit( _
   ByVal NUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDisplacementConstraint
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

- `NUnit`: Units as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)

### Return Value

Result code as defined in [swsTopologyStudy_DisplacementConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_DisplacementConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyDisplacementConstraint::SetUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDisplacementConstraint~SetUnit.html).

## Examples

See the [ICWTopologyDisplacementConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html) example.

## Remarks

This method is valid only when [ICWTopologyDisplacementConstraint::SetValuationPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetValuationPreference.html) sets NValuationOption = [swsTopologyStudyConstraintValuationOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyConstraintValuationOption_e.html).swsTopologyConstraintValuationOption_AbsValue

## See Also

[ICWTopologyDisplacementConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint.html)
[ICWTopologyDisplacementConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint_members.html)
[ICWTopologyDisplacementConstraint::SetValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDisplacementConstraint~SetValue.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
