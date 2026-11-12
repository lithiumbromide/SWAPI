---
title: "Basic Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "Basic"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~Basic.html"
---

# Basic Property (IInspectionProjectData)

Gets and sets whether to extract basic dimensions from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Basic As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Boolean

instance.Basic = value

value = instance.Basic
```

### C#

```csharp
System.bool Basic {get; set;}
```

### C++/CLI

```cpp
property System.bool Basic {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract basic dimensions, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## Remarks

This property is valid only if [IInspectionProjectData::InspectionOnly](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~InspectionOnly.html) is false.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
