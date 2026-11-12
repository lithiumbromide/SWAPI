---
title: "AddProfileBspline Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "AddProfileBspline"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~AddProfileBspline.html"
---

# AddProfileBspline Method (IBody)

Obsolete. Superseded by [IBody2::AddProfileBspline](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~AddProfileBspline.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddProfileBspline( _
   ByVal Props As System.Object, _
   ByVal Knots As System.Object, _
   ByVal CtrlPtCoords As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim Props As System.Object
Dim Knots As System.Object
Dim CtrlPtCoords As System.Object
Dim value As System.Object

value = instance.AddProfileBspline(Props, Knots, CtrlPtCoords)
```

### C#

```csharp
System.object AddProfileBspline(
   System.object Props,
   System.object Knots,
   System.object CtrlPtCoords
)
```

### C++/CLI

```cpp
System.Object^ AddProfileBspline(
   System.Object^ Props,
   System.Object^ Knots,
   System.Object^ CtrlPtCoords
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Props`:
- `Knots`:
- `CtrlPtCoords`:

## VBA Syntax

See [Body::AddProfileBspline](ms-its:sldworksapivb6.chm::/sldworks~Body~AddProfileBspline.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
