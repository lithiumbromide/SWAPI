---
title: "SetMouseDragMode Method (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "SetMouseDragMode"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~SetMouseDragMode.html"
---

# SetMouseDragMode Method (ISldWorks)

Sets the command-mouse mode.

## Syntax

### Visual Basic (Declaration)

```vb
Function SetMouseDragMode( _
   ByVal Command As System.Integer _
) As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim Command As System.Integer
Dim value As System.Boolean

value = instance.SetMouseDragMode(Command)
```

### C#

```csharp
System.bool SetMouseDragMode(
   System.int Command
)
```

### C++/CLI

```cpp
System.bool SetMouseDragMode(
   System.int Command
)
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Parameters

- `Command`: Command mode that you want to check as defined in [swMouseDragMode_e](ms-its:swconst.chm::/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMouseDragMode_e.html)

### Return Value

True if the specified command mode was set, false if not

## VBA Syntax

See [SldWorks::SetMouseDragMode](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~SetMouseDragMode.html).

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)
[ISldWorks::GetMouseDragMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetMouseDragMode.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
