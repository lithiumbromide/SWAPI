---
title: "GetConfigurations Method (IFamilyTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IFamilyTableFeature"
member: "GetConfigurations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature~GetConfigurations.html"
---

# GetConfigurations Method (IFamilyTableFeature)

Gets the configurations to use based on the specified criteria.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetConfigurations( _
   ByVal Criteria As System.Integer _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IFamilyTableFeature
Dim Criteria As System.Integer
Dim value As System.Object

value = instance.GetConfigurations(Criteria)
```

### C#

```csharp
System.object GetConfigurations(
   System.int Criteria
)
```

### C++/CLI

```cpp
System.Object^ GetConfigurations(
   System.int Criteria
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Criteria`: Criteria as defined by [swFamilyTableGetConfigurationCriteria_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swFamilyTableGetConfigurationCriteria_e.html)

### Return Value

Array of configurations

## VBA Syntax

See [FamilyTableFeature::GetConfigurations](ms-its:sldworksapivb6.chm::/sldworks~FamilyTableFeature~GetConfigurations.html).

## See Also

[IFamilyTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature.html)
[IFamilyTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFamilyTableFeature_members.html)

## Availability

SOLIDWORKS 2026 FCS, Revision Number 34
