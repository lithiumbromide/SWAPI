---
title: "UpdateStandardViews Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "UpdateStandardViews"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~UpdateStandardViews.html"
---

# UpdateStandardViews Method (IModelDocExtension)

Changes the specified standard view to the current model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function UpdateStandardViews( _
   ByVal ViewName As System.String, _
   ByVal ViewId As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim ViewName As System.String
Dim ViewId As System.Integer
Dim value As System.Boolean

value = instance.UpdateStandardViews(ViewName, ViewId)
```

### C#

```csharp
System.bool UpdateStandardViews(
   System.string ViewName,
   System.int ViewId
)
```

### C++/CLI

```cpp
System.bool UpdateStandardViews(
   System.String^ ViewName,
   System.int ViewId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewName`: Name of the standard model view to change; empty string to use ViewId (**see Remarks**)
- `ViewId`: View ID as defined in [swStandardViews_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html); -1 to use ViewName (**see Remarks**)

### Return Value

True if the standard model view update is successful, false if not

## VBA Syntax

See [ModelDocExtension::UpdateStandardViews](ms-its:sldworksapivb6.chm::/Sldworks~ModelDocExtension~UpdateStandardViews.html).

## Remarks

This method works with parts and assemblies only.

If you set both ViewName and ViewId, then ViewId takes precedence if the two arguments do not resolve to the same standard model view.

This method does not support the following standard model views:

- [swStandardViews_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html).swDimetricView
- swStandardViews_e.swIsometricView
- swStandardViews_e.swTrimetricView

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::ResetStandardViews Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~ResetStandardViews.html)
[IModelDoc2::ShowNamedView2 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowNamedView2.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
