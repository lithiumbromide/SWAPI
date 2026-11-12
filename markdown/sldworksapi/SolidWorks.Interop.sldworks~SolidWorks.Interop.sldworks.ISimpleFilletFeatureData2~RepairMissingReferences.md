---
title: "RepairMissingReferences Method (ISimpleFilletFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "ISimpleFilletFeatureData2"
member: "RepairMissingReferences"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2~RepairMissingReferences.html"
---

# RepairMissingReferences Method (ISimpleFilletFeatureData2)

Finds missing references in this fillet/chamfer and reassigns them to new edges.

## Syntax

### Visual Basic (Declaration)

```vb
Sub RepairMissingReferences()
```

### Visual Basic (Usage)

```vb
Dim instance As ISimpleFilletFeatureData2

instance.RepairMissingReferences()
```

### C#

```csharp
void RepairMissingReferences()
```

### C++/CLI

```cpp
void RepairMissingReferences();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [SimpleFilletFeatureData2::RepairMissingReferences](ms-its:sldworksapivb6.chm::/sldworks~SimpleFilletFeatureData2~RepairMissingReferences.html).

## Remarks

If you delete a feature that this fillet or chamfer is referencing and then create a similar feature with the same geometry, the references do not reattach. The missing references appear in the **Items To Fillet** list box of the Fillet PropertyManager, but finding the valid edges to reattach is difficult. Call this method to find all missing references and reassign them to new edges.

## See Also

[ISimpleFilletFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2.html)
[ISimpleFilletFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISimpleFilletFeatureData2_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
