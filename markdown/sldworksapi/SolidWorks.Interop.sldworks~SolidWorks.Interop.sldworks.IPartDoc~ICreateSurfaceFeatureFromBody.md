---
title: "ICreateSurfaceFeatureFromBody Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ICreateSurfaceFeatureFromBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBody.html"
---

# ICreateSurfaceFeatureFromBody Method (IPartDoc)

Creates a surface feature from a body.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSurfaceFeatureFromBody() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As Feature

value = instance.ICreateSurfaceFeatureFromBody()
```

### C#

```csharp
Feature ICreateSurfaceFeatureFromBody()
```

### C++/CLI

```cpp
Feature^ ICreateSurfaceFeatureFromBody();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Surface [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) array

## VBA Syntax

See [PartDoc::ICreateSurfaceFeatureFromBody](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~ICreateSurfaceFeatureFromBody.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::CreateSurfaceFeatureFromBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateSurfaceFeatureFromBody.html)
[IPartDoc::CreateFeatureFromBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateFeatureFromBody3.html)
[IPartDoc::ICreateFeatureFromBody4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.html)
[IPartDoc::ICreateSurfaceFeatureFromBodyCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBodyCount2.html)

## Availability

SOLIDWORKS 2001 FCS, Revision number 9.0
