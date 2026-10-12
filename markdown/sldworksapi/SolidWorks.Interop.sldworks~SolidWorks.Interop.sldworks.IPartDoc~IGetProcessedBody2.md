---
title: "IGetProcessedBody2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IGetProcessedBody2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetProcessedBody2.html"
---

# IGetProcessedBody2 Method (IPartDoc)

Pre-processes the geometry of a body so that:

- Closed periodic faces (for example, the lateral face of a cylinder) are split into two faces.
- Faces that straddle the seam, if any, of the underlying surface are split into two faces.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProcessedBody2() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As Body2

value = instance.IGetProcessedBody2()
```

### C#

```csharp
Body2 IGetProcessedBody2()
```

### C++/CLI

```cpp
Body2^ IGetProcessedBody2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Processed [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), which is a copy of the body for this part

## VBA Syntax

See [PartDoc::IGetProcessedBody2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IGetProcessedBody2.html).

## Remarks

Preprocessing is sometimes necessary (for example, IGES files), for exporting to systems that have difficulty with periodic conditions.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IBody2::GetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.html)
[IBody2::GetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.html)
[IBody2::IGetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.html)
[IPartDoc::IGetProcessedBodyWithSelFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetProcessedBodyWithSelFace2.html)
[IBody2::IGetProcessedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBody.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
