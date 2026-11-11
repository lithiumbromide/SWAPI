---
title: "GetRawData Method (IHyperLink)"
project: ""
interface: "IHyperLink"
member: "GetRawData"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetRawData.html"
---

# GetRawData Method (IHyperLink)

Gets the raw data of the hyperlink.

## Syntax

### Visual Basic

```vb
Sub GetRawData( _
   ByRef Address As System.String, _
   ByRef Sublocation As System.String, _
   ByRef Description As System.String _
)
```

### C#

```csharp
void GetRawData(
   out System.string Address,
   out System.string Sublocation,
   out System.string Description
)
```

### JScript

```
function GetRawData(
   Address : System.String,
   Sublocation : System.String,
   Description : System.String
);
```

### Managed Extensions for C++

```
void GetRawData(
   [PARAMFLAG::Out] System.string* Address,
   [PARAMFLAG::Out] System.string* Sublocation,
   [PARAMFLAG::Out] System.string* Description
)
```

### C++/CLI

```cpp
void GetRawData(
   [Out] System.String^ Address,
   [Out] System.String^ Sublocation,
   [Out] System.String^ Description
)
```

### Parameters

- `Address`: URL of the web page, path and file name of the file, or an email address
- `Sublocation`: URL of the web page or the path and file name of the file, if the web page or file exists
- `Description`: ToolTip of the hyperlink

## See Also

[IHyperLink Interface](Interop.dsAutomation~Interop.dsAutomation.IHyperLink.html)
[IHyperLink Members](Interop.dsAutomation~Interop.dsAutomation.IHyperLink_members.html)

## Availability

DraftSight V1R1.3
