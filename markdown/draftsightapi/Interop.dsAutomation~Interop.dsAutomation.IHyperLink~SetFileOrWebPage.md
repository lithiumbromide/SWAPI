---
title: "SetFileOrWebPage Method (IHyperLink)"
project: ""
interface: "IHyperLink"
member: "SetFileOrWebPage"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHyperLink~SetFileOrWebPage.html"
---

# SetFileOrWebPage Method (IHyperLink)

Sets the hyperlink to be a URL of a web page or the path and file name of a file.

## Syntax

### Visual Basic

```vb
Sub SetFileOrWebPage( _
   ByVal Destination As System.String, _
   ByVal Sublocation As System.String _
)
```

### C#

```csharp
void SetFileOrWebPage(
   System.string Destination,
   System.string Sublocation
)
```

### JScript

```
function SetFileOrWebPage(
   Destination : System.String,
   Sublocation : System.String
);
```

### Managed Extensions for C++

```
void SetFileOrWebPage(
   System.string* Destination,
   System.string* Sublocation
)
```

### C++/CLI

```cpp
void SetFileOrWebPage(
   System.String^ Destination,
   System.String^ Sublocation
)
```

### Parameters

- `Destination`: URL of a web page or the path and file name of a file
- `Sublocation`: Valid URL of a web page or the path and file name of a file

## Remarks

This method is valid only if [IHyperLink::GetType](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetType.html) is dsHyperLinkType_e.dsHyperLinkType_FileOrWebPage.

## See Also

[IHyperLink Interface](Interop.dsAutomation~Interop.dsAutomation.IHyperLink.html)
[IHyperLink Members](Interop.dsAutomation~Interop.dsAutomation.IHyperLink_members.html)
[IHyperLink::GetAsFileOrWebPage Method](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetAsFileOrWebPage.html)

## Availability

DraftSight V1R1.3
