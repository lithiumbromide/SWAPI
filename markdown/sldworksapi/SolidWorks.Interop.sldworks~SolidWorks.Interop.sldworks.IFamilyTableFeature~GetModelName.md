---
title: "GetModelName Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "GetModelName"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetModelName.html"
---

# GetModelName Method (IFamilyTableFeature)

Gets the name of the part or assembly whose drawing contains this family table.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModelName() As System.String
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim value As System.String

value = instance.GetModelName()
```

### C#

```csharp
System.string GetModelName()
```

### C++/CLI

```cpp
System.String^ GetModelName();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Name of part or assembly

## VBA Syntax

See [FamilyTableFeature::GetModelName](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~GetModelName.html).

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
