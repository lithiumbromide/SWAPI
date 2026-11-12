---
title: "Level Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "Level"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~Level.html"
---

# Level Property (IInspectionProjectData)

Gets and sets the sampling level for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Level As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Integer

instance.Level = value

value = instance.Level
```

### C#

```csharp
System.int Level {get; set;}
```

### C++/CLI

```cpp
property System.int Level {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Sampling level as defined by [swiSamplingLevel_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiSamplingLevel_e.html)

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
