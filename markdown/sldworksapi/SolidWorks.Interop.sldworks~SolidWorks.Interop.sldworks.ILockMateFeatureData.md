---
title: "ILockMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ILockMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILockMateFeatureData.html"
---

# ILockMateFeatureData Interface

Allows access to lock mate features.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ILockMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ILockMateFeatureData
```

### C#

```csharp
public interface ILockMateFeatureData
```

### C++/CLI

```cpp
public interface class ILockMateFeatureData
```

## VBA Syntax

See [LockMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~LockMateFeatureData.html).

## Examples

[Create Standard Mates (VBA)](Create_Standard_Mates_Example_VB.htm)
[Create Standard Mates (C#)](Create_Standard_Mates_Example_CSharp.htm)

## Remarks

A lock mate:

- Maintains the position and orientation between two components.
- Fully constrains the components.
- Is like a rigid subasssembly of components.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a lock mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [ILockMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILockMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1.

To edit a lock mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a LockMateFeatureData object.
3. Modify the LockMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete this lock mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[LockMateFeatureData](SWObjectModel.pdf#LockMateFeatureData)

## See Also

[ILockMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILockMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
