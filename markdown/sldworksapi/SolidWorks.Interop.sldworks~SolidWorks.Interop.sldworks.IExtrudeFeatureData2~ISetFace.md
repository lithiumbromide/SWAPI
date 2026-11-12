---
title: "ISetFace Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "ISetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetFace.html"
---

# ISetFace Method (IExtrudeFeatureData2)

Obsolete. Superseded by [IExtrudeFeatureData2::SetEndConditionReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFace( _
   ByVal Forward As System.Boolean, _
   ByVal Face As Face2 _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim Forward As System.Boolean
Dim Face As Face2

instance.ISetFace(Forward, Face)
```

### C#

```csharp
void ISetFace(
   System.bool Forward,
   Face2 Face
)
```

### C++/CLI

```cpp
void ISetFace(
   System.bool Forward,
   Face2^ Face
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `Face`:

## VBA Syntax

See [ExtrudeFeatureData2::ISetFace](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~ISetFace.html).

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
