---
title: "D1EndSeedReferenceType Property (ILocalLinearPatternFeatureData)"
project: "SOLIDWORKS API Help"
interface: "ILocalLinearPatternFeatureData"
member: "D1EndSeedReferenceType"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndSeedReferenceType.html"
---

# D1EndSeedReferenceType Property (ILocalLinearPatternFeatureData)

Gets the type of [ILocalLinearPatternFeatureData::D1EndSeedReference](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData~D1EndSeedReference.html).

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property D1EndSeedReferenceType As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As ILocalLinearPatternFeatureData
Dim value As System.Integer

value = instance.D1EndSeedReferenceType
```

### C#

```csharp
System.int D1EndSeedReferenceType {get;}
```

### C++/CLI

```cpp
property System.int D1EndSeedReferenceType {
   System.int get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Type as defined in [swSelectType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSelectType_e.html)

## VBA Syntax

See [LocalLinearPatternFeatureData::D1EndSeedReferenceType](ms-its:sldworksapivb6.chm::/sldworks~LocalLinearPatternFeatureData~D1EndSeedReferenceType.html).

## See Also

[ILocalLinearPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData.html)
[ILocalLinearPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILocalLinearPatternFeatureData_members.html)

## Availability

SOLIDWORKS 2020 FCS, Revision Number 28.0
