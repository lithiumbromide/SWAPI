---
title: "GetTableAnnotations Method (IGeneralToleranceTableFeature)"
project: "SOLIDWORKS API Help"
interface: "IGeneralToleranceTableFeature"
member: "GetTableAnnotations"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature~GetTableAnnotations.html"
---

# GetTableAnnotations Method (IGeneralToleranceTableFeature)

Gets the table annotations for this general tolerance table feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetTableAnnotations() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IGeneralToleranceTableFeature
Dim value As System.Object

value = instance.GetTableAnnotations()
```

### C#

```csharp
System.object GetTableAnnotations()
```

### C++/CLI

```cpp
System.Object^ GetTableAnnotations();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Array of [IGeneralToleranceTableAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableAnnotation.html)s

## VBA Syntax

See [GeneralToleranceTableFeature::GetTableAnnotations](ms-its:sldworksapivb6.chm::/sldworks~GeneralToleranceTableFeature~GetTableAnnotations.html).

## See Also

[IGeneralToleranceTableFeature Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature.html)
[IGeneralToleranceTableFeature Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGeneralToleranceTableFeature_members.html)

## Availability

SOLIDWORKS 2018 FCS, Revision Number 26.0
