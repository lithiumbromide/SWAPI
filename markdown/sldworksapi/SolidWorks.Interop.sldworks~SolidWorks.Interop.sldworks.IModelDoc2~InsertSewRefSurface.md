---
title: "InsertSewRefSurface Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSewRefSurface"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSewRefSurface.html"
---

# InsertSewRefSurface Method (IModelDoc2)

Obsolete. Superseded by [IFeatureManager::InsertSewRefSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertSewRefSurface.html).

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSewRefSurface()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.InsertSewRefSurface()
```

### C#

```csharp
void InsertSewRefSurface()
```

### C++/CLI

```cpp
void InsertSewRefSurface();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::InsertSewRefSurface](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSewRefSurface.html).

## Remarks

Make selections using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with a mark number of 1. See the SOLIDWORKS Help for information about what entities are valid for selection.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[ISurfaceKnitFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurfaceKnitFeatureData.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
