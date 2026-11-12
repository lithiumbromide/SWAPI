---
title: "AutoExplodeHoleCallout Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "AutoExplodeHoleCallout"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~AutoExplodeHoleCallout.html"
---

# AutoExplodeHoleCallout Property (InspectionProjectData)

Gets and sets whether to auto-explode hole callouts.

## Syntax

### Visual Basic (Declaration)

```vb
Property AutoExplodeHoleCallout As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.AutoExplodeHoleCallout = value

value = instance.AutoExplodeHoleCallout
```

### C#

```csharp
System.bool AutoExplodeHoleCallout {get; set;}
```

### C++/CLI

```cpp
property System.bool AutoExplodeHoleCallout {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to create a separate instance for each section of the hole callout, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
