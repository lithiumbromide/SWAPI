---
title: "Description Property (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "Description"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~Description.html"
---

# Description Property (IAdvancedSaveAsOptions)

Adds a desciption of the save.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property Description As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions

instance.Description = value
```

### C#

```csharp
System.string Description {set;}
```

### C++/CLI

```cpp
property System.String^ Description {
   void set (    System.String^ value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Description

## VBA Syntax

See [AdvancedSaveAsOptions::Description](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~Description.html).

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)

## Availability

SOLIDWORKS 2020 SP02, Revision Number 28.2
