---
title: "ColorData Property (IDropData)"
project: ""
interface: "IDropData"
member: "ColorData"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDropData~ColorData.html"
---

# ColorData Property (IDropData)

Gets or sets the Color stored in this drop's MIME data.

## Syntax

### Visual Basic

```vb
Property ColorData As Color
```

### C#

```csharp
Color ColorData {get; set;}
```

### JScript

```
function get,set ColorData : Color
```

### Managed Extensions for C++

```
__property Color* get_ColorData();
__property void set_ColorData(
   Color* value
);
```

### C++/CLI

```cpp
property Color^ ColorData {
   Color^ get();
   void set (    Color^ value);
}
```

### Property Value

[IColor](Interop.dsAutomation~Interop.dsAutomation.IColor.html)

## Remarks

The setter of this property is valid only if [IDropData::HasColorData](Interop.dsAutomation~Interop.dsAutomation.IDropData~HasColorData.html) is true.

## See Also

[IDropData Interface](Interop.dsAutomation~Interop.dsAutomation.IDropData.html)
[IDropData Members](Interop.dsAutomation~Interop.dsAutomation.IDropData_members.html)

## Availability

DraftSight 2020 SP3
