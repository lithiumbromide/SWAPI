---
title: "GetFeatureId Method (IFace2)"
project: "SOLIDWORKS API Help"
interface: "IFace2"
member: "GetFeatureId"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeatureId.html"
---

# GetFeatureId Method (IFace2)

Gets the order number for the owning feature of this face.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeatureId() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IFace2
Dim value As System.Integer

value = instance.GetFeatureId()
```

### C#

```csharp
System.int GetFeatureId()
```

### C++/CLI

```cpp
System.int GetFeatureId();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Order number of the owning feature

## VBA Syntax

See [Face2::GetFeatureId](ms-its:sldworksapivb6.chm::/sldworks~Face2~GetFeatureId.html).

## See Also

[IFace2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.html)
[IFace2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2_members.html)
[IFace2::GetFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~GetFeature.html)
[IFace2::IGetFeature Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2~IGetFeature.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
