---
title: "ICheckInterference Method (IModeler)"
project: "SOLIDWORKS API Help"
interface: "IModeler"
member: "ICheckInterference"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler~ICheckInterference.html"
---

# ICheckInterference Method (IModeler)

Obsolete. Superseded by [IModeler::ICheckInterference2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModeler~ICheckInterference2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub ICheckInterference( _
   ByRef Body1InterferedFaceArray As Face, _
   ByRef Body2InterferedFaceArray As Face, _
   ByRef IntersectedBodyArray As Body _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModeler
Dim Body1InterferedFaceArray As Face
Dim Body2InterferedFaceArray As Face
Dim IntersectedBodyArray As Body

instance.ICheckInterference(Body1InterferedFaceArray, Body2InterferedFaceArray, IntersectedBodyArray)
```

### C#

```csharp
void ICheckInterference(
   out Face Body1InterferedFaceArray,
   out Face Body2InterferedFaceArray,
   out Body IntersectedBodyArray
)
```

### C++/CLI

```cpp
void ICheckInterference(
   [Out] Face^ Body1InterferedFaceArray,
   [Out] Face^ Body2InterferedFaceArray,
   [Out] Body^ IntersectedBodyArray
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body1InterferedFaceArray`:
- `Body2InterferedFaceArray`:
- `IntersectedBodyArray`:

## VBA Syntax

See [Modeler::ICheckInterference](ms-its:sldworksapivb6.chm::/sldworks~Modeler~ICheckInterference.html).

## See Also

[IModeler Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler.html)
[IModeler Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModeler_members.html)
