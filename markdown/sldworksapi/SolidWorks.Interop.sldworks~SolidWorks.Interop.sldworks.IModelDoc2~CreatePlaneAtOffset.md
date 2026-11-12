---
title: "CreatePlaneAtOffset Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreatePlaneAtOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtOffset.html"
---

# CreatePlaneAtOffset Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreatePlaneAtOffset3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePlaneAtOffset3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub CreatePlaneAtOffset( _
   ByVal Val As System.Double, _
   ByVal FlipDir As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Val As System.Double
Dim FlipDir As System.Boolean

instance.CreatePlaneAtOffset(Val, FlipDir)
```

### C#

```csharp
void CreatePlaneAtOffset(
   System.double Val,
   System.bool FlipDir
)
```

### C++/CLI

```cpp
void CreatePlaneAtOffset(
   System.double Val,
   System.bool FlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`:
- `FlipDir`:

## VBA Syntax

See [ModelDoc2::CreatePlaneAtOffset](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreatePlaneAtOffset.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
