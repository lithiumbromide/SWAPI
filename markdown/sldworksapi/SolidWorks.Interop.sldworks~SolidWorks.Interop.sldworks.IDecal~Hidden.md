---
title: "Hidden Property (IDecal)"
project: "SOLIDWORKS API Help"
interface: "IDecal"
member: "Hidden"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~Hidden.html"
---

# Hidden Property (IDecal)

Gets or sets whether the decal hidden.

## Syntax

### Visual Basic (Declaration)

```vb
Property Hidden As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IDecal
Dim value As System.Boolean

instance.Hidden = value

value = instance.Hidden
```

### C#

```csharp
System.bool Hidden {get; set;}
```

### C++/CLI

```cpp
property System.bool Hidden {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the decal is hidden, false if not

## VBA Syntax

See [Decal::Hidden](ms-its:sldworksapivb6.chm::/sldworks~Decal~Hidden.html).

## See Also

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
