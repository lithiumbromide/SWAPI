---
title: "GetRoutingLibComponentReferences Method (IRouteManager)"
project: "SOLIDWORKS Routing API Help"
interface: "IRouteManager"
member: "GetRoutingLibComponentReferences"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager~GetRoutingLibComponentReferences.html"
---

# GetRoutingLibComponentReferences Method (IRouteManager)

Gets the routing library component references.

## Syntax

### Visual Basic (Declaration)

```vb
Function GetRoutingLibComponentReferences( _
   ByVal bstrFolder As System.String _
) As System.Object
```

### Visual Basic (Usage)

```vb
Dim instance As IRouteManager
Dim bstrFolder As System.String
Dim value As System.Object

value = instance.GetRoutingLibComponentReferences(bstrFolder)
```

### C#

```csharp
System.object GetRoutingLibComponentReferences(
   System.string bstrFolder
)
```

### C++/CLI

```cpp
System.Object^ GetRoutingLibComponentReferences(
   System.String^ bstrFolder
)
```

### Parameters

- `bstrFolder`: Routing Library folder

### Return Value

Routing component references

## VBA Syntax

See [RouteManager::GetRoutingLibComponentReferences](ms-its:routingapivb6.chm::/SWRoutingLib~RouteManager~GetRoutingLibComponentReferences.html).

## See Also

[IRouteManager Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager.html)
[IRouteManager Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.IRouteManager_members.html)

## Availability

SOLIDWORKS Routing 2007 SP1
