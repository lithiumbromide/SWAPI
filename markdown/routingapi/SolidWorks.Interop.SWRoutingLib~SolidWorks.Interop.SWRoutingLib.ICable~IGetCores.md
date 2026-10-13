---
title: "IGetCores Method (ICable)"
project: "SOLIDWORKS Routing API Help"
interface: "ICable"
member: "IGetCores"
kind: "method"
source: "routingapi/SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~IGetCores.html"
---

# IGetCores Method (ICable)

Gets the cores in this cable.

## Syntax

### Visual Basic (Declaration)

```vb
Function IGetCores( _
   ByRef Count As System.Integer _
) As System.IntPtr
```

### Visual Basic (Usage)

```vb
Dim instance As ICable
Dim Count As System.Integer
Dim value As System.IntPtr

value = instance.IGetCores(Count)
```

### C#

```csharp
System.IntPtr IGetCores(
   out System.int Count
)
```

### C++/CLI

```cpp
System.IntPtr IGetCores(
   [Out] System.int Count
)
```

### Parameters

- `Count`: Number of cores in this cable

### Return Value

- in-process, unmanaged C++: Pointer to an array of [cores](SOLIDWORKS.Interop.SWRoutingLib~SOLIDWORKS.Interop.SWRoutingLib.IWire.html) in this cable
- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

## See Also

[ICable Interface](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable.html)
[ICable Members](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable_members.html)
[ICable::GetCores Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICable~GetCores.html)
[ICableProperty::GetCoreProperties Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~GetCoreProperties.html)
[ICableProperty::GetCorePropertyCount Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~GetCorePropertyCount.html)
[ICableProperty::IGetCoreProperties Method](SolidWorks.Interop.SWRoutingLib~SolidWorks.Interop.SWRoutingLib.ICableProperty~IGetCoreProperties.html)

## Availability

SOLIDWORKS Routing 2006 FCS
