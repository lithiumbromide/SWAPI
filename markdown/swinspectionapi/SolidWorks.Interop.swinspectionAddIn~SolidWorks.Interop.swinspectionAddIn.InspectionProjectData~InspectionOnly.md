---
title: "InspectionOnly Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "InspectionOnly"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~InspectionOnly.html"
---

# InspectionOnly Property (InspectionProjectData)

Gets and sets whether to extract inspection-only dimensions from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property InspectionOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.InspectionOnly = value

value = instance.InspectionOnly
```

### C#

```csharp
System.bool InspectionOnly {get; set;}
```

### C++/CLI

```cpp
property System.bool InspectionOnly {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract inspection-only dimensions, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
