---
title: "CreatePlaneAtAngle Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "CreatePlaneAtAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtAngle.html"
---

# CreatePlaneAtAngle Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::CreatePlaneAtAngle3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePlaneAtAngle3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub CreatePlaneAtAngle( _
   ByVal Val As System.Double, _
   ByVal FlipDir As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim Val As System.Double
Dim FlipDir As System.Boolean

instance.CreatePlaneAtAngle(Val, FlipDir)
```

### C#

```csharp
void CreatePlaneAtAngle(
   System.double Val,
   System.bool FlipDir
)
```

### C++/CLI

```cpp
void CreatePlaneAtAngle(
   System.double Val,
   System.bool FlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`:
- `FlipDir`:

## VBA Syntax

See [ModelDoc2::CreatePlaneAtAngle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~CreatePlaneAtAngle.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
