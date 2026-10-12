---
title: "IWidthMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IWidthMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData.html"
---

# IWidthMateFeatureData Interface

Allows access to width mate feature data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IWidthMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IWidthMateFeatureData
```

### C#

```csharp
public interface IWidthMateFeatureData
```

### C++/CLI

```cpp
public interface class IWidthMateFeatureData
```

## VBA Syntax

See [WidthMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~WidthMateFeatureData.html).

## Examples

[Create and Edit Width Mate (VBA)](Create_Width_Mate_Example_VB.htm)
[Create and Edit Width Mate (C#)](Create_Width_Mate_Example_CSharp.htm)

## Remarks

SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html

A width mate constrains a tab between two planar faces.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this advanced mate interface.

To create a width mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [IWidthMateFeatureData::TabSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~TabSelection.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the tab using Mark = 16.
3. Specify [IWidthMateFeatureData::WidthSelection](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~WidthSelection.html) or use IModelDocExtension::SelectByID2 to pre-select the width using Mark = 1.
4. Specify [IWidthMateFeatureData::ConstraintType](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData~ConstraintType.html).
5. Specify other properties of the WidthMateFeatureData object as required.

To edit a width mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a WidthMateFeatureData object.
3. Modify the WidthMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete a width mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[WidthMateFeatureData](SWObjectModel.pdf#WidthMateFeatureData)

## See Also

[IWidthMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IWidthMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
