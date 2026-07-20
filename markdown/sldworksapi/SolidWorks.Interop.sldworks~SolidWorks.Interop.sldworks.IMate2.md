---
title: "IMate2 Interface"
project: "SOLIDWORKS API Help"
interface: "IMate2"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html"
---

# IMate2 Interface

Allows access to various assembly mate parameters.

**NOTE:**Click the**Members**link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IMate2
```

### Visual Basic (Usage)

```vb
Dim instance As IMate2
```

### C#

```csharp
public interface IMate2
```

### C++/CLI

```cpp
public interface class IMate2
```

## VBA Syntax

See

[Mate2](ms-its:sldworksapivb6.chm::/sldworks~Mate2.html)

.

## Examples

[Get Mates and Mate Entities (C#)](Get_Mates_and_Mate_Entities_Example_CSharp.htm)

[Get Mates and Mate Entities (VB.NET)](Get_Mates_and_Mate_Entities_Example_VBNET.htm)

[Get Mates and Mate Entities (VBA)](Get_Mates_and_Mate_Entities_Example_VB.htm)

## Remarks

To get the IMate2 object, you must first get it as a[IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html)object and then use[IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)or QueryInterface to return the IMate2 interface.

The IMate2 object is actually a subfeature beneath a MateGroup feature. To access the IMate2 subfeature by traversing the FeatureManager design tree, you can call[IFeature::GetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetFirstSubFeature.html)or[IFeature::IGetFirstSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetFirstSubFeature.html)and then[IFeature::GetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetNextSubFeature.html)or[IFeature::IGetNextSubFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~IGetNextSubFeature.html)when the current feature type is MateGroup.

## Accessors

[IAssemblyDoc::AddConcentricMateWithTolerance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddConcentricMateWithTolerance.html)

[IAssemblyDoc::AddDistanceMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddDistanceMate.html)

[IAssemblyDoc::AddMate3](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IAssemblyDoc~AddMate3.html)

[IAssemblyDoc::AutoMateRepair](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AutoMateRepair.html)

[IAssemblyDoc::CollectAllSupportiveMates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CollectAllSupportiveMates.html)

[IComponent2::GetMates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetMates.html)

[IFeature::GetSpecificFeature2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature~GetSpecificFeature2.html)

[IMate2::GetLinkedMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~GetLinkedMate.html)

[IMateControllerFeatureData::Mates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateControllerFeatureData~Mates.html)

[IMateLoadReference::Mate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMateLoadReference~Mate.html)

[IMoveCopyBodyFeatureData::AddMate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~AddMate.html)and[IMoveCopyBodyFeatureData::IAddMate](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMoveCopyBodyFeatureData~IAddMate.html)

## Access Diagram

[Mate2](SWObjectModel.pdf#Mate2)

## See Also

[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.html)

[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)

[IMateEntity2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateEntity2.html)

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.html)

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.html)
