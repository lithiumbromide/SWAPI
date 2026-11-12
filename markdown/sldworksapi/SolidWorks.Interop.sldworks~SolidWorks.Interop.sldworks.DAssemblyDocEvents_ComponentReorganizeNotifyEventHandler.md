---
title: "DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler.html"
---

# DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when one or more components are reorganized in an assembly or sub-assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler( _
   ByVal sourceName As System.String, _
   ByVal targetName As System.String _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler(
   System.string sourceName,
   System.string targetName
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_ComponentReorganizeNotifyEventHandler(
   System.String^ sourceName,
   System.String^ targetName
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `sourceName`: Source name
- `targetName`: Target name

## VBA Syntax

See [ComponentReorganizeNotify Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~ComponentReorganizeNotify_EV.html).

## Examples

[Reorganize Components (VBA)](Reorganize_Components_Example_VB.htm)

## Remarks

If developing a C++ application, use [swAssemblyComponentReorganizeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2009 FCS, Revision Number 17.0
