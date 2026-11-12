---
title: "GetNextNeutralSheet Method (IMidSurface2)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface2"
member: "GetNextNeutralSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNextNeutralSheet.html"
---

# GetNextNeutralSheet Method (IMidSurface2)

Obsolete. Superseded by [IMidSurface3::GetNextNeutralSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetNextNeutralSheet.html).

## Syntax

### Visual Basic (Declaration)

```vb
Function GetNextNeutralSheet() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface2
Dim value As System.Object

value = instance.GetNextNeutralSheet()
```

### C#

```csharp
System.object GetNextNeutralSheet()
```

### C++/CLI

```cpp
System.Object^ GetNextNeutralSheet();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

Next reference surface sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) in this midsurface feature

## VBA Syntax

See [MidSurface2::GetNextNeutralSheet](ms-its:sldworksapivb6.chm::/sldworks~MidSurface2~GetNextNeutralSheet.html).

## Remarks

Each reference surface in the midsurface feature is considered a sheet body. If the reference surfaces are sewn together during the creation of the midsurface feature ([IModelDoc2::InsertMidSurfaceExt](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertMidSurfaceExt.html)), then the midsurface feature contains only one reference surface sheet body. If this is the case, then this method returns NULL. Use [IMidSurface2::GetFirstNeutralSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface2~GetNeutralSheetCount.html) to get the first and only reference surface sheet body.

The sheet body returned from this method has the normal topology that you would expect to find on a body (for example, faces, edges, and so on). See the [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object for methods that provide access to this topology.

## See Also

[IMidSurface2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2.html)
[IMidSurface2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2_members.html)
[IMidSurface2::IGetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextNeutralSheet.html)
[IMidSurface2::IGetFirstNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetFirstNeutralSheet.html)
[IMidSurface2::GetNeutralSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNeutralSheetCount.html)

## Availability

SolidWork s2001Plus FCS, Revision Number 10.0
