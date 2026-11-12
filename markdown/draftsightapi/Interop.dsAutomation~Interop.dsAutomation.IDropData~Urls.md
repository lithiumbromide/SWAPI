---
title: "Urls Property (IDropData)"
project: ""
interface: "IDropData"
member: "Urls"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IDropData~Urls.html"
---

# Urls Property (IDropData)

Gets or sets the URLs stored in this drop's MIME data.

## Syntax

### Visual Basic

```vb
Property Urls As System.Object
```

### C#

```csharp
System.object Urls {get; set;}
```

### JScript

```
function get,set Urls : System.Object
```

### Managed Extensions for C++

```
__property System.Object* get_Urls();
__property void set_Urls(
   System.Object* value
);
```

### C++/CLI

```cpp
property System.Object^ Urls {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

String array of URLs

## Remarks

The setter of this property is valid only if [IDropData::HasUrls](Interop.dsAutomation~Interop.dsAutomation.IDropData~HasUrls.html) is true.

## See Also

[IDropData Interface](Interop.dsAutomation~Interop.dsAutomation.IDropData.html)
[IDropData Members](Interop.dsAutomation~Interop.dsAutomation.IDropData_members.html)

## Availability

DraftSight 2020 SP3
