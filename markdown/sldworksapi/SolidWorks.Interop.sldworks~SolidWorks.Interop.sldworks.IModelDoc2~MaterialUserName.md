---
title: "MaterialUserName Property (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "MaterialUserName"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MaterialUserName.html"
---

# MaterialUserName Property (IModelDoc2)

Gets or sets the material name.

## Syntax

### Visual Basic (Declaration)

```vb
Property MaterialUserName As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
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

Material's name property

## VBA Syntax

See [ModelDoc2::MaterialUserName](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~MaterialUserName.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IMaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IMaterialPropertyValues.html)
[IModelDoc2::MaterialIdName Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MaterialIdName.html)
[IModelDoc2::MaterialPropertyValues Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~MaterialPropertyValues.html)
[IModelDocExtension::GetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetMaterialPropertyValues.html)
[IModelDocExtension::IGetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetMaterialPropertyValues.html)
[IModelDocExtension::IRemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IRemoveMaterialProperty.html)
[IModelDocExtension::ISetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ISetMaterialPropertyValues.html)
[IModelDocExtension::RemoveMaterialProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~RemoveMaterialProperty.html)
[IModelDocExtension::SetMaterialPropertyValues Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetMaterialPropertyValues.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
