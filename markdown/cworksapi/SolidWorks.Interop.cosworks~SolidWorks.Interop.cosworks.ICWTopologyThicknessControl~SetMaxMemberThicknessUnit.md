---
title: "SetMaxMemberThicknessUnit Method (ICWTopologyThicknessControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyThicknessControl"
member: "SetMaxMemberThicknessUnit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetMaxMemberThicknessUnit.html"
---

# SetMaxMemberThicknessUnit Method (ICWTopologyThicknessControl)

Sets the units of maximum member thickness for this topology study thickness manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMaxMemberThicknessUnit( _
   ByVal NUnit As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyThicknessControl
Dim NUnit As System.Integer

instance.SetMaxMemberThicknessUnit(NUnit)
```

### C#

```csharp
void SetMaxMemberThicknessUnit(
   System.int NUnit
)
```

### C++/CLI

```cpp
void SetMaxMemberThicknessUnit(
   System.int NUnit
)
```

### Parameters

- `NUnit`: Units of thickness as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWTopologyThicknessControl::SetMaxMemberThicknessUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyThicknessControl~SetMaxMemberThicknessUnit.html).

## Examples

See the [ICWTopologyThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html) example.

## Remarks

This method is valid only if [ICWTopologyThicknessControl::SetIncludeMaxMemberThickness](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetIncludeMaxMemberThickness.html) sets BFlag to true.

## See Also

[ICWTopologyThicknessControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html)
[ICWTopologyThicknessControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
