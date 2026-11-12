---
title: "Lock Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "Lock"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~Lock.html"
---

# Lock Method (IModelDoc2)

Blocks the modifying commands in the user interface, effectively locking the application.

## Syntax

### Visual Basic (Declaration)

```vb
Sub Lock()
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2

instance.Lock()
```

### C#

```csharp
void Lock()
```

### C++/CLI

```cpp
void Lock();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

## VBA Syntax

See [ModelDoc2::Lock](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~Lock.html).

## Remarks

This method also changes the status bar to display Processing. Use this method with [IModelDoc2::UnLock](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~UnLock.html) .

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2001Plus FCS, Revision Number 10.0
