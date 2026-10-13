---
title: "GetStandardViewRotation Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "GetStandardViewRotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetStandardViewRotation.html"
---

# GetStandardViewRotation Method (IModelDoc2)

Gets the specified view orientation matrix with respect to the Front view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetStandardViewRotation( _
   ByVal ViewId As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ViewId As System.Integer
Dim value As System.Object

value = instance.GetStandardViewRotation(ViewId)
```

### C#

```csharp
System.object GetStandardViewRotation(
   System.int ViewId
)
```

### C++/CLI

```cpp
System.Object^ GetStandardViewRotation(
   System.int ViewId
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewId`: View ID that you want to evaluate as defined in [swStandardViews_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swStandardViews_e.html)

### Return Value

Array describing the view rotation with respect to the Front view; this is an array of 9 doubles

## VBA Syntax

See [ModelDoc2::GetStandardViewRotation](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~GetStandardViewRotation.html).

## Examples

[Show Named View (VBA)](Show_Named_View_Example_VB.htm)

## Remarks

The end-user may have redefined the Front view to be something other than the X-Y plane.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::IGetStandardViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetStandardViewRotation.html)
[IModelDocExtension::IGetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetNamedViewRotation.html)
[IModelDocExtension::GetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetNamedViewRotation.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
