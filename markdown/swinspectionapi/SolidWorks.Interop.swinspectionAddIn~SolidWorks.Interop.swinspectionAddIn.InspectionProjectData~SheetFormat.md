---
title: "SheetFormat Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "SheetFormat"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~SheetFormat.html"
---

# SheetFormat Property (InspectionProjectData)

Gets and sets whether to extract sheet format notes from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property SheetFormat As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.SheetFormat = value

value = instance.SheetFormat
```

### C#

```csharp
System.bool SheetFormat {get; set;}
```

### C++/CLI

```cpp
property System.bool SheetFormat {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract sheet format notes, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## Remarks

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
