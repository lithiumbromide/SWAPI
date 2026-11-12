---
title: "IGetMaterials Method (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "IGetMaterials"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMaterials.html"
---

# IGetMaterials Method (ICostAnalysisMachining)

Gets the names of the materials in the specified class from the Costing template for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMaterials( _
   ByVal ClassName As System.String, _
   ByVal NumMaterialNames As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim ClassName As System.String
Dim NumMaterialNames As System.Integer
Dim value As System.String

value = instance.IGetMaterials(ClassName, NumMaterialNames)
```

### C#

```csharp
System.string IGetMaterials(
   System.string ClassName,
   System.int NumMaterialNames
)
```

### C++/CLI

```cpp
System.String^ IGetMaterials(
   System.String^ ClassName,
   System.int NumMaterialNames
)
```

### Parameters

- `ClassName`: Name of material class
- `NumMaterialNames`: Number of the materials in the specified material class

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the materials in the specified class

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this method, call [ICostAnalysisMachining::GetMaterialCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterialCount.html) to get the NumMaterialNames value.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachining::GetMaterials Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterials.html)
[ICostAnalysisMachining::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterialClasses.html)
[ICostAnalysisMachining::IGetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMaterialClasses.html)
[ICostAnalysisMachining::CurrentMaterial Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentMaterial.html)
[ICostAnalysisMachining::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentMaterialClass.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
