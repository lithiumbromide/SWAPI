---
title: "ICWSolidComponent Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidComponent"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent.html"
---

# ICWSolidComponent Interface

Allows access to solid components in a study.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWSolidComponent
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidComponent
```

### C#

```csharp
public interface ICWSolidComponent
```

### C++/CLI

```cpp
public interface class ICWSolidComponent
```

## VBA Syntax

See [CWSolidComponent](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidComponent.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## Remarks

SOLIDWORKS Simulation supports multi-body components.

Material properties must be defined for every solid body before running analysis.

## Accessors

[ICWSolidManager::GetComponentAt](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidManager~GetComponentAt.html)

## See Also

[ICWSolidComponent Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWSolidBody Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html)
[ICWSolidManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html)
