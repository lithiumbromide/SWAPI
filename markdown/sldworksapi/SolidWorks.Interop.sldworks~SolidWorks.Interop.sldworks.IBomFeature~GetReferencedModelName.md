---
title: "GetReferencedModelName Method (IBomFeature)"
project: "SOLIDWORKS API Help"
interface: "IBomFeature"
member: "GetReferencedModelName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature~GetReferencedModelName.html"
---

# GetReferencedModelName Method (IBomFeature)

Gets the name of the model referenced by this BOM feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetReferencedModelName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IBomFeature
Dim value As System.String

value = instance.GetReferencedModelName()
```

### C#

```csharp
System.string GetReferencedModelName()
```

### C++/CLI

```cpp
System.String^ GetReferencedModelName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of the model referenced by this BOM feature

## VBA Syntax

See [BomFeature::GetReferencedModelName](ms-its:sldworksapivb6.chm::/sldworks~BomFeature~GetReferencedModelName.html).

## See Also

[IBomFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature.html)
[IBomFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBomFeature_members.html)

## Availability

SOLIDWORKS 2007 SP5, Revision Number 15.5
