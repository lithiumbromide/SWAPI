---
title: "DocumentTitle Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "DocumentTitle"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~DocumentTitle.html"
---

# DocumentTitle Property (IExportSettings)

Gets or sets the title of the document.

## Syntax

### Visual Basic

```vb
Property DocumentTitle As System.String
```

### C#

```csharp
System.string DocumentTitle {get; set;}
```

### JScript

```
function get,set DocumentTitle : System.String
```

### Managed Extensions for C++

```
__property System.string* get_DocumentTitle();
__property void set_DocumentTitle(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ DocumentTitle {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Document title; default is an empty string

## Remarks

Search engines may use the title in search results lists.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)

## Availability

DraftSight 2018 SP2
