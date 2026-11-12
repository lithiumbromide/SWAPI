---
title: "DeleteNamedView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "DeleteNamedView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteNamedView.html"
---

# DeleteNamedView Method (IModelDoc2)

Deletes the specified model view.

## Syntax

### Visual Basic (Declaration)

```vb
Function DeleteNamedView( _
   ByVal ViewName As System.String _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim ViewName As System.String
Dim value As System.Boolean

value = instance.DeleteNamedView(ViewName)
```

### C#

```csharp
System.bool DeleteNamedView(
   System.string ViewName
)
```

### C++/CLI

```cpp
System.bool DeleteNamedView(
   System.String^ ViewName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ViewName`: Name of the model view to delete

### Return Value

True if the named view is deleted, false if not

## VBA Syntax

See [ModelDoc2::DeleteNamedView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~DeleteNamedView.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ShowNamedView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowNamedView2.html)
[IModelDoc2::NameView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.html)
[IModelDocExtension::GetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetNamedViewRotation.html)
[IModelDocExtension::IGetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetNamedViewRotation.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
