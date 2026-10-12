---
title: "GetCostingManager Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetCostingManager"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCostingManager.html"
---

# GetCostingManager Method (IModelDocExtension)

Gets the entry-point interface to the SOLIDWORKS Costing API and gets the CostingManager.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCostingManager() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Object

value = instance.GetCostingManager()
```

### C#

```csharp
System.object GetCostingManager()
```

### C++/CLI

```cpp
System.Object^ GetCostingManager();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[ICostManager](ms-its:swcostingapi.chm::/SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostManager.html)

## VBA Syntax

See [ModelDocExtension::GetCostingManager](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~GetCostingManager.html).

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)
[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

SOLIDWORKS Costing and its API are only available in SOLIDWORKS Professional and SOLIDWORKS Premium.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS API 2013 FCS, Revision Number 21.0
