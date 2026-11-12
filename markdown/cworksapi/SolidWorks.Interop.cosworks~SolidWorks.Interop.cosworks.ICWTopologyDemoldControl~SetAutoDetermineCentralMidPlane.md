---
title: "SetAutoDetermineCentralMidPlane Method (ICWTopologyDemoldControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDemoldControl"
member: "SetAutoDetermineCentralMidPlane"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SetAutoDetermineCentralMidPlane.html"
---

# SetAutoDetermineCentralMidPlane Method (ICWTopologyDemoldControl)

Obsolete. Superseded by [ICWTopologyDemoldControl::SetAutoDetermineCentralMidPlane2](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SetAutoDetermineCentralMidPlane2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAutoDetermineCentralMidPlane( _
   ByVal BFlag As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDemoldControl
Dim BFlag As System.Integer

instance.SetAutoDetermineCentralMidPlane(BFlag)
```

### C#

```csharp
void SetAutoDetermineCentralMidPlane(
   System.int BFlag
)
```

### C++/CLI

```cpp
void SetAutoDetermineCentralMidPlane(
   System.int BFlag
)
```

### Parameters

- `BFlag`: 1 to automatically determine the central mid plane, 0 to explicitly specify it

## VBA Syntax

See [CWTopologyDemoldControl::SetAutoDetermineCentralMidPlane](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDemoldControl~SetAutoDetermineCentralMidPlane.html).

## Remarks

This method is valid only if [ICWTopologyDemoldControl::SelectDemoldDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectDemoldDirection.html) sets NDir to [swsTopologyDemoldDirectionOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyDemoldDirectionOption_e.html).swsTopologyDemoldDirection_TwoDirectionMidPlane.

If BFlag is set to:

- 0, use [ICWTopologyDemoldControl::SelectPlaneForDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectPlaneForDirection.html) to specify the central mid plane.
- 1, use [ICWTopologyDemoldControl::SelectEdgeForPullDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectEdgeForPullDirection.html).

## See Also

[ICWTopologyDemoldControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html)
[ICWTopologyDemoldControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
