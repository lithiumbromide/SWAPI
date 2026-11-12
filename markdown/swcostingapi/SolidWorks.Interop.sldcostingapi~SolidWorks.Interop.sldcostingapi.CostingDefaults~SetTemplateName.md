---
title: "SetTemplateName Method (CostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "CostingDefaults"
member: "SetTemplateName"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults~SetTemplateName.html"
---

# SetTemplateName Method (CostingDefaults)

Sets the path and file name of the default Costing template for the specified type of Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetTemplateName( _
   ByVal CostingType As System.Integer, _
   ByVal TemplateName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As CostingDefaults
Dim CostingType As System.Integer
Dim TemplateName As System.String

instance.SetTemplateName(CostingType, TemplateName)
```

### C#

```csharp
void SetTemplateName(
   System.int CostingType,
   System.string TemplateName
)
```

### C++/CLI

```cpp
void SetTemplateName(
   System.int CostingType,
   System.String^ TemplateName
)
```

### Parameters

- `CostingType`: Type of Costing analysis as defined in [swcCostingType_e](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.swcCostingType_e.html)
- `TemplateName`: Path and file name of the default Costing template

## VBA Syntax

See [CostDefaults::SetTemplateName](swcostingapivb6.chm::/SldCostingAPI~CostingDefaults~SetTemplateName.html).

## Remarks

Changes made to default settings are saved to the registry and are applied in the next and subsequent Costing sessions.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[CostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults.html)
[CostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.CostingDefaults_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
