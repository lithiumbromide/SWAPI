---
title: "OpenWebHelp Method (IApplication)"
project: ""
interface: "IApplication"
member: "OpenWebHelp"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenWebHelp.html"
---

# OpenWebHelp Method (IApplication)

Opens the specified web help URL.

## Syntax

### Visual Basic

```vb
Function OpenWebHelp( _
   ByVal WebUrl As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool OpenWebHelp(
   System.string WebUrl
)
```

### JScript

```
function OpenWebHelp(
   WebUrl : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool OpenWebHelp(
   System.string* WebUrl
)
```

### C++/CLI

```cpp
System.bool OpenWebHelp(
   System.String^ WebUrl
)
```

### Parameters

- `WebUrl`: URL of the landing page of an online HTML help system

### Return Value

True if web help successfully opened, false if not

## Remarks

Use [IApplication::GetWebLink](Interop.dsAutomation~Interop.dsAutomation.IApplication~GetWebLink.html) to populate WebUrl.

WebUrl may contain an additional parameter, as in:

http://www.mysite.com/myhelp.html?id=1

## See Also

[IApplication Interface](Interop.dsAutomation~Interop.dsAutomation.IApplication.html)
[IApplication Members](Interop.dsAutomation~Interop.dsAutomation.IApplication_members.html)
[IApplication::IsWebHelpEnabled Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~IsWebHelpEnabled.html)
[IApplication::OpenChmHelp Method ()](Interop.dsAutomation~Interop.dsAutomation.IApplication~OpenChmHelp.html)

## Availability

DraftSight 2019 SP0
