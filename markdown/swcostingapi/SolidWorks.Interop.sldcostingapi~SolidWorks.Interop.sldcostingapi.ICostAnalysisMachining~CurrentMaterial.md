---
title: "CurrentMaterial Property (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "CurrentMaterial"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentMaterial.html"
---

# CurrentMaterial Property (ICostAnalysisMachining)

Gets or sets the name of the material for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentMaterial As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim value As System.String

instance.CurrentMaterial = value

value = instance.CurrentMaterial
```

### C#

```csharp
System.string CurrentMaterial {get; set;}
```

### C++/CLI

```cpp
property System.String^ CurrentMaterial {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the material

## VBA Syntax

See [CostAnalysisMachining::CurrentMaterial.](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisMachining~CurrentMaterial.html)

## Examples

[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## Remarks

Setting this property might invalidate other settings; e.g., plate thickness.

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::GetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterials.html)
[ICostAnalysisMachining::IGetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMaterials.html)
[ICostAnalysisMachining::GetMaterialCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterialCount.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
