---
title: "DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)"
project: "SOLIDWORKS API Help"
interface: "DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler"
member: ""
kind: "topic"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler.html"
---

# DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler Delegate (SolidWorks.Interop.sldworks)

Fired when 3DExperience changes state.

## Syntax

### Visual Basic (Declaration)

```vb
Public Delegate Function DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler( _
   ByVal newState As System.Integer _
) As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As New DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler(AddressOf HandlerMethod)
```

### C#

```csharp
public delegate System.int DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler(
   System.int newState
)
```

### C++/CLI

```cpp
public delegate System.int DSldWorksEvents_On3DExperienceStateChangeNotifyEventHandler(
   System.int newState
)
```

NOTE:

See

[Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm)

.

### Parameters

- `newState`: New state as defined by

[sw3DExperienceState_e](ms-its:swconst.chm::/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.sw3DExperienceState_e.html)

## VBA Syntax

See

[On3DExperienceStateChangeNotify Event (SldWorks)](ms-its:sldworksapivb6.chm::/SldWorks~SldWorks~On3DExperienceStateChangeNotify_EV.html)

.

## Remarks

If developing a C++ application, use

[swAppOn3DExperienceStateChangeNotify](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swAppNotify_e.html)

to register for this notification.

## Availability

SOLIDWORKS 2025 SP01, Revision Number 33.1
