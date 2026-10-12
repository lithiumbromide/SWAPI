---
title: "IGetNamedViewRotation Method (IModelDocExtension)"
project: "SOLIDWORKS API Help"
interface: "IModelDocExtension"
member: "IGetNamedViewRotation"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetNamedViewRotation.html"
---

# IGetNamedViewRotation Method (IModelDocExtension)

Gets the specified named view orientation matrix with respect to the Front view.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNamedViewRotation( _
   ByVal Name As System.String _
) As System.Double
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDocExtension
Dim Name As System.String
Dim value As System.Double

value = instance.IGetNamedViewRotation(Name)
```

### C#

```csharp
System.double IGetNamedViewRotation(
   System.string Name
)
```

### C++/CLI

```cpp
System.double IGetNamedViewRotation(
   System.String^ Name
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Name`: Name of the named view

## VBA Syntax

See [ModelDocExtension::IGetNamedViewRotation](ms-its:sldworksapivb6.chm::/sldworks~ModelDocExtension~IGetNamedViewRotation.html).

## Remarks

Array of 9 doubles describing the view rotation with respect to the Front view

## See Also

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.html)
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.html)
[IModelDoc2::IModelDocExtension::GetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetNamedViewRotation.html)
[IModelDoc2::DeleteNamedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteNamedView.html)
[IModelDoc2::GetStandardViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetStandardViewRotation.html)
[IModelDoc2::IGetStandardViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IGetStandardViewRotation.html)
[IModelDoc2::NameView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.html)
[IModelDoc2::ShowNamedView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowNamedView2.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
