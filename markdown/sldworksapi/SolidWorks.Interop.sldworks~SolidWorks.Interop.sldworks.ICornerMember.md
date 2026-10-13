---
title: "ICornerMember Interface"
project: "SOLIDWORKS API Help"
interface: "ICornerMember"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember.html"
---

# ICornerMember Interface

Allows access to a corner member of a complex or two member structure system corner treatment feature.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ICornerMember
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerMember
```

### C#

```csharp
public interface ICornerMember
```

### C++/CLI

```cpp
public interface class ICornerMember
```

## VBA Syntax

See [CornerMember](ms-its:sldworksapivb6.chm::/sldworks~CornerMember.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Accessors

[IComplexCornerTreatmentFeatureData::GetBodyTrimMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetBodyTrimMembers.html) and then cast to ICornerMember

[IComplexCornerTreatmentFeatureData::GetPlanarTrimMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetPlanarTrimMembers.html) and then cast to ICornerMember

[IComplexCornerTreatmentFeatureData::GetTrimToolMember](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetTrimToolMember.html) and then cast to ICornerMember

[ITwoMemberCornerTreatmentFeatureData::GetCornerGroupMembers](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~GetCornerGroupMembers.html) and then cast to ICornerMember

## Access Diagram

[CornerMember](SWObjectModel.pdf#CornerMember)

## See Also

[ICornerMember Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerMember_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
