---
title: "SetModeTrackingFlag2 Method (ICWTopologyFrequencyConstraint)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyFrequencyConstraint"
member: "SetModeTrackingFlag2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint~SetModeTrackingFlag2.html"
---

# SetModeTrackingFlag2 Method (ICWTopologyFrequencyConstraint)

Sets whether mode-tracking is on for this topology study frequency constraint.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetModeTrackingFlag2( _
   ByVal BFlag As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyFrequencyConstraint
Dim BFlag As System.Boolean

instance.SetModeTrackingFlag2(BFlag)
```

### C#

```csharp
void SetModeTrackingFlag2(
   System.bool BFlag
)
```

### C++/CLI

```cpp
void SetModeTrackingFlag2(
   System.bool BFlag
)
```

### Parameters

- `BFlag`: -1 or true to turn mode-tracking on, 0 or false to not

## VBA Syntax

See [CWTopologyFrequencyConstraint::SetModeTrackingFlag2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyFrequencyConstraint~SetModeTrackingFlag2.html).

## See Also

[ICWTopologyFrequencyConstraint Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint.html)
[ICWTopologyFrequencyConstraint Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyFrequencyConstraint_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
