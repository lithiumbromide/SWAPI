---
title: "IncludeSuppressed Property (IPackAndGo)"
project: "SOLIDWORKS API Help"
interface: "IPackAndGo"
member: "IncludeSuppressed"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo~IncludeSuppressed.html"
---

# IncludeSuppressed Property (IPackAndGo)

Gets or sets whether to included suppressed components in Pack and Go.

## Syntax

### Visual Basic (Declaration)

```vb
Property IncludeSuppressed As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPackAndGo
Dim value As System.Boolean

instance.IncludeSuppressed = value

value = instance.IncludeSuppressed
```

### C#

```csharp
System.bool IncludeSuppressed {get; set;}
```

### C++/CLI

```cpp
property System.bool IncludeSuppressed {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if suppressed components are added to Pack and Go, false if not

## VBA Syntax

See [PackAndGo::IncludeSuppressed](ms-its:sldworksapivb6.chm::/sldworks~PackAndGo~IncludeSuppressed.html).

## See Also

[IPackAndGo Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo.html)
[IPackAndGo Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPackAndGo_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
