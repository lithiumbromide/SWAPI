---
title: "GetNamedViewRotation Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "GetNamedViewRotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetNamedViewRotation.html"
---

# GetNamedViewRotation Method (IModelDocExtension)

Gets the specified named view orientation matrix with respect to the Front view.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNamedViewRotation( _
   ByVal Name As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Name As System.String
Dim value As System.Object

value = instance.GetNamedViewRotation(Name)
```

### C#

```csharp
System.object GetNamedViewRotation(
   System.string Name
)
```

### C++/CLI

```cpp
System.Object^ GetNamedViewRotation(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the named view

### Return Value

Array of 9 doubles describing the view rotation with respect to the Front view

## VBA Syntax

See [ModelDocExtension::GetNamedViewRotation](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~GetNamedViewRotation.html).

## Remarks

The end-user may have redefined the Front view to be something other than the X-Y plane.

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDocExtension::IGetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetNamedViewRotation.html)
[IModelDoc2::GetStandardViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetStandardViewRotation.html)
[IModelDoc2::IGetStandardViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetStandardViewRotation.html)
[IModelDoc2::DeleteNamedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteNamedView.html)
[IModelDoc2::NameView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.html)
[IModelDoc2::ShowNamedView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowNamedView2.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
