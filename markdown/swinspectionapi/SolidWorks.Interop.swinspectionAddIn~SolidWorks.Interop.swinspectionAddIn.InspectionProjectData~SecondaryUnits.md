---
title: "SecondaryUnits Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "SecondaryUnits"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~SecondaryUnits.html"
---

# SecondaryUnits Property (InspectionProjectData)

Gets and sets whether to extract dual dimensions from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property SecondaryUnits As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.SecondaryUnits = value

value = instance.SecondaryUnits
```

### C#

```csharp
System.bool SecondaryUnits {get; set;}
```

### C++/CLI

```cpp
property System.bool SecondaryUnits {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract dual dimensions, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
