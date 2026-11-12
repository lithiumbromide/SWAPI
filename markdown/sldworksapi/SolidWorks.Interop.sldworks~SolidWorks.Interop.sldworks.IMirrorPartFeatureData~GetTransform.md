---
title: "GetTransform Method (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "GetTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~GetTransform.html"
---

# GetTransform Method (IMirrorPartFeatureData)

Gets the transform of this mirror part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransform() As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As MathTransform

value = instance.GetTransform()
```

### C#

```csharp
MathTransform GetTransform()
```

### C++/CLI

```cpp
MathTransform^ GetTransform();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IMathTransform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [MirrorPartFeatureData::GetTransform](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~GetTransform.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
