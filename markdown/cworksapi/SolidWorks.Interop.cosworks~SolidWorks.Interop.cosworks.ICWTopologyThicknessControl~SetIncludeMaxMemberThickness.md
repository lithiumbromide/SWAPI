---
title: "SetIncludeMaxMemberThickness Method (ICWTopologyThicknessControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyThicknessControl"
member: "SetIncludeMaxMemberThickness"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetIncludeMaxMemberThickness.html"
---

# SetIncludeMaxMemberThickness Method (ICWTopologyThicknessControl)

Obsolete. Superseded by [ICWTopologyThicknessControl::SetIncludeMaxMemberThickness2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetIncludeMaxMemberThickness2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIncludeMaxMemberThickness( _
   ByVal BFlag As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyThicknessControl
Dim BFlag As System.Integer

instance.SetIncludeMaxMemberThickness(BFlag)
```

### C#

```csharp
void SetIncludeMaxMemberThickness(
   System.int BFlag
)
```

### C++/CLI

```cpp
void SetIncludeMaxMemberThickness(
   System.int BFlag
)
```

### Parameters

- `BFlag`: 1 to specify the maximum member thickness, 0 to not

## VBA Syntax

See [CWTopologyThicknessControl::SetIncludeMaxMemberThickness](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyThicknessControl~SetIncludeMaxMemberThickness.html).

## Examples

See the [ICWTopologyThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html) example.

## Remarks

If BFlag is set to true, set [ICWTopologyThicknessControl::SetMaxMemberThickness](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetMaxMemberThickness.html) and [ICWTopologyThicknessControl::SetMaxMemberThicknessUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetMaxMemberThicknessUnit.html).

## See Also

[ICWTopologyThicknessControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html)
[ICWTopologyThicknessControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
