---
title: "CustomPropertyManager Property (IConfiguration)"
project: "SOLIDWORKS API Help"
interface: "IConfiguration"
member: "CustomPropertyManager"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~CustomPropertyManager.html"
---

# CustomPropertyManager Property (IConfiguration)

Gets the custom property information for this configuration.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CustomPropertyManager As CustomPropertyManager
```

### Visual Basic (Usage)

```vb
Dim instance As IConfiguration
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

Pointer to [ICustomPropertyManager](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomPropertyManager.html) object

## VBA Syntax

See [Configuration::CustomPropertyManager](ms-its:sldworksapivb6.chm::/sldworks~Configuration~CustomPropertyManager.html).

## Examples

[Get Custom Properties for Configuration (VBA)](Get_Custom_Properties_for_Configuration_Example_VB.htm)

## See Also

[IConfiguration Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration.html)
[IConfiguration Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration_members.html)
[IFeature::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~CustomPropertyManager.html)
[IModelDocExtension::CustomPropertyManager Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~CustomPropertyManager.html)

## Availability

SOLIDWORKS 2007 FCS, Revision Number 15.0
