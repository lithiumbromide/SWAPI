---
title: "Add Method (IPDMWProperties)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProperties"
member: "Add"
kind: "method"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties~Add.html"
---

# Add Method (IPDMWProperties)

Adds a new property if the name of the property is not already in the collection.

## Syntax

### Visual Basic (Declaration)

```vb
Function Add( _
   ByVal Name As System.String _
) As PDMWProperty
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProperties
Dim Name As System.String
Dim value As PDMWProperty

value = instance.Add(Name)
```

### C#

```csharp
PDMWProperty Add(
   System.string Name
)
```

### C++/CLI

```cpp
PDMWProperty^ Add(
   System.String^ Name
)
```

### Parameters

- `Name`: Name of the property

### Return Value

[IPDMWProperty](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty.html)

## VBA Syntax

See [PDMWProperties::Add](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProperties~Add.html).

## Remarks

If using this property to add a PDMWProperty to a [IPDMWProperties](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties.html) collection, assign a value to the property using [IPDMWProperty::Value](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperty~Value.html) and then use [IPDMWProperties::Update](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties~Update.html) to update the SOLIDWORKS Workgroup PDM vault. Otherwise, the property is not added.

Use this method before using IPDMWProperties::Update.

You cannot add new properties to collections of vault administrator-assigned custom properties.

## See Also

[IPDMWProperties Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties.html)
[IPDMWProperties Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProperties_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
