---
title: "SetMinimumMemberThickness Method (ICWTopologyThicknessControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyThicknessControl"
member: "SetMinimumMemberThickness"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetMinimumMemberThickness.html"
---

# SetMinimumMemberThickness Method (ICWTopologyThicknessControl)

Sets the minimum member thickness for this topology study thickness manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMinimumMemberThickness( _
   ByVal DThickness As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyThicknessControl
Dim DThickness As System.Double

instance.SetMinimumMemberThickness(DThickness)
```

### C#

```csharp
void SetMinimumMemberThickness(
   System.double DThickness
)
```

### C++/CLI

```cpp
void SetMinimumMemberThickness(
   System.double DThickness
)
```

### Parameters

- `DThickness`: Minimum member thickness

## VBA Syntax

See [CWTopologyThicknessControl::SetMinimumMemberThickness](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyThicknessControl~SetMinimumMemberThickness.html).

## Examples

See the [ICWTopologyThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html) example.

## Remarks

This method is valid only if [ICWTopologyThicknessControl::SetIncludeMinMemberThickness](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetIncludeMinMemberThickness.html) sets BFlag to true.

## See Also

[ICWTopologyThicknessControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html)
[ICWTopologyThicknessControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
