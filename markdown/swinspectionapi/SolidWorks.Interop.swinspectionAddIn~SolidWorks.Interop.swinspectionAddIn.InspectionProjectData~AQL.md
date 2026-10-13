---
title: "AQL Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "AQL"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~AQL.html"
---

# AQL Property (InspectionProjectData)

Gets and sets the sampling acceptable quality level (AQL) for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property AQL As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.String

instance.AQL = value

value = instance.AQL
```

### C#

```csharp
System.string AQL {get; set;}
```

### C++/CLI

```cpp
property System.String^ AQL {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Acceptable quality level (see **Remarks**)

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## Remarks

Acceptable Quality Levels:

- 0.010
- 0.015
- 0.025
- 0.040
- 0.065
- 0.10
- 0.15
- 0.25
- 0.40
- 0.65
- 1.0
- 1.5
- 2.5
- 4.0
- 6.5
- 10
- 15
- 25
- 40
- 65
- 100
- 150
- 250
- 400
- 650
- 1000

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
