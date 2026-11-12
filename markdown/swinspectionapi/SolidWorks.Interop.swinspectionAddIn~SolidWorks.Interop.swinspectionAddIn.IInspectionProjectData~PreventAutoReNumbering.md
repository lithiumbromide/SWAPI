---
title: "PreventAutoReNumbering Property (IInspectionProjectData)"
project: "SOLIDWORKS Inspection API Help"
interface: "IInspectionProjectData"
member: "PreventAutoReNumbering"
kind: "property"
source: "swinspectionapi/SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData~PreventAutoReNumbering.html"
---

# PreventAutoReNumbering Property (IInspectionProjectData)

Gets and sets whether to re-order balloons when one is removed.

## Syntax

### Visual Basic (Declaration)

```vb
Property PreventAutoReNumbering As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IInspectionProjectData
Dim value As System.Boolean

instance.PreventAutoReNumbering = value

value = instance.PreventAutoReNumbering
```

### C#

```csharp
System.bool PreventAutoReNumbering {get; set;}
```

### C++/CLI

```cpp
property System.bool PreventAutoReNumbering {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to prevent re-ordering of balloons, false to re-order when balloons are added or removed

## VBA Syntax

See [InspectionProjectData](ms-its:swinspectionapivb6.chm::/SWInspectionAddin~InspectionProjectData_members.html) properties.

## See Also

[IInspectionProjectData Interface](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData.html)
[IInspectionProjectData Members](SolidWorks.Interop.swinspectionAddIn~SolidWorks.Interop.swinspectionAddIn.IInspectionProjectData_members.html)

## Availability

SOLIDWORKS Inspection API 2022 FCS
