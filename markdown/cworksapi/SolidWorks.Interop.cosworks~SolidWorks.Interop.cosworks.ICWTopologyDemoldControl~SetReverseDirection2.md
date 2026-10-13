---
title: "SetReverseDirection2 Method (ICWTopologyDemoldControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDemoldControl"
member: "SetReverseDirection2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SetReverseDirection2.html"
---

# SetReverseDirection2 Method (ICWTopologyDemoldControl)

Sets whether to reverse the pull direction of this topology study de-mold manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetReverseDirection2( _
   ByVal BFlag As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDemoldControl
Dim BFlag As System.Boolean

instance.SetReverseDirection2(BFlag)
```

### C#

```csharp
void SetReverseDirection2(
   System.bool BFlag
)
```

### C++/CLI

```cpp
void SetReverseDirection2(
   System.bool BFlag
)
```

### Parameters

- `BFlag`: -1 or true to reverse the pull direction, 0 or falseto not

## Examples

See the [ICWTopologyDemoldControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html) example.

## Remarks

This method is valid only if [ICWTopologyDemoldControl::SelectDemoldDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectDemoldDirection.html) sets NDir to:

- [swsTopologyDemoldDirectionOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyDemoldDirectionOption_e.html).swsTopologyDemoldDirection_PullDirectionOnly

- or -

- swsTopologyDemoldDirectionOption_e.swsTpologyDemoldDirection_Stamping

## See Also

[ICWTopologyDemoldControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html)
[ICWTopologyDemoldControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
