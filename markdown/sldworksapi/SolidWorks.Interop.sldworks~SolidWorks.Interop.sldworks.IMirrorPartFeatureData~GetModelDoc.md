---
title: "GetModelDoc Method (IMirrorPartFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IMirrorPartFeatureData"
member: "GetModelDoc"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData~GetModelDoc.html"
---

# GetModelDoc Method (IMirrorPartFeatureData)

Gets the base model document of this mirror part feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelDoc() As ModelDoc2
```

### Visual Basic (Usage)

```vb
Dim instance As IMirrorPartFeatureData
Dim value As ModelDoc2

value = instance.GetModelDoc()
```

### C#

```csharp
ModelDoc2 GetModelDoc()
```

### C++/CLI

```cpp
ModelDoc2^ GetModelDoc();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IModelDoc2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2.html)

## VBA Syntax

See [MirrorPartFeatureData::GetModelDoc](ms-its:sldworksapivb6.chm::/sldworks~MirrorPartFeatureData~GetModelDoc.html).

## See Also

[IMirrorPartFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData.html)
[IMirrorPartFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMirrorPartFeatureData_members.html)

## Availability

SOLIDWORKS 2014 FCS, Revision Number 22.0
