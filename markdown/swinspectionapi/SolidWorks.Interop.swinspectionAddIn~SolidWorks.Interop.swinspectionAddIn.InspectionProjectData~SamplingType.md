---
title: "SamplingType Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "SamplingType"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~SamplingType.html"
---

# SamplingType Property (InspectionProjectData)

Gets and sets the statistical sampling type for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property SamplingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Integer

instance.SamplingType = value

value = instance.SamplingType
```

### C#

```csharp
System.int SamplingType {get; set;}
```

### C++/CLI

```cpp
property System.int SamplingType {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Sampling type as defined by [swiSamplingType_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiSamplingType_e.html)

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
