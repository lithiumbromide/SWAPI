---
title: "AllowWrite Property (IPDMWProject)"
project: "SOLIDWORKS Workgroup PDM API Help"
interface: "IPDMWProject"
member: "AllowWrite"
kind: "property"
source: "pdmworksapi/PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~AllowWrite.html"
---

# AllowWrite Property (IPDMWProject)

Gets whether the user has write access to this project.

## Syntax

### Visual Basic (Declaration)

```vb
Property AllowWrite As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPDMWProject
Dim value As System.Integer

instance.AllowWrite = value

value = instance.AllowWrite
```

### C#

```csharp
System.int AllowWrite {get; set;}
```

### C++/CLI

```cpp
property System.int AllowWrite {
   System.int get();
   void set (    System.int value);
}
```

### Property Value

0 if not allowed, 1 if allowed

## VBA Syntax

See [PDMWProject::AllowWrite](ms-its:pdmworksapivb6.chm::/pdmworks~PDMWProject~AllowWrite.html).

## See Also

[IPDMWProject Interface](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject.html)
[IPDMWProject Members](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject_members.html)
[IPDMWProject::AllowRead Property](PDMWorks.Interop.pdmworks~PDMWorks.Interop.pdmworks.IPDMWProject~AllowRead.html)

## Availability

SOLIDWORKS Workgroup PDM 2003 FCS
