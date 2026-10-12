---
title: "GetMirrorPlane Method (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "GetMirrorPlane"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~GetMirrorPlane.html"
---

# GetMirrorPlane Method (IMirrorPartFeatureData)

Gets the plane about which this part is mirrored.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetMirrorPlane() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As System.Object

value = instance.GetMirrorPlane()
```

### C#

```csharp
System.object GetMirrorPlane()
```

### C++/CLI

```cpp
System.Object^ GetMirrorPlane();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IRefPlane](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IRefPlane.html) or [IFace2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFace2.html)

## VBA Syntax

See [MirrorPartFeatureData::GetMirrorPlane](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~GetMirrorPlane.html).

## Examples

See the [IMirrorPartFeatureData](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData.html) examples.

## Remarks

Before calling this method, call [IMirrorPartFeatureData::GetMirrorPlaneType](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMirrorPartFeatureData~GetMirrorPlaneType.html) to determine the type of mirror plane that this method returns.

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
