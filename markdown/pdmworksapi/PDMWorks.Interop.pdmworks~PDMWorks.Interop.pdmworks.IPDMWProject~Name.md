---
title: "Name Property (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "Name"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~Name.html"
---

# Name Property (IPDMWProject)

Gets or sets the name of this project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Name As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
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

Name of this project

## VBA Syntax

See [PDMWProject::Name](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~Name.html).

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
