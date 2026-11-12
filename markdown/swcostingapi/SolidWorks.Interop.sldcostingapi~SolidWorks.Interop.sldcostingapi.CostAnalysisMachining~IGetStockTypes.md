---
title: "IGetStockTypes Method (CostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "CostAnalysisMachining"
member: "IGetStockTypes"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining~IGetStockTypes.html"
---

# IGetStockTypes Method (CostAnalysisMachining)

Gets the stock types for the specified material from the Costing template for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetStockTypes( _
   ByVal MaterialClass As System.String, _
   ByVal MaterialName As System.String, _
   ByVal NumStockTypes As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostAnalysisMachining
Dim MaterialClass As System.String
Dim MaterialName As System.String
Dim NumStockTypes As System.Integer
Dim value As System.Integer

value = instance.IGetStockTypes(MaterialClass, MaterialName, NumStockTypes)
```

### C#

```csharp
System.int IGetStockTypes(
   System.string MaterialClass,
   System.string MaterialName,
   System.int NumStockTypes
)
```

### C++/CLI

```cpp
System.int IGetStockTypes(
   System.String^ MaterialClass,
   System.String^ MaterialName,
   System.int NumStockTypes
)
```

### Parameters

- `MaterialClass`: Name of the material class
- `MaterialName`: Name of the material
- `NumStockTypes`: Number of stock types defined for the specified material

### Return Value

- in-process, unmanaged C++: Pointer to an array of integers of the stock types of the specified material as defined in [swcStockType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcStockType_e.html)

- VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this method, call [ICostAnalysisMachining::GetStockTypeCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~GetStockTypeCount.html) to get the NumStockTypes value.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining.html)
[CostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostAnalysisMachining_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
