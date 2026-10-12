---
title: "EndEdit Method (ICWTopologyFrequencyConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyFrequencyConstraint"
member: "EndEdit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint~EndEdit.html"
---

# EndEdit Method (ICWTopologyFrequencyConstraint)

Ends editing this topology study frequency constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndEdit() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyFrequencyConstraint
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

Result code as defined in [swsTopologyStudy_FrequencyConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_FrequencyConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyFrequencyConstraint::EndEdit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyFrequencyConstraint~EndEdit.html).

## Examples

See the [ICWTopologyFrequencyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html) example.

## Remarks

To begin editing this frequency constraint, call [ICWTopologyFrequencyConstraint::BeginEdit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint~BeginEdit.html).

## See Also

[ICWTopologyFrequencyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html)
[ICWTopologyFrequencyConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
