---
title: "IncludeNotes Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "IncludeNotes"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~IncludeNotes.html"
---

# IncludeNotes Property (InspectionProjectData)

Gets and sets whether to extract all notes from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeNotes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.IncludeNotes = value

value = instance.IncludeNotes
```

### C#

```csharp
System.bool IncludeNotes {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeNotes {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract all notes, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## Remarks

When set to true, this property extracts all notes including sheet format notes.

Set IInspectionProjectData::SheetFormat to false to not include sheet format notes.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
