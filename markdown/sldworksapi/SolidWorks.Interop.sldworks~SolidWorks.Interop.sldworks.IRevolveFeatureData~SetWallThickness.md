---
title: "SetWallThickness Method (IRevolveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData"
member: "SetWallThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData~SetWallThickness.html"
---

# SetWallThickness Method (IRevolveFeatureData)

Obsolete. Superseded by [IRevolveFeatureData2::SetWallThickness](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~SetWallThickness.html).

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
Dim instance As IRevolveFeatureData
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

See [RevolveFeatureData::SetWallThickness](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData~SetWallThickness.html).

## See Also

[IRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData.html)
[IRevolveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData_members.html)
