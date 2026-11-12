---
title: "Text Property (IDropData)"
project: ""
interface: "IDropData"
member: "Text"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDropData~Text.html"
---

# Text Property (IDropData)

Gets or sets the text stored in this drop's MIME data.

## Syntax

### Visual Basic

```vb
Property Text As System.String
```

### C#

```csharp
System.string Text {get; set;}
```

### JScript

```
function get,set Text : System.String
```

### Managed Extensions for C++

```
__property System.string* get_Text();
__property void set_Text(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ Text {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Text string

## Remarks

The setter of this property is valid only if [IDropData::HasText](Interop.dsAutomation~Interop.dsAutomation.IDropData~HasText.html) is true.

## See Also

[IDropData Interface](Interop.dsAutomation~Interop.dsAutomation.IDropData.html)
[IDropData Members](Interop.dsAutomation~Interop.dsAutomation.IDropData_members.html)

## Availability

DraftSight 2020 SP3
