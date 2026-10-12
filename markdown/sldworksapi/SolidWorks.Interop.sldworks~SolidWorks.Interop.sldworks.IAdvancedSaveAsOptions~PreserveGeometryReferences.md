---
title: "PreserveGeometryReferences Property (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "PreserveGeometryReferences"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~PreserveGeometryReferences.html"
---

# PreserveGeometryReferences Property (IAdvancedSaveAsOptions)

Sets whether to preserve geometry references only when saving an assembly as a part.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property PreserveGeometryReferences As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions

instance.PreserveGeometryReferences = value
```

### C#

```csharp
System.bool PreserveGeometryReferences {set;}
```

### C++/CLI

```cpp
property System.bool PreserveGeometryReferences {
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to preserve geometry references, false to not

## VBA Syntax

See [AdvancedSaveAsOptions::PreserveGeometryReferences](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~PreserveGeometryReferences.html).

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)

## Availability

SOLIDWORKS 2020 SP02, Revision Number 28.2
