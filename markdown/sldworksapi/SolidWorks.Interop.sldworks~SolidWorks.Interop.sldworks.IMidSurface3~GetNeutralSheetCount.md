---
title: "GetNeutralSheetCount Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "GetNeutralSheetCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNeutralSheetCount.html"
---

# GetNeutralSheetCount Method (IMidSurface3)

Gets the total number of reference surfaces found in this midsurface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNeutralSheetCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface3
Dim value As System.Integer

value = instance.GetNeutralSheetCount()
```

### C#

```csharp
System.int GetNeutralSheetCount()
```

### C++/CLI

```cpp
System.int GetNeutralSheetCount();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Number of reference surface sheet bodies found in this midsurface feature

## VBA Syntax

See [MidSurface3::GetNeutralSheetCount](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~GetNeutralSheetCount.html).

## Remarks

Each reference surface in the midsurface feature is considered to be a sheet body. If the reference surfaces are sewn together during the creation of our midsurface feature, [IFeatureManager::InsertMidSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMidSurface.html), then the midsurface feature contains only one reference surface sheet body.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::GetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstNeutralSheet.html)
[IMidSurface3::GetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextNeutralSheet.html)
[IMidSurface3::IGetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetFirstNeutralSheet.html)
[IMidSurface3::IGetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextNeutralSheet.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
