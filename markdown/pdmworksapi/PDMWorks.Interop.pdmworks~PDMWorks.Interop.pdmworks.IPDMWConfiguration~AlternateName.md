---
title: "AlternateName Property (IPDMWConfiguration)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWConfiguration"
member: "AlternateName"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration~AlternateName.html"
---

# AlternateName Property (IPDMWConfiguration)

Gets the alternate name for the configuration.

## Syntax

### Visual Basic (Declaration)

```vb
Property AlternateName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWConfiguration
Dim value As System.String

instance.AlternateName = value

value = instance.AlternateName
```

### C#

```csharp
System.string AlternateName {get; set;}
```

### C++/CLI

```cpp
property System.String^ AlternateName {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Alternate name for the configuration

## VBA Syntax

See [PDMWConfiguration::AlternateName](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWConfiguration~AlternateName.html).

## See Also

[IPDMWConfiguration Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration.html)
[IPDMWConfiguration Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWConfiguration_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
