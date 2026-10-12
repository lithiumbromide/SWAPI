---
title: "CustomProperties Property (IImport3DInterconnectData)"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: "CustomProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~CustomProperties.html"
---

# CustomProperties Property (IImport3DInterconnectData)

Gets or sets whether to import custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
Property CustomProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
Dim value As System.Boolean

instance.CustomProperties = value

value = instance.CustomProperties
```

### C#

```csharp
System.bool CustomProperties {get; set;}
```

### C++/CLI

```cpp
property System.bool CustomProperties {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import custom properties, metadata, or user-defined attributes as SOLIDWORKS custom properties, false to not

## VBA Syntax

See [Import3DInterconnectData::CustomProperties](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData~CustomProperties.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## See Also

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
