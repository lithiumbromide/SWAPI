---
title: "AutoBalloon Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "AutoBalloon"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~AutoBalloon.html"
---

# AutoBalloon Property (IInspectionProjectData)

Gets and sets whether to autoballoon drawings in this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoBalloon As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
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

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
