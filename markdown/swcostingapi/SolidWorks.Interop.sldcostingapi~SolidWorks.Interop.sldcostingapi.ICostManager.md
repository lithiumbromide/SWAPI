---
title: "ICostManager Interface"
project: "SOLIDWORKS Costing API Help"
interface: "ICostManager"
member: ""
kind: "interface"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager.html"
---

# ICostManager Interface

Allows access to the entry-point interface of the SOLIDWORKS Costing API and the CostingManager.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICostManager
```

### Visual Basic (Usage)

```vb
Dim instance As ICostManager
```

### C#

```csharp
public interface ICostManager
```

### C++/CLI

```cpp
public interface class ICostManager
```

## VBA Syntax

See [CostManager](swcostingapivb6.chm::/SldCostingAPI~CostManager.html).

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

SOLIDWORKS Costing and its API are only available in SOLIDWORKS Professional and SOLIDWORKS Premium.

If Costing is not licensed on the host system, then null is returned.

## Accessors

[IModelDocExtension::GetCostingManager](ms-its:sldworksapi.chm::/SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~GetCostingManager.html)

## See Also

[ICostManager Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager_members.html)
[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
[ICostManager::Close Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~Close.html)
