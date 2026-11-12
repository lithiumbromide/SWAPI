---
title: "GetFaceId Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetFaceId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFaceId.html"
---

# GetFaceId Method (IFace2)

Gets the face ID of an imported body.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFaceId() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Integer

value = instance.GetFaceId()
```

### C#

```csharp
System.int GetFaceId()
```

### C++/CLI

```cpp
System.int GetFaceId();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Face ID

## VBA Syntax

See [Face2::GetFaceId](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetFaceId.html).

## Remarks

SOLIDWORKS uses face IDs to track specific faces of imported bodies (for example, IGES imports).

Prior to [setting a face ID](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2~SetFaceId.html), you should examine all faces in the model to get their face IDs, if any, to ensure that the face ID you are setting is unique to the model.

Face IDs are saved with the document, but face IDs are removed whenever the document is rebuilt. Typically you assign face IDs to a read-only copy of the finalized model.

Any third-party application can change a face ID. The intent is that you assign face IDs so that you can refer to those faces within your application.

Use the [IAttribute](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAttribute.html) object to store data with a face.

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::RemoveFaceId Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~RemoveFaceId.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
