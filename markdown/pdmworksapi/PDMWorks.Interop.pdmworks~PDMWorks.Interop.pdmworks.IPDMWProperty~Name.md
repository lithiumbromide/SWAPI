---
title: "Name Property (IPDMWProperty)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProperty"
member: "Name"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty~Name.html"
---

# Name Property (IPDMWProperty)

Gets the name of this property.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProperty
Dim value As System.String

instance.Name = value

value = instance.Name
```

### C#

```csharp
System.string Name {get; set;}
```

### C++/CLI

```cpp
property System.String^ Name {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Name of this property

## VBA Syntax

See [PDMWProperty::Name](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProperty~Name.html).

## See Also

[IPDMWProperty Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty.html)
[IPDMWProperty Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
