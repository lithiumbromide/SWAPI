---
title: "GetMirrorPlaneType Method (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "GetMirrorPlaneType"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~GetMirrorPlaneType.html"
---

# GetMirrorPlaneType Method (IMirrorPartFeatureData)

Gets whether the mirror plane is a face or a reference plane.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMirrorPlaneType() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Integer

value = instance.GetMirrorPlaneType()
```

### C#

```csharp
System.int GetMirrorPlaneType()
```

### C++/CLI

```cpp
System.int GetMirrorPlaneType();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Type of mirror plane as defined in [swMirrorPlaneType_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorPlaneType_e.html)

## VBA Syntax

See [MirrorPartFeatureData::GetMirrorPlaneType](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~GetMirrorPlaneType.html).

## Examples

See the [IMirrorPartFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData.html) examples.

## Remarks

Call this method to determine the type of mirror plane returned by [IMirrorPartFeatureData::GetMirrorPlane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData~GetMirrorPlane.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
