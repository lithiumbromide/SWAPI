---
title: "ITwoMemberCornerTreatmentFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ITwoMemberCornerTreatmentFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData.html"
---

# ITwoMemberCornerTreatmentFeatureData Interface

Allows access to a two member corner treatment feature of a structure system.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ITwoMemberCornerTreatmentFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ITwoMemberCornerTreatmentFeatureData
```

### C#

```csharp
public interface ITwoMemberCornerTreatmentFeatureData
```

### C++/CLI

```cpp
public interface class ITwoMemberCornerTreatmentFeatureData
```

## VBA Syntax

See [TwoMemberCornerTreatmentFeatureData](ms-its:sldworksapivb6.chm::/sldworks~TwoMemberCornerTreatmentFeatureData.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

This interface is:

- derived from [ICornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.html).
- valid only if [ICornerTreatmentFeatureData::IgnoreCornerTreatment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~IgnoreCornerTreatment.html) is false.

A two member corner is the position in a structure system where two members intersect. You can assign one member as a trim tool and use it to add or remove material from the other member. The trim tool member may be assigned to either member in a planar or body trim type.

In the SOLIDWORKS Design user interface, the Two member Corner PropertyManager contains three lists that you can manage using the APIs in this interface and elsewhere:

- [Corner groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetCornerTreatments.html)
- [Corner group members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~GetCornerGroupMembers.html)
- [Miter trim plane point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData~MiterTrimPlanePoint.html)

For more information, see:

- **SOLIDWORKS Design user-interface help > Weldments and Structure System > Structure System > Corner Management**
- **SOLIDWORKS Design user-interface help > Weldments and Structure System > Structure System > Two Member PropertyManager**

## Accessors

Cast an ICornerTreatmentFeatureData object to this interface.

## Access Diagram

[TwoMemberCornerTreatmentFeatureData](SWObjectModel.pdf#TwoMemberCornerTreatmentFD)

## See Also

[ITwoMemberCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ITwoMemberCornerTreatmentFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
