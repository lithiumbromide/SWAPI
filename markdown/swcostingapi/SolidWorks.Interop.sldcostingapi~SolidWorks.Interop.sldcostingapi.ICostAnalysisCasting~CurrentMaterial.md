---
title: "CurrentMaterial Property (ICostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisCasting"
member: "CurrentMaterial"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~CurrentMaterial.html"
---

# CurrentMaterial Property (ICostAnalysisCasting)

Gets or sets the name of the material for this casting Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentMaterial As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisCasting
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

See [CostAnalysisCasting::CurrentMaterial](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisCasting~CurrentMaterial.html).

## Examples

See the [ICostAnalysisCasting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html) examples.

## Remarks

Setting this property could invalidate other settings.

## See Also

[ICostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html)
[ICostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting_members.html)
[ICostAnalysisCasting::GetMaterialCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialCount.html)
[ICostAnalysisCasting::GetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterials.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
