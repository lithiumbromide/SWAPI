---
title: "ISetFace Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "ISetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~ISetFace.html"
---

# ISetFace Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::SetEndConditionReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ISetFace( _
   ByVal Forward As System.Boolean, _
   ByVal Face As Face _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim Face As Face

instance.ISetFace(Forward, Face)
```

### C#

```csharp
void ISetFace(
   System.bool Forward,
   Face Face
)
```

### C++/CLI

```cpp
void ISetFace(
   System.bool Forward,
   Face^ Face
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `Face`: v

## VBA Syntax

See [ExtrudeFeatureData::ISetFace](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~ISetFace.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
