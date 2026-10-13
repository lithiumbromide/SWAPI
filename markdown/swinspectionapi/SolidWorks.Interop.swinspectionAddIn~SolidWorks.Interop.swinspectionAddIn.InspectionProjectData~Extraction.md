---
title: "Extraction Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "Extraction"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~Extraction.html"
---

# Extraction Property (InspectionProjectData)

Gets and sets the type of extraction for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Extraction As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Integer

instance.Extraction = value

value = instance.Extraction
```

### C#

```csharp
System.int Extraction {get; set;}
```

### C++/CLI

```cpp
property System.int Extraction {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

Type of extraction as defined by [swiCharacteristicInfoExtraction_e](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.swiCharacteristicInfoExtraction_e.html)

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
