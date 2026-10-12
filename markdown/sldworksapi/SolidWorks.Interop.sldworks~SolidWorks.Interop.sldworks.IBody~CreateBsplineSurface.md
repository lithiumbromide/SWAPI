---
title: "CreateBsplineSurface Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "CreateBsplineSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~CreateBsplineSurface.html"
---

# CreateBsplineSurface Method (IBody)

Obsolete. Superseded by [IBody2::CreateBsplineSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~CreateBsplineSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateBsplineSurface( _
   ByVal Props As System.Object, _
   ByVal UKnots As System.Object, _
   ByVal VKnots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Props As System.Object
Dim UKnots As System.Object
Dim VKnots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As System.Object

value = instance.CreateBsplineSurface(Props, UKnots, VKnots, CtrlPtCoords)
```

### C#

```csharp
System.object CreateBsplineSurface(
   System.object Props,
   System.object UKnots,
   System.object VKnots,
   System.object CtrlPtCoords
)
```

### C++/CLI

```cpp
System.Object^ CreateBsplineSurface(
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

See [Body::CreateBsplineSurface](ms-its:sldworksapivb6.chm::/sldworks~Body~CreateBsplineSurface.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
