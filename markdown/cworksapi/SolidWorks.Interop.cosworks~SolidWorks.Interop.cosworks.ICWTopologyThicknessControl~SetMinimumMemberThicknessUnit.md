---
title: "SetMinimumMemberThicknessUnit Method (ICWTopologyThicknessControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyThicknessControl"
member: "SetMinimumMemberThicknessUnit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetMinimumMemberThicknessUnit.html"
---

# SetMinimumMemberThicknessUnit Method (ICWTopologyThicknessControl)

Sets the units of minimum member thickness for this topology study thickness manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMinimumMemberThicknessUnit( _
   ByVal NUnit As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyThicknessControl
Dim NUnit As System.Integer

instance.SetMinimumMemberThicknessUnit(NUnit)
```

### C#

```csharp
void SetMinimumMemberThicknessUnit(
   System.int NUnit
)
```

### C++/CLI

```cpp
void SetMinimumMemberThicknessUnit(
   System.int NUnit
)
```

### Parameters

- `NUnit`: Units of thickness as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWTopologyThicknessControl::SetMinimumMemberThicknessUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyThicknessControl~SetMinimumMemberThicknessUnit.html).

## Examples

See the [ICWTopologyThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html) example.

## Remarks

This method is valid only if [ICWTopologyThicknessControl::SetIncludeMinMemberThickness](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetIncludeMinMemberThickness.html) sets BFlag to true.

## See Also

[ICWTopologyThicknessControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html)
[ICWTopologyThicknessControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
