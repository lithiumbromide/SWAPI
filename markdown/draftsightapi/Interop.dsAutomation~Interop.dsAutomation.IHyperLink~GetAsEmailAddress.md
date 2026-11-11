---
title: "GetAsEmailAddress Method (IHyperLink)"
project: ""
interface: "IHyperLink"
member: "GetAsEmailAddress"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetAsEmailAddress.html"
---

# GetAsEmailAddress Method (IHyperLink)

Gets the the email address and subject line of the hyperlink.

## Syntax

### Visual Basic

```vb
Function GetAsEmailAddress( _
   ByRef EmailAddress As System.String, _
   ByRef Subject As System.String _
) As System.Boolean
```

### C#

```csharp
System.bool GetAsEmailAddress(
   out System.string EmailAddress,
   out System.string Subject
)
```

### JScript

```
function GetAsEmailAddress(
   EmailAddress : System.String,
   Subject : System.String
) : System.boolean;
```

### Managed Extensions for C++

```
System.bool GetAsEmailAddress(
   [PARAMFLAG::Out] System.string* EmailAddress,
   [PARAMFLAG::Out] System.string* Subject
)
```

### C++/CLI

```cpp
System.bool GetAsEmailAddress(
   [Out] System.String^ EmailAddress,
   [Out] System.String^ Subject
)
```

### Parameters

- `EmailAddress`: Email address
- `Subject`: Subject line of the email

### Return Value

True if successful, false if not

## Remarks

This method is valid only if [IHyperLink::GetType](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetType.html) is dsHyperLinkType_e.dsHyperLinkType_EmailAddress.

## See Also

[IHyperLink Interface](Interop.dsAutomation~Interop.dsAutomation.IHyperLink.html)
[IHyperLink Members](Interop.dsAutomation~Interop.dsAutomation.IHyperLink_members.html)
[IHyperLink::SetEmailAddress Method](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~SetEmailAddress.html)

## Availability

DraftSight V1R1.3
