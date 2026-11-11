---
title: "DocumentKeywords Property (IExportSettings)"
project: ""
interface: "IExportSettings"
member: "DocumentKeywords"
kind: "property"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IExportSettings~DocumentKeywords.html"
---

# DocumentKeywords Property (IExportSettings)

Gets or sets the keywords for the document.

## Syntax

### Visual Basic

```vb
Property DocumentKeywords As System.String
```

### C#

```csharp
System.string DocumentKeywords {get; set;}
```

### JScript

```
function get,set DocumentKeywords : System.String
```

### Managed Extensions for C++

```
__property System.string* get_DocumentKeywords();
__property void set_DocumentKeywords(
   System.string* value
);
```

### C++/CLI

```cpp
property System.String^ DocumentKeywords {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Document keywords; default is an empty string

## Remarks

Search engines use keywords to narrow searches.

## See Also

[IExportSettings Interface](Interop.dsAutomation~Interop.dsAutomation.IExportSettings.html)
[IExportSettings Members](Interop.dsAutomation~Interop.dsAutomation.IExportSettings_members.html)

## Availability

DraftSight 2018 SP2
