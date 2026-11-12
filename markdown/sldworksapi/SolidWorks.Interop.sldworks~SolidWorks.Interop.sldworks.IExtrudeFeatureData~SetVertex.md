---
title: "SetVertex Method (IExtrudeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData"
member: "SetVertex"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData~SetVertex.html"
---

# SetVertex Method (IExtrudeFeatureData)

Obsolete. Superseded by [IExtrudeFeatureData2::SetEndConditionReference](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~SetEndConditionReference.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetVertex( _
   ByVal Forward As System.Boolean, _
   ByVal Face As System.Object _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData
Dim Forward As System.Boolean
Dim Face As System.Object

instance.SetVertex(Forward, Face)
```

### C#

```csharp
void SetVertex(
   System.bool Forward,
   System.object Face
)
```

### C++/CLI

```cpp
void SetVertex(
   System.bool Forward,
   System.Object^ Face
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Forward`:
- `Face`:

## VBA Syntax

See [ExtrudeFeatureData::SetVertex](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData~SetVertex.html).

## See Also

[IExtrudeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData.html)
[IExtrudeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData_members.html)
