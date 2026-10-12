---
title: "AddProfileLine Method (IBody)"
project: "SOLIDWORKS API Help"
interface: "IBody"
member: "AddProfileLine"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody~AddProfileLine.html"
---

# AddProfileLine Method (IBody)

Obsolete. Superseded by [IBody2::AddProfileBLine](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2~AddProfileLine.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function AddProfileLine( _
   ByVal RootPoint As System.Object, _
   ByVal Direction As System.Object _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IBody
Dim RootPoint As System.Object
Dim Direction As System.Object
Dim value As System.Object

value = instance.AddProfileLine(RootPoint, Direction)
```

### C#

```csharp
System.object AddProfileLine(
   System.object RootPoint,
   System.object Direction
)
```

### C++/CLI

```cpp
System.Object^ AddProfileLine(
   System.Object^ RootPoint,
   System.Object^ Direction
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `RootPoint`:
- `Direction`:

## VBA Syntax

See [Body::AddProfileLine](ms-its:sldworksapivb6.chm::/sldworks~Body~AddProfileLine.html).

## See Also

[IBody Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody.html)
[IBody Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody_members.html)
