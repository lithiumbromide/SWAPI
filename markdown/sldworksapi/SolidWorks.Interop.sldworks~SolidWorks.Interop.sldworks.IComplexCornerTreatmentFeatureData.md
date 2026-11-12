---
title: "IComplexCornerTreatmentFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "IComplexCornerTreatmentFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData.html"
---

# IComplexCornerTreatmentFeatureData Interface

Allows access to a complex corner treatment feature of a structure system.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface IComplexCornerTreatmentFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As IComplexCornerTreatmentFeatureData
```

### C#

```csharp
public interface IComplexCornerTreatmentFeatureData
```

### C++/CLI

```cpp
public interface class IComplexCornerTreatmentFeatureData
```

## VBA Syntax

See [ComplexCornerTreatmentFeatureData](ms-its:sldworksapivb6.chm::/sldworks~ComplexCornerTreatmentFeatureData.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

This interface is:

- derived from [ICornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.html).
- valid only if [ICornerTreatmentFeatureData::IgnoreCornerTreatment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~IgnoreCornerTreatment.html) is false.

A complex corner is the position in a structure system where three or more members intersect.

In the SOLIDWORKS Design user interface, the Complex Corner PropertyManager contains five lists that you can manage using the APIs in this interface and elsewhere:

- [Corner groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetCornerTreatments.html)
- [Trim tool](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetTrimToolMember.html) member
- [Body trim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetBodyTrimMembers.html) members
- [Planar trim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~GetPlanarTrimMembers.html) members
- [User defined trim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData~UserDefinedTrimFaces.html) faces

You can assign one member as a trim tool and use it to add or remove material from adjacent members. Other members are trimmed based on their designated trim orders and positions with respect to touching members.

For more information, see:

- **SOLIDWORKS Design user-interface help > Weldments and Structure System > Structure System > Corner Management > Trimming Complex Corners**
- ****SOLIDWORKS Design user-interface help > Weldments and Structure System > Structure System > Corner Management > Examples of Complex Corner Management****
- **SOLIDWORKS Design user-interface help > Weldments and Structure System > Structure System > Complex Corner PropertyManager**

## Accessors

Cast an ICornerTreatmentFeatureData object to this interface.

## Access Diagram

[ComplexCornerTreatmentFeatureData](SWObjectModel.pdf#ComplexCornerTreatmentFD)

## See Also

[IComplexCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComplexCornerTreatmentFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
