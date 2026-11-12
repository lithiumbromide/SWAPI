---
title: "GetPositionReferenceType Method (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "GetPositionReferenceType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~GetPositionReferenceType.html"
---

# GetPositionReferenceType Method (IEdgeFlangeFeatureData)

Gets the position reference type from the edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetPositionReferenceType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As System.Integer

value = instance.GetPositionReferenceType()
```

### C#

```csharp
System.int GetPositionReferenceType()
```

### C++/CLI

```cpp
System.int GetPositionReferenceType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Position reference type as defined in [swSelectionReferenceTypes_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swSelectionReferenceTypes_e.html)

## VBA Syntax

See [EdgeFlangeFeatureData::GetPositionReferenceType](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~GetPositionReferenceType.html).

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::PositionType Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~PositionType.html)
[IEdgeFlangeFeatureData::UsePositionTrimSideBends Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UsePositionTrimSideBends.html)

## Availability

SOLIDWORKS 2001 SP2, Revision Number 9.2
