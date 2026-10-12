---
title: "ExtractionCriteria Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "ExtractionCriteria"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~ExtractionCriteria.html"
---

# ExtractionCriteria Property (IInspectionProjectData)

Gets and sets the regular expression to filter notes for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property ExtractionCriteria As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.String

instance.ExtractionCriteria = value

value = instance.ExtractionCriteria
```

### C#

```csharp
System.string ExtractionCriteria {get; set;}
```

### C++/CLI

```cpp
property System.String^ ExtractionCriteria {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Regular expression

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## Remarks

This property is valid only if [IInspectionProjectData::IncludeNotes](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~IncludeNotes.html) is set to true.

For definitions, constructs and examples, see the Note Extraction Criteria topic in **SOLIDWORKS Inspection Add-in user-interface help > SOLIDWORKS Inspection > SOLIDWORKS Inspection Add-in > Getting Started > Creating an Inspection Project > Create Inspection Project PropertyManager > Extraction Settings**.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
