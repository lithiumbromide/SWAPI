---
title: "UpdateSunLight Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "UpdateSunLight"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateSunLight.html"
---

# UpdateSunLight Method (IModelDocExtension)

Updates sunlight position, color, and background image.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateSunLight() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.UpdateSunLight()
```

### C#

```csharp
System.bool UpdateSunLight()
```

### C++/CLI

```cpp
System.bool UpdateSunLight();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the update is successful, false if not

## VBA Syntax

See [ModelDocExtension::UpdateSunLight](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~UpdateSunLight.html).

## Remarks

Before calling this method, call [IModelDocExtension::SetSunLightAdvancedPropertyValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SetSunLightAdvancedPropertyValues.html) to set sunlight advanced properties.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::GetSunLightAdvancedPropertyValues Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetSunLightAdvancedPropertyValues.html)
[IModelDocExtension::SunLightInformation Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SunLightInformation.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
