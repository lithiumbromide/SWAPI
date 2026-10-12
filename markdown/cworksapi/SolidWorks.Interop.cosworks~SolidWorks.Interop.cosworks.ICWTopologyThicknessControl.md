---
title: "ICWTopologyThicknessControl Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWTopologyThicknessControl"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl.html"
---

# ICWTopologyThicknessControl Interface

Allows access to a thickness manufacturing control in a topology study. **NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWTopologyThicknessControl
```

### Visual Basic (Usage)

```vb
Dim instance As ICWTopologyThicknessControl
```

### C#

```csharp
public interface ICWTopologyThicknessControl
```

### C++/CLI

```cpp
public interface class ICWTopologyThicknessControl
```

## VBA Syntax

See [CWTopologyThicknessControl](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWTopologyThicknessControl.html).

## Examples

[Create Topology Study (VBA)](Create_Topology_Study_Example_VB.htm)

## Remarks

Thickness manufacturing controls are member size restrictions during optimization that prevent the creation of very thin or thick regions that make manufacture difficult.

See the **Manufacturing Controls** topic in the Simulation user-interface help for more information.

## Accessors

[ICWTopologyStudyManager::CreateThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~CreateThicknessControl.html)

[ICWTopologyStudyManager::GetThicknessControl](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyStudyManager~GetThicknessControl.html)

## See Also

[ICWTopologyThicknessControl Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWTopologyThicknessControl_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
