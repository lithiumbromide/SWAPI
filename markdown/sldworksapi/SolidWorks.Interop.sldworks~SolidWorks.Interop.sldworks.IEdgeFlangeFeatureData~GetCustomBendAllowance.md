---
title: "GetCustomBendAllowance Method (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "GetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~GetCustomBendAllowance.html"
---

# GetCustomBendAllowance Method (IEdgeFlangeFeatureData)

Gets the custom bend allowance for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetCustomBendAllowance() As CustomBendAllowance
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim value As CustomBendAllowance

value = instance.GetCustomBendAllowance()
```

### C#

```csharp
CustomBendAllowance GetCustomBendAllowance()
```

### C++/CLI

```cpp
CustomBendAllowance^ GetCustomBendAllowance();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Pointer to the [ICustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) object

## VBA Syntax

See [EdgeFlangeFeatureData::GetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~GetCustomBendAllowance.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

This method is valid only if [IEdgeFlangeFeatureData::UseDefaultBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseDefaultBendAllowance.html) is set to false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::SetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~SetCustomBendAllowance.html)
[IEdgeFlangeFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseDefaultBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
