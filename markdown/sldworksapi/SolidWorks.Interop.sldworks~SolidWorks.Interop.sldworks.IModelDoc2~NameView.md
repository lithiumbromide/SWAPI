---
title: "NameView Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "NameView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~NameView.html"
---

# NameView Method (IModelDoc2)

Creates a named view using the current view.

## Syntax

### Visual Basic (Declaration)

```vb
Sub NameView( _
   ByVal VName As System.String _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim VName As System.String

instance.NameView(VName)
```

### C#

```csharp
void NameView(
   System.string VName
)
```

### C++/CLI

```cpp
void NameView(
   System.String^ VName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `VName`: Name for the new view

## VBA Syntax

See [ModelDoc2::NameView](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~NameView.html).

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::ShowNamedView2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ShowNamedView2.html)
[IModelDoc2::DeleteNamedView Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~DeleteNamedView.html)
[IModelDocExtension::IGetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~IGetNamedViewRotation.html)
[IModelDocExtension::GetNamedViewRotation Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetNamedViewRotation.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
