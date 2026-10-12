---
title: "CreatePlaneAtAngle Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreatePlaneAtAngle"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreatePlaneAtAngle.html"
---

# CreatePlaneAtAngle Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreatePlaneAtAngle](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePlaneAtAngle.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::CreatePlaneAtAngle](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreatePlaneAtAngle.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
