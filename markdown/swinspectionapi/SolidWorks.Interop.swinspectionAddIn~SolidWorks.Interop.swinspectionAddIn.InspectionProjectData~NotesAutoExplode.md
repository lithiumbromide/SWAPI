---
title: "NotesAutoExplode Property (InspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "InspectionProjectData"
member: "NotesAutoExplode"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData~NotesAutoExplode.html"
---

# NotesAutoExplode Property (InspectionProjectData)

Gets and sets whether to create a separate instance for each section of the note.

## Syntax

### Visual Basic (Declaration)

```vb
Property NotesAutoExplode As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As InspectionProjectData
Dim value As System.Boolean

instance.NotesAutoExplode = value

value = instance.NotesAutoExplode
```

### C#

```csharp
System.bool NotesAutoExplode {get; set;}
```

### C++/CLI

```cpp
property System.bool NotesAutoExplode {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to create sub-notes from a large, multi-item note, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## Remarks

This property is valid only if [IInspectionProjectData::IncludeNotes](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~IncludeNotes.html) is set to true.

## See Also

[InspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData.html)
[InspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.InspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
