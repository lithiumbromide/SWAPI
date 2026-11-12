---
title: "Description Property (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "Description"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~Description.html"
---

# Description Property (IPDMWProject)

Gets or sets the description for this project.

## Syntax

### Visual Basic (Declaration)

```vb
Property Description As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
Dim value As System.String

instance.Description = value

value = instance.Description
```

### C#

```csharp
System.string Description {get; set;}
```

### C++/CLI

```cpp
property System.String^ Description {
   System.String^ get();
   void set (    System.String^ value);
}
```

### Property Value

Description for this project

## VBA Syntax

See [PDMWProject::Description](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~Description.html).

## Remarks

Only a vault administrator can set the description.

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
