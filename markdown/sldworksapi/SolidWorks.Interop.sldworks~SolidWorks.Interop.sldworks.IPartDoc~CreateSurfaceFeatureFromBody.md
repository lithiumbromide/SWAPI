---
title: "CreateSurfaceFeatureFromBody Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "CreateSurfaceFeatureFromBody"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateSurfaceFeatureFromBody.html"
---

# CreateSurfaceFeatureFromBody Method (IPartDoc)

Creates a surface feature from a body.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateSurfaceFeatureFromBody( _
   ByVal Body As System.Object, _
   ByVal Options As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim Body As System.Object
Dim Options As System.Integer
Dim value As System.Object

value = instance.CreateSurfaceFeatureFromBody(Body, Options)
```

### C#

```csharp
System.object CreateSurfaceFeatureFromBody(
   System.object Body,
   System.int Options
)
```

### C++/CLI

```cpp
System.Object^ CreateSurfaceFeatureFromBody(
   System.Object^ Body,
   System.int Options
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Body`: [Body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) from which to create surface feature
- `Options`: Surface feature options as defined in [swCreateFeatureBodyOpts_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swCreateFeatureBodyOpts_e.html)

### Return Value

Surface [feature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) array

## VBA Syntax

See [PartDoc::CreateSurfaceFeatureFromBody](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~CreateSurfaceFeatureFromBody.html).

## Examples

[Create Loft Surface Body and Change Into Feature (VBA)](Create_Loft_Surface_Body_and_Change_Into_Feature_Example_VB.htm)

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IPartDoc::ICreateSurfaceFeatureFromBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBody.html)
[IPartDoc::ICreateSurfaceFeatureFromBodyCount2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateSurfaceFeatureFromBodyCount2.html)
[IPartDoc::ICreateFeatureFromBody4 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ICreateFeatureFromBody4.html)
[IPartDoc::CreateFeatureFromBody3 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateFeatureFromBody3.html)

## Availability

SOLIDWORKS 2001 FCS, Revision number 9.0
