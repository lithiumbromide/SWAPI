---
title: "ComponentPrimaryIdentifier Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "ComponentPrimaryIdentifier"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ComponentPrimaryIdentifier.html"
---

# ComponentPrimaryIdentifier Property (IFeatureManager)

Gets the primary element displayed for the components in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ComponentPrimaryIdentifier As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Integer

value = instance.ComponentPrimaryIdentifier
```

### C#

```csharp
System.int ComponentPrimaryIdentifier {get;}
```

### C++/CLI

```cpp
property System.int ComponentPrimaryIdentifier {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Primary identifier as defined by [swComponentIdentifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentIdentifier_e.html)

## VBA Syntax

See [FeatureManager::ComponentPrimaryIdentifier](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~ComponentPrimaryIdentifier.html).

## Remarks

This property works in both SOLIDWORKS Design and [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::SetComponentIdentifiers Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetComponentIdentifiers.html)

## Availability

SOLIDWORKS 2022 SP01, Revision Number 30.1
