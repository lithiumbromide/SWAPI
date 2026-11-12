---
title: "SheetFormat Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "SheetFormat"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~SheetFormat.html"
---

# SheetFormat Property (IInspectionProjectData)

Gets and sets whether to extract sheet format notes from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property SheetFormat As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
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

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
