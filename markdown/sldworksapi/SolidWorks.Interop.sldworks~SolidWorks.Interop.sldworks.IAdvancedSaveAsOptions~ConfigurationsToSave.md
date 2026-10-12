---
title: "ConfigurationsToSave Property (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "ConfigurationsToSave"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~ConfigurationsToSave.html"
---

# ConfigurationsToSave Property (IAdvancedSaveAsOptions)

Sets the subset of configurations to save.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property ConfigurationsToSave As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions

instance.ConfigurationsToSave = value
```

### C#

```csharp
System.object ConfigurationsToSave {set;}
```

### C++/CLI

```cpp
property System.Object^ ConfigurationsToSave {
   void set (    System.Object^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Array of configuration names to save

## VBA Syntax

See [AdvancedSaveAsOptions::ConfigurationsToSave](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~ConfigurationsToSave.html).

## Remarks

The active configuration is always saved with the subset of configurations.

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)

## Availability

SOLIDWORKS 2020 SP02, Revision Number 28.2
