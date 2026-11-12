---
title: "CurrentMaterialClass Property (ICostAnalysis3dPrinting)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysis3dPrinting"
member: "CurrentMaterialClass"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~CurrentMaterialClass.html"
---

# CurrentMaterialClass Property (ICostAnalysis3dPrinting)

Gets or sets the name of the material class for this 3D printing Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property CurrentMaterialClass As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysis3dPrinting
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

See [CostAnalysis3dPrinting::CurrentMaterialClass](swcostingapivb6.chm::/SldCostingAPI~CostAnalysis3dPrinting~CurrentMaterialClass.html).

## Examples

See the [ICostAnalysis3dPrinting](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html) examples.

## Remarks

Setting this property could invalidate other settings.

## See Also

[ICostAnalysis3dPrinting Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting.html)
[ICostAnalysis3dPrinting Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting_members.html)
[ICostAnalysis3dPrinting::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~GetMaterialClasses.html)
[ICostAnalysis3dPrinting::GetMaterialClassesCount Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysis3dPrinting~GetMaterialClassesCount.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
