---
title: "GetCornerTreatments Method (ICornerTreatmentGroupFolder)"
project: "SOLIDWORKS API Help"
interface: "ICornerTreatmentGroupFolder"
member: "GetCornerTreatments"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder~GetCornerTreatments.html"
---

# GetCornerTreatments Method (ICornerTreatmentGroupFolder)

Gets the corner treatments in this corner treatment group folder.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCornerTreatments() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As ICornerTreatmentGroupFolder
Dim value As System.Object

value = instance.GetCornerTreatments()
```

### C#

```csharp
System.object GetCornerTreatments()
```

### C++/CLI

```cpp
System.Object^ GetCornerTreatments();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)s

## VBA Syntax

See [CornerTreatmentGroupFolder::GetCornerTreatments](ms-its:sldworksapivb6.chm::/sldworks~CornerTreatmentGroupFolder~GetCornerTreatments.html).

## Examples

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.html) examples.

## Remarks

Cast the returned features to [ICornerTreatmentFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.html) or call [IFeature::GetDefinition](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature~GetDefinition.html).

## See Also

[ICornerTreatmentGroupFolder Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder.html)
[ICornerTreatmentGroupFolder Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentGroupFolder_members.html)

## Availability

SOLIDWORKS 2023 FCS, Revision Number 31
