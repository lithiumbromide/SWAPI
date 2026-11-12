---
title: "IConcentricMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IConcentricMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.html"
---

# IConcentricMateFeatureData Interface

Allows access to a concentric mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IConcentricMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IConcentricMateFeatureData
```

### C#

```csharp
public interface IConcentricMateFeatureData
```

### C++/CLI

```cpp
public interface class IConcentricMateFeatureData
```

## VBA Syntax

See [ConcentricMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~ConcentricMateFeatureData.html).

## Examples

[Create Standard Mates (VBA)](Create_Standard_Mates_Example_VB.htm)
[Create Standard Mates (C#)](Create_Standard_Mates_Example_CSharp.htm)

## Remarks

A concentric mate:

- Places selections so that they share the same axis.
- Can be configured to prevent rotation.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a concentric mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [IConcentricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1.
3. Specify other properties of the ConcentricMateFeatureData object.

To edit a concentric mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a ConcentricMateFeatureData object.
3. Modify the ConcentricMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete this concentric mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[ConcentricMateFeatureData](SWObjectModel.pdf#ConcentricMateFeatureData)

## See Also

[IConcentricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
