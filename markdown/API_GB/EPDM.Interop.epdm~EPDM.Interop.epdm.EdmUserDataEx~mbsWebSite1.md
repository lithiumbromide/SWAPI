---
title: "mbsWebSite1 Field"
project: "SOLIDWORKS PDM Professional API Help"
interface: "EdmUserDataEx"
member: "mbsWebSite1"
kind: "topic"
source: "API_GB/EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx~mbsWebSite1.html"
---

# mbsWebSite1 Field

First website address.

## Syntax

### Visual Basic

```vb
Public mbsWebSite1 As System.String
```

### C#

```csharp
public System.string mbsWebSite1
```

### C++/CLI

```cpp
public:
System.String^ mbsWebSite1
```

## Remarks

The websites appear as buttons in the user popup windows. You can provide a custom ToolTip for web addresses by appending a new line and the Tooltip to the address like this: **www.solidworks.com\nSOLIDWORKS!**. The button is retrieved from the website's **favicon.ico** file.

## See Also

[EdmUserDataEx Structure](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx.html)
[EdmUserDataEx Members](EPDM.Interop.epdm~EPDM.Interop.epdm.EdmUserDataEx_members.html)
