---
title: "ForceReleaseLocks Method (IModelDoc2)"
project: "SOLIDWORKS API Help"
interface: "IModelDoc2"
member: "ForceReleaseLocks"
kind: "method"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ForceReleaseLocks.html"
---

# ForceReleaseLocks Method (IModelDoc2)

Releases the locks that a file system places on a file when it is opened and detaches that file from the file system.

## Syntax

### Visual Basic (Declaration)

```vb
Function ForceReleaseLocks() As System.Integer
```

### Visual Basic (Usage)

```vb
Dim instance As IModelDoc2
Dim value As System.Integer

value = instance.ForceReleaseLocks()
```

### C#

```csharp
System.int ForceReleaseLocks()
```

### C++/CLI

```cpp
System.int ForceReleaseLocks();
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Return Value

1 if locks are released, 0 if not

## VBA Syntax

See [ModelDoc2::ForceReleaseLocks](ms-its:sldworksapivb6.chm::/sldworks~ModelDoc2~ForceReleaseLocks.html).

## Remarks

This method only supports part and assembly documents; it does not support drawing documents. See [ISldWorks::CloseAndReopen](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.ISldWorks~CloseAndReopen.html) for details about closing and reopening a drawing document without unloading its references from memory.

You must call [IModelDoc2::ReloadOrReplace](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.IModelDoc2~ReloadOrReplace.html) after calling IModelDoc2::ForceReleaseLocks to re-attach the detached file to the file system. If you do not call IModelDoc2::ReloadOrReplace after calling IModelDoc2::ForceReleaseLocks, then you will experience problems with OLE objects (e.g., design tables).

IModelDoc2::ReloadOrReplace re-attaches the detached file to the file system; however, any changes made to the detached file are not preserved unless you save the file to disk before calling IModelDoc2::ReloadOrReplace.

CAUTION: This method is intended to be used by PDM systems. Using this method incorrectly could corrupt your data.

## See Also

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.html)
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.html)

## Availability

SOLIDWORKS 2003 FCS, Revision Number 11.0
