---
title: "SketchesAndCurves Property (IImport3DInterconnectData)"
project: "SOLIDWORKS API Help"
interface: "IImport3DInterconnectData"
member: "SketchesAndCurves"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData~SketchesAndCurves.html"
---

# SketchesAndCurves Property (IImport3DInterconnectData)

Gets or sets whether to import unconsumed sketches or curve data as 2D or 3D sketches.

## Syntax

### Visual Basic (Declaration)

```vb
Property SketchesAndCurves As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IImport3DInterconnectData
Dim value As System.Boolean

instance.SketchesAndCurves = value

value = instance.SketchesAndCurves
```

### C#

```csharp
System.bool SketchesAndCurves {get; set;}
```

### C++/CLI

```cpp
property System.bool SketchesAndCurves {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True to import unconsumed sketches or curve data as 2D or 3D sketches, false to not

## VBA Syntax

See [Import3DInterconnectData::SketchesAndCurves](ms-its:sldworksapivb6.chm::/sldworks~Import3DInterconnectData~SketchesAndCurves.html).

## Examples

See the [IImport3DInterconnectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html) examples.

## See Also

[IImport3DInterconnectData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData.html)
[IImport3DInterconnectData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IImport3DInterconnectData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
