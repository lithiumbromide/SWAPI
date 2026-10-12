---
title: "CommandInProgress Property (ISldWorks)"
project: "SOLIDWORKS API Help"
interface: "ISldWorks"
member: "CommandInProgress"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~CommandInProgress.html"
---

# CommandInProgress Property (ISldWorks)

Improves performance of out-of-process applications by informing SOLIDWORKS that a sequence of API calls will be made by the out-of-process application.

## Syntax

### Visual Basic (Declaration)

```vb
Property CommandInProgress As System.Boolean
```

### Visual Basic (Usage)

```vb
Dim instance As ISldWorks
Dim value As System.Boolean

instance.CommandInProgress = value

value = instance.CommandInProgress
```

### C#

```csharp
System.bool CommandInProgress {get; set;}
```

### C++/CLI

```cpp
property System.bool CommandInProgress {
   System.bool get();
   void set (    System.bool value);
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Set to True before calling the sequence of API calls, then set to false after calling the sequence of API calls

## VBA Syntax

See [SldWorks::CommandInProgress](ms-its:sldworksapivb6.chm::/sldworks~SldWorks~CommandInProgress.html).

## Remarks

SOLIDWORKS then reduces the number of updates it makes during these calls. Use of this property only effects out-of-process applications.

## See Also

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.html)
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.html)

## Availability

SOLIDWORKS 2006 SP2, Revision Number 14.2
