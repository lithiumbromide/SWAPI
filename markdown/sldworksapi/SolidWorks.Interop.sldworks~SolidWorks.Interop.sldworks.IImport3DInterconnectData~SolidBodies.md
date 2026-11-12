---
title: "SolidBodies Property (IImport3DInterconnectData)"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: "SolidBodies"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~SolidBodies.html"
---

# SolidBodies Property (IImport3DInterconnectData)

Gets or sets whether to import solid bodies.

## Syntax

### Visual Basic (Declaration)

```vb
Property SolidBodies As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
Dim value As System.Boolean

instance.SolidBodies = value

value = instance.SolidBodies
```

### C#

```csharp
System.bool SolidBodies {get; set;}
```

### C++/CLI

```cpp
property System.bool SolidBodies {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import solid bodies, false to not

## VBA Syntax

See [Import3DInterconnectData::SolidBodies](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData~SolidBodies.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## See Also

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
