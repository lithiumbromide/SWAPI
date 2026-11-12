---
title: "GetD1OffsetReferenceType Method (IBaseFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IBaseFlangeFeatureData"
member: "GetD1OffsetReferenceType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetD1OffsetReferenceType.html"
---

# GetD1OffsetReferenceType Method (IBaseFlangeFeatureData)

Gets the type of reference geometry for Direction 1 for this base flange feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetD1OffsetReferenceType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IBaseFlangeFeatureData
Dim value As System.Integer

value = instance.GetD1OffsetReferenceType()
```

### C#

```csharp
System.int GetD1OffsetReferenceType()
```

### C++/CLI

```cpp
System.int GetD1OffsetReferenceType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of reference geometry as defined in [swSelectionReferenceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectionReferenceTypes_e.html)

## VBA Syntax

See [BaseFlangeFeatureData::GetD1OffsetReferenceType](ms-its:sldworksapivb6.chm::/sldworks~BaseFlangeFeatureData~GetD1OffsetReferenceType.html).

## See Also

[IBaseFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData.html)
[IBaseFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData_members.html)
[IBaseFlangeFeatureData::GetD2OffsetReferenceType Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBaseFlangeFeatureData~GetD2OffsetReferenceType.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
