---
title: "ISymmetricMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ISymmetricMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData.html"
---

# ISymmetricMateFeatureData Interface

Allows access to symmetry mate feature data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISymmetricMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ISymmetricMateFeatureData
```

### C#

```csharp
public interface ISymmetricMateFeatureData
```

### C++/CLI

```cpp
public interface class ISymmetricMateFeatureData
```

## VBA Syntax

See [SymmetricMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~SymmetricMateFeatureData.html).

## Examples

[Create and Edit Symmetric Mate (VBA)](Create_Symmetric_Mate_Example_VB.htm)
[Create and Edit Symmetric Mate (C#)](Create_Symmetric_Mate_Example_CSharp.htm)

## Remarks

SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html

Symmetry mates force two similar entities to be symmetric about a plane or planar face.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this advanced mate interface.

To create a symmetry mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [ISymmetricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities using Mark = 1.
3. Specify [ISymmetricMateFeatureData::SymmetryPlane](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData~SymmetryPlane.html) or use IModelDocExtension::SelectByID2 to pre-select the symmetry plane using Mark = 4.
4. Specify other properties of the SymmetricMateFeatureData object as required.

To edit a symmetry mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a SymmetricMateFeatureData object.
3. Modify the SymmetricMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete a symmetry mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[SymmetricMateFeatureData](SWObjectModel.pdf#SymmetricMateFeatureData)

## See Also

[ISymmetricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISymmetricMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
