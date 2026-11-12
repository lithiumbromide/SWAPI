---
title: "SaveAllAsCopy Property (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "SaveAllAsCopy"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~SaveAllAsCopy.html"
---

# SaveAllAsCopy Property (IAdvancedSaveAsOptions)

Sets whether to save all component references as copies.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property SaveAllAsCopy As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions

instance.SaveAllAsCopy = value
```

### C#

```csharp
System.bool SaveAllAsCopy {set;}
```

### C++/CLI

```cpp
property System.bool SaveAllAsCopy {
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to save all as a copy, false (default) to not

## VBA Syntax

See [AdvancedSaveAsOptions::SaveAllAsCopy](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~SaveAllAsCopy.html).

## Examples

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html) example.

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)

## Availability

SOLIDWORKS 2020 SP02, Revision Number 28.2
