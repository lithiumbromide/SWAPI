---
title: "SetFace Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "SetFace"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetFace.html"
---

# SetFace Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::SetEndConditionReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFace( _
   ByVal Forward As System.Boolean, _
   ByVal Face As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim Face As System.Object

instance.SetFace(Forward, Face)
```

### C#

```csharp
void SetFace(
   System.bool Forward,
   System.object Face
)
```

### C++/CLI

```cpp
void SetFace(
   System.bool Forward,
   System.Object^ Face
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `Face`:

## VBA Syntax

See [ExtrudeFeatureData::SetFace](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~SetFace.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
