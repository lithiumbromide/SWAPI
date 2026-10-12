---
title: "IGetFirstNeutralSheet Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "IGetFirstNeutralSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstNeutralSheet.html"
---

# IGetFirstNeutralSheet Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::IGetFirstNeutralSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~IGetFirstNeutralSheet.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetFirstNeutralSheet() As Body2
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface2
Dim value As Body2

value = instance.IGetFirstNeutralSheet()
```

### C#

```csharp
Body2 IGetFirstNeutralSheet()
```

### C++/CLI

```cpp
Body2^ IGetFirstNeutralSheet();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First reference surface sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) in this midsurface feature

## VBA Syntax

See [MidSurface2::IGetFirstNeutralSheet](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~IGetFirstNeutralSheet.html).

## Remarks

Each reference surface in the midsurface feature is considered to be a sheet body. If the reference surfaces are sewn together during the creation of the midsurface feature ([IModelDoc2::IInsertMidSurfaceExt](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IInsertMidSurfaceExt.html)), then the midsurface feature contains only one reference surface sheet body.

The sheet body returned from this method has the normal topology that you would expect to find on a body (for example, faces, edges, and so on). See the [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object for methods that provide access to this topology.

Call [IMidSurface2::IGetNextNeutralSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~IGetNextNeutralSheet.html) to get the next reference surface in this midsurface feature.

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::GetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstNeutralSheet.html)
[IMidSurface2::GetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextNeutralSheet.html)
[IMidSurface2::GetNeutralSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNeutralSheetCount.html)

## Availability

SOLIDWORKS 2001Pus FCS, Revision Number 10.0
