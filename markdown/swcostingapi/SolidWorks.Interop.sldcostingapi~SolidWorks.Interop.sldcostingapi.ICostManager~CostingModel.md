---
title: "CostingModel Property (ICostManager)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostManager"
member: "CostingModel"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~CostingModel.html"
---

# CostingModel Property (ICostManager)

Gets a Costing model.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CostingModel As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostManager
Dim value As System.Object

value = instance.CostingModel
```

### C#

```csharp
System.object CostingModel {get;}
```

### C++/CLI

```cpp
property System.Object^ CostingModel {
   System.Object^ get();
}
```

### Property Value

[Costing model](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostPart.html)

## VBA Syntax

See [CostManager::CostingModel](swcostingapivb6.chm::/SldCostingAPI~CostManager~CostingModel.html).

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## See Also

[ICostManager Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager.html)
[ICostManager Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager_members.html)

## Availability

SOLIDWORKS Costing 2013 SP0
