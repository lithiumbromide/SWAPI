---
title: "GetFeature Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "GetFeature"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetFeature.html"
---

# GetFeature Method (IFamilyTableFeature)

Gets the parent feature of this family table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFeature() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim value As System.Object

value = instance.GetFeature()
```

### C#

```csharp
System.object GetFeature()
```

### C++/CLI

```cpp
System.Object^ GetFeature();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

[IFeature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html)

## VBA Syntax

See [FamilyTableFeature::GetFeature](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~GetFeature.html).

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
