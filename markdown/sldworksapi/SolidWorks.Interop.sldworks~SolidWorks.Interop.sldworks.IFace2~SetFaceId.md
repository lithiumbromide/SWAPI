---
title: "SetFaceId Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "SetFaceId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~SetFaceId.html"
---

# SetFaceId Method (IFace2)

Sets the face ID on an imported body.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetFaceId( _
   ByVal IdIn As System.Integer _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim IdIn As System.Integer

instance.SetFaceId(IdIn)
```

### C#

```csharp
void SetFaceId(
   System.int IdIn
)
```

### C++/CLI

```cpp
void SetFaceId(
   System.int IdIn
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IdIn`: Face ID

## VBA Syntax

See [Face2::SetFaceId](ms-its:sldworksapivb6.chm::/sldworks~Face2~SetFaceId.html).

## Remarks

SOLIDWORKS uses face IDs to track specific faces of imported bodies (for example, IGES imports).

Prior to setting a face ID, you should examine all faces in the model to [get their face IDs](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~GetFaceId.html), if any, to ensure that the face ID you are setting is unique to the model.

Face IDs are saved with the document, but face IDs are removed whenever the document is rebuilt. Typically you assign face IDs to a read-only copy of the finalized model.

Any third-party application can change a face ID. The intent is that you assign face IDs so that you can refer to those faces within your application.

To store data with a face, use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) object.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::RemoveFaceId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveFaceId.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
