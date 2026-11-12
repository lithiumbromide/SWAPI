---
title: "IncludeDimensions Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "IncludeDimensions"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~IncludeDimensions.html"
---

# IncludeDimensions Property (IInspectionProjectData)

Gets and sets whether to extract all dimension types from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeDimensions As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Boolean

instance.IncludeDimensions = value

value = instance.IncludeDimensions
```

### C#

```csharp
System.bool IncludeDimensions {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeDimensions {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract all dimension types, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## Remarks

When set to true, this property extracts all of these dimension types:

- Reference
- Basic
- Feature
- Dual (secondary units)
- Overridden
- Split chamfer

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
