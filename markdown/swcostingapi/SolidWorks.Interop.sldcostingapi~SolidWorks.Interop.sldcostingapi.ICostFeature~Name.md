---
title: "Name Property (ICostFeature)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature"
member: "Name"
kind: "property"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~Name.html"
---

# Name Property (ICostFeature)

Gets or sets the name of the Costing feature in the CostingManager.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostFeature
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the Costing feature in the CostingManager

## VBA Syntax

See [CostFeature::Name](swcostingapivb6.chm::/SldCostingAPI~CostFeature~Name.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## See Also

[ICostFeature Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature.html)
[ICostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature_members.html)
[ICostFeature::GetType Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature~GetType.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
