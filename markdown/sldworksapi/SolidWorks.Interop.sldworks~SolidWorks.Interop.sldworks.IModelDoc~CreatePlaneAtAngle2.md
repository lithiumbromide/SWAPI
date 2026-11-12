---
title: "CreatePlaneAtAngle2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "CreatePlaneAtAngle2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreatePlaneAtAngle2.html"
---

# CreatePlaneAtAngle2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::CreatePlaneAtAngle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~CreatePlaneAtAngle2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreatePlaneAtAngle2( _
   ByVal Val As System.Double, _
   ByVal FlipDir As System.Boolean _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Val As System.Double
Dim FlipDir As System.Boolean
Dim value As System.Object

value = instance.CreatePlaneAtAngle2(Val, FlipDir)
```

### C#

```csharp
System.object CreatePlaneAtAngle2(
   System.double Val,
   System.bool FlipDir
)
```

### C++/CLI

```cpp
System.Object^ CreatePlaneAtAngle2(
   System.double Val,
   System.bool FlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`:
- `FlipDir`:

## VBA Syntax

See [ModelDoc::CreatePlaneAtAngle2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~CreatePlaneAtAngle2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
