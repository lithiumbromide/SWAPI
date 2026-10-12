---
title: "EndVariablePitchHelix Method (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "EndVariablePitchHelix"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~EndVariablePitchHelix.html"
---

# EndVariablePitchHelix Method (IFeatureManager)

Ends and inserts a variable-pitch helix.

## Syntax

### Visual Basic (Declaration)

```vb
Function EndVariablePitchHelix() As Feature
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As Feature

value = instance.EndVariablePitchHelix()
```

### C#

```csharp
Feature EndVariablePitchHelix()
```

### C++/CLI

```cpp
Feature^ EndVariablePitchHelix();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) object

## VBA Syntax

See [FeatureManager::EndVariablePitchHelix](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~EndVariablePitchHelix.html).

## Examples

[Create Variable-pitch Helix (C#)](Create_Variable_Pitch_Helix_Example_CSharp.htm)
[Create Variable-pitch Helix (VB.NET)](Create_Variable_Pitch_Helix_Example_VBNET.htm)
[Create Variable-pitch Helix (VBA)](Create_Variable_Pitch_Helix_Example_VB.htm)
[Create and Modify Variable-pitch Helix (C#)](Create_and_Modify_Variable-pitch_Helix_Example_CSharp.htm)
[Create and Modify Variable-pitch Helix (VB.NET)](Create_and_Modify_Variable-pitch_Helix_Example_VBNET.htm)
[Create and Modify Variable-pitch Helix (VBA)](Create_and_Modify_Variable-pitch_Helix_Example_VB.htm)

## Remarks

To create and insert a variable-pitch helix, call:

1. [IFeatureManager::InsertVariablePitchHelix](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertVariablePitchHelix.html) to create it.
2. [IFeatureManager::AddVariablePitchHelixFirstPitchAndDiamenter](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddVariablePitchHelixFirstPitchAndDiameter.html) to add the first segment.
3. [IFeatureManager::AddVariablePitchHelixSegment](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~AddVariablePitchHelixSegment.html) one or more times to add the remaining segments.
4. IFeatureManager::EndVariablePitchHelix to insert it.

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IHelixFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IHelixFeatureData.html)

## Availability

SOLIDWORKS 2006 FCS, Revision Number 14.0
