---
title: "IgnoreHiddenEntities Property (IImport3DInterconnectData)"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: "IgnoreHiddenEntities"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~IgnoreHiddenEntities.html"
---

# IgnoreHiddenEntities Property (IImport3DInterconnectData)

Gets or sets whether to ignore hidden entities.

## Syntax

### Visual Basic (Declaration)

```vb
Property IgnoreHiddenEntities As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
Dim value As System.Boolean

instance.IgnoreHiddenEntities = value

value = instance.IgnoreHiddenEntities
```

### C#

```csharp
System.bool IgnoreHiddenEntities {get; set;}
```

### C++/CLI

```cpp
property System.bool IgnoreHiddenEntities {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to ignore hidden entities, false to not

## VBA Syntax

See [Import3DInterconnectData::IgnoreHiddenEntities](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData~IgnoreHiddenEntities.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## See Also

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
