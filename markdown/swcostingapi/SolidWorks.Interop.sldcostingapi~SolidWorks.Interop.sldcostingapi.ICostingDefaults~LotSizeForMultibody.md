---
title: "LotSizeForMultibody Property (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "LotSizeForMultibody"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~LotSizeForMultibody.html"
---

# LotSizeForMultibody Property (ICostingDefaults)

Gets or sets the default lot size for multibody mode for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property LotSizeForMultibody As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostingDefaults
Dim value As System.Integer

instance.LotSizeForMultibody = value

value = instance.LotSizeForMultibody
```

### C#

```csharp
System.int LotSizeForMultibody {get; set;}
```

### C++/CLI

```cpp
property System.int LotSizeForMultibody {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Default lot size for multibody mode

## VBA Syntax

See [CostDefaults::LotSizeForMultibody](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~LotSizeForMultibody.html).

## See Also

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::TotalNumberOfPartsForMultibody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~TotalNumberOfPartsForMultibody.html)
[ICostingDefaults::LotSizeForSingleBody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~LotSizeForSingleBody.html)
[ICostingDefaults::TotalNumberOfPartsForSingleBody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~TotalNumberOfPartsForSingleBody.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
