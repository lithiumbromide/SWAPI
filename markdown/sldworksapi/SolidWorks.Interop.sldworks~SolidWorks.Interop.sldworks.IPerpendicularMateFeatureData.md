---
title: "IPerpendicularMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IPerpendicularMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData.html"
---

# IPerpendicularMateFeatureData Interface

Allows access to a perpendicular mate feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IPerpendicularMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IPerpendicularMateFeatureData
```

### C#

```csharp
public interface IPerpendicularMateFeatureData
```

### C++/CLI

```cpp
public interface class IPerpendicularMateFeatureData
```

## VBA Syntax

See [PerpendicularMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~PerpendicularMateFeatureData.html).

## Examples

[Create Standard Mates (VBA)](Create_Standard_Mates_Example_VB.htm)
[Create Standard Mates (C#)](Create_Standard_Mates_Example_CSharp.htm)

## Remarks

A perpendicular mate places selected items at a 90⁰ angle.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this mate interface.

To create a perpendicular mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [IPerpendicularMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities to mate using Mark = 1.
3. Specify other properties of the PerpendicularMateFeatureData object.

To edit a perpendicular mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a PerpendicularMateFeatureData object.
3. Modify the PerpendicularMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete this perpendicular mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[PerpendicularMateFeatureData](SWObjectModel.pdf#PerpendicularMateFeatureData)

## See Also

[IPerpendicularMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPerpendicularMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
