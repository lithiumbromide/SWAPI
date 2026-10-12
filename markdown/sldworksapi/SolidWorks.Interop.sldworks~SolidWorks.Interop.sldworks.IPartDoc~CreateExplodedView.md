---
title: "CreateExplodedView Method (IPartDoc)"
project: "SOLIDWORKS API Help"
interface: "IPartDoc"
member: "CreateExplodedView"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~CreateExplodedView.html"
---

# CreateExplodedView Method (IPartDoc)

Creates an explode view of this multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function CreateExplodedView() As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As IPartDoc
Dim value As System.Boolean

value = instance.CreateExplodedView()
```

### C#

```csharp
System.bool CreateExplodedView()
```

### C++/CLI

```cpp
System.bool CreateExplodedView();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

True if the explode view is successfully created, false if not

## VBA Syntax

See [PartDoc::CreateExplodedView](ms-its:sldworksapivb6.chm::/sldworks~PartDoc~CreateExplodedView.html).

## Examples

See the [IPartExplodeStep](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html) example.

## See Also

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.html)
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.html)
[IConfiguration::AddPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~AddPartExplodeStep.html)
[IConfiguration::GetPartExplodeStep Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConfiguration~GetPartExplodeStep.html)
[IPartDoc::GetExplodedViewNames Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewNames.html)
[IPartDoc::GetExplodedViewConfigurationName Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewConfigurationName.html)
[IPartDoc::ShowExploded Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~ShowExploded.html)
[IPartDoc::GetExplodedViewCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~GetExplodedViewCount.html)
[IPartExplodeStep Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartExplodeStep.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
