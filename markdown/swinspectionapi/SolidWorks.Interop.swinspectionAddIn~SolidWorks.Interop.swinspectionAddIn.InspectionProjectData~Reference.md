---
title: "Reference Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "Reference"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~Reference.html"
---

# Reference Property (InspectionProjectData)

Gets and sets whether to extract driven (e.g., read-only) dimensions from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Reference As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.Reference = value

value = instance.Reference
```

### C#

```csharp
System.bool Reference {get; set;}
```

### C++/CLI

```cpp
property System.bool Reference {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract driven dimensions, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## Remarks

This property is valid only if [IInspectionProjectData::InspectionOnly](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~InspectionOnly.html) is false.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
