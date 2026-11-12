---
title: "HideGeometryOnSheet Property (IPrintManager)"
project: ""
interface: "IPrintManager"
member: "HideGeometryOnSheet"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IPrintManager~HideGeometryOnSheet.html"
---

# HideGeometryOnSheet Property (IPrintManager)

Gets or sets whether the geometry of the model shown in Viewports is printed with hidden lines removed.

## Syntax

### Visual Basic

```vb
Property HideGeometryOnSheet As System.Boolean
```

### C#

```csharp
System.bool HideGeometryOnSheet {get; set;}
```

### JScript

```
function get,set HideGeometryOnSheet : System.boolean
```

### Managed Extensions for C++

```
__property System.bool get_HideGeometryOnSheet();
__property void set_HideGeometryOnSheet(
   System.bool value
);
```

### C++/CLI

```cpp
property System.bool HideGeometryOnSheet {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True to hide the geometry of the model shown in Viewports with hidden lines removed, false to show the geometry of the model shown in Viewports with hidden lines removed

## Remarks

This property is only available when the working space is a [Sheet](Interop.dsAutomation~Interop.dsAutomation.ISheet.html).

## See Also

[IPrintManager Interface](Interop.dsAutomation~Interop.dsAutomation.IPrintManager.html)
[IPrintManager Members](Interop.dsAutomation~Interop.dsAutomation.IPrintManager_members.html)

## Availability

DraftSight V1R1.1
