---
title: "SelectPlaneForDirection Method (ICWTopologyDemoldControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDemoldControl"
member: "SelectPlaneForDirection"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectPlaneForDirection.html"
---

# SelectPlaneForDirection Method (ICWTopologyDemoldControl)

Sets the central mid plane of this topology study de-mold manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectPlaneForDirection( _
   ByVal PlaneDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDemoldControl
Dim PlaneDisp As System.Object

instance.SelectPlaneForDirection(PlaneDisp)
```

### C#

```csharp
void SelectPlaneForDirection(
   System.object PlaneDisp
)
```

### C++/CLI

```cpp
void SelectPlaneForDirection(
   System.Object^ PlaneDisp
)
```

### Parameters

- `PlaneDisp`: Plane object

## VBA Syntax

See [CWTopologyDemoldControl::SelectPlaneForDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDemoldControl~SelectPlaneForDirection.html).

## Examples

See the [ICWTopologyDemoldControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html) example.

## Remarks

This method is valid only if:

- [ICWTopologyDemoldControl::SetAutoDetermineCentralMidPlane](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SetAutoDetermineCentralMidPlane.html) is set to 0

- and -

- [ICWTopologyDemoldControl::SelectDemoldDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectDemoldDirection.html) sets NDir to [swsTopologyDemoldDirectionOption_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyDemoldDirectionOption_e.html).swsTopologyDemoldDirection_TwoDirectionMidPlane.

## See Also

[ICWTopologyDemoldControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html)
[ICWTopologyDemoldControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl_members.html)
[ICWTopologyDemoldControl::ClearPlaneSelection Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~ClearPlaneSelection.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
