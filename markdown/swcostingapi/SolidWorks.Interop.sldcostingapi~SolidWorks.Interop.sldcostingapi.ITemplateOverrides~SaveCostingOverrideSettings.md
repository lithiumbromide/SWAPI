---
title: "SaveCostingOverrideSettings Method (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "SaveCostingOverrideSettings"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SaveCostingOverrideSettings.html"
---

# SaveCostingOverrideSettings Method (ITemplateOverrides)

Saves all overridden system-level settings to the registry.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SaveCostingOverrideSettings()
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides

instance.SaveCostingOverrideSettings()
```

### C#

```csharp
void SaveCostingOverrideSettings()
```

### C++/CLI

```cpp
void SaveCostingOverrideSettings();
```

## VBA Syntax

See [TemplateOverrides::SaveCostingOverrideSettings](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~SaveCostingOverrideSettings.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

Overridden system-level settings are saved to the registry and are applied in the next and subsequent Costing sessions.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[ITemplateOverrides::ApplyOverrides Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~ApplyOverrides.html)
[ITemplateOverrides::ResetAll Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~ResetAll.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
