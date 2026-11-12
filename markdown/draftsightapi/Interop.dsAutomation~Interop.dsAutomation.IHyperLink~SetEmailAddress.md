---
title: "SetEmailAddress Method (IHyperLink)"
project: ""
interface: "IHyperLink"
member: "SetEmailAddress"
kind: "method"
source: "draftsightapi/Interop.dsAutomation~Interop.dsAutomation.IHyperLink~SetEmailAddress.html"
---

# SetEmailAddress Method (IHyperLink)

Sets the hyperlink to be an email address.

## Syntax

### Visual Basic

```vb
Sub SetEmailAddress( _
   ByVal EmailAddress As System.String, _
   ByVal Subject As System.String _
)
```

### C#

```csharp
void SetEmailAddress(
   System.string EmailAddress,
   System.string Subject
)
```

### JScript

```
function SetEmailAddress(
   EmailAddress : System.String,
   Subject : System.String
);
```

### Managed Extensions for C++

```
void SetEmailAddress(
   System.string* EmailAddress,
   System.string* Subject
)
```

### C++/CLI

```cpp
void SetEmailAddress(
   System.String^ EmailAddress,
   System.String^ Subject
)
```

### Parameters

- `EmailAddress`: Email address
- `Subject`: Subject line of the email

## Remarks

This method is valid only if [IHyperLink::GetType](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetType.html) is dsHyperLinkType_e.dsHyperLinkType_EmailAddress.

## See Also

[IHyperLink Interface](Interop.dsAutomation~Interop.dsAutomation.IHyperLink.html)
[IHyperLink Members](Interop.dsAutomation~Interop.dsAutomation.IHyperLink_members.html)
[IHyperLink::GetAsEmailAddress Method](Interop.dsAutomation~Interop.dsAutomation.IHyperLink~GetAsEmailAddress.html)

## Availability

DraftSight V1R1.3
