---
title: "SurfaceBodies Property (IImport3DInterconnectData)"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: "SurfaceBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~SurfaceBodies.html"
---

# SurfaceBodies Property (IImport3DInterconnectData)

Gets or sets whether to import the data as surface entities.

## Syntax

### Visual Basic (Declaration)

```vb
Property SurfaceBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
Dim value As System.Boolean

instance.SurfaceBodies = value

value = instance.SurfaceBodies
```

### C#

```csharp
System.bool SurfaceBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool SurfaceBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import the data as surface entities, false to not

## VBA Syntax

See [Import3DInterconnectData::SurfaceBodies](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData~SurfaceBodies.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## See Also

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
