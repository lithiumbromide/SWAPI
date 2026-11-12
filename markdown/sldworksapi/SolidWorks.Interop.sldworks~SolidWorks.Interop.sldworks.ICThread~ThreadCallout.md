---
title: "ThreadCallout Property (ICThread)"
project: "SOLIDWORKS API Help"
interface: "ICThread"
member: "ThreadCallout"
kind: "property"
source: "sldworksapi/SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread~ThreadCallout.html"
---

# ThreadCallout Property (ICThread)

Gets the note for this cosmetic thread callout in a drawing.

## Syntax

### Visual Basic (Declaration)

```vb
ReadOnly Property ThreadCallout As Note
```

### Visual Basic (Usage)

```vb
Dim instance As ICThread
Dim value As Note

value = instance.ThreadCallout
```

### C#

```csharp
Note ThreadCallout {get;}
```

### C++/CLI

```cpp
property Note^ ThreadCallout {
   Note^ get();
}
```

**NOTE:** See [Differences Between Unmanaged C++ and C++/CLI Code](DifferencesBetweenUnManagedAndCPPCLI.htm).

### Property Value

Pointer to the [INote](SOLIDWORKS.Interop.sldworks~SOLIDWORKS.Interop.sldworks.INote.html) object for this cosmetic thread callout in a drawing

## VBA Syntax

See [CThread::ThreadCallout](ms-its:sldworksapivb6.chm::/sldworks~CThread~ThreadCallout.html).

## Remarks

By getting the INote interface, you have access to all of its methods and properties, such as the ability to get or set the text or change the text format.

## See Also

[ICThread Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread.html)
[ICThread Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICThread_members.html)

## Availability

SOLIDWORKS 2003 SP1, Revision Number 11.1
