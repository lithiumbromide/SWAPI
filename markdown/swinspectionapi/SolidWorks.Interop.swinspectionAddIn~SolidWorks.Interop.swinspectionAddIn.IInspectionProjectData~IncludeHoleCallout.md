---
title: "IncludeHoleCallout Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "IncludeHoleCallout"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~IncludeHoleCallout.html"
---

# IncludeHoleCallout Property (IInspectionProjectData)

Gets and sets whether to extract hole callouts from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeHoleCallout As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Boolean

instance.IncludeHoleCallout = value

value = instance.IncludeHoleCallout
```

### C#

```csharp
System.bool IncludeHoleCallout {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeHoleCallout {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract hole callouts, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
