---
title: "GetAsFileOrWebPage Method (IHyperLink)"
project: ""
interface: "IHyperLink"
member: "GetAsFileOrWebPage"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetAsFileOrWebPage.html"
---

# GetAsFileOrWebPage Method (IHyperLink)

Gets the URL of the web page or the path and file name of the file for the hyperlink.

## Syntax

### Visual Basic

```vb
Function GetAsFileOrWebPage( _
   ByRef Destination As System.String, _
   ByRef Sublocation As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool GetAsFileOrWebPage(
   out System.string Destination,
   out System.string Sublocation
)
```

### JScript

```
function GetAsFileOrWebPage(
   Destination : System.String,
   Sublocation : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetAsFileOrWebPage(
   [PARAMFLAG::Out] System.string* Destination,
   [PARAMFLAG::Out] System.string* Sublocation
)
```

### C++/CLI

```cpp
System.bool GetAsFileOrWebPage(
   [Out] System.String^ Destination,
   [Out] System.String^ Sublocation
)
```

### Parameters

- `Destination`: URL of the web page or the path and file name of a file
- `Sublocation`: URL of the web page or the path and file name of the file, if the web page or file exists

### Return Value

True if successful, false if not

## Remarks

This method is valid only if [IHyperLink::GetType](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetType.html) is dsHyperLinkType_e.dsHyperLinkType_FileOrWebPage.

## See Also

[IHyperLink Interface](Interop.dsAutomation~Interop.dsAutomation.IHyperLink.html)
[IHyperLink Members](Interop.dsAutomation~Interop.dsAutomation.IHyperLink_members.html)
[IHyperLink::SetFileOrWebPage Method](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~SetFileOrWebPage.html)

## Availability

DraftSight V1R1.3
