---
title: "SetValue Method (ICWTopologyFactorOfSafetyConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyFactorOfSafetyConstraint"
member: "SetValue"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint~SetValue.html"
---

# SetValue Method (ICWTopologyFactorOfSafetyConstraint)

Sets the value to use in the equation of this topology study Factor Of Safety constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetValue( _
   ByVal DValue As System.Double _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyFactorOfSafetyConstraint
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

- `DValue`: 1.0 <= Value in the Factor Of Safety constraint equation <= 10000.0

### Return Value

Result code as defined in [swsTopologyStudy_FOSConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_FOSConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyFactorOfSafetyConstraint::SetValue](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyFactorOfSafetyConstraint~SetValue.html).

## Examples

See the [ICWTopologyFactorOfSafetyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html) example.

## Remarks

This Factor Of Safety constraint equation:

```
FOS_component comparator DValue
```

## See Also

[ICWTopologyFactorOfSafetyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html)
[ICWTopologyFactorOfSafetyConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
