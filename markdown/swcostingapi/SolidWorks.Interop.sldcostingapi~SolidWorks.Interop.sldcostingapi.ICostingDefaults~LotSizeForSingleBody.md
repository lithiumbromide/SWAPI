---
title: "LotSizeForSingleBody Property (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "LotSizeForSingleBody"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~LotSizeForSingleBody.html"
---

# LotSizeForSingleBody Property (ICostingDefaults)

Gets or sets the default lot size for single-body mode for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property LotSizeForSingleBody As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostingDefaults
Dim value As System.Integer

instance.LotSizeForSingleBody = value

value = instance.LotSizeForSingleBody
```

### C#

```csharp
System.int LotSizeForSingleBody {get; set;}
```

### C++/CLI

```cpp
property System.int LotSizeForSingleBody {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Default lot size for single-body mode

## VBA Syntax

See [CostDefaults::LotSizeForSingleBody](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~LotSizeForSingleBody.html).

## Examples

See the [ICostingDefaults](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html) examples.

## See Also

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::TotalNumberOfPartsForSingleBody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~TotalNumberOfPartsForSingleBody.html)
[ICostingDefaults::LotSizeForMultibody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~LotSizeForMultibody.html)
[ICostingDefaults::TotalNumberOfPartsForMultibody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~TotalNumberOfPartsForMultibody.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
