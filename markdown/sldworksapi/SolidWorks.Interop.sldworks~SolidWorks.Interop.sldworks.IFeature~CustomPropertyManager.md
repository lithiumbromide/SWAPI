---
title: "CustomPropertyManager Property (IFeature)"
project: "SOLIDWORKS API Help"
interface: "IFeature"
member: "CustomPropertyManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CustomPropertyManager.html"
---

# CustomPropertyManager Property (IFeature)

Gets the custom property information for weldment and cut-list item features only.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CustomPropertyManager As CustomPropertyManager
```

### Visual Basic (Usage)

```vb
Dim instance As IFeature
Dim value As CustomPropertyManager

value = instance.CustomPropertyManager
```

### C#

```csharp
CustomPropertyManager CustomPropertyManager {get;}
```

### C++/CLI

```cpp
property CustomPropertyManager^ CustomPropertyManager {
   CustomPropertyManager^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [ICustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager.html) object

## VBA Syntax

See [Feature::CustomPropertyManager](ms-its:sldworksapivb6.chm::/sldworks~Feature~CustomPropertyManager.html).

## Examples

[Add and Get Custom Properties (VBA)](Add_and_Get_Custom_Properties_Example_VB.htm)
[Get Custom Properties for Cut-list Item (VBA)](Get_Custom_Properties_for_Cut-list_Item_Example_VB.htm)

## See Also

[IFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)
[IFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature_members.html)
[IModelDocExtension::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html)
[IConfiguration::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.html)

## Availability

SOLIDWORKS 2004 FCS, Revision Number 12.0
