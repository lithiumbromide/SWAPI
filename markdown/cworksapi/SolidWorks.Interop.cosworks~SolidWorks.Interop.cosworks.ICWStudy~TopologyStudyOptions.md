---
title: "TopologyStudyOptions Property (ICWStudy)"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWStudy"
member: "TopologyStudyOptions"
kind: "property"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~TopologyStudyOptions.html"
---

# TopologyStudyOptions Property (ICWStudy)

Gets this topology study's options.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TopologyStudyOptions As CWTopologyStudyOptions
```

### Visual Basic (Usage)

```vb
Dim instance As ICWStudy
Dim value As CWTopologyStudyOptions

value = instance.TopologyStudyOptions
```

### C#

```csharp
CWTopologyStudyOptions TopologyStudyOptions {get;}
```

### C++/CLI

```cpp
property CWTopologyStudyOptions^ TopologyStudyOptions {
   CWTopologyStudyOptions^ get();
}
```

### Property Value

[ICWTopologyStudyOptions](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyOptions.html)

## VBA Syntax

See [CWStudy::TopologyStudyOptions](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWStudy~TopologyStudyOptions.html).

## Examples

[Create Topology Study (VBA)](Create_Topology_Study_Example_VB.htm)

## Remarks

This property is only valid for topology studies.

## See Also

[ICWStudy Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy.html)
[ICWStudy Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy_members.html)

## Availability

SOLIDWORKS Simulation API 2019 SP0
