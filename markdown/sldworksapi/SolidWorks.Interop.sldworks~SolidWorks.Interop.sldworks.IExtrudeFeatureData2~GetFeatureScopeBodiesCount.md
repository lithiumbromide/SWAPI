---
title: "GetFeatureScopeBodiesCount Method (IExtrudeFeatureData2)"
project: "SOLIDWORKS API Help"
interface: "IExtrudeFeatureData2"
member: "GetFeatureScopeBodiesCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~GetFeatureScopeBodiesCount.html"
---

# GetFeatureScopeBodiesCount Method (IExtrudeFeatureData2)

Gets the number of solid bodies affected by the extrude feature in a multibody part.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureScopeBodiesCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IExtrudeFeatureData2
Dim value As System.Integer

value = instance.GetFeatureScopeBodiesCount()
```

### C#

```csharp
System.int GetFeatureScopeBodiesCount()
```

### C++/CLI

```cpp
System.int GetFeatureScopeBodiesCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of solid bodies affected

## VBA Syntax

See [ExtrudeFeatureData2::GetFeatureScopeBodiesCount](ms-its:sldworksapivb6.chm::/sldworks~ExtrudeFeatureData2~GetFeatureScopeBodiesCount.html).

## Remarks

Call this method before calling [IExtrudeFeatureData2::IGetFeatureScopeBodies](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~IGetFeatureScopeBodies.html).

If [IExtrudeFeatureData2::FeatureScope](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IExtrudeFeatureData2~FeatureScope.html) is false, then count will be 0.

## See Also

[IExtrudeFeatureData2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2.html)
[IExtrudeFeatureData2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2_members.html)
[IExtrudeFeatureData2::AutoSelect Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~AutoSelect.html)
[IExtrudeFeatureData2::FeatureScopeBodies Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~FeatureScopeBodies.html)
[IExtrudeFeatureData2::ISetFeatureScopeBodies Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IExtrudeFeatureData2~ISetFeatureScopeBodies.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
