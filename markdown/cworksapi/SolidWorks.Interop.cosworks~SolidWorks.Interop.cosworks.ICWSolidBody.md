---
title: "ICWSolidBody Interface"
project: "SOLIDWORKS Simulation API Help"
interface: "ICWSolidBody"
member: ""
kind: "interface"
source: "cworksapi/SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody.html"
---

# ICWSolidBody Interface

Allows access to solid bodies in a study.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICWSolidBody
```

### Visual Basic (Usage)

```vb
Dim instance As ICWSolidBody
```

### C#

```csharp
public interface ICWSolidBody
```

### C++/CLI

```cpp
public interface class ICWSolidBody
```

## VBA Syntax

See [CWSolidBody](ms-its:cworksapivb6.chm::/CosmosWorksLib~CWSolidBody.html).

## Examples

[Create Nonlinear Study and Apply Materials (C#)](Create_Nonlinear_Study_and_Apply_Materials_Example_CSharp.htm)
[Create Nonlinear Study and Apply Materials (VB.NET)](Create_Nonlinear_Study_and_Apply_Materials_Example_VBNET.htm)
[Create Nonlinear Study and Apply Materials (VBA)](Create_Nonlinear_Study_and_Apply_Materials_Example_VB.htm)

## Remarks

SOLIDWORKS Simulation supports multi-body components.

Material properties must be defined for every solid body before running an analysis.

## Accessors

[ICWSolidComponent::GetSolidBodyAt](SOLIDWORKS.Interop.cosworks~SOLIDWORKS.Interop.cosworks.ICWSolidComponent~GetSolidBodyAt.html)

[ICWSolidManager::GetSolidBodyByName](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager~GetSolidBodyByName.html)

## See Also

[ICWSolidBody Members](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidBody_members.html)
[SolidWorks.Interop.cosworks Namespace](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks_namespace.html)
[ICWSolidComponent Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidComponent.html)
[ICWSolidManager Interface](SolidWorks.Interop.cosworks~SolidWorks.Interop.cosworks.ICWSolidManager.html)
