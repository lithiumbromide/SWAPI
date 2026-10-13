---
title: "ICostFeature Interface"
project: "SOLIDWORKS Costing API Help"
interface: "ICostFeature"
member: ""
kind: "interface"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature.html"
---

# ICostFeature Interface

Allows access to Costing features and subfeatures.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICostFeature
```

### Visual Basic (Usage)

```vb
Dim instance As ICostFeature
```

### C#

```csharp
public interface ICostFeature
```

### C++/CLI

```cpp
public interface class ICostFeature
```

## VBA Syntax

See [CostFeature](swcostingapivb6.chm::/SldCostingAPI~CostFeature.html).

## Examples

[Create Sheet Metal Costing Analysis (C#)](Create_Sheet_Metal_Costing_Analyses_Example_CSharp.htm)
[Create Sheet Metal Costing Analysis (VB.NET)](Create_Sheet_Metal_Costing_Analyses_Example_VBNET.htm)
[Create Sheet Metal Costing Analysis (VBA)](Create_Sheet_Metal_Costing_Analyses_Example_VB.htm)
[Create Machining Costing Analysis (C#)](Create_Machining_Costing_Analyses_Example_CSharp.htm)
[Create Machining Costing Analysis (VB.NET)](Create_Machining_Costing_Analyses_Example_VBNET.htm)
[Create Machining Costing Analysis (VBA)](Create_Machining_Costing_Analyses_Example_VB.htm)

## Remarks

SOLIDWORKS Costing interprets geometry as to how it will be manufactured, not how it is designed.

In the Costing tool, the features that are seen in the CostingManager are not the same as SOLIDWORKS features. Costing features are created as a result of Costing feature recognition.

For example, in sheet metal Costing, a Hole Wizard hole through a sheet metal part is recognized as a cut path. This cut path is manufactured using laser, waterjet, or plasma cutting. In machining Costing, an extruded cut or Hole Wizard hole in SOLIDWORKS is recognized as a drilled hole.

Sometimes an entire group of SOLIDWORKS features is recognized as one manufacturing feature in Costing. For example, the outside edges of a part might consist of fillets and straight edges. These are recognized in Costing as one cut path.

## Accessors

[ICostAnalysis::GetFirstCostFeature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysis~GetFirstCostFeature.html)

[ICostFeature::GetFirstSubFeature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostFeature~GetFirstSubFeature.html)

[ICostFeature::GetNextFeature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostFeature~GetNextFeature.html)

[ICostFeature::GetNextSubFeature](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostFeature~GetNextSubFeature.html)

## See Also

[ICostFeature Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostFeature_members.html)
[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
[ICostBody Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBody.html)
[ICostPart Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostPart.html)
