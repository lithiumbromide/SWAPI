---
title: "Classification Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "Classification"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~Classification.html"
---

# Classification Property (InspectionProjectData)

Gets and sets the defect classification for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Classification As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Integer

instance.Classification = value

value = instance.Classification
```

### C#

```csharp
System.int Classification {get; set;}
```

### C++/CLI

```cpp
property System.int Classification {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Defect classification as defined by [swiCharacteristicClassification_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiCharacteristicClassification_e.html)

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
