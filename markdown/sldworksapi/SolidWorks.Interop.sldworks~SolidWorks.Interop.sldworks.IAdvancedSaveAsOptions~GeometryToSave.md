---
title: "GeometryToSave Property (IAdvancedSaveAsOptions)"
project: "SOLIDWORKS API Help"
interface: "IAdvancedSaveAsOptions"
member: "GeometryToSave"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~GeometryToSave.html"
---

# GeometryToSave Property (IAdvancedSaveAsOptions)

Sets the geometry to save only when saving an assembly as a part.

## Syntax

### Visual Basic (Declaration)

```vb
WriteOnly Property GeometryToSave As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IAdvancedSaveAsOptions

instance.GeometryToSave = value
```

### C#

```csharp
System.int GeometryToSave {set;}
```

### C++/CLI

```cpp
property System.int GeometryToSave {
   void set (    System.int value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Geometry to save as defined in [swGeometryToSave_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swGeometryToSave_e.html)

## VBA Syntax

See [AdvancedSaveAsOptions::GeometryToSave](ms-its:sldworksapivb6.chm::/sldworks~AdvancedSaveAsOptions~GeometryToSave.html).

## See Also

[IAdvancedSaveAsOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.html)
[IAdvancedSaveAsOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions_members.html)

## Availability

SOLIDWORKS 2020 SP02, Revision Number 28.2
