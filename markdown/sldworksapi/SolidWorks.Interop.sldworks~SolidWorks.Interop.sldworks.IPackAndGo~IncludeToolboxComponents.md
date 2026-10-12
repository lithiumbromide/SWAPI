---
title: "IncludeToolboxComponents Property (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "IncludeToolboxComponents"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeToolboxComponents.html"
---

# IncludeToolboxComponents Property (IPackAndGo)

Gets or sets whether to include SOLIDWORKS Toolbox components in Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeToolboxComponents As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim value As System.Boolean

instance.IncludeToolboxComponents = value

value = instance.IncludeToolboxComponents
```

### C#

```csharp
System.bool IncludeToolboxComponents {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeToolboxComponents {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to include SOLIDWORKS Toolbox components in Pack and Go, false to not

## VBA Syntax

See [PackAndGo::IncludeToolboxComponents](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~IncludeToolboxComponents.html).

## Examples

[Pack and Go an Assembly (C#)](Pack_and_Go_an_Assembly_Example_CSharp.htm)
[Pack and Go an Assembly (VB.NET)](Pack_and_Go_an_Assembly_Example_VBNET.htm)
[Pack and Go an Assembly (VBA)](Pack_and_Go_an_Assembly_Example_VB.htm)

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
