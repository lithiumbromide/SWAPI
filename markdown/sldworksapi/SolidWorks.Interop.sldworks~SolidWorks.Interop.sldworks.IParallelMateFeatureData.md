---
title: "IParallelMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IParallelMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData.html"
---

# IParallelMateFeatureData Interface

Allows access to a parallel mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IParallelMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IParallelMateFeatureData
```

### C#

```csharp
public interface IParallelMateFeatureData
```

### C++/CLI

```cpp
public interface class IParallelMateFeatureData
```

## VBA Syntax

See [ParallelMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~ParallelMateFeatureData.html).

## Examples

[Create Standard Mates (VBA)](Create_Standard_Mates_Example_VB.htm)
[Create Standard Mates (C#)](Create_Standard_Mates_Example_CSharp.htm)

## Remarks

A parallel mate places selected items a constant distance apart.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a parallel mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [IParallelMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1.
3. Specify other properties of the ParallelMateFeatureData object.

To edit a parallel mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a ParallelMateFeatureData object.
3. Modify the ParallelMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete this parallel mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[ParallelMateFeatureData](SWObjectModel.pdf#ParallelMateFeatureData)

## See Also

[IParallelMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IParallelMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
