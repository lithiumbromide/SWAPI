---
title: "Axes Property (IImport3DInterconnectData)"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: "Axes"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~Axes.html"
---

# Axes Property (IImport3DInterconnectData)

Gets or sets whether to import reference axes.

## Syntax

### Visual Basic (Declaration)

```vb
Property Axes As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
Dim value As System.Boolean

instance.Axes = value

value = instance.Axes
```

### C#

```csharp
System.bool Axes {get; set;}
```

### C++/CLI

```cpp
property System.bool Axes {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import reference axes, false to not

## VBA Syntax

See [Import3DInterconnectData::Axes](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData~Axes.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## Remarks

Reference axes can be imported only from CATIA® V5 files.

## See Also

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
