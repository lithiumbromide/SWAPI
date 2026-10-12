---
title: "Email Property (IPDMWUser)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWUser"
member: "Email"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~Email.html"
---

# Email Property (IPDMWUser)

Gets or sets the email address for this user.

## Syntax

### Visual Basic (Declaration)

```vb
Property Email As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWUser
Dim value As System.String

instance.Email = value

value = instance.Email
```

### C#

```csharp
System.string Email {get; set;}
```

### C++/CLI

```cpp
property System.String^ Email {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Email address

## VBA Syntax

See [PDMWUser::Email](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWUser~Email.html).

## See Also

[IPDMWUser Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser.html)
[IPDMWUser Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser_members.html)

## Availability

DPMWorks Workgroup 2004 FCS
