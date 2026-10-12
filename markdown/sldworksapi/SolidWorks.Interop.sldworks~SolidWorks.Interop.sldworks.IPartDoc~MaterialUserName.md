---
title: "MaterialUserName Property (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "MaterialUserName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialUserName.html"
---

# MaterialUserName Property (IPartDoc)

Gets or sets the material name. This name is visible to the user.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialUserName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
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

Material's user name property

## VBA Syntax

See [PartDoc::MaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~MaterialUserName.html).

## Examples

[Get Material Property Names (VBA)](Get_Material_Property_Names_Example_VB.htm)

## Remarks

This name is visible to the user.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialIdName.html)
[IPartDoc::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~MaterialPropertyValues.html)
[IPartDoc::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IMaterialPropertyValues.html)
[IPartDoc::SetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialVisualProperties.html)
[IPartDoc::SetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~SetMaterialPropertyName2.html)
[IPartDoc::GetMaterialVisualProperties Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialVisualProperties.html)
[IPartDoc::GetMaterialPropertyName2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetMaterialPropertyName2.html)
