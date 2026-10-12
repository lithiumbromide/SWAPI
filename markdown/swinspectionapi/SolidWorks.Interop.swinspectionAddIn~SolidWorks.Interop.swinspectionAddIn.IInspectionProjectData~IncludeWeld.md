---
title: "IncludeWeld Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "IncludeWeld"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~IncludeWeld.html"
---

# IncludeWeld Property (IInspectionProjectData)

Gets and sets whether to extract welds from the drawing for this inspection project.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeWeld As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Boolean

instance.IncludeWeld = value

value = instance.IncludeWeld
```

### C#

```csharp
System.bool IncludeWeld {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeWeld {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to extract welds, false to not

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
