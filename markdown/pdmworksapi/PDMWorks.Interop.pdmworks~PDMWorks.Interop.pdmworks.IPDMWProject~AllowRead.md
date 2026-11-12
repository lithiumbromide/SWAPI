---
title: "AllowRead Property (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "AllowRead"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~AllowRead.html"
---

# AllowRead Property (IPDMWProject)

Gets whether the user has read access to this project.

## Syntax

### Visual Basic (Declaration)

```vb
Property AllowRead As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
Dim value As System.Integer

instance.AllowRead = value

value = instance.AllowRead
```

### C#

```csharp
System.int AllowRead {get; set;}
```

### C++/CLI

```cpp
property System.int AllowRead {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

0 if not allowed, 1 if allowed

## VBA Syntax

See [PDMWProject::AllowRead](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~AllowRead.html).

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)
[IPDMWProject::AllowWrite Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~AllowWrite.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
