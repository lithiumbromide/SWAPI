---
title: "SetDepth Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "SetDepth"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetDepth.html"
---

# SetDepth Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::SetDepth](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetDepth.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetDepth( _
   ByVal Forward As System.Boolean, _
   ByVal Depth As System.Double _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim Depth As System.Double

instance.SetDepth(Forward, Depth)
```

### C#

```csharp
void SetDepth(
   System.bool Forward,
   System.double Depth
)
```

### C++/CLI

```cpp
void SetDepth(
   System.bool Forward,
   System.double Depth
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `Depth`:

## VBA Syntax

See [ExtrudeFeatureData::SetDepth](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~SetDepth.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
