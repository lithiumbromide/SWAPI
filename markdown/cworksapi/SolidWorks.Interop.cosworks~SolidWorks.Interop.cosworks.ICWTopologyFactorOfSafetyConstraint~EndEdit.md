---
title: "EndEdit Method (ICWTopologyFactorOfSafetyConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyFactorOfSafetyConstraint"
member: "EndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint~EndEdit.html"
---

# EndEdit Method (ICWTopologyFactorOfSafetyConstraint)

Ends editing this topology study Factor Of Safety constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyFactorOfSafetyConstraint
Dim value As System.Integer

value = instance.EndEdit()
```

### C#

```csharp
System.int EndEdit()
```

### C++/CLI

```cpp
System.int EndEdit();
```

### Return Value

Result code as defined in [swsTopologyStudy_FOSConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_FOSConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyFactorOfSafetyConstraint::EndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyFactorOfSafetyConstraint~EndEdit.html).

## Examples

See the [ICWTopologyFactorOfSafetyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html) example.

## Remarks

To begin editing this Factor Of Safety constraint, call [ICWTopologyFactorOfSafetyConstraint::BeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint~BeginEdit.html).

## See Also

[ICWTopologyFactorOfSafetyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint.html)
[ICWTopologyFactorOfSafetyConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFactorOfSafetyConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
