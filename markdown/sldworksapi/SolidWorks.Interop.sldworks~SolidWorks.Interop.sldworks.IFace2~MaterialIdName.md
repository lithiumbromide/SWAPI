---
title: "MaterialIdName Property (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "MaterialIdName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialIdName.html"
---

# MaterialIdName Property (IFace2)

Gets or sets the material name.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialIdName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.String

instance.MaterialIdName = value

value = instance.MaterialIdName
```

### C#

```csharp
System.string MaterialIdName {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaterialIdName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Material name

## VBA Syntax

See [Face2::MaterialIdName](ms-its:sldworksapivb6.chm::/sldworks~Face2~MaterialIdName.html).

## Remarks

This property is unsupported for faces obtained from reference surface bodies.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IModelDoc2::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MaterialIdName.html)
[IPartDoc::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.html)
[IFace2::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
