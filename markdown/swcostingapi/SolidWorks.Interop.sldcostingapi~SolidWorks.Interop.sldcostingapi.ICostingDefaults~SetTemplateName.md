---
title: "SetTemplateName Method (ICostingDefaults)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostingDefaults"
member: "SetTemplateName"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~SetTemplateName.html"
---

# SetTemplateName Method (ICostingDefaults)

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
Dim instance As ICostingDefaults
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

[ICostingDefaults Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults.html)
[ICostingDefaults Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults_members.html)
[ICostingDefaults::GetTemplateName Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostingDefaults~GetTemplateName.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
