---
title: "ICreatePlaneAtAngle2 Method (IModelDoc)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc"
member: "ICreatePlaneAtAngle2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~ICreatePlaneAtAngle2.html"
---

# ICreatePlaneAtAngle2 Method (IModelDoc)

Obsolete. Superseded by [IModelDoc2::ICreatePlaneAtAngle2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreatePlaneAtAngle2.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePlaneAtAngle2( _
   ByVal Val As System.Double, _
   ByVal FlipDir As System.Boolean _
) As RefPlane
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc
Dim Val As System.Double
Dim FlipDir As System.Boolean
Dim value As RefPlane

value = instance.ICreatePlaneAtAngle2(Val, FlipDir)
```

### C#

```csharp
RefPlane ICreatePlaneAtAngle2(
   System.double Val,
   System.bool FlipDir
)
```

### C++/CLI

```cpp
RefPlane^ ICreatePlaneAtAngle2(
   System.double Val,
   System.bool FlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`:
- `FlipDir`:

## VBA Syntax

See [ModelDoc::ICreatePlaneAtAngle2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc~ICreatePlaneAtAngle2.html).

## See Also

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.html)
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.html)
