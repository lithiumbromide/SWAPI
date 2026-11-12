---
title: "SetFrequencyData Method (ICWTopologyFrequencyConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyFrequencyConstraint"
member: "SetFrequencyData"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint~SetFrequencyData.html"
---

# SetFrequencyData Method (ICWTopologyFrequencyConstraint)

Sets the equations for this topology study frequency constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetFrequencyData( _
   ByVal VarModeShapes As System.Object, _
   ByVal VarComparators As System.Object, _
   ByVal VarFrequencyValues As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyFrequencyConstraint
Dim VarModeShapes As System.Object
Dim VarComparators As System.Object
Dim VarFrequencyValues As System.Object
Dim value As System.Integer

value = instance.SetFrequencyData(VarModeShapes, VarComparators, VarFrequencyValues)
```

### C#

```csharp
System.int SetFrequencyData(
   System.object VarModeShapes,
   System.object VarComparators,
   System.object VarFrequencyValues
)
```

### C++/CLI

```cpp
System.int SetFrequencyData(
   System.Object^ VarModeShapes,
   System.Object^ VarComparators,
   System.Object^ VarFrequencyValues
)
```

### Parameters

- `VarModeShapes`: Array of mode shape numbers (see **Remarks**)
- `VarComparators`: Array of [swsTopologyStudyConstraintComparator_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudyConstraintComparator_e.html) (see **Remarks**)
- `VarFrequencyValues`: Array of frequency values (see **Remarks**)

### Return Value

Result code as defined in [swsTopologyStudy_FrequencyConstraintErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_FrequencyConstraintErrors_e.html)

## VBA Syntax

See [CWTopologyFrequencyConstraint::SetFrequencyData](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyFrequencyConstraint~SetFrequencyData.html).

## Examples

See the [ICWTopologyFrequencyConstraint](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html) example.

## Remarks

The arrays of VarModeShapes, VarComparators, and VarFrequencyValues map one-to-one and onto. Together they define `n` frequency constraint equations as follows:

```
for i = 0 to n-1
```

```
  VarModeShapes[i] VarComparators[i] VarFrequencyValues[i]
```

```
next  i
```

The VarModeShapes array must be in mode shape ascending order, and the VarFrequencyValues array must be in frequency ascending order.

If the VarComparators array contains swsTopologyStudyConstraintComparator_e.swsTopologyConstraintComparator_IsInBetween, then the corresponding value in VarFrequencyValues must be specified with a range of values, e.g., "200-400".

## See Also

[ICWTopologyFrequencyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html)
[ICWTopologyFrequencyConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint_members.html)
[ICWTopologyFrequencyConstraint::ClearFrequencyData Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint~ClearFrequencyData.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
