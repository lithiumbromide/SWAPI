---
title: "GetWallThickness Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "GetWallThickness"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~GetWallThickness.html"
---

# GetWallThickness Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::GetWallThickness](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~GetWallThickness.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetWallThickness( _
   ByVal Forward As System.Boolean _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
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

See [ExtrudeFeatureData::GetWallThickness](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~GetWallThickness.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
