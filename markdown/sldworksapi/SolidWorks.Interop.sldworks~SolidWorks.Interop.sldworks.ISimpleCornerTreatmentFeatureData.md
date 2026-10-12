---
title: "ISimpleCornerTreatmentFeatureData Interface"
project: "SOLIDWORKS API Help"
interface: "ISimpleCornerTreatmentFeatureData"
member: ""
kind: "interface"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData.html"
---

# ISimpleCornerTreatmentFeatureData Interface

Allows access to a simple corner treatment feature of a structure system.

**NOTE:** Click the **Members** link, located near the top of the topic, to see this interface's methods and properties.

## Syntax

### Visual Basic (Declaration)

```vb
Public Interface ISimpleCornerTreatmentFeatureData
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleCornerTreatmentFeatureData
```

### C#

```csharp
public interface ISimpleCornerTreatmentFeatureData
```

### C++/CLI

```cpp
public interface class ISimpleCornerTreatmentFeatureData
```

## VBA Syntax

See [SimpleCornerTreatmentFeatureData](ms-its:sldworksapivb6.chm::/sldworks~SimpleCornerTreatmentFeatureData.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

This interface is:

- derived from [ICornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.html).
- valid only if [ICornerTreatmentFeatureData::IgnoreCornerTreatment](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~IgnoreCornerTreatment.html) is false.

A simple corner is the position in a structure system where the ends of two members meet either in a body trim or a planar trim fashion.

In the SOLIDWORKS Design user interface, the Simple Corner PropertyManager contains two lists that you can manage using the APIs in this interface and elsewhere:

- [Corner groups](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetCornerTreatments.html)
- [User defined trim](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData~UserDefinedTrimFaces.html) faces

For more information, see:

- **SOLIDWORKS Design user-interface help > Weldments and Structure System > Structure System > Corner Management > Editing Simple Corners**
- **SOLIDWORKS Design user-interface help > Weldments and Structure System > Structure System > Simple Corner PropertyManager**

## Accessors

Cast an ICornerTreatmentFeatureData object to this interface.

## Access Diagram

[SimpleCornerTreatmentFeatureData](SWObjectModel.pdf#SimpleCornerTreatmentFD)

## See Also

[ISimpleCornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleCornerTreatmentFeatureData_members.html)
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.html)
