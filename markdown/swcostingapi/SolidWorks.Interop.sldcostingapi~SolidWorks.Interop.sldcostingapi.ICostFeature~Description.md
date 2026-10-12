---
title: "Description Property (ICostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature"
member: "Description"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~Description.html"
---

# Description Property (ICostFeature)

Gets or sets the description of this Costing feature, including information about selected sub-operation options.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property Description As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostFeature
Dim value As System.String

value = instance.Description
```

### C#

```csharp
System.string Description {get;}
```

### C++/CLI

```cpp
property System.String^ Description {
   System.String^ get();
}
```

### Property Value

Description of this Costing feature, including information about selected sub-operation options

## VBA Syntax

See [CostFeature::Description](swcostingapivb6.chm::/SldCostingAPI~CostFeature~Description.html).

## See Also

[ICostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature.html)
[ICostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature_members.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
