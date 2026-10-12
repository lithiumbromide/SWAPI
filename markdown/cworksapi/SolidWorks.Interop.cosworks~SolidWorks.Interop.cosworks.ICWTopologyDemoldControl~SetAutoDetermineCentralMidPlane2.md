---
title: "SetAutoDetermineCentralMidPlane2 Method (ICWTopologyDemoldControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDemoldControl"
member: "SetAutoDetermineCentralMidPlane2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SetAutoDetermineCentralMidPlane2.html"
---

# SetAutoDetermineCentralMidPlane2 Method (ICWTopologyDemoldControl)

Sets whether to atomatically determine the central mid plane of this topology study de-mold manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAutoDetermineCentralMidPlane2( _
   ByVal BFlag As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDemoldControl
Dim BFlag As System.Boolean

instance.SetAutoDetermineCentralMidPlane2(BFlag)
```

### C#

```csharp
void SetAutoDetermineCentralMidPlane2(
   System.bool BFlag
)
```

### C++/CLI

```cpp
void SetAutoDetermineCentralMidPlane2(
   System.bool BFlag
)
```

### Parameters

- `BFlag`: -1 or true to automatically determine the central mid plane, 0 or false to explicitly specify it

## Examples

See the [ICWTopologyDemoldControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html) example.

## Remarks

This method is valid only if [ICWTopologyDemoldControl::SelectDemoldDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectDemoldDirection.html) sets NDir to [swsTopologyDemoldDirectionOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyDemoldDirectionOption_e.html).swsTopologyDemoldDirection_TwoDirectionMidPlane.

If BFlag is set to:

- 0, use [ICWTopologyDemoldControl::SelectPlaneForDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectPlaneForDirection.html) to specify the central mid plane.
- -1, use [ICWTopologyDemoldControl::SelectEdgeForPullDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectEdgeForPullDirection.html).

## See Also

[ICWTopologyDemoldControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html)
[ICWTopologyDemoldControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
