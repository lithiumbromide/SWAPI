---
title: "GetNeutralSheetCount Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "GetNeutralSheetCount"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNeutralSheetCount.html"
---

# GetNeutralSheetCount Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::GetNeutralSheetCount](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetNeutralSheetCount.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNeutralSheetCount() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface2
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

See [MidSurface2::GetNeutralSheetCount](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~GetNeutralSheetCount.html).

## Remarks

Each reference surface in the midsurface feature is considered to be a sheet body. If the reference surfaces are sewn together during the creation of our midsurface feature ([IModelDoc2::InsertMidSurfaceExt](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertMidSurfaceExt.html) or [IModelDoc2::IInsertMidSurfaceExt](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~IInsertMidSurfaceExt.html)), then the midsurface feature contains only one reference surface sheet body.

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::IGetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstNeutralSheet.html)
[IMidSurface2::GetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetFirstNeutralSheet.html)
[IMidSurface2::IGetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextNeutralSheet.html)
[IMidSurface2::GetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextNeutralSheet.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
