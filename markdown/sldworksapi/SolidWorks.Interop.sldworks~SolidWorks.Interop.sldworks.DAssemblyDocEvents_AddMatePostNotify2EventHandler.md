---
title: "DAssemblyDocEvents_AddMatePostNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DAssemblyDocEvents_AddMatePostNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_AddMatePostNotify2EventHandler.html"
---

# DAssemblyDocEvents_AddMatePostNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Fired after one or more mates are created in an assembly.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DAssemblyDocEvents_AddMatePostNotify2EventHandler( _
   ByRef Mates As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DAssemblyDocEvents_AddMatePostNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DAssemblyDocEvents_AddMatePostNotify2EventHandler(
   ref System.object Mates
)
```

### C++/CLI

```cpp
public delegate System.int DAssemblyDocEvents_AddMatePostNotify2EventHandler(
   System.Object^% Mates
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Mates`: Array of new [mates](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.html)

## VBA Syntax

See [AddMatePostNotify2 Event (AssemblyDoc)](ms-its:sldworksapivb6.chm::/SldWorks~AssemblyDoc~AddMatePostNotify2_EV.html).

## Examples

[Fire Notification After Adding a Mate (VBA)](Fire_Notification_After_Adding_a_Mate_Example_VB.htm)
[Fire Notification After Adding a Mate (VB.NET)](Fire_Notification_After_Adding_a_Mate_Example_VBNET.htm)
[Fire Notification After Adding a Mate (C#)](Fire_Notification_After_Adding_a_Mate_Example_CSharp.htm)

## Remarks

If developing a C++ application, use [swAssemblyAddMatePostNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAssemblyNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2019 FCS, Revision Number 27.0
