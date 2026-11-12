---
title: "GetIntersectingObjectTypes Method (ISecondaryMemberSupportPlaneFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ISecondaryMemberSupportPlaneFeatureData"
member: "GetIntersectingObjectTypes"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData~GetIntersectingObjectTypes.html"
---

# GetIntersectingObjectTypes Method (ISecondaryMemberSupportPlaneFeatureData)

Gets the types of support plane entities used to create this secondary structure system member.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetIntersectingObjectTypes() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ISecondaryMemberSupportPlaneFeatureData
Dim value As System.Object

value = instance.GetIntersectingObjectTypes()
```

### C#

```csharp
System.object GetIntersectingObjectTypes()
```

### C++/CLI

```cpp
System.Object^ GetIntersectingObjectTypes();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of entities as defined by swSelectType_e:

- swSelFACES
- swSelREFFACES
- swSelDATUMPLANES

## VBA Syntax

See [SecondaryMemberSupportPlaneFeatureData::GetIntersectingObjectTypes](ms-its:sldworksapivb6.chm::/sldworks~SecondaryMemberSupportPlaneFeatureData~GetIntersectingObjectTypes.html).

## See Also

[ISecondaryMemberSupportPlaneFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData.html)
[ISecondaryMemberSupportPlaneFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISecondaryMemberSupportPlaneFeatureData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
