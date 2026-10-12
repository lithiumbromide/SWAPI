---
title: "CornerIndex Property (ISMCornerReliefData)"
project: "SOLIDWORKS API Help"
interface: "ISMCornerReliefData"
member: "CornerIndex"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData~CornerIndex.html"
---

# CornerIndex Property (ISMCornerReliefData)

Gets the index of this corner in the corner relief feature.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property CornerIndex As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ISMCornerReliefData
Dim value As System.Integer

value = instance.CornerIndex
```

### C#

```csharp
System.int CornerIndex {get;}
```

### C++/CLI

```cpp
property System.int CornerIndex {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

One-based index of this corner

## VBA Syntax

See [SMCornerReliefData::CornerIndex](ms-its:sldworksapivb6.chm::/sldworks~SMCornerReliefData~CornerIndex.html).

## Examples

See the [ICornerReliefFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerReliefFeatureData.html) examples.

## See Also

[ISMCornerReliefData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData.html)
[ISMCornerReliefData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISMCornerReliefData_members.html)

## Availability

SOLIDWORKS 2022 FCS, Revision Number 30
