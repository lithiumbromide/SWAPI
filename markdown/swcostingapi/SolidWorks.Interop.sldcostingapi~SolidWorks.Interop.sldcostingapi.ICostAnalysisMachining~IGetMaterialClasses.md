---
title: "IGetMaterialClasses Method (ICostAnalysisMachining)"
project: "SOLIDWORKS Costing API Help"
interface: "ICostAnalysisMachining"
member: "IGetMaterialClasses"
kind: "method"
source: "swcostingapi/SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~IGetMaterialClasses.html"
---

# IGetMaterialClasses Method (ICostAnalysisMachining)

Gets the names of the material classes from the Costing template for this machining Costing analysis.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetMaterialClasses( _
   ByVal NumClassNames As System.Integer _
) As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As ICostAnalysisMachining
Dim NumClassNames As System.Integer
Dim value As System.String

value = instance.IGetMaterialClasses(NumClassNames)
```

### C#

```csharp
System.string IGetMaterialClasses(
   System.int NumClassNames
)
```

### C++/CLI

```cpp
System.String^ IGetMaterialClasses(
   System.int NumClassNames
)
```

### Parameters

- `NumClassNames`: Number of material classes

### Return Value

- in-process, unmanaged C++: Pointer to an array of strings of the names of the material classes

VBA, VB.NET, C#, and C++/CLI: Not supported

## Remarks

Before calling this method, call [ICostAnalsyisMachining::GetMaterialClassesCount](SOLIDWORKS.Interop.sldcostingapi~SOLIDWORKS.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterialClassesCount.html) to get the NumClassNames value.

See [Getting Started](GettingStarted-swcostingapi.html) for details about Costing templates.

## See Also

[ICostAnalysisMachining Interface](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining.html)
[ICostAnalysisMachining Members](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining_members.html)
[ICostAnalysisMachinging::GetMaterialClasses Method ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~GetMaterialClasses.html)
[ICostAnalysisMachinging::CurrentMaterialClass Property ()](SolidWorks.Interop.sldcostingapi~SolidWorks.Interop.sldcostingapi.ICostAnalysisMachining~CurrentMaterialClass.html)

## Availability

SOLIDWORKS Costing API 2013 SP0
