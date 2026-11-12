---
title: "SetName Method (ICWTopologyFactorOfSafetyConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyFactorOfSafetyConstraint"
member: "SetName"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint~SetName.html"
---

# SetName Method (ICWTopologyFactorOfSafetyConstraint)

Sets the name of this topology study Factor Of Safety constraint

## Syntax

### Visual Basic (Declaration)

```vb
Function SetName( _
   ByVal SName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyFactorOfSafetyConstraint
Dim SName As System.String
Dim value As System.Integer

value = instance.SetName(SName)
```

### C#

```csharp
System.int SetName(
   System.string SName
)
```

### C++/CLI

```cpp
System.int SetName(
   System.String^ SName
)
```

### Parameters

- `SName`: Name of the Factor Of Safety constraint

### Return Value

Result code as defined in [swsTopologyStudy_FOSConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_FOSConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyFactorOfSafetyConstraint::SetName](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyFactorOfSafetyConstraint~SetName.html).

## Examples

See the [ICWTopologyFactorOfSafetyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html) example.

## See Also

[ICWTopologyFactorOfSafetyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html)
[ICWTopologyFactorOfSafetyConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint_members.html)
[ICWTopologyFactorofSafetyConstraint::GetName Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint~GetName.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
