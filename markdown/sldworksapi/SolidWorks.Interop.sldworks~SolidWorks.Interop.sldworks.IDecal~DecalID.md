---
title: "DecalID Property (IDecal)"
project: "SOLIDWORKS API Help"
interface: "IDecal"
member: "DecalID"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal~DecalID.html"
---

# DecalID Property (IDecal)

Gets the SOLIDWORKS decal ID.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property DecalID As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IDecal
Dim value As System.Integer

value = instance.DecalID
```

### C#

```csharp
System.int DecalID {get;}
```

### C++/CLI

```cpp
property System.int DecalID {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

SOLIDWORKS decal ID (index number)

## VBA Syntax

See [Decal::DecalID](ms-its:sldworksapivb6.chm::/sldworks~Decal~DecalID.html).

## Remarks

By default, decal IDs are persistent, which means if three decals (IDs 1, 2, and 3) were applied to the model, and you [removed decal](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~DeleteDecal.html) ID 2, then the remaining decal IDs are 1 and 3.

## See Also

[IDecal Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.html)
[IDecal Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal_members.html)

## Availability

SOLIDWORKS 2008 FCS, Revision Number 16.0
