---
title: "DisplayName Property (IPDMWUser)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWUser"
member: "DisplayName"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~DisplayName.html"
---

# DisplayName Property (IPDMWUser)

Gets or sets the name of the user record to display.

## Syntax

### Visual Basic (Declaration)

```vb
Property DisplayName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWUser
Dim value As System.String

instance.DisplayName = value

value = instance.DisplayName
```

### C#

```csharp
System.string DisplayName {get; set;}
```

### C++/CLI

```cpp
property System.String^ DisplayName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of the user record to display

## VBA Syntax

See [PDMWUser::DisplayName](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWUser~DisplayName.html).

## See Also

[IPDMWUser Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser.html)
[IPDMWUser Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2004 FCS
