---
title: "IGetCoreProperties Method (ICableProperty)"
project: "SOLIDWORKS Routing API Help"
interface: "ICableProperty"
member: "IGetCoreProperties"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~IGetCoreProperties.html"
---

# IGetCoreProperties Method (ICableProperty)

Gets the core properties in the cable.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCoreProperties( _
   ByRef Count As System.Integer _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As ICableProperty
Dim Count As System.Integer
Dim value As System.IntPtr

value = instance.IGetCoreProperties(Count)
```

### C#

```csharp
System.IntPtr IGetCoreProperties(
   out System.int Count
)
```

### C++/CLI

```cpp
System.IntPtr IGetCoreProperties(
   [Out] System.int Count
)
```

### Parameters

- `Count`: Number of core properties

### Return Value

- in-process, unmanaged C++: Pointer to an array of [core properties](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWireProperty.html)
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWireProperty.html

## See Also

[ICableProperty Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty.html)
[ICableProperty Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty_members.html)
[ICableProperty::GetCoreProperties Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~GetCoreProperties.html)
[ICable::GetCores Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~GetCores.html)
[ICable::GetCoresCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~GetCoresCount.html)
[ICable::IGetCores Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~IGetCores.html)

## Availability

SOLIDWORKS Routing 2006 FCS
