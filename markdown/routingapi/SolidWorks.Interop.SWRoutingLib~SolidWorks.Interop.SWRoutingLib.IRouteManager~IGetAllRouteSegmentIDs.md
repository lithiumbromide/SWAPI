---
title: "IGetAllRouteSegmentIDs Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "IGetAllRouteSegmentIDs"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~IGetAllRouteSegmentIDs.html"
---

# IGetAllRouteSegmentIDs Method (IRouteManager)

Gets all of the route segment IDs for the active route.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetAllRouteSegmentIDs( _
   ByRef Count As System.Integer _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim Count As System.Integer
Dim value As System.IntPtr

value = instance.IGetAllRouteSegmentIDs(Count)
```

### C#

```csharp
System.IntPtr IGetAllRouteSegmentIDs(
   out System.int Count
)
```

### C++/CLI

```cpp
System.IntPtr IGetAllRouteSegmentIDs(
   [Out] System.int Count
)
```

### Parameters

- `Count`: Number of route segments for the active route

### Return Value

- in-process, unmanaged C++: Pointer to an array of route segment IDs for the active route
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)
[IRouteManager::GetAllRouteSegmentIDs Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetAllRouteSegmentIDs.html)

## Availability

SOLIDWORKS Routing 2008 FCS
