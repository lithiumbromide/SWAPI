---
title: "SelectEdgeForPullDirection Method (ICWTopologyDemoldControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyDemoldControl"
member: "SelectEdgeForPullDirection"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectEdgeForPullDirection.html"
---

# SelectEdgeForPullDirection Method (ICWTopologyDemoldControl)

Selects the edge for the pull direction of this topology study de-mold manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SelectEdgeForPullDirection( _
   ByVal EdgeDisp As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyDemoldControl
Dim EdgeDisp As System.Object

instance.SelectEdgeForPullDirection(EdgeDisp)
```

### C#

```csharp
void SelectEdgeForPullDirection(
   System.object EdgeDisp
)
```

### C++/CLI

```cpp
void SelectEdgeForPullDirection(
   System.Object^ EdgeDisp
)
```

### Parameters

- `EdgeDisp`: Edge object

## VBA Syntax

See [CWTopologyDemoldControl::SelectEdgeForPullDirection](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyDemoldControl~SelectEdgeForPullDirection.html).

## Examples

See the [ICWTopologyDemoldControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html) example.

## Remarks

This method is valid for all directions specified in [ICWTopologyDemoldControl::SelectDemoldDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectDemoldDirection.html), but is invalid if [ICWTopologyDemoldControl::SetAutoDetermineCentralMidPlane](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SetAutoDetermineCentralMidPlane.html) is set to 0, in which case you must use [ICWTopologyDemoldControl::SelectPlaneForDirection](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~SelectPlaneForDirection.html) to specify the pull direction.

## See Also

[ICWTopologyDemoldControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl.html)
[ICWTopologyDemoldControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl_members.html)
[ICWTopologyDemoldControl::ClearEdgeSelection Method ()](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyDemoldControl~ClearEdgeSelection.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
