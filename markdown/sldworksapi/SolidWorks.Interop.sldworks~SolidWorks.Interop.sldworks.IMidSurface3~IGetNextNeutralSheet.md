---
title: "IGetNextNeutralSheet Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "IGetNextNeutralSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~IGetNextNeutralSheet.html"
---

# IGetNextNeutralSheet Method (IMidSurface3)

Gets the next reference surface in this midsurface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetNextNeutralSheet() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface3
Dim value As Body2

value = instance.IGetNextNeutralSheet()
```

### C#

```csharp
Body2 IGetNextNeutralSheet()
```

### C++/CLI

```cpp
Body2^ IGetNextNeutralSheet();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next reference surface sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) in this midsurface feature

## VBA Syntax

See [MidSurface3::IGetNextNeutralSheet](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~IGetNextNeutralSheet.html).

## Remarks

Each reference surface in the midsurface feature is considered a sheet body. If the reference surfaces are sewn together during the creation of the midsurface feature ([IFeatureManager::InsertMidSurface](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeatureManager~InsertMidSurface.html)), then the midsurface feature contains only one reference surface sheet body. If this is the case, then this method returns NULL. Use [IMidSurface3::IGetFirstNeutralSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetFirstNeutralSheet.html) to get the first and only reference surface sheet body.

The sheet body returned from this method has the normal topology that you would expect to find on a body (for example, faces, edges, and so on). See the [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object for methods that provide access to this topology.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::GetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstNeutralSheet.html)
[IMidSurface3::GetNeutralSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNeutralSheetCount.html)
[IMidSurface3::GetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetNextNeutralSheet.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
