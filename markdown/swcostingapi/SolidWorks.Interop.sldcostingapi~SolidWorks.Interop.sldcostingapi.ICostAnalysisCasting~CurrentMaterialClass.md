---
title: "CurrentMaterialClass Property (ICostAnalysisCasting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisCasting"
member: "CurrentMaterialClass"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~CurrentMaterialClass.html"
---

# CurrentMaterialClass Property (ICostAnalysisCasting)

Gets or sets the name of the material class for this casting Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentMaterialClass As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisCasting
Dim value As System.String

instance.CurrentMaterialClass = value

value = instance.CurrentMaterialClass
```

### C#

```csharp
System.string CurrentMaterialClass {get; set;}
```

### C++/CLI

```cpp
property System.String^ CurrentMaterialClass {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the material class

## VBA Syntax

See [CostAnalysisCasting::CurrentMaterialClass](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisCasting~CurrentMaterialClass.html).

## Examples

See the [ICostAnalysisCasting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html) examples.

## Remarks

Setting this property could invalidate other settings.

## See Also

[ICostAnalysisCasting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting.html)
[ICostAnalysisCasting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting_members.html)
[ICostAnalysisCasting::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialClasses.html)
[ICostAnalysisCasting::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisCasting~GetMaterialClassesCount.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
