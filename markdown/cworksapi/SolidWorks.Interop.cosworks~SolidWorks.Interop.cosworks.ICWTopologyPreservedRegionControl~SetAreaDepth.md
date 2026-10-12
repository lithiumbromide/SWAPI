---
title: "SetAreaDepth Method (ICWTopologyPreservedRegionControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyPreservedRegionControl"
member: "SetAreaDepth"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl~SetAreaDepth.html"
---

# SetAreaDepth Method (ICWTopologyPreservedRegionControl)

Sets the preserved area depth in this topology study preserved region manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAreaDepth( _
   ByVal DDepth As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyPreservedRegionControl
Dim DDepth As System.Double

instance.SetAreaDepth(DDepth)
```

### C#

```csharp
void SetAreaDepth(
   System.double DDepth
)
```

### C++/CLI

```cpp
void SetAreaDepth(
   System.double DDepth
)
```

### Parameters

- `DDepth`: Preserved area depth

## VBA Syntax

See [CWTopologyPreservedRegion::SetAreaDepth](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyPreservedRegion~SetAreaDepth.html).

## Examples

See the [ICWTopologyPreservedRegionControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html) example.

## Remarks

This method is valid only if [ICWTopologyPreservedRegionControl::SetIncludeRegionDepth](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl~SetIncludeRegionDepth.html) is set to 1.

## See Also

[ICWTopologyPreservedRegionControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html)
[ICWTopologyPreservedRegionControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
