---
title: "Comment Property (IPDMWConfiguration)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfiguration"
member: "Comment"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~Comment.html"
---

# Comment Property (IPDMWConfiguration)

Gets comments for the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property Comment As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfiguration
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

See [PDMWConfiguration::Comment](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfiguration~Comment.html).

## See Also

[IPDMWConfiguration Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)
[IPDMWConfiguration Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
