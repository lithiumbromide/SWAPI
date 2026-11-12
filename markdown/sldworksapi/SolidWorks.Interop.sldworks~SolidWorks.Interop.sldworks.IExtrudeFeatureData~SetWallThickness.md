---
title: "SetWallThickness Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "SetWallThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetWallThickness.html"
---

# SetWallThickness Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::SetWallThickness](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetWallThickness.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetWallThickness( _
   ByVal Forward As System.Boolean, _
   ByVal WallThickness As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim WallThickness As System.Double

instance.SetWallThickness(Forward, WallThickness)
```

### C#

```csharp
void SetWallThickness(
   System.bool Forward,
   System.double WallThickness
)
```

### C++/CLI

```cpp
void SetWallThickness(
   System.bool Forward,
   System.double WallThickness
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `WallThickness`:

## VBA Syntax

See [ExtrudeFeatureData::SetWallThickness](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~SetWallThickness.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
