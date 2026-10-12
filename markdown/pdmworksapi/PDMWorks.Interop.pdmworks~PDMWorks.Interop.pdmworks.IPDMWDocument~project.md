---
title: "project Property (IPDMWDocument)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWDocument"
member: "project"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument~project.html"
---

# project Property (IPDMWDocument)

Gets the name of the project to which this document belongs.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property project As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWDocument
Dim value As System.String

value = instance.project
```

### C#

```csharp
System.string project {get;}
```

### C++/CLI

```cpp
property System.String^ project {
   System.String^ get();
}
```

### Property Value

Name of project to which this document belongs

## VBA Syntax

See [PDMWDocument::project](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWDocument~project.html).

## Examples

[Get Names of Projects for All Documents in Vault (VB.NET)](Get_Names_Projects_for_Documents_in_Vault_Example_VBNET.htm)

## See Also

[IPDMWDocument Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument.html)
[IPDMWDocument Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWDocument_members.html)
[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
