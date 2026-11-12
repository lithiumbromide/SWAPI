---
title: "IGetProcessedBodyWithSelFace2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "IGetProcessedBodyWithSelFace2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetProcessedBodyWithSelFace2.html"
---

# IGetProcessedBodyWithSelFace2 Method (IPartDoc)

Gets a processed body.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetProcessedBodyWithSelFace2() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As Body2

value = instance.IGetProcessedBodyWithSelFace2()
```

### C#

```csharp
Body2 IGetProcessedBodyWithSelFace2()
```

### C++/CLI

```cpp
Body2^ IGetProcessedBodyWithSelFace2();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Processed [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html), which is a copy of the body for this part

## VBA Syntax

See [PartDoc::IGetProcessedBodyWithSelFace2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~IGetProcessedBodyWithSelFace2.html).

## Remarks

This method requires that you preselect a face.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::IGetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetProcessedBody2.html)
[IBody2::GetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.html)
[IBody2::GetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.html)
[IBody2::IGetProcessedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBody.html)
[IBody2::IGetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
