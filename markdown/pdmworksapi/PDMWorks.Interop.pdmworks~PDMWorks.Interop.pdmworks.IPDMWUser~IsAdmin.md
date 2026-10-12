---
title: "IsAdmin Property (IPDMWUser)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWUser"
member: "IsAdmin"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~IsAdmin.html"
---

# IsAdmin Property (IPDMWUser)

Gets or sets whether this user is a vault administrator.

## Syntax

### Visual Basic (Declaration)

```vb
Property IsAdmin As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWUser
Dim value As System.Boolean

instance.IsAdmin = value

value = instance.IsAdmin
```

### C#

```csharp
System.bool IsAdmin {get; set;}
```

### C++/CLI

```cpp
property System.bool IsAdmin {
   System.bool get();
   void set (    System.bool value);
}
```

### Property Value

True if user is a vault administrator, false if not

## VBA Syntax

See [PDMWUser::IsAdmin](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWUser~IsAdmin.html).

## Remarks

Only a vault administrator can set this user is a vault administration.

A vault administrator cannot remove himself or herself from the list of vault administrators.

## See Also

[IPDMWUser Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser.html)
[IPDMWUser Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
