---
title: "SupportPaths Property (ISystemFiles)"
project: ""
interface: "ISystemFiles"
member: "SupportPaths"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.ISystemFiles~SupportPaths.html"
---

# SupportPaths Property (ISystemFiles)

Gets or sets the where to search for add-in applications, area Hatch patterns, customization files, drawing files, fonts, and LineStyle files.

## Syntax

### Visual Basic

```vb
Property SupportPaths As System.Object
```

### C#

```csharp
System.object SupportPaths {get; set;}
```

### JScript

```
function get,set SupportPaths : System.Object
```

### Managed Extensions for C++

```
__property System.Object* get_SupportPaths();
__property void set_SupportPaths(
   System.Object* value
);
```

### C++/CLI

```cpp
property System.Object^ SupportPaths {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

### Property Value

Array of strings of the paths indicating where to search for add-in applications, area Hatch patterns, customization files, drawing files, fonts, and LineStyle files

## Examples

See the [ISystemFiles](Interop.dsAutomation~Interop.dsAutomation.ISystemFiles.html) examples.

## See Also

[ISystemFiles Interface](Interop.dsAutomation~Interop.dsAutomation.ISystemFiles.html)
[ISystemFiles Members](Interop.dsAutomation~Interop.dsAutomation.ISystemFiles_members.html)

## Availability

DraftSight V1R3.0
