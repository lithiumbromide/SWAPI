---
title: "GetFirstNeutralSheet Method (IMidSurface3)"
project: "SOLIDWORKS API Help"
interface: "IMidSurface3"
member: "GetFirstNeutralSheet"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3~GetFirstNeutralSheet.html"
---

# GetFirstNeutralSheet Method (IMidSurface3)

Gets the first reference surface in this midsurface feature.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetFirstNeutralSheet() As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IMidSurface3
Dim value As System.Object

value = instance.GetFirstNeutralSheet()
```

### C#

```csharp
System.object GetFirstNeutralSheet()
```

### C++/CLI

```cpp
System.Object^ GetFirstNeutralSheet();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

First reference surface sheet [body](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) in this midsurface feature

## VBA Syntax

See [MidSurface3::GetFirstNeutralSheet](ms-its:sldworksapivb6.chm::/sldworks~MidSurface3~GetFirstNeutralSheet.html).

## Remarks

Each reference surface in the midsurface feature is considered to be a sheet body. If the reference surfaces are sewn together during the creation of the midsurface feature ([IModelDoc2::InsertMidSurfaceExt](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~InsertMidSurfaceExt.html)), then the midsurface feature contains only one reference surface sheet body.

The sheet body returned from this method has the normal topology that you would expect to find on a body (for example, faces, edges, and so on). See the [IBody2](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IBody2.html) object for methods that provide access to this topology.

Call [IMidSurface3::GetNextNeutralSheet](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IMidSurface3~GetNextNeutralSheet.html) to get the next reference surface in this midsurface feature.

## See Also

[IMidSurface3 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3.html)
[IMidSurface3 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface3_members.html)
[IMidSurface3::IGetNextNeutralSheet Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IGetNextNeutralSheet.html)
[IMidSurface3::GetNeutralSheetCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~GetNeutralSheetCount.html)

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
