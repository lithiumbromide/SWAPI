---
title: "ICWTopologyStudyManager Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyStudyManager"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager.html"
---

# ICWTopologyStudyManager Interface

Allows you to manage topology studies. **NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWTopologyStudyManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyStudyManager
```

### C#

```csharp
public interface ICWTopologyStudyManager
```

### C++/CLI

```cpp
public interface class ICWTopologyStudyManager
```

## VBA Syntax

See [CWTopologyStudyManager](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyStudyManager.html).

## Examples

[Create Topology Study (VBA)](Create_Topology_Study_Example_VB.htm)

## Remarks

A topology study:

- seeks to optimize the material layout of parts by redistributing material, subject to all applied loads, fixtures, and manufacturing constraints.
- consists of optimization goals, constraints, preserved regions, and manufacturing controls. A topology constraint defines, for example, how much material to remove (mass constraint) or how far to displace a component (displacement constraint) to satisfy a given topology optimization goal (e.g., minimize maximum displacement).
- is available with SOLIDWORKS Simulation Professional and Premium licenses only.

See the **Topology Study** topic in the Simulation user-interface help for more information.

## Accessors

[ICWStudy::TopologyStudyManager](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWStudy~TopologyStudyManager.html)

## See Also

[ICWTopologyStudyManager Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
