---
title: "SheetmetalBlankSizeType Property (CostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "CostingDefaults"
member: "SheetmetalBlankSizeType"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults~SheetmetalBlankSizeType.html"
---

# SheetmetalBlankSizeType Property (CostingDefaults)

Gets or sets the default type of sheet metal blank size for this Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Property SheetmetalBlankSizeType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As CostingDefaults
Dim value As System.Integer

instance.SheetmetalBlankSizeType = value

value = instance.SheetmetalBlankSizeType
```

### C#

```csharp
System.int SheetmetalBlankSizeType {get; set;}
```

### C++/CLI

```cpp
property System.int SheetmetalBlankSizeType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Default type of sheet metal blank size as defined in [swcSheetMetalBlankSizeType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcSheetMetalBlankSizeType_e.html)

## VBA Syntax

See [CostDefaults::SheetmetalBlankSizeType](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~SheetmetalBlankSizeType.html).

## Examples

See the [ICostingDefaults](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html) examples.

## See Also

[CostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults.html)
[CostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
