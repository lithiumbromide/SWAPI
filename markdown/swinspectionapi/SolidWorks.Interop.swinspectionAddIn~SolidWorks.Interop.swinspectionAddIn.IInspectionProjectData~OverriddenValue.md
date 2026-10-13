---
title: "OverriddenValue Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "OverriddenValue"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~OverriddenValue.html"
---

# OverriddenValue Property (IInspectionProjectData)

Gets and sets whether to extract overridden dimension values from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property OverriddenValue As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Boolean

instance.OverriddenValue = value

value = instance.OverriddenValue
```

### C#

```csharp
System.bool OverriddenValue {get; set;}
```

### C++/CLI

```cpp
property System.bool OverriddenValue {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to always use overridden dimension values when they are defined, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
