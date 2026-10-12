---
title: "AutoBalloon Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "AutoBalloon"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~AutoBalloon.html"
---

# AutoBalloon Property (InspectionProjectData)

Gets and sets whether to autoballoon drawings in this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoBalloon As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.AutoBalloon = value

value = instance.AutoBalloon
```

### C#

```csharp
System.bool AutoBalloon {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoBalloon {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to autoballoon the drawing, false to manually add balloons to the drawing

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
