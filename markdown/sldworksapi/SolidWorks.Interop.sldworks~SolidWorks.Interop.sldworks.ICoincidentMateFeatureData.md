---
title: "ICoincidentMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ICoincidentMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.html"
---

# ICoincidentMateFeatureData Interface

Allows access to a coincident mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICoincidentMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ICoincidentMateFeatureData
```

### C#

```csharp
public interface ICoincidentMateFeatureData
```

### C++/CLI

```cpp
public interface class ICoincidentMateFeatureData
```

## VBA Syntax

See [CoincidentMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~CoincidentMateFeatureData.html).

## Examples

[Create Standard Mates (VBA)](Create_Standard_Mates_Example_VB.htm)
[Create Standard Mates (C#)](Create_Standard_Mates_Example_CSharp.htm)

## Remarks

A coincident mate:

- Positions the selected faces, edges, and planes so they share the same infinite plane.
- Positions two vertices so they touch.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a coincident mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [ICoincidentMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1.
3. Specify other properties of the CoincidentMateFeatureData object.

To edit a coincident mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a CoincidentMateFeatureData object.
3. You cannot change the entities to mate by pre-selection. You must use ICoincidentMateFeatureData::EntitiesToMate to modify them.
4. Modify other properties of the CoincidentMateFeatureData object.
5. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete this coincident mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[CoincidentMateFeatureData](SWObjectModel.pdf#CoincidentMateFeatureData)

## See Also

[ICoincidentMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
