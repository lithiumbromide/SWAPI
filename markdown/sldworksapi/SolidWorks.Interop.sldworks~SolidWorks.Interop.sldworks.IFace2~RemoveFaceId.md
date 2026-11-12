---
title: "RemoveFaceId Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "RemoveFaceId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveFaceId.html"
---

# RemoveFaceId Method (IFace2)

Removes the face ID on an imported body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RemoveFaceId( _
   ByVal IdIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim IdIn As System.Integer

instance.RemoveFaceId(IdIn)
```

### C#

```csharp
void RemoveFaceId(
   System.int IdIn
)
```

### C++/CLI

```cpp
void RemoveFaceId(
   System.int IdIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IdIn`: Face ID

## VBA Syntax

See [Face2::RemoveFaceId](ms-its:sldworksapivb6.chm::/sldworks~Face2~RemoveFaceId.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::SetFaceId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetFaceId.html)
[IFace2::GetFaceId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFaceId.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
