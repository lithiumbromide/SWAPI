---
title: "TemplateOverrides Property (ICostPart)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostPart"
member: "TemplateOverrides"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart~TemplateOverrides.html"
---

# TemplateOverrides Property (ICostPart)

Gets the ITemplateOverrides object.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property TemplateOverrides As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICostPart
Dim value As System.Object

value = instance.TemplateOverrides
```

### C#

```csharp
System.object TemplateOverrides {get;}
```

### C++/CLI

```cpp
property System.Object^ TemplateOverrides {
   System.Object^ get();
}
```

### Property Value

[ITemplateOverrides](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ITemplateOverrides.html) object

## VBA Syntax

See [CostPart::TemplateOverrides](swcostingapivb6.chm::/SldCostingAPI~CostPart~TemplateOverrides.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)

## See Also

[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
[ICostPart Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart_members.html)

## Availability

SOLIDWORKS Costing API 2015 SP0
