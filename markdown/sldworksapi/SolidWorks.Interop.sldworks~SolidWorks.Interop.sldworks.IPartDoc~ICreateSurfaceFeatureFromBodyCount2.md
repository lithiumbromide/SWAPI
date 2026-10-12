---
title: "ICreateSurfaceFeatureFromBodyCount2 Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "ICreateSurfaceFeatureFromBodyCount2"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBodyCount2.html"
---

# ICreateSurfaceFeatureFromBodyCount2 Method (IPartDoc)

Gets the number of surface features to create from the body.

## Syntax

### Visual Basic (Declaration)

```vb
Function ICreateSurfaceFeatureFromBodyCount2( _
   ByVal Body As Body2, _
   ByVal Options As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Body As Body2
Dim Options As System.Integer
Dim value As System.Integer

value = instance.ICreateSurfaceFeatureFromBodyCount2(Body, Options)
```

### C#

```csharp
System.int ICreateSurfaceFeatureFromBodyCount2(
   Body2 Body,
   System.int Options
)
```

### C++/CLI

```cpp
System.int ICreateSurfaceFeatureFromBodyCount2(
   Body2^ Body,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body`: Body from which to create surface features
- `Options`: Options as defined in [swCreateFeatureBodyOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateFeatureBodyOpts_e.html)

### Return Value

Number of surface features to create from the body

## VBA Syntax

See [PartDoc::ICreateSurfaceFeatureFromBodyCount2](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~ICreateSurfaceFeatureFromBodyCount2.html).

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::ICreateSurfaceFeatureFromBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBody.html)
[IPartDoc::ICreateFeatureFromBody4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.html)
[IPartDoc::CreateFeatureFromBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateFeatureFromBody3.html)
[IPartDoc::CreateSurfaceFeatureFromBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateSurfaceFeatureFromBody.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
