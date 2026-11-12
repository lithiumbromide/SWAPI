---
title: "ITemplateOverrides Interface"
project: "SOLIDWORKS Costing API Help"
interface: "ITemplateOverrides"
member: ""
kind: "interface"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html"
---

# ITemplateOverrides Interface

Allows access to system-level Costing options that can be overridden.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ITemplateOverrides
```

### Visual Basic (Usage)

```vb
Dim instance As ITemplateOverrides
```

### C#

```csharp
public interface ITemplateOverrides
```

### C++/CLI

```cpp
public interface class ITemplateOverrides
```

## VBA Syntax

See [TemplateOverrides](swcostingapivb6.chm::/SldCostingAPI~TemplateOverrides.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## Remarks

You can only override system-level Costing options if [ICostPart::GetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~GetCostingMethod.html) is equal to one to the following:

- swcMethodType_e.swcMethodType_MachinedPlate
- swcMethodType_e.swcMethodType_Machining
- swcMethodType_e.swcMethodType_Sheetmetal

To set the Costing method, use [ICostPart::SetCostingMethod](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~SetCostingMethod.html).

## Accessors

[ICostPart::TemplateOverrides](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~TemplateOverrides.html)

## See Also

[ITemplateOverrides Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides_members.html)
[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
