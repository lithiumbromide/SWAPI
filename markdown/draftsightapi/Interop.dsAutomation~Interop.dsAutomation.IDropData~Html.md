---
title: "Html Property (IDropData)"
project: ""
interface: "IDropData"
member: "Html"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDropData~Html.html"
---

# Html Property (IDropData)

Gets or sets the HTML for this drop's MIME data.

## Syntax

### Visual Basic

```vb
Property Html As System.String
```

### C#

```csharp
System.string Html {get; set;}
```

### JScript

```
function get,set Html : System.String
```

### Managed Extensions for C++

```
__property System.string* get_Html();
__property void set_Html(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ Html {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

HTML string

## Remarks

The setter of this property is valid only if [IDropData::HasHtml](Interop.dsAutomation~Interop.dsAutomation.IDropData~HasHtml.html) is true.

## See Also

[IDropData Interface](Interop.dsAutomation~Interop.dsAutomation.IDropData.html)
[IDropData Members](Interop.dsAutomation~Interop.dsAutomation.IDropData_members.html)

## Availability

DraftSight 2020 SP3
