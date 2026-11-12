---
title: "RemoveAllSelections Method (ICWTopologyPreservedRegionControl)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyPreservedRegionControl"
member: "RemoveAllSelections"
kind: "method"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl~RemoveAllSelections.html"
---

# RemoveAllSelections Method (ICWTopologyPreservedRegionControl)

Removes selected faces from the selection list for this topology study preserved region manufacturing control.

## Syntax

### Visual Basic (Declaration)

```vb
Function RemoveAllSelections() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyPreservedRegionControl
Dim value As System.Integer

value = instance.RemoveAllSelections()
```

### C#

```csharp
System.int RemoveAllSelections()
```

### C++/CLI

```cpp
System.int RemoveAllSelections();
```

### Return Value

Result code as defined in [swsTopologyStudy_PreservedRegionErrors_e](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.swsTopologyStudy_PreservedRegionErrors_e.html)

## VBA Syntax

See [CWTopologyPreservedRegion::RemoveAllSelections](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyPreservedRegion~RemoveAllSelections.html).

## See Also

[ICWTopologyPreservedRegionControl Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl.html)
[ICWTopologyPreservedRegionControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyPreservedRegionControl_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
