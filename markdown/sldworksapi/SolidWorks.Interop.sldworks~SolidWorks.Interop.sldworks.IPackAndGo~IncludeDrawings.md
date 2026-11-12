---
title: "IncludeDrawings Property (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "IncludeDrawings"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeDrawings.html"
---

# IncludeDrawings Property (IPackAndGo)

Gets or sets whether to add the model's drawing documents to Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeDrawings As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim value As System.Boolean

instance.IncludeDrawings = value

value = instance.IncludeDrawings
```

### C#

```csharp
System.bool IncludeDrawings {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeDrawings {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the model's drawings documents are added to Pack and Go, false if not

## VBA Syntax

See [PackAndGo::IncludeDrawings](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~IncludeDrawings.html).

## Examples

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)

## Availability

SOLIDWORKS 2011 FCS, Revision Number 19.0
