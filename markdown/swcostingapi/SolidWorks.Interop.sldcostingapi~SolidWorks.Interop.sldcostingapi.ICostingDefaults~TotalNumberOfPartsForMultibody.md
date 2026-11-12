---
title: "TotalNumberOfPartsForMultibody Property (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "TotalNumberOfPartsForMultibody"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~TotalNumberOfPartsForMultibody.html"
---

# TotalNumberOfPartsForMultibody Property (ICostingDefaults)

Sets the default total number of parts for multibody mode in this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property TotalNumberOfPartsForMultibody As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ICostingDefaults
Dim value As System.Integer

instance.TotalNumberOfPartsForMultibody = value

value = instance.TotalNumberOfPartsForMultibody
```

### C#

```csharp
System.int TotalNumberOfPartsForMultibody {get; set;}
```

### C++/CLI

```cpp
property System.int TotalNumberOfPartsForMultibody {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Default total number of parts for multibody mode

## VBA Syntax

See [CostDefaults::TotalNumberOfPartsForMultibody](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~TotalNumberOfPartsForMultibody.html).

## See Also

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::LotSizeForMultibody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~LotSizeForMultibody.html)
[ICostingDefaults::TotalNumberOfPartsForSingleBody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~TotalNumberOfPartsForSingleBody.html)
[ICostingDefaults::LotSizeForSingleBody Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~LotSizeForSingleBody.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
