---
title: "OverrideDefaults Property (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "OverrideDefaults"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~OverrideDefaults.html"
---

# OverrideDefaults Property (IAdvancedSaveAsOptions)

Sets whether to override defaults only when saving an assembly as a part.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property OverrideDefaults As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions

instance.OverrideDefaults = value
```

### C#

```csharp
System.bool OverrideDefaults {set;}
```

### C++/CLI

```cpp
property System.bool OverrideDefaults {
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to override defaults, false to not

## VBA Syntax

See [AdvancedSaveAsOptions::OverrideDefaults](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~OverrideDefaults.html).

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)

## Availability

SOLIDWORKS 2020 SP02, Revision Number 28.2
