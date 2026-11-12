---
title: "PropertyFilterName Property (IPDMWUser)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWUser"
member: "PropertyFilterName"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~PropertyFilterName.html"
---

# PropertyFilterName Property (IPDMWUser)

Gets or sets the name of the property to use as a filter.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropertyFilterName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWUser
Dim value As System.String

instance.PropertyFilterName = value

value = instance.PropertyFilterName
```

### C#

```csharp
System.string PropertyFilterName {get; set;}
```

### C++/CLI

```cpp
property System.String^ PropertyFilterName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of property

## VBA Syntax

See [PDMWUser::PropertyFilterName](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWUser~PropertyFilterName.html).

## Remarks

Only a vault administrator can get or set the name of a property to use as a filter.

## See Also

[IPDMWUser Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser.html)
[IPDMWUser Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser_members.html)
[IPDMWUser::PropertyFilterValue Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~PropertyFilterValue.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
