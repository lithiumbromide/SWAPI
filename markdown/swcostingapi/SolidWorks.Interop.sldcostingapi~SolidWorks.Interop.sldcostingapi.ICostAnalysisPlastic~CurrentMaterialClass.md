---
title: "CurrentMaterialClass Property (ICostAnalysisPlastic)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisPlastic"
member: "CurrentMaterialClass"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~CurrentMaterialClass.html"
---

# CurrentMaterialClass Property (ICostAnalysisPlastic)

Gets or sets the name of the material class for this plastic Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentMaterialClass As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisPlastic
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

See [CostAnalysisPlastic::CurrentMaterialClass](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisPlastic~CurrentMaterialClass.html).

## Examples

See the [ICostAnalysisPlastic](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html) examples.

## Remarks

Setting this property could invalidate other settings.

## See Also

[ICostAnalysisPlastic Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic.html)
[ICostAnalysisPlastic Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic_members.html)
[ICostAnalysisPlastic::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~GetMaterialClasses.html)
[ICostAnalysisPlastic::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisPlastic~GetMaterialClassesCount.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
