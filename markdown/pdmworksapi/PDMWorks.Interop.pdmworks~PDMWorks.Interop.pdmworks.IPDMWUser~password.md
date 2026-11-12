---
title: "password Property (IPDMWUser)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWUser"
member: "password"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~password.html"
---

# password Property (IPDMWUser)

Gets or sets the password for this user.

## Syntax

### Visual Basic (Declaration)

```vb
Property password As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWUser
Dim value As System.String

instance.password = value

value = instance.password
```

### C#

```csharp
System.string password {get; set;}
```

### C++/CLI

```cpp
property System.String^ password {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Password

## VBA Syntax

See [PDMWUser::password](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWUser~password.html).

## See Also

[IPDMWUser Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser.html)
[IPDMWUser Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
