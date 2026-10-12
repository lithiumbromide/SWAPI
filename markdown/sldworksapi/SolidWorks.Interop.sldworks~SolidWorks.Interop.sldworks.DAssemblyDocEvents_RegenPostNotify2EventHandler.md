---
title: "DAssemblyDocEvents_RegenPostNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_RegenPostNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenPostNotify2EventHandler.html"
---

# DAssemblyDocEvents_RegenPostNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when an assembly document is rebuilt.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_RegenPostNotify2EventHandler( _
   ByVal stopFeature As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_RegenPostNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_RegenPostNotify2EventHandler(
   System.object stopFeature
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_RegenPostNotify2EventHandler(
   System.Object^ stopFeature
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `stopFeature`: - If rolled back, the [assembly feature](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFeature.html) below the rollback bar in the FeatureManager design tree

  - If rebuilt, Nothing or null

## VBA Syntax

See [RegenPostNotify2 Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~RegenPostNotify2_EV.html).

## Examples

[Fire Assembly Rebuild Events (C#)](Regen_Post_Notify2_Event_Handler_Example_CSharp.htm)
[Fire Assembly Rebuild Events (VB.NET)](Regen_Post_Notify2_Event_Handler_Example_VBNET.htm)
[Fire Assembly Rebuild Events (VBA)](Regen_Post_Notify2_Event_Handler_Example_VB.htm)

## Remarks

If developing a C++ application, use [swAssemblyRegenPostNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

Use [DAssemblyDocEvents RegenNotifyEventHandler](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_RegenNotifyEventHandler.html) to fire an event before the assembly is about to be rebuilt.

You can also use [IModelDoc2::GetUpdateStamp](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~GetUpdateStamp.html) to determine when changes take place in this document.

## Availability

SOLIDWORKS 2010 FCS, Revision Number 18.0
