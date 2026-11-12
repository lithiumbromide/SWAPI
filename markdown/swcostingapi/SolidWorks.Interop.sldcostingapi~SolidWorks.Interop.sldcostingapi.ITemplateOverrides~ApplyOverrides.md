---
title: "ApplyOverrides Method (ITemplateOverrides)"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: "ApplyOverrides"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~ApplyOverrides.html"
---

# ApplyOverrides Method (ITemplateOverrides)

Applies all overridden system-level options.

## Syntax

### Visual Basic (Declaration)

```vb
Sub ApplyOverrides()
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides

instance.ApplyOverrides()
```

### C#

```csharp
void ApplyOverrides()
```

### C++/CLI

```cpp
void ApplyOverrides();
```

## VBA Syntax

See [TemplateOverrides::ApplyOverrides](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides~ApplyOverrides.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

Call this method after setting any of the [ITemplateOverrides properties](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_properties.html) to override that system-level option.

## See Also

[ITemplateOverrides Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html)
[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[ITemplateOverrides::ResetAll Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~ResetAll.html)
[ITemplateOverrides::SaveCostingOverrideSettings Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides~SaveCostingOverrideSettings.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
