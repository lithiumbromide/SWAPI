---
title: "Comment Property (IPDMWUser)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWUser"
member: "Comment"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~Comment.html"
---

# Comment Property (IPDMWUser)

Gets or sets the comments for this user record.

## Syntax

### Visual Basic (Declaration)

```vb
Property Comment As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWUser
Dim value As System.String

instance.Comment = value

value = instance.Comment
```

### C#

```csharp
System.string Comment {get; set;}
```

### C++/CLI

```cpp
property System.String^ Comment {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Comments

## VBA Syntax

See [PDMWUser::Comment](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWUser~Comment.html).

## See Also

[IPDMWUser Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser.html)
[IPDMWUser Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
