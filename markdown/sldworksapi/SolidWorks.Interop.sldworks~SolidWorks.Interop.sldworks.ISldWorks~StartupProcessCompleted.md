---
title: "StartupProcessCompleted Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "StartupProcessCompleted"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~StartupProcessCompleted.html"
---

# StartupProcessCompleted Property (ISldWorks)

Gets whether the SOLIDWORKS startup process, including loading all startup add-ins, has completed.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property StartupProcessCompleted As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

value = instance.StartupProcessCompleted
```

### C#

```csharp
System.bool StartupProcessCompleted {get;}
```

### C++/CLI

```cpp
property System.bool StartupProcessCompleted {
   System.bool get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

True if the SOLIDWORKS startup process, including loading all startup add-ins, has completed, false if not (see **Remarks**)

## VBA Syntax

See [SldWorks::StartupProcessCompleted](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~StartupProcessCompleted.html)

## Remarks

Use this property in out-of-process add-in applications to ensure that SOLIDWORKS, including loading all startup add-ins, is ready to receive additional API calls. For example, call this property before calling [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.html) in an out-of-process add-in application.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2015 FCS, Revision Number 23.0
