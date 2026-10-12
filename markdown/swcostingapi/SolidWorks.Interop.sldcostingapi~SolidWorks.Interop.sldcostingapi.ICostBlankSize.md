---
title: "ICostBlankSize Interface"
project: "SOLIDWORKS Costing API Help"
interface: "ICostBlankSize"
member: ""
kind: "interface"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBlankSize.html"
---

# ICostBlankSize Interface

Allows access to a custom blank of a sheet metal part in a sheet metal Costing analysis.
**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICostBlankSize
```

### Visual Basic (Usage)

```vb
Dim instance As ICostBlankSize
```

### C#

```csharp
public interface ICostBlankSize
```

### C++/CLI

```cpp
public interface class ICostBlankSize
```

## VBA Syntax

See [CostBlankSize](swcostingapivb6.chm::/SldCostingAPI~CostBlankSize.html).

## Remarks

[ICostAnalysisSheetMetal::BlankSizeType](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~BlankSizeType.html) must be set to swcSheetMetalBlankSizeType_e.swcSheetMetalBlankSizeType_CustomSize to set the length or width of a custom blank.

## Accessors

[ICostAnalysisSheetMetal::CustomBlankSize](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisSheetMetal~CustomBlankSize.html)

## See Also

[ICostBlankSize Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostBlankSize_members.html)
[SolidWorks.Interop.sldcostingapi Namespace](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi_namespace.html)
