---
title: "ICreateBsplineSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "ICreateBsplineSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~ICreateBsplineSurface.html"
---

# ICreateBsplineSurface Method (IBody)

Obsolete. Superseded by [IBody2::ICreateBsplineSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~ICreateBsplineSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateBsplineSurface( _
   ByVal Props As System.Object, _
   ByVal UKnots As System.Object, _
   ByVal VKnots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As Surface
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Props As System.Object
Dim UKnots As System.Object
Dim VKnots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As Surface

value = instance.ICreateBsplineSurface(Props, UKnots, VKnots, CtrlPtCoords)
```

### C#

```csharp
Surface ICreateBsplineSurface(
   System.object Props,
   System.object UKnots,
   System.object VKnots,
   System.object CtrlPtCoords
)
```

### C++/CLI

```cpp
Surface^ ICreateBsplineSurface(
   System.Object^ Props,
   System.Object^ UKnots,
   System.Object^ VKnots,
   System.Object^ CtrlPtCoords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Props`:
- `UKnots`:
- `VKnots`:
- `CtrlPtCoords`:

## VBA Syntax

See [Body::ICreateBsplineSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~ICreateBsplineSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
