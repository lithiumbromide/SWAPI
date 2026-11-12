---
title: "InsertSplitLineProject Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "InsertSplitLineProject"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineProject.html"
---

# InsertSplitLineProject Method (IModelDoc2)

Splits a face by projecting sketch lines onto the face.

## Syntax

### Visual Basic (Declaration)

```vb
Sub InsertSplitLineProject( _
   ByVal IsDirectional As System.Boolean, _
   ByVal FlipDir As System.Boolean _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim IsDirectional As System.Boolean
Dim FlipDir As System.Boolean

instance.InsertSplitLineProject(IsDirectional, FlipDir)
```

### C#

```csharp
void InsertSplitLineProject(
   System.bool IsDirectional,
   System.bool FlipDir
)
```

### C++/CLI

```cpp
void InsertSplitLineProject(
   System.bool IsDirectional,
   System.bool FlipDir
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `IsDirectional`: Whether to project in one direction:

  - 0 projects in both directions
  - 1 projects in one direction
- `FlipDir`: Whether to project along the normal to the sketch plane; valid only when isDirectional = 1:

  - 0 projects in a direction opposite to the normal of the sketch plane
  - 1 projects along the normal of the sketch plane

## VBA Syntax

See [ModelDoc2::InsertSplitLineProject](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~InsertSplitLineProject.html).

## Examples

[Create Projection Split Line Feature (VBA)](Create_Projection_Split_Line_Example_VB.htm)
[Create Projection Split Line Feature (VB.NET)](Create_Projection_Split_Line_Example_VBNET.htm)
[Create Projection Split Line Feature (C#)](Create_Projection_Split_Line_Example_CSharp.htm)

## Remarks

- The sketch to project must be selected using [IModelDocExtension::SelectByID2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDocExtension~SelectByID2.html) with a mark value of 4.
- The faces to split must be selected using IModelDocExtension::SelectByID2 with mark values of 1.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)
[IModelDoc2::InsertSplitLineSil Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertSplitLineSil.html)
[ISplitLineFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISplitLineFeatureData.html)
[IFeatureManager::InsertSplitLineIntersect Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~InsertSplitLineIntersect.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
