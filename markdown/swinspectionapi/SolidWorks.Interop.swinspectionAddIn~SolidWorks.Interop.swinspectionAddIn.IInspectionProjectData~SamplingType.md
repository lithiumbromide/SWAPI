---
title: "SamplingType Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "SamplingType"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~SamplingType.html"
---

# SamplingType Property (IInspectionProjectData)

Gets and sets the statistical sampling type for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property SamplingType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
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

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
