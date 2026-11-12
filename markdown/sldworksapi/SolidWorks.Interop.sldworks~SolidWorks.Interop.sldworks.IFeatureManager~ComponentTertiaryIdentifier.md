---
title: "ComponentTertiaryIdentifier Property (IFeatureManager)"
project: "SOLIDWORKS API Help"
interface: "IFeatureManager"
member: "ComponentTertiaryIdentifier"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~ComponentTertiaryIdentifier.html"
---

# ComponentTertiaryIdentifier Property (IFeatureManager)

Gets the tertiary element(s) displayed for the components in the FeatureManager design tree.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ComponentTertiaryIdentifier As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFeatureManager
Dim value As System.Integer

value = instance.ComponentTertiaryIdentifier
```

### C#

```csharp
System.int ComponentTertiaryIdentifier {get;}
```

### C++/CLI

```cpp
property System.int ComponentTertiaryIdentifier {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Tertiary identifier(s) as defined by [swComponentIdentifier_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swComponentIdentifier_e.html)

## VBA Syntax

See [FeatureManager::ComponentTertiaryIdentifier](ms-its:sldworksapivb6.chm::/sldworks~FeatureManager~ComponentTertiaryIdentifier.html).

## Remarks

This property works in both SOLIDWORKS Design and [SOLIDWORKS Design connected to the 3DEXPERIENCE platform](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

## See Also

[IFeatureManager Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager.html)
[IFeatureManager Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager_members.html)
[IFeatureManager::SetComponentIdentifiers Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeatureManager~SetComponentIdentifiers.html)

## Availability

SOLIDWORKS 2022 SP01, Revision Number 30.1
