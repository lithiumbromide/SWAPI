---
title: "MaterialUserName Property (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "MaterialUserName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialUserName.html"
---

# MaterialUserName Property (IFace2)

Gets or sets the material name, which is visible to the user.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialUserName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.String

instance.MaterialUserName = value

value = instance.MaterialUserName
```

### C#

```csharp
System.string MaterialUserName {get; set;}
```

### C++/CLI

```cpp
property System.String^ MaterialUserName {
   System.String^ get();
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Material user name property on the face

## VBA Syntax

See [Face2::MaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~Face2~MaterialUserName.html).

## Remarks

This property is not supported for faces obtained from reference surface bodies.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~MaterialIdName.html)
[IModelDoc2::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MaterialUserName.html)
[IPartDoc::MaterialUserName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
