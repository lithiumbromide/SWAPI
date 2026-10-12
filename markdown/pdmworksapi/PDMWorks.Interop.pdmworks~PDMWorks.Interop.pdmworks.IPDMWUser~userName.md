---
title: "userName Property (IPDMWUser)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWUser"
member: "userName"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~userName.html"
---

# userName Property (IPDMWUser)

Gets the username for this user.

## Syntax

### Visual Basic (Declaration)

```vb
Property userName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWUser
Dim value As System.String

instance.userName = value

value = instance.userName
```

### C#

```csharp
System.string userName {get; set;}
```

### C++/CLI

```cpp
property System.String^ userName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Username

## VBA Syntax

See [PDMWUser::userName](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWUser~userName.html).

## See Also

[IPDMWUser Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser.html)
[IPDMWUser Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
