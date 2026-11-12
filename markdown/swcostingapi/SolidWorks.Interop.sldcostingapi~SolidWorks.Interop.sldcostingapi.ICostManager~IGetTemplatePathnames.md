---
title: "IGetTemplatePathnames Method (ICostManager)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostManager"
member: "IGetTemplatePathnames"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~IGetTemplatePathnames.html"
---

# IGetTemplatePathnames Method (ICostManager)

Gets the paths and filenames of the Costing templates available for the specified type of Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetTemplatePathnames( _
   ByVal CostingType As System.Integer, _
   ByVal NumTemplates As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostManager
Dim CostingType As System.Integer
Dim NumTemplates As System.Integer
Dim value As System.String

value = instance.IGetTemplatePathnames(CostingType, NumTemplates)
```

### C#

```csharp
System.string IGetTemplatePathnames(
   System.int CostingType,
   System.int NumTemplates
)
```

### C++/CLI

```cpp
System.String^ IGetTemplatePathnames(
   System.int CostingType,
   System.int NumTemplates
)
```

### Parameters

- `CostingType`: Type of Costing analysis as defined in [swcCostingType_e](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.swcCostingType_e.html)
- `NumTemplates`: Number of Costing templates available for CostingType

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the paths and filenames of the Costing templates available for CostingType
- VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this method, call [ICostManager::GetTemplateCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostManager~GetTemplateCount.html) to get the NumTemplates value.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostManager Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager.html)
[ICostManager Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager_members.html)
[ICostManager::GetTemplatePathnames Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostManager~GetTemplatePathnames.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
