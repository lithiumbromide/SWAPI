---
title: "IIsSame Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "IIsSame"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IIsSame.html"
---

# IIsSame Method (IFace2)

Gets whether the two faces are the same.

## Syntax

### Visual Basic (Declaration)

```vb
Function IIsSame( _
   ByVal FaceIn As Face2 _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim FaceIn As Face2
Dim value As System.Boolean

value = instance.IIsSame(FaceIn)
```

### C#

```csharp
System.bool IIsSame(
   Face2 FaceIn
)
```

### C++/CLI

```cpp
System.bool IIsSame(
   Face2^ FaceIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `FaceIn`: Pointer to the [face](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html) to which to compare this face

### Return Value

True if the two faces are the same, false if they are different

## VBA Syntax

See [Face2::IIsSame](ms-its:sldworksapivb6.chm::/sldworks~Face2~IIsSame.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::IsSame Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IsSame.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
