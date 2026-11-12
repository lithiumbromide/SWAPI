---
title: "GetTransform Method (IMirrorSolidFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorSolidFeatureData"
member: "GetTransform"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData~GetTransform.html"
---

# GetTransform Method (IMirrorSolidFeatureData)

Gets the transform for this mirror-solid feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTransform() As MathTransform
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorSolidFeatureData
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

[Transform](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMathTransform.html)

## VBA Syntax

See [MirrorSolidFeatureData::GetTransform](ms-its:sldworksapivb6.chm::/sldworks~MirrorSolidFeatureData~GetTransform.html).

## See Also

[IMirrorSolidFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData.html)
[IMirrorSolidFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorSolidFeatureData_members.html)

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
