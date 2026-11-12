---
title: "SetIncludeMinMemberThickness Method (ICWTopologyThicknessControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyThicknessControl"
member: "SetIncludeMinMemberThickness"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetIncludeMinMemberThickness.html"
---

# SetIncludeMinMemberThickness Method (ICWTopologyThicknessControl)

Obsolete. Superseded by [ICWTopologyThicknessControl::SetIncludeMinMemberThickness2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetIncludeMinMemberThickness2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIncludeMinMemberThickness( _
   ByVal BFlag As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyThicknessControl
Dim BFlag As System.Integer

instance.SetIncludeMinMemberThickness(BFlag)
```

### C#

```csharp
void SetIncludeMinMemberThickness(
   System.int BFlag
)
```

### C++/CLI

```cpp
void SetIncludeMinMemberThickness(
   System.int BFlag
)
```

### Parameters

- `BFlag`: 1 to specify the minimum member thickness, 0 to not

## VBA Syntax

See [CWTopologyThicknessControl::SetIncludeMinMemberThickness](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyThicknessControl~SetIncludeMinMemberThickness.html).

## Examples

See the [ICWTopologyThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html) example.

## Remarks

If BFlag is set to true, set [ICWTopologyThicknessControl::SetMinimumMemberThickness](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetMinimumMemberThickness.html) and [ICWTopologyThicknessControl::SetMinimumMemberThicknessUnit](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetMinimumMemberThicknessUnit.html).

## See Also

[ICWTopologyThicknessControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html)
[ICWTopologyThicknessControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
