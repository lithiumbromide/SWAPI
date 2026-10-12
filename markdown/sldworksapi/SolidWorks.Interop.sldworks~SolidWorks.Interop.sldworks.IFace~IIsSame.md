---
title: "IIsSame Method (IFace)"
project: "SOLIDWORKS API Help"
interface: "IFace"
member: "IIsSame"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace~IIsSame.html"
---

# IIsSame Method (IFace)

Obsolete. Superseded by [IFace2::IIsSame](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~IIsSame.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IIsSame( _
   ByVal FaceIn As Face _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace
Dim FaceIn As Face
Dim value As System.Boolean

value = instance.IIsSame(FaceIn)
```

### C#

```csharp
System.bool IIsSame(
   Face FaceIn
)
```

### C++/CLI

```cpp
System.bool IIsSame(
   Face^ FaceIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceIn`:

## VBA Syntax

See [Face::IIsSame](ms-its:sldworksapivb6.chm::/sldworks~Face~IIsSame.html).

## See Also

[IFace Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace.html)
[IFace Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace_members.html)
