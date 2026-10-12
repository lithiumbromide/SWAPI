---
title: "GetWallThickness Method (IRevolveFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IRevolveFeatureData"
member: "GetWallThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData~GetWallThickness.html"
---

# GetWallThickness Method (IRevolveFeatureData)

Obsolete. Superseded by [IRevolveFeatureData2::GetWallThickness](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRevolveFeatureData2~GetWallThickness.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWallThickness( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IRevolveFeatureData
Dim Forward As System.Boolean
Dim value As System.Double

value = instance.GetWallThickness(Forward)
```

### C#

```csharp
System.double GetWallThickness(
   System.bool Forward
)
```

### C++/CLI

```cpp
System.double GetWallThickness(
   System.bool Forward
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:

## VBA Syntax

See [RevolveFeatureData::GetWallThickness](ms-its:sldworksapivb6.chm::/sldworks~RevolveFeatureData~GetWallThickness.html).

## See Also

[IRevolveFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData.html)
[IRevolveFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRevolveFeatureData_members.html)
