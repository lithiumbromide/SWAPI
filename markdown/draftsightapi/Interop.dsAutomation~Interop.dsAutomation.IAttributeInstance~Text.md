---
title: "Text Property (IAttributeInstance)"
project: ""
interface: "IAttributeInstance"
member: "Text"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Text.html"
---

# Text Property (IAttributeInstance)

Gets or sets the Note associated with this multiline BlockAttribute instance.

## Syntax

### Visual Basic

```vb
Property Text As Note
```

### C#

```csharp
Note Text {get; set;}
```

### JScript

```
function get,set Text : Note
```

### Managed Extensions for C++

```
__property Note* get_Text();
__property void set_Text(
   Note* value
);
```

### C++/CLI

```cpp
property Note^ Text {
   Note^ get();
   void set (    Note^ value);
}
```

### Property Value

[INote](Interop.dsAutomation~Interop.dsAutomation.INote.html) (see **Remarks**)

## Remarks

This property returns an INote only if [IAttributeInstance::Multilines](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance~Multilines.html) is set to true. Otherwise it returns null or Nothing.

Use the returned Note to set the background color of this multiline text.

## See Also

[IAttributeInstance Interface](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance.html)
[IAttributeInstance Members](Interop.dsAutomation~Interop.dsAutomation.IAttributeInstance_members.html)

## Availability

DraftSight 2018 SP0
