---
title: "PropertyFilterValue Property (IPDMWUser)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWUser"
member: "PropertyFilterValue"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~PropertyFilterValue.html"
---

# PropertyFilterValue Property (IPDMWUser)

Gets or sets the value of a property to use as a filter.

## Syntax

### Visual Basic (Declaration)

```vb
Property PropertyFilterValue As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWUser
Dim value As System.String

instance.PropertyFilterValue = value

value = instance.PropertyFilterValue
```

### C#

```csharp
System.string PropertyFilterValue {get; set;}
```

### C++/CLI

```cpp
property System.String^ PropertyFilterValue {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Value of a property to use as a filter

## VBA Syntax

See [PDMWUser::PropertyFilterValue](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWUser~PropertyFilterValue.html).

## Remarks

Only a vault administrator can get or set the value of a property to use as a filter.

## See Also

[IPDMWUser Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser.html)
[IPDMWUser Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser_members.html)
[IPDMWUser::IPDMWUser::PropertyFilterName Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~PropertyFilterName.html)
[IPDMWUser::PropertyFilterValue Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWUser~PropertyFilterValue.html)

## Availability

SOLIDWORKS Workgroup PDM 2006 FCS
