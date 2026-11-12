---
title: "SetCustomBendAllowance Method (IEdgeFlangeFeatureData)"
project: "SOLIDWORKS API Help"
interface: "IEdgeFlangeFeatureData"
member: "SetCustomBendAllowance"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~SetCustomBendAllowance.html"
---

# SetCustomBendAllowance Method (IEdgeFlangeFeatureData)

Sets the custom bend allowance for this edge flange.

## Syntax

### Visual Basic (Declaration)

```vb
Sub SetCustomBendAllowance( _
   ByVal PBendData As CustomBendAllowance _
)
```

### Visual Basic (Usage)

```vb
Dim instance As IEdgeFlangeFeatureData
Dim PBendData As CustomBendAllowance

instance.SetCustomBendAllowance(PBendData)
```

### C#

```csharp
void SetCustomBendAllowance(
   CustomBendAllowance PBendData
)
```

### C++/CLI

```cpp
void SetCustomBendAllowance(
   CustomBendAllowance^ PBendData
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `PBendData`: Pointer to the [ICustomBendAllowance](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ICustomBendAllowance.html) object

## VBA Syntax

See [EdgeFlangeFeatureData::SetCustomBendAllowance](ms-its:sldworksapivb6.chm::/sldworks~EdgeFlangeFeatureData~SetCustomBendAllowance.html).

## Examples

See the [IEdgeFlangeFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html) examples.

## Remarks

This method is valid only if [IEdgeFlangeFeatureData::UseDefaultBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseDefaultBendAllowance.html) is set to false.

See [Accessing Selections that Define Features](sldworksAPIProgGuide.chm::/Miscellaneous/Accessing_Selections_that_Define_Features.htm) for additional details on using this method.

## See Also

[IEdgeFlangeFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData.html)
[IEdgeFlangeFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData_members.html)
[IEdgeFlangeFeatureData::GetCustomBendAllowance Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~GetCustomBendAllowance.html)
[IEdgeFlangeFeatureData::UseDefaultBendAllowance Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdgeFlangeFeatureData~UseDefaultBendAllowance.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
