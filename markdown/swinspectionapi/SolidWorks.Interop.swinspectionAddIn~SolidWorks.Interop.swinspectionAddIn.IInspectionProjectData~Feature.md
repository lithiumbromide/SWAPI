---
title: "Feature Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "Feature"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~Feature.html"
---

# Feature Property (IInspectionProjectData)

Gets and sets whether to extract feature dimensions from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Feature As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Boolean

instance.Feature = value

value = instance.Feature
```

### C#

```csharp
System.bool Feature {get; set;}
```

### C++/CLI

```cpp
property System.bool Feature {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract feature dimensions, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## Remarks

This property is valid only if [IInspectionProjectData::InspectionOnly](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~InspectionOnly.html) is false.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
