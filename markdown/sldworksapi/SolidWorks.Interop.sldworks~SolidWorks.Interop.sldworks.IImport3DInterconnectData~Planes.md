---
title: "Planes Property (IImport3DInterconnectData)"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: "Planes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~Planes.html"
---

# Planes Property (IImport3DInterconnectData)

Gets or sets whether to import reference planes.

## Syntax

### Visual Basic (Declaration)

```vb
Property Planes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
Dim value As System.Boolean

instance.Planes = value

value = instance.Planes
```

### C#

```csharp
System.bool Planes {get; set;}
```

### C++/CLI

```cpp
property System.bool Planes {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import reference planes, false to not

## VBA Syntax

See [Import3DInterconnectData::Planes](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData~Planes.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## See Also

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
