---
title: "Value Property (IPDMWProperty)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProperty"
member: "Value"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty~Value.html"
---

# Value Property (IPDMWProperty)

Gets or sets the value of the property.

## Syntax

### Visual Basic (Declaration)

```vb
Default Property Value As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProperty
Dim value As System.String

instance.Value = value

value = instance.Value
```

### C#

```csharp
System.string this {get; set;}
```

### C++/CLI

```cpp
property System.String^ default [] {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Value of this property

## VBA Syntax

See [PDMWProperty::Value](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProperty~Value.html).

## Remarks

Use [IPDMWProperties::Update](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties~Update.html) to update the SOLIDWORKS Workgroup PDM vault after using this property to change the value of a property.

## See Also

[IPDMWProperty Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty.html)
[IPDMWProperty Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
