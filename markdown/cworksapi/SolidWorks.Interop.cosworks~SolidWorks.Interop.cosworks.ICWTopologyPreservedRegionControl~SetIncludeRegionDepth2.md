---
title: "SetIncludeRegionDepth2 Method (ICWTopologyPreservedRegionControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyPreservedRegionControl"
member: "SetIncludeRegionDepth2"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl~SetIncludeRegionDepth2.html"
---

# SetIncludeRegionDepth2 Method (ICWTopologyPreservedRegionControl)

Sets whether to include the preserved area depth in this topology study preserved region manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetIncludeRegionDepth2( _
   ByVal BFlag As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyPreservedRegionControl
Dim BFlag As System.Boolean

instance.SetIncludeRegionDepth2(BFlag)
```

### C#

```csharp
void SetIncludeRegionDepth2(
   System.bool BFlag
)
```

### C++/CLI

```cpp
void SetIncludeRegionDepth2(
   System.bool BFlag
)
```

### Parameters

- `BFlag`: -1 or true to include preserved area depth, 0 or false to not

## VBA Syntax

See [CWTopologyPreservedRegion::SetIncludeRegionDepth2](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyPreservedRegion~SetIncludeRegionDepth2.html).

## Examples

See the [ICWTopologyPreservedRegionControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html) example.

## See Also

[ICWTopologyPreservedRegionControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html)
[ICWTopologyPreservedRegionControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl_members.html)

## Availability

SOLIDWORKS Simulation API 2022 SP0
