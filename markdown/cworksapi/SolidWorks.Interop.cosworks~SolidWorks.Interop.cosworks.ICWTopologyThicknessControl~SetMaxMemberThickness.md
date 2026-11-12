---
title: "SetMaxMemberThickness Method (ICWTopologyThicknessControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyThicknessControl"
member: "SetMaxMemberThickness"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetMaxMemberThickness.html"
---

# SetMaxMemberThickness Method (ICWTopologyThicknessControl)

Sets the maximum member thickness for this topology study thickness manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetMaxMemberThickness( _
   ByVal DThickness As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyThicknessControl
Dim DThickness As System.Double

instance.SetMaxMemberThickness(DThickness)
```

### C#

```csharp
void SetMaxMemberThickness(
   System.double DThickness
)
```

### C++/CLI

```cpp
void SetMaxMemberThickness(
   System.double DThickness
)
```

### Parameters

- `DThickness`: Maximum member thickness

## VBA Syntax

See [CWTopologyThicknessControl::SetMaxMemberThickness](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyThicknessControl~SetMaxMemberThickness.html).

## Examples

See the [ICWTopologyThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html) example.

## Remarks

This method is valid only if [ICWTopologyThicknessControl::SetIncludeMaxMemberThickness](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetIncludeMaxMemberThickness.html) sets BFlag to true.

## See Also

[ICWTopologyThicknessControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html)
[ICWTopologyThicknessControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
