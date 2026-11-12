---
title: "CreatePlaneAtOffset Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreatePlaneAtOffset"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreatePlaneAtOffset.html"
---

# CreatePlaneAtOffset Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreatePlaneAtOffset](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePlaneAtOffset.html).

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
Dim instance As IModelDoc
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

See [ModelDoc::CreatePlaneAtOffset](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreatePlaneAtOffset.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
