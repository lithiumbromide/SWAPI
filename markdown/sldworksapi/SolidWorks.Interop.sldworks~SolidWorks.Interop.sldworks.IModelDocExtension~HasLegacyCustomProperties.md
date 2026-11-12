---
title: "HasLegacyCustomProperties Property (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "HasLegacyCustomProperties"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~HasLegacyCustomProperties.html"
---

# HasLegacyCustomProperties Property (IModelDocExtension)

Gets whether this model has legacy custom properties.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property HasLegacyCustomProperties As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim value As System.Boolean

value = instance.HasLegacyCustomProperties
```

### C#

```csharp
System.bool HasLegacyCustomProperties {get;}
```

### C++/CLI

```cpp
property System.bool HasLegacyCustomProperties {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the model has legacy custom properties, false if not

## VBA Syntax

See [ModelDocExtension::HasLegacyCustomProperties](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~HasLegacyCustomProperties.html).

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
