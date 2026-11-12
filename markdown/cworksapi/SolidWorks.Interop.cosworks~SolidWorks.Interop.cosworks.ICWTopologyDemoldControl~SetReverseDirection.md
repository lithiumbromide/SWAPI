---
title: "SetReverseDirection Method (ICWTopologyDemoldControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDemoldControl"
member: "SetReverseDirection"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SetReverseDirection.html"
---

# SetReverseDirection Method (ICWTopologyDemoldControl)

Obsolete. Superseded by [ICWTopologyDemoldControl::SetReverseDirection2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SetReverseDirection2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReverseDirection( _
   ByVal BFlag As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDemoldControl
Dim BFlag As System.Integer

instance.SetReverseDirection(BFlag)
```

### C#

```csharp
void SetReverseDirection(
   System.int BFlag
)
```

### C++/CLI

```cpp
void SetReverseDirection(
   System.int BFlag
)
```

### Parameters

- `BFlag`: 1 to reverse the pull direction, 0 to not

## VBA Syntax

See [CWTopologyDemoldControl::SetReverseDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDemoldControl~SetReverseDirection.html).

## Remarks

This method is valid only if [ICWTopologyDemoldControl::SelectDemoldDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectDemoldDirection.html) sets NDir to:

- [swsTopologyDemoldDirectionOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyDemoldDirectionOption_e.html).swsTopologyDemoldDirection_PullDirectionOnly

- or -

- swsTopologyDemoldDirectionOption_e.swsTpologyDemoldDirection_Stamping

## See Also

[ICWTopologyDemoldControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html)
[ICWTopologyDemoldControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
