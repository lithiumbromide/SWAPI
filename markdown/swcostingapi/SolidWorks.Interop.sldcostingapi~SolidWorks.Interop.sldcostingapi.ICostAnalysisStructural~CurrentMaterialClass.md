---
title: "CurrentMaterialClass Property (ICostAnalysisStructural)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisStructural"
member: "CurrentMaterialClass"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~CurrentMaterialClass.html"
---

# CurrentMaterialClass Property (ICostAnalysisStructural)

Gets or sets the name of the material class for this structural Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentMaterialClass As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisStructural
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

See [CostAnalysisStructural::CurrentMaterialClass](swcostingapivb6.chm::/SldCostingAPI~CostAnalysisStructural~CurrentMaterialClass.html).

## Examples

See the [ICostAnalysisStructural](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html) examples.

## Remarks

Setting this property could invalidate other settings, e.g., material and weldment stock profile.

## See Also

[ICostAnalysisStructural Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural.html)
[ICostAnalysisStructural Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural_members.html)
[ICostAnalysisStructural::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~GetMaterialClasses.html)
[ICostAnalysisStructural::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisStructural~GetMaterialClassesCount.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
