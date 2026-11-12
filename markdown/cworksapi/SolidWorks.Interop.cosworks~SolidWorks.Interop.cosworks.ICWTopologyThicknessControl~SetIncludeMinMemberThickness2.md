---
title: "SetIncludeMinMemberThickness2 Method (ICWTopologyThicknessControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyThicknessControl"
member: "SetIncludeMinMemberThickness2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl~SetIncludeMinMemberThickness2.html"
---

# SetIncludeMinMemberThickness2 Method (ICWTopologyThicknessControl)

Sets whether to specify the minimum member thickness for this topology study thickness manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIncludeMinMemberThickness2( _
   ByVal BFlag As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyThicknessControl
Dim BFlag As System.Boolean

instance.SetIncludeMinMemberThickness2(BFlag)
```

### C#

```csharp
void SetIncludeMinMemberThickness2(
   System.bool BFlag
)
```

### C++/CLI

```cpp
void SetIncludeMinMemberThickness2(
   System.bool BFlag
)
```

### Parameters

- `BFlag`: -1 or true to specify the minimum member thickness, 0 or false to not

## VBA Syntax

See [CWTopologyThicknessControl::SetIncludeMinMemberThickness2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyThicknessControl~SetIncludeMinMemberThickness2.html).

## See Also

[ICWTopologyThicknessControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html)
[ICWTopologyThicknessControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
