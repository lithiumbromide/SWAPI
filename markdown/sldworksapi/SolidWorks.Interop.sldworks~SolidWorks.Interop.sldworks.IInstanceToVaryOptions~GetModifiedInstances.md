---
title: "GetModifiedInstances Method (IInstanceToVaryOptions)"
project: "SOLIDWORKS API Help"
interface: "IInstanceToVaryOptions"
member: "GetModifiedInstances"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetModifiedInstances.html"
---

# GetModifiedInstances Method (IInstanceToVaryOptions)

Gets instance numbers of modified pattern instances of the specified type.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetModifiedInstances( _
   ByVal ModificationType As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IInstanceToVaryOptions
Dim ModificationType As System.Integer
Dim value As System.Object

value = instance.GetModifiedInstances(ModificationType)
```

### C#

```csharp
System.object GetModifiedInstances(
   System.int ModificationType
)
```

### C++/CLI

```cpp
System.Object^ GetModifiedInstances(
   System.int ModificationType
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `ModificationType`: Modification type as defined by [swInstanceToVaryModificationType_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swInstanceToVaryModificationType_e.html)

### Return Value

Array of pattern instance numbers

## VBA Syntax

See [InstanceToVaryOptions::GetModifiedInstances](ms-its:sldworksapivb6.chm::/sldworks~InstanceToVaryOptions~GetModifiedInstances.html).

## See Also

[IInstanceToVaryOptions Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions.html)
[IInstanceToVaryOptions Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions_members.html)
[IInstanceToVaryOptions::GetModifiedDimensions Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetModifiedDimensions.html)
[IInstanceToVaryOptions::GetD1ModifiedSpacingValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetD1ModifiedSpacingValue.html)
[IInstanceToVaryOptions::GetD2ModifiedSpacingValue Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IInstanceToVaryOptions~GetD2ModifiedSpacingValue.html)

## Availability

SOLIDWORKS 2021 FCS, Revision Number 29
