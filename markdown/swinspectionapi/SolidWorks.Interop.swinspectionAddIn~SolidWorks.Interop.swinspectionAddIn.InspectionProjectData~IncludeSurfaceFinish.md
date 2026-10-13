---
title: "IncludeSurfaceFinish Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "IncludeSurfaceFinish"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~IncludeSurfaceFinish.html"
---

# IncludeSurfaceFinish Property (InspectionProjectData)

Gets and sets whether to extract surface finishes from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeSurfaceFinish As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.IncludeSurfaceFinish = value

value = instance.IncludeSurfaceFinish
```

### C#

```csharp
System.bool IncludeSurfaceFinish {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeSurfaceFinish {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract surface finishes, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
