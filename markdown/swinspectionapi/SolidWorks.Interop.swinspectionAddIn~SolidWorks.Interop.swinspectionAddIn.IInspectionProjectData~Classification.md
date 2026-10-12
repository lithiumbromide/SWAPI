---
title: "Classification Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "Classification"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~Classification.html"
---

# Classification Property (IInspectionProjectData)

Gets and sets the defect classification for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Classification As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
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

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
