---
title: "ICreatePlaneAtAngle2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreatePlaneAtAngle2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtAngle2.html"
---

# ICreatePlaneAtAngle2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::ICreatePlaneAtAngle3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreatePlaneAtAngle3.html).

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
Dim instance As IModelDoc2
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

See [ModelDoc2::ICreatePlaneAtAngle2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreatePlaneAtAngle2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
