---
title: "GetWebLink Method (IApplication)"
project: ""
interface: "IApplication"
member: "GetWebLink"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~GetWebLink.html"
---

# GetWebLink Method (IApplication)

Gets the web URL of the landing page of an online HTML help system.

## Syntax

### Visual Basic

```vb
Function GetWebLink() As System.String
```

### C#

```csharp
System.string GetWebLink()
```

### JScript

```
function GetWebLink() : System.String;
```

### Managed Extensions for C++

```
System.string* GetWebLink();
```

### C++/CLI

```cpp
System.String^ GetWebLink();
```

### Return Value

Web help URL

## Remarks

Call this method before calling [IApplication::OpenWebHelp](Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenWebHelp.html).

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)

## Availability

DraftSight 2019 SP0
