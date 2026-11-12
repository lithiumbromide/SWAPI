---
title: "TotalNumberOfPartsForSingleBody Property (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "TotalNumberOfPartsForSingleBody"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~TotalNumberOfPartsForSingleBody.html"
---

# TotalNumberOfPartsForSingleBody Property (ICostingDefaults)

Gets or sets the default total number of parts for single-body mode in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property TotalNumberOfPartsForSingleBody As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostingDefaults
Dim value As System.Integer

instance.TotalNumberOfPartsForSingleBody = value

value = instance.TotalNumberOfPartsForSingleBody
```

### C#

```csharp
System.int TotalNumberOfPartsForSingleBody {get; set;}
```

### C++/CLI

```cpp
property System.int TotalNumberOfPartsForSingleBody {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Default total number of parts for single-body mode

## VBA Syntax

See [CostDefaults::TotalNumberOfPartsForSingleBody](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~TotalNumberOfPartsForSingleBody.html).

## Examples

See the [ICostingDefaults](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html) examples.

## See Also

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::LotSizeForSingleBody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~LotSizeForSingleBody.html)
[ICostingDefaults::TotalNumberOfPartsForMultibody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~TotalNumberOfPartsForMultibody.html)
[ICostingDefaults::LotSizeForMultibody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~LotSizeForMultibody.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
