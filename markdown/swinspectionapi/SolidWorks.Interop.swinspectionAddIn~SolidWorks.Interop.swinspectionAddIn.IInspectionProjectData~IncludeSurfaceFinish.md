---
title: "IncludeSurfaceFinish Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "IncludeSurfaceFinish"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~IncludeSurfaceFinish.html"
---

# IncludeSurfaceFinish Property (IInspectionProjectData)

Gets and sets whether to extract surface finishes from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeSurfaceFinish As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
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

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
