---
title: "ICreatePlaneAtOffset2 Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ICreatePlaneAtOffset2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtOffset2.html"
---

# ICreatePlaneAtOffset2 Method (IModelDoc2)

Obsolete. Superseded by [IModelDoc2::ICreatePlaneAtOffset3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ICreatePlaneAtOffset3.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreatePlaneAtOffset2( _
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

value = instance.ICreatePlaneAtOffset2(Val, FlipDir)
```

### C#

```csharp
RefPlane ICreatePlaneAtOffset2(
   System.double Val,
   System.bool FlipDir
)
```

### C++/CLI

```cpp
RefPlane^ ICreatePlaneAtOffset2(
   System.double Val,
   System.bool FlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Val`:
- `FlipDir`:

## VBA Syntax

See [ModelDoc2::ICreatePlaneAtOffset2](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ICreatePlaneAtOffset2.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
