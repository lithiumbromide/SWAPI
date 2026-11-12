---
title: "EndEdit Method (ICWTopologyMassConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyMassConstraint"
member: "EndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~EndEdit.html"
---

# EndEdit Method (ICWTopologyMassConstraint)

Ends editing this topology study mass constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyMassConstraint
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

Result code as defined in [swsTopologyStudy_MassConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_MassConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyMassConstraint::EndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyMassConstraint~EndEdit.html).

## Examples

See the [ICWTopologyMassConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html) example.

## Remarks

To begin editing this mass constraint, call [ICWTopologyMassConstraint::BeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint~BeginEdit.html).

## See Also

[ICWTopologyMassConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint.html)
[ICWTopologyMassConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyMassConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
