---
title: "DPartDocEvents_RegenPostNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DPartDocEvents_RegenPostNotify2EventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_RegenPostNotify2EventHandler.html"
---

# DPartDocEvents_RegenPostNotify2EventHandler Delegate (SolidWorks.Interop.sldworks)

Post-notifies the user program when a part document has been rebuilt or rolled back.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DPartDocEvents_RegenPostNotify2EventHandler( _
   ByVal stopFeature As System.Object _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DPartDocEvents_RegenPostNotify2EventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DPartDocEvents_RegenPostNotify2EventHandler(
   System.object stopFeature
)
```

### C++/CLI

```cpp
public delegate System.int DPartDocEvents_RegenPostNotify2EventHandler(
   System.Object^ stopFeature
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `stopFeature`: - If a rollback, [IFeature](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IFeature.html) immediately below the rollback bar in the FeatureManager design tree
  - If a rebuild, NULL

## VBA Syntax

See [RegenPostNotify2 Event (PartDoc)](ms-its:sldworksapivb6.chm::/SldWorks~PartDoc~RegenPostNotify2_EV.html).

## Remarks

If developing a C++ application, use [swPartRegenPostNotify2](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swPartNotify_e.html) to register for this notification.

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
