---
title: "InspectionOnly Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "InspectionOnly"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~InspectionOnly.html"
---

# InspectionOnly Property (IInspectionProjectData)

Gets and sets whether to extract inspection-only dimensions from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property InspectionOnly As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
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

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
