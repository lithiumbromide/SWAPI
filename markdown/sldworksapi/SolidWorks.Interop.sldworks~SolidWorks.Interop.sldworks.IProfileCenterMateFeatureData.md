---
title: "IProfileCenterMateFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IProfileCenterMateFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData.html"
---

# IProfileCenterMateFeatureData Interface

Allows access to profile center mate feature data.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IProfileCenterMateFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IProfileCenterMateFeatureData
```

### C#

```csharp
public interface IProfileCenterMateFeatureData
```

### C++/CLI

```cpp
public interface class IProfileCenterMateFeatureData
```

## VBA Syntax

See [ProfileCenterMateFeatureData](ms-its:sldworksapivb6.chm::/sldworks~ProfileCenterMateFeatureData.html).

## Examples

[Create and Edit Profile Center Mate (VBA)](Create_Profile_Center_Mate_Example_VB.htm)
[Create and Edit Profile Center Mate (C#)](Create_Profile_Center_Mate_Example_CSharp.htm)

## Remarks

SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html

A profile center mate centrally aligns rectangular and circular profiles to each other and fully defines the components.

[IMateFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateFeatureData.html) is the parent of this advanced mate interface.

To create a profile center mate:

1. Follow general instructions in the [IAssemblyDoc::CreateMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateMate.html) Remarks.
2. Specify [IProfileCenterMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData~EntitiesToMate.html) or use [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.html) to pre-select the entities using Mark = 1.
3. Specify other properties of the ProfileCenterMateFeatureData object.

To edit a profile center mate:

1. Access its feature and call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html) to get the MateFeatureData object.
2. Cast the MateFeatureData object to a ProfileCenterMateFeatureData object.
3. Modify the ProfileCenterMateFeatureData object.
4. Call [IFeature::ModifyDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~ModifyDefinition.html).

To delete a profile center mate, use [IModelDocExtension::DeleteSelection2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~DeleteSelection2.html).

## Access Diagram

[ProfileCenterMateFeatureData](SWObjectModel.pdf#ProfileCenterMateFeatureData)

## See Also

[IProfileCenterMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IProfileCenterMateFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
