---
title: "SetAreaDepthUnit Method (ICWTopologyPreservedRegionControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyPreservedRegionControl"
member: "SetAreaDepthUnit"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl~SetAreaDepthUnit.html"
---

# SetAreaDepthUnit Method (ICWTopologyPreservedRegionControl)

Sets the units of preserved area depth in this topology study preserved region manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetAreaDepthUnit( _
   ByVal NUnit As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyPreservedRegionControl
Dim NUnit As System.Integer

instance.SetAreaDepthUnit(NUnit)
```

### C#

```csharp
void SetAreaDepthUnit(
   System.int NUnit
)
```

### C++/CLI

```cpp
void SetAreaDepthUnit(
   System.int NUnit
)
```

### Parameters

- `NUnit`: Units of preserved area depth as defined in [swsLinearUnit_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsLinearUnit_e.html)

## VBA Syntax

See [CWTopologyPreservedRegion::SetAreaDepthUnit](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyPreservedRegion~SetAreaDepthUnit.html).

## Examples

See the [ICWTopologyPreservedRegionControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html) example.

## Remarks

This method is valid only if [ICWTopologyPreservedRegionControl::SetIncludeRegionDepth](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl~SetIncludeRegionDepth.html) is set to 1.

## See Also

[ICWTopologyPreservedRegionControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html)
[ICWTopologyPreservedRegionControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
