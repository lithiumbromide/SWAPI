---
title: "PrintSheetLast Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "PrintSheetLast"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~PrintSheetLast.html"
---

# PrintSheetLast Property (IPrintManager)

Gets or sets whether to print first the geometry of the model in Viewports or the geometry of the Sheet in the graphics area.

## Syntax

### Visual Basic

```vb
Property PrintSheetLast As System.Boolean
```

### C#

```csharp
System.bool PrintSheetLast {get; set;}
```

### JScript

```
function get,set PrintSheetLast : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_PrintSheetLast();
__property void set_PrintSheetLast(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool PrintSheetLast {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to print first the geometry of the model in Viewports, false to print first the geometry of the Sheet in the graphics area

## Remarks

This property is only available when the working space is a [Sheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html).

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1.1
