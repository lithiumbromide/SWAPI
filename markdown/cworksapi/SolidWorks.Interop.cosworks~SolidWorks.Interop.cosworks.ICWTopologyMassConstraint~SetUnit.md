---
title: "SetUnit Method (ICWTopologyMassConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMassConstraint"
member: "SetUnit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~SetUnit.html"
---

# SetUnit Method (ICWTopologyMassConstraint)

Sets the units of mass for this topology study mass constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetUnit( _
   ByVal NUnit As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMassConstraint
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

- `NUnit`: Units of mass as defined in [swsMassUnits_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsMassUnits_e.html) (see **Remarks**)

### Return Value

Result code as defined in [swsTopologyStudy_MassConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MassConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyMassConstraint::SetUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMassConstraint~SetUnit.html).

## Examples

See the [ICWTopologyMassConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html) example.

## Remarks

This method is valid only if [ICWTopologyMassConstraint::SetMassPreference](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~SetMassPreference.html) sets [swsTopologyStudyMassConstraintOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyMassConstraintOption_e.html).swsTopologyMassConstraintOption_AbsoluteValue.

## See Also

[ICWTopologyMassConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html)
[ICWTopologyMassConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint_members.html)
[ICWTopologyMassConstraint::SetValue Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~SetValue.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
