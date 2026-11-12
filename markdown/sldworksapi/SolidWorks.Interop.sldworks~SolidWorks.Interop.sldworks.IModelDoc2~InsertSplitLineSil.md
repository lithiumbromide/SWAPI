---
title: "InsertSplitLineSil Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSplitLineSil"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineSil.html"
---

# InsertSplitLineSil Method (IModelDoc2)

Splits a face by creating split lines along the silhouette of the selected faces.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSplitLineSil()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.InsertSplitLineSil()
```

### C#

```csharp
void InsertSplitLineSil()
```

### C++/CLI

```cpp
void InsertSplitLineSil();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::InsertSplitLineSil](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSplitLineSil.html).

## Remarks

The silhouette curves differ based on your orientation. Therefore, this method requires a selection to specify the desired direction.

Valid items to select to specify the direction are:

- reference plane
- planar face
- edge
- axis
- two points

The item selected for direction must be selected using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with a mark value of 2. The faces to split must be selected using IModelDocExtension::SelectByID2 with mark values of 1.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertSplitLineProject Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineProject.html)
[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[IFeatureManager::InsertSplitLineIntersect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSplitLineIntersect.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
